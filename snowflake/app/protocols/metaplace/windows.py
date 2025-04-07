
from __future__ import annotations
from typing import Dict, Callable

from app.data import WindowAction, MessageType, EventType
from app import protocols

import config
import json
import time

class SWFWindow:
    """
    This class represents a swf window inside the game. The window can be loaded, using the WindowManager class.
    The server can then send various payloads to the window, which can do different things, depending on the swf file.
    For example: `cardjitsu_snowtimer.swf` will receive a "tick" update every second, which will update the timer.
    """

    def __init__(
        self,
        client: protocols.MetaplaceProtocol,
        url: str | None = None,
        name: str | None = None,
        layer: str = 'topLayer'
    ) -> None:
        if not name:
            # "filename.swf"
            name = url.split('/')[-1]

        elif not url:
            # Default location
            url = f'{config.WINDOW_BASEURL}/{name}'

        assert url or name, 'You must provide either a url or a name for the window.'

        self.name = name
        self.url = url
        self.client = client
        self.layer = layer # TODO: topLayer, bottomLayer, toolLayer
        self.asset_path = '' # TODO
        self.loaded = False

        self.on_load: Callable | None = None
        self.on_close: Callable | None = None

    def __repr__(self) -> str:
        return f"<SWF ({self.name})>"

    def send(self, content: dict = {}, message_type = MessageType.RECEIVED_JSON, **kwargs):
        content.update(kwargs)
        self.client.send_tag(
            'UI_CLIENTEVENT',
            self.client.server.world_id,
            message_type.value,
            json.dumps(content)
        )

    def load(self, initial_payload: dict = None, **kwargs):
        if config.APPLY_WINDOWMANAGER_OFFSET:
            kwargs['xPercent'] = kwargs.get('xPercent', 0) - 0.5
            kwargs['yPercent'] = kwargs.get('yPercent', 0) - 0.5

        self.send(
            {
                'windowUrl': self.url,
                'layerName': self.layer,
                'assetPath': self.asset_path,
                'initializationPayload': initial_payload,
                'action': WindowAction.LOAD_WINDOW.value,
                'type': EventType.PLAY_ACTION.value
            },
            **kwargs
        )

    def close(self, **kwargs):
        self.send(
            {
                'targetWindow': self.url,
                'action': WindowAction.CLOSE_WINDOW.value,
                'type': EventType.PLAY_ACTION.value,
            },
            **kwargs
        )

    def send_payload(self, trigger_name: str, payload: dict = {}, type = EventType.IMMEDIATE, **kwargs):
        self.send(
            {
                'jsonPayload': payload,
                'targetWindow': self.url,
                'triggerName': trigger_name,
                'action': WindowAction.JSON_PAYLOAD.value,
                'type': type.value
            },
            **kwargs
        )

    def send_action(self, action: str, type = EventType.IMMEDIATE, **kwargs):
        self.send(
            {
                'action': action,
                'type': type.value
            },
            **kwargs
        )

class WindowManager(Dict[str, SWFWindow]):
    """
    This class represents the window manager, which is responsible for loading and closing swf files/windows.
    It will get loaded after the clients sends the /ready command to the server.
    """

    def __init__(
        self,
        client: protocols.MetaplaceProtocol,
        swf_url: str = config.WINDOW_MANAGER_LOCATION
    ) -> None:
        self.element_name = "WindowManagerSwf"
        self.command_prefix = "/framework"
        self.element_id = client.server.world_id
        self.swf_url = swf_url
        self.client = client

        self.parent_id = 0
        self.swf_x = 0
        self.swf_y = 0
        self.swf_width = 0
        self.swf_height = 0

        self.loaded = False
        self.ready = False

    def __setitem__(self, name: str, window: SWFWindow) -> None:
        return super().__setitem__(name, window)

    def get_window(self, name: str | None = None, url: str | None = None):
        assert url or name, 'You must provide either a url or a name for the window.'

        if (name in self):
            return self[name]

        elif (url != None) and (url.split('/')[-1] in self):
            return self[url]

        self[name] = (
            SWFWindow(self.client, url, name)
        )

        return self[name]

    def load(self):
        self.client.send_tag(
            'UI_CROSSWORLDSWFREF',
            self.element_id,
            self.parent_id,
            self.element_name,
            self.swf_x,
            self.swf_y,
            self.swf_width,
            self.swf_height,
            0,
            self.swf_url,
            self.command_prefix
        )
        self.loaded = True

        self['windowmanager.swf'] = SWFWindow(
            self.client,
            self.swf_url,
            'windowmanager.swf'
        )

    def wait_for_window(self, window: SWFWindow, loaded: bool = True, timeout: int = 8):
        start_time = time.time()

        while window.loaded != loaded:
            if self.client.disconnected:
                return

            if time.time() - start_time > timeout:
                self.logger.warning(f'Window Timeout: {window.name}')
                return

            time.sleep(0.05)

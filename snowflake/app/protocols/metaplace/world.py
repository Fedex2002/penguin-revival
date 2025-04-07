
from __future__ import annotations

from twisted.internet.address import IPv4Address, IPv6Address
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from typing import Dict

from app.protocols.metaplace import MetaplaceProtocol, Place
from app.objects import Players, AssetCollection
from app.data import ServerType, BuildType

import logging

class MetaplaceWorldServer(Factory):
    protocol = MetaplaceProtocol

    def __init__(
        self,
        world_id: int,
        world_name: str,
        world_owner: str,
        stylesheet_id: str,
        policy_domain: str = "*",
        policy_port: str = "*",
        server_type: ServerType = ServerType.LIVE,
        build_type: BuildType = BuildType.RELEASE
    ) -> None:
        self.world_id = world_id
        self.world_name = world_name
        self.world_owner = world_owner
        self.build_type = build_type
        self.server_type = server_type
        self.stylesheet_id = stylesheet_id

        self.logger = logging.getLogger(world_name)
        self.places: Dict[str, Place] = {}

        self.sound_assets = AssetCollection()
        self.assets = AssetCollection()
        self.players = Players()

        self.policy_file = (
            f"<cross-domain-policy>"
            f"<allow-access-from domain='{policy_domain}' to-ports='{policy_port}' />"
            f"</cross-domain-policy>"
        )

    def get_place(self, place_id: int) -> Place | None:
        return next((place for place in self.places.values() if place.id == place_id), None)

    def register_place(self, place: Place) -> None:
        self.places[place.name] = place
        self.logger.info(f'Registered place: "{place.name}"')

    def listen(self, port: int) -> None:
        self.logger.info(f'Starting world server "{self.world_name}" ({port})')
        reactor.listenTCP(port, self)

    def buildProtocol(self, address: IPv4Address | IPv6Address) -> MetaplaceProtocol:
        self.logger.debug(f'-> "{address.host}:{address.port}"')
        self.players.add(player := self.protocol(self, address))
        return player

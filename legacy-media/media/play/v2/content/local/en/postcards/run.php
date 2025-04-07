<?php
foreach(range(0, 1000) as $postcard){
	@copy('http://media1.clubpenguin.com/play/v2/content/local/de/postcards/' . $postcard . '.swf', $postcard . '.swf');
}

?>

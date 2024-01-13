import re

from flask import url_for

from sports_streaming.browsers.base import BaseBrowser

from sports_streaming.config import config


class EmbedFlixBrowser(BaseBrowser):
    def get_games(self):
        self.driver.get('https://embedflix.net/tv')
        result = []
        for card in self.find_elements('.tvchannel_item'):
            tag = f'<div class="w3-quarter">{card.get_attribute("innerHTML")}</div>'
            url = re.findall(r'href="https://embedflix\.net/tv/.+?"', tag)[0]
            player_id = re.findall(r'href="https://embedflix\.net/tv/(.+?)"', tag)[0]
            tag = tag.replace(url, config['DOMAIN'] + url_for('embed_flix_player', player_id=player_id))
            tag = tag.replace('tvchannel_name', 'btn btn-block btn-dark')
            tag = tag.replace('img', 'img class="w3-hover-opacity" style="width:100%"')
            tag = tag.replace('tvchannel_item', 'w3-quarter')
            result.append(tag)
        return result

    def get_player_script(self, player_id):
        pass

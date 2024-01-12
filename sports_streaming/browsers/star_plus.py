import re

from flask import url_for

from sports_streaming.browsers.base import BaseBrowser
from sports_streaming.config import config


class StarPlusBrowser(BaseBrowser):
    def get_games(self):
        self.driver.get('https://starplus.eventos.wtf')
        result = []
        for card in self.find_elements('.w3-quarter'):
            tag = f'<div class="w3-quarter">{card.get_attribute("innerHTML")}</div>'
            href = self.find_element('a', element=card).get_attribute('href')
            player_id = re.findall(r'id=(.+)', href)[0]
            tag = tag.replace(
                href,
                config['DOMAIN']
                + url_for('star_plus_player', player_id=player_id),
            )
            result.append(tag)
        return result

    def get_player_script(self, player_id):
        self.driver.get(
            f'https://starplus.eventos.wtf/player.php?id={player_id}'
        )
        for script in self.find_elements('script'):
            if 'playerInstance' in script.get_attribute('innerHTML'):
                result = script.get_attribute('innerHTML').replace(
                    'width: "100%', 'width: "100vw'
                )
                result = result.replace('height: "100%', 'height: "100vh')
                return result

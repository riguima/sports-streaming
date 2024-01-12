from flask import Flask, render_template

from sports_streaming.browsers.embed_flix import EmbedFlixBrowser
from sports_streaming.browsers.star_plus import StarPlusBrowser

star_plus_browser = StarPlusBrowser()

embed_flix_browser = EmbedFlixBrowser()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    @app.get('/star-plus')
    def star_plus():
        return render_template(
            'star_plus.html', games=star_plus_browser.get_games()
        )

    @app.get('/star-plus/<player_id>')
    def star_plus_player(player_id):
        return render_template(
            'star_plus_player.html',
            player_script=star_plus_browser.get_player_script(player_id),
        )

    @app.get('/embed-flix')
    def embed_flix():
        return render_template(
            'embed_flix.html', games=embed_flix_browser.get_games()
        )

    @app.get('/embed-flix/<player_id>')
    def embed_flix_player(player_id):
        return render_template(
            'embed_flix_player.html',
            player_script=embed_flix_browser.get_player_script(player_id),
        )

    return app


app = create_app()

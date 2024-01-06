from flask import Flask, render_template

from m3u8_links_api.browser import Browser

browser = Browser()


def create_app():
    app = Flask(__name__, template_folder="templates")

    @app.get("/m3u8/<player_id>")
    def get_m3u8(player_id):
        return render_template(
            "m3u8.html", player_script=browser.get_player_script(player_id)
        )

    return app


app = create_app()

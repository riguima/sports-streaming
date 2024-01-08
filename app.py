from flask import Flask, render_template

from m3u8_links_api.browser import Browser

browser = Browser()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    @app.get("/")
    def index():
        return render_template("index.html", games=browser.get_games())

    @app.get("/<player_id>")
    def video(player_id):
        return render_template(
            "video.html", player_script=browser.get_player_script(player_id)
        )

    return app


app = create_app()

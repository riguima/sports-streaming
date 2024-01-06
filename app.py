from pathlib import Path

from flask import Flask, redirect, url_for
from httpx import Client

from m3u8_links_api.browser import Browser

browser = Browser()


def create_app():
    app = Flask(__name__, static_folder="static")

    @app.get("/m3u8/<player_id>")
    def get_m3u8(player_id):
        url = browser.get_m3u8_url(player_id)
        with Client() as client:
            response = client.get(url)
            with open(Path("static") / f"{player_id}.m3u8", "wb") as file:
                file.write(response.content)
        return redirect(url_for("static", filename=f"{player_id}.m3u8"))

    return app


app = create_app()

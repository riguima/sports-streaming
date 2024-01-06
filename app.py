from flask import Flask, jsonify

from m3u8_links_api.browser import Browser

browser = Browser()


def create_app():
    app = Flask(__name__)

    @app.get("/links")
    def links():
        return jsonify(browser.get_links())

    return app


app = create_app()

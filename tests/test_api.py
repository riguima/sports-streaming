import re

import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_links(client):
    response = client.get("/links")
    already_links = []
    for link in response.json:
        assert link not in already_links
        assert re.findall(
            r"^https://starplus\.eventos\.wtf/player\.php\?id=.+$",
            link,
        )
        already_links.append(link)

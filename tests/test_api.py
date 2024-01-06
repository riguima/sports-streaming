from pathlib import Path

import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_m3u8(client):
    response = client.get(
        "/m3u8/T2tsYWhvbWEgU3RhdGUgdnMuIE5DIFN0YXRl", follow_redirects=True
    )
    assert response.data == open(Path("tests") / "expected_m3u8.m3u8", "rb").read()

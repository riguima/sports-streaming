import re

import pytest

from m3u8_links_api.browser import Browser


@pytest.fixture(scope="function")
def browser():
    return Browser(headless=False)


def test_get_links(browser):
    already_links = []
    for link in browser.get_links():
        assert link not in already_links
        assert re.findall(
            r"^https://starplus\.eventos\.wtf/player\.php\?id=.+$",
            link,
        )
        already_links.append(link)

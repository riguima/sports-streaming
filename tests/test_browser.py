import pytest

from m3u8_links_api.browser import Browser


@pytest.fixture(scope="function")
def browser():
    return Browser(headless=False)


def test_get_m3u8_url(browser):
    url = browser.get_m3u8_url("T2tsYWhvbWEgU3RhdGUgdnMuIE5DIFN0YXRl")
    assert (
        url
        == "https://live-ftc-na-south-2.media.starott.com/clt2/va01/starplus/event/2024/01/06/Oklahoma_State_vs_NC_Stat_20240106_1704493851017/ctr-all-complete.m3u8"
    )

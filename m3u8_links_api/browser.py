import base64
import re

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
        self.driver = Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def get_m3u8_url(self, player_id):
        self.driver.get(f"https://starplus.eventos.wtf/player.php?id={player_id}")
        for script in self.find_elements("script"):
            if "playerInstance" in script.get_attribute("innerHTML"):
                base64_url = re.findall(
                    r"file.+?atob\(\"(.+?)\"\)",
                    script.get_attribute("innerHTML"),
                    re.DOTALL,
                )[0]
                url = base64.b64decode(base64_url).decode("utf-8")
                url = url[: url.rfind("m3u8")] + "m3u8"
                return url

    def find_elements(self, selector, element=None, wait=10):
        element = element or self.driver
        return WebDriverWait(element, wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

from abc import ABC, abstractmethod

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseBrowser(ABC):
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
        self.driver = Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    @abstractmethod
    def get_games(self):
        raise NotImplementedError()

    @abstractmethod
    def get_player_script(self, player_id):
        raise NotImplementedError()

    def find_element(self, selector, element=None, wait=10):
        element = element or self.driver
        return WebDriverWait(element, wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def find_elements(self, selector, element=None, wait=10):
        element = element or self.driver
        return WebDriverWait(element, wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

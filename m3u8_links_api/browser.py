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

    def get_links(self):
        self.driver.get("https://starplus.eventos.wtf")
        return [
            link.get_attribute("href")
            for link in self.find_elements(".w3-quarter a.btn")
        ]

    def find_elements(self, selector, element=None, wait=10):
        element = element or self.driver
        return WebDriverWait(element, wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

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

    def get_player_script(self, player_id):
        self.driver.get(f"https://starplus.eventos.wtf/player.php?id={player_id}")
        for script in self.find_elements("script"):
            if "playerInstance" in script.get_attribute("innerHTML"):
                result = script.get_attribute("innerHTML").replace(
                    'width: "100%', 'width: "100vw'
                )
                result = result.replace('height: "100%', 'height: "100vh')
                return result

    def find_elements(self, selector, element=None, wait=10):
        element = element or self.driver
        return WebDriverWait(element, wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

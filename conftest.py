from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

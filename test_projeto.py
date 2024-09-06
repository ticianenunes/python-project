import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()

def test_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_cart(driver):
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bike-light']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-fleece-jacket']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()

    badge = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").text

    assert badge == "6"

def test_remove_product_from_badge(driver):
    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']").click()

    badge = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").text

    assert badge == "5"


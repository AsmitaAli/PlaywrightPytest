import pytest
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

@pytest.fixture
def login(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    return page


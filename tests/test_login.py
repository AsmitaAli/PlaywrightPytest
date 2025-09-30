import pytest
from playwright.sync_api import Page

@pytest.mark.smoke
def test_login_success(login):
    page = login
    assert page.url == "https://www.saucedemo.com/inventory.html"

              
def test_login_failure(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("wrong_user")
    page.fill("#password", "wrong_pass")
    page.get_by_text("Login").click()
    error_message = page.text_content("h3[data-test='error']")
    assert "Epic sadface" in error_message


              
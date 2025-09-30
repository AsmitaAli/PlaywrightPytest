import pytest
def test_checkout_flow(login):
    page = login

    # Step1: Add product to cart
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("button[data-test='add-to-cart-sauce-labs-bike-light']")

    # Verify cart badge
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "2", "Cart badge should show 2 items"

    # Step2: Go to Cart
    page.click("a.shopping_cart_link")

    cart_items = page.locator(".cart_item")
    assert cart_items.count() == 2, "Cart should contain 2 items"

    #Step3 Remove one Item
    page.click("button[data-test='remove-sauce-labs-bike-light']")
    assert cart_items.count() ==1, "Cart should contain 1 item after removal"

    #Step4: proceed to checkout
    page.click("button[data-test='checkout']")
    page.fill("input[data-test='firstName']", "John")
    page.fill("input[data-test='lastName']", "Doe")
    page.fill("input[data-test='postalCode']", "123456")
    page.click("input[data-test='continue']")

    #step5: Finish order
    page.click("button[data-test='finish']")

    # Validate confirmation
    confirmation = page.locator(".complete-header")
    assert confirmation.inner_text() == "Thank you for your order!"


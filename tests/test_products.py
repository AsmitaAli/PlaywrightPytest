

def test_add_to_cart(login):
    page = login
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
    badge = page.locator(".shopping_cart_badge")
    assert badge.inner_text() == "1" 

def test_product_titles_visible(login):
    page = login
    titles = page.locator(".inventory_item_name")    
    assert titles.count() > 0 
    
    
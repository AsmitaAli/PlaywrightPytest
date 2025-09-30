from utils.assertions import assert_sorted

# Sort A-Z
def test_sort_products_by_name_az(login):
    page = login
    page.select_option("select.product_sort_container","az")
    titles = page.locator(".inventory_item_name").all_inner_texts()
    # assert titles == sorted(titles), f"Expected A-Z sorting, but got {titles}"  
    assert_sorted(titles, message="Expected A-Z sorting")  

 # Sort Z-A

def test_sort_products_by_name_za(login):
    page = login
    page.select_option("select.product_sort_container", label="Name (Z to A)")
    titles = page.locator(".inventory_item_name").all_inner_texts()
    # assert titles == sorted(titles, reverse=True), f"Expected Z-A sorting, but got {titles}" 
    assert_sorted(titles, reverse=True, message="Expected Z - A sorting")  

# Price Low-high

def test_sort_products_by_orice_low_high(login):
    page = login
    page.select_option("select.product_sort_container", index=2)
    prices = page.locator(".inventory_item_price").all_inner_texts()
    prices = [float(price.replace("$", "")) for price in prices]
    # assert prices == sorted(prices), f"Expected low-high sorting, but got {prices}" 
    assert_sorted(prices, message="Expected low-high sorting")  


# Price high-low
def test_sort_products_by_orice_high_low(login):
    page = login
    page.select_option("select.product_sort_container", index=3)
    prices = page.locator(".inventory_item_price").all_inner_texts()
    prices = [float(price.replace("$", "")) for price in prices]
    # assert prices == sorted(prices, reverse=True), f"Expected low-high sorting, but got {prices}" 
    assert_sorted(prices, reverse=True, message="Expected high-low sorting")  
    

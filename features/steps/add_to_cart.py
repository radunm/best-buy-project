from behave import when, then


@then("On search results page choose {index_to_click} element and click it")
def choose_product(context, index_to_click):
    context.app.search_results_page.click_list_item(int(index_to_click))


@when("Add product to shopping cart")
def add_to_cart(context):
    context.app.search_results_page.add_to_cart_click()


@then("Expected product would be in cart")
def verify_product_in_cart(context):
    context.app.search_results_page.click_go_to_cart()
    context.app.cart_page.verify_item_in_cart()


@then("Close all pop-ups")
def close_popup(context):
    # There are no pop-ups
    pass
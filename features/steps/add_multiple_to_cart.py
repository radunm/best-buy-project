from behave import then


@then("Return to product search page")
def return_to_page(context):
    context.app.cart_page.previous_page()


@then("Expected products would be in cart")
def verify_products_in_cart(context):
    context.app.search_results_page.click_go_to_cart()
    context.app.cart_page.verify_item_in_cart()
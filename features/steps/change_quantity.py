from behave import when, then


@when("Click go to cart button")
def click_cart(context):
    context.app.search_results_page.click_go_to_cart()


@when("Change quantity from 1 to {quantity}")
def change_quantity(context, quantity):
    context.app.cart_page.select_quantity(quantity)


@then("Expected items in cart will be {quantity}")
def verify_quantity(context, quantity):
    context.app.cart_page.verify_item_in_cart()
    context.app.cart_page.verify_quantity(quantity)
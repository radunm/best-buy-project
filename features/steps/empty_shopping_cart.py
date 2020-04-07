from behave import when, then


@when("Click cart button")
def click_cart(context):
    context.app.main_page.click_cart_button()


@then("Expected cart page will have {expected_text} in the title")
def cart_is_empty(context, expected_text):
    context.app.cart_page.verify_empty_cart(expected_text)
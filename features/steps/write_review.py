from behave import when, then


# @when("Insert {search_words} in search field and click")
# def search_product(context, search_words):
#     context.app.main_page.search_product(search_words)
#     # sleep(2)
#     # context.app.main_page.click_search_button()


@when("Click review button")
def click_review_button(context):
    context.app.product_page.review_click()


@then("Expected product has {expected_text} button")
def verify_write_review_button(context, expected_text):
    context.app.product_page.verify_button(expected_text)
from behave import when, then


@when("Insert {search_word} into search field")
def search_product_name(context, search_word):
    context.app.main_page.search_product_click(search_word)


# @when("Click search button")
# def click_search_button(context):
#     context.app.main_page.click_search_button()


@then("Check that title contains {expected_text}")
def check_title(context, expected_text):
    context.app.search_results_page.check_title(expected_text)
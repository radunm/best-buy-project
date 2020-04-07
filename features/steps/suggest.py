from behave import when, then, given


@given("Open {main} page")
def open_best_buy(context, main):
    context.app.main_page.open()
    # Choose country
    context.app.main_page.choose_country()
    # Close pop-up
    context.app.main_page.close_pop_up()


@when("Insert {search_words} in search field")
def search_product_name(context, search_words):
    context.app.main_page.search_product(search_words)


@when("Wait a couple of seconds")
def wait(context):
    context.app.main_page.wait_all_elements()


@then("See and count {expected_value} suggestions")
def count_suggestions(context, expected_value):
    context.app.main_page.count_list(expected_value)
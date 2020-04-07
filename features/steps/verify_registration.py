from behave import when, then


@when('Click account button')
def account_button(context):
    context.app.main_page.click_account_button()


@when('Best Buy: click "Create account"')
def create_account_button(context):
    context.app.main_page.click_create_account()


@then("Fill all fields with fake data")
def fill_data(context):
    context.app.registration_page.verify_page()
    context.app.registration_page.fill_data()


@when("Click submit")
def click_submit(context):
    context.app.registration_page.click_create_account()


@then("Expected registration will be complete successfully")
def registration_complete(context):
    name = context.app.registration_page.data_list[0]
    context.app.my_account_page.verify_registration(name)
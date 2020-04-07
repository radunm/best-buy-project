from behave import when, then


@when("Click Sign in button")
def click_sign_in(context):
    context.app.main_page.click_sign_in_button()


@when("Fill valid data")
def fill_user_data(context):
    email = context.app.registration_page.data_list[2]
    password = context.app.registration_page.data_list[3]
    context.app.main_page.fill_data(email, password)


@when("Click submit button")
def click_submit(context):
    context.app.main_page.click_submit_button()


@then("Expected login will be complete successfully")
def verify_sign_in(context):
    name = context.app.registration_page.data_list[0]
    context.app.main_page.success_login(name)
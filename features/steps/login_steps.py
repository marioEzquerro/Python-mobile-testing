from behave import *


@given(u'the user is in login page')
def the_user_is_in_login_page(context):
    context.app.login_page.verify_login_page_is_opened()


@given(u'user enters name "{name}" and password "{password}"')
def user_enters_name(context, name, password):
    context.app.login_page.enter_username(name)
    context.app.login_page.enter_password(password)


@when(u'user click iniciar sesion')
def click_login_button(context):
    context.app.login_page.click_login_button()


@then(u'user is logged in')
def user_is_in(context):
    context.app.main_page.verify_main_page_is_open()

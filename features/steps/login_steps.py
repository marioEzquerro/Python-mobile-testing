from behave import *


@given(u'the user is in login page')
def the_user_is_in_login_page(context):
    context.app.login_page.verify_login_page_is_opened()


@given(u'user enters name "{name}"')
def user_enters_name(context, name):
    context.app.login_page.enter_username(name)


@given(u'user enters password "{text}"')
def user_enters_password(context, text):
    context.app.login_page.enter_password(text)


@when(u'user click iniciar sesion')
def click_login_button(context):
    context.app.login_page.click_login_button()


@then(u'user is logged in')
def user_is_in(context):
    context.app.verifyMainPage()

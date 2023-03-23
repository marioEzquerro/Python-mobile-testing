from behave import given, when, then


@given(u'User is in the app')
def user_is_in_the_app(self):
    assert self.app.login_page.user_in_login_page(), 'User in login'


@when(u'User enters username "{name}" and password "{password}" and cliks login button')
def step_def(self, name, password):
    self.app.login_page.enter_username(name)
    self.app.login_page.enter_password(password)
    self.app.login_page.click_login()


@then(u'User is in main page')
def step_def(self):
    assert self.app.onboarding_page.user_in_onboarding_page(), 'Not logged in'

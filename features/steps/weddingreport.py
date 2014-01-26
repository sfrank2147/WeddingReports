from config import BASE_URL

@when('I load the login page')
def step_impl(context):
    context.browser.get(BASE_URL + '/login')

@when('I log in')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('email').send_keys('test@email.com')
    br.find_element_by_name('password').send_keys('test')
    br.find_element_by_id('submit').click()

@then('I should be logged in')
def step_impl(context):
    assert 'Logged in as test@email.com' in \
            context.browser.find_element_by_id('login-status').text






@when('I log out')
def step_impl(context):
    context.browser.find_element_by_id('logout').click()

@then('I should be logged out')
def step_imple(context):
    assert 'Not logged in' in \
            context.browser.find_element_by_id('login-status').text
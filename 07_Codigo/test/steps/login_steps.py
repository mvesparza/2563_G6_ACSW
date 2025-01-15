from behave import given, when

@given('I have registered a user with username "{username}" and password "{password}"')
def step_register_user_for_login(context, username, password):
    context.simulator.register_user(username, password)

@when('I login with username "{username}" and password "{password}"')
def step_login_user(context, username, password):
    context.result = context.simulator.verify_user(username, password)

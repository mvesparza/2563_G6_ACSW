from behave import when

@when('I register a user with username "{username}" and password "{password}"')
def step_register_user(context, username, password):
    context.result = context.simulator.register_user(username, password)

@given('I register a user with username "{username}" and password "{password}"')
def step_register_user_given(context, username, password):
    context.result = context.simulator.register_user(username, password)

@when('I try to register the same user with username "{username}" and password "{password}"')
def step_register_duplicate_user(context, username, password):
    context.result = context.simulator.register_user(username, password)

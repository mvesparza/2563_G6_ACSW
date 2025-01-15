from behave import given, when

@given('I have captured facial data for the user "{username}"')
def step_capture_facial_data(context, username):
    context.simulator.register_user(username, "password")  # Registra el usuario
    context.result = context.simulator.capture_face(username)

@when('I verify the user "{username}" with face recognition')
def step_verify_face(context, username):
    context.result = context.simulator.verify_face(username)

@when('I try to verify the user "{username}" with face recognition')
def step_verify_unregistered_face(context, username):
    context.result = context.simulator.verify_face(username)

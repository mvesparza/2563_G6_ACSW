from behave import given, then
from SimuladorBiometrico import BiometricSimulator

@given('the BiometricSimulator is running')
def step_setup_simulator(context):
    """Inicializa el simulador biométrico para las pruebas."""
    context.simulator = BiometricSimulator()
    print("BiometricSimulator initialized.")

@then('the system should confirm "{message}"')
def step_verify_message(context, message):
    """Verifica que el sistema confirma un mensaje esperado."""
    assert context.result == message, f"Expected '{message}' but got '{context.result}'"

@then('the system should show an error "{message}"')
def step_verify_error_message(context, message):
    """Verifica que el sistema muestra un mensaje de error esperado."""
    assert context.result == message, f"Expected '{message}' but got '{context.result}'"

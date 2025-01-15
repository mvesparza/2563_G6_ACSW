Feature: Register a user successfully
  As a user
  I want to register a user
  So that I can use the system

  Scenario: Successfully register a new user
    Given the BiometricSimulator is running
    When I register a user with username "new_user" and password "secure_password"
    Then the system should confirm "Usuario new_user registrado con éxito."

Feature: User Registration
  As a user
  I want to register an account
  So that I can use the system

  Scenario: Register a new user successfully
    Given the BiometricSimulator is running
    When I register a user with username "test_user8" and password "secure_password"
    Then the system should confirm "Usuario test_user8 registrado con éxito."

  Scenario: Attempt to register a duplicate user
    Given the BiometricSimulator is running
    And I register a user with username "duplicate_user" and password "password123"
    When I try to register the same user with username "duplicate_user" and password "password123"
    Then the system should show an error "Error: El nombre de usuario ya está en uso."

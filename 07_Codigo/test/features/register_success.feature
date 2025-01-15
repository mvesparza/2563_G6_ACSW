Feature: Registro nuevo usuario
  As a user
  I want to register a user
  So that I can use the system

  Scenario: Successfully register a new user
    Given the BiometricSimulator is running
    When I register a user with username "Jose" and password "secure_password"
    Then the system should confirm "Usuario Jose registrado con éxito."

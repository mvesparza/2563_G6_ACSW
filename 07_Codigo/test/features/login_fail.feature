Feature: Login fails with invalid credentials
  As a user
  I want to log in to my account
  So that I can access the system

  Scenario: Fail to login with invalid credentials
    Given the BiometricSimulator is running
    When I login with username "invalid_user" and password "wrong_password"
    Then the system should show an error "Error: Credenciales incorrectas."

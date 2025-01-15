Feature: User Login
  As a user
  I want to log in to my account
  So that I can access the system

  Scenario: Login with valid credentials
    Given the BiometricSimulator is running
    And I have registered a user with username "test_user" and password "password"
    When I login with username "test_user" and password "password"
    Then the system should confirm "¡Bienvenido, test_user!"

  Scenario: Login with invalid credentials
    Given the BiometricSimulator is running
    When I login with username "wrong_user" and password "wrong_password"
    Then the system should show an error "Error: Credenciales incorrectas."

  

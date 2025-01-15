Feature: Login successfully
  As a user
  I want to log in to my account
  So that I can access the system

  Scenario: Successfully login with valid credentials
    Given the BiometricSimulator is running
    And I have registered a user with username "valid_user" and password "secure_password"
    When I login with username "valid_user" and password "secure_password"
    Then the system should confirm "¡Bienvenido, valid_user!"

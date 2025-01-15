Feature: Biometric Authentication
  As a user
  I want to use biometric authentication
  So that I can securely log in

  Scenario: Verify face recognition for a registered user
    Given the BiometricSimulator is running
    And I have captured facial data for the user "test_user"
    When I verify the user "test_user" with face recognition
    Then the system should confirm "¡Bienvenido, test_user!"

  Scenario: Verify face recognition fails for an unregistered user
    Given the BiometricSimulator is running
    When I try to verify the user "unregistered_user" with face recognition
    Then the system should show an error "Error: No hay datos faciales almacenados para este usuario."

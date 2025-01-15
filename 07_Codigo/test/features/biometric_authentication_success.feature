Feature: Rostro Verificado
  As a user
  I want to use biometric authentication
  So that I can securely log in

  Scenario: Successfully verify face recognition for a registered user
    Given the BiometricSimulator is running
    And I have captured facial data for the user "registered_user"
    When I verify the user "registered_user" with face recognition
    Then the system should confirm "¡Bienvenido, registered_user!"

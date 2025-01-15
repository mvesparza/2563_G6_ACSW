Feature: Rostro no Verificado
  As a user
  I want to use biometric authentication
  So that I can securely log in

  Scenario: Fail to verify face recognition for an unregistered user
    Given the BiometricSimulator is running
    When I try to verify the user "unregistered_user" with face recognition
    Then the system should show an error "Error: No hay datos faciales almacenados para este usuario."

Feature: Create New Rent Contract
  Scenarios related to the creation and activation of a rent smart contract.

@CreateRentContract
Scenario: Create a rent contract succeeding
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And today is 10
 When the contract is created today
 Then the contract landlord must be Landlord01
  And the contract tenant must be Tenant01
  And the contract tenant address must be Address01
  And the contract total value must be 24000
  And the contract monthly value must be 2000
  And the contract months quantity must be 12
  And the contract creation day must be 10
  And the contract effective day must be 30
  And the contract status must be Created

@ActivateRentContract
Scenario: Activate a rent contract succeeding
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And the creation date 10
  And the contract is created
 When today is 30
  And the contract is activated today
 Then the contract status must be InEffect

@ActivateRentContractUnsuccessfully
Scenario: Activate a rent contract with no success
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And the creation date 10
  And the contract is created
 When today is 20
  And the contract is activated today
 Then the contract status must be Created





  
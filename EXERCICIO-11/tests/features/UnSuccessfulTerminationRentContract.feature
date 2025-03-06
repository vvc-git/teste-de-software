Feature: Unsuccessful Terminate Rent Contract
  Scenarios related to the unsuccessful termination of a rent smart contract.


@UnsuccessfulTerminationRentContract
Scenario: Terminate contract due to late payment
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And the creation date 10
  And the contract is created
  And the contract is activated
  And a monthly payment is done on day 40
When a monthly payment is done on day 100
Then the contract status must be UnsuccessfulTermination


@UnsuccessfulTerminationRentContractDueToWater
Scenario: Terminate contract due to water payment
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And the creation date 10
  And the contract is created
  And the contract is activated
  And a monthly payment is done on day 40
  And a monthly payment is done on day 70
  And a monthly payment is done on day 100
  And a monthly payment is done on day 130
  And a monthly payment is done on day 160
  And a monthly payment is done on day 190
  And missed the water bill payment
  And a monthly payment is done on day 220
  And a monthly payment is done on day 250
  And a monthly payment is done on day 280
  And a monthly payment is done on day 310
  And a monthly payment is done on day 340
When a monthly payment is done on day 370
Then the contract status must be UnsuccessfulTermination

@UnsuccessfulTerminationRentContractDueToTax
Scenario: Terminate contract due to tax payment
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12
  And the effective date of the contract 30
  And the creation date 10
  And the contract is created
  And the contract is activated
  And a monthly payment is done on day 40
  And a monthly payment is done on day 70
  And a monthly payment is done on day 100
  And a monthly payment is done on day 130
  And a monthly payment is done on day 160
  And a monthly payment is done on day 190
  And missed the tax payment
  And a monthly payment is done on day 220
  And a monthly payment is done on day 250
  And a monthly payment is done on day 280
  And a monthly payment is done on day 310
  And a monthly payment is done on day 340
When a monthly payment is done on day 370
Then the contract status must be UnsuccessfulTermination
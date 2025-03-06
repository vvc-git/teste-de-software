Feature: Successful Terminate Rent Contract
  Scenarios related to the successful termination of a rent smart contract.

@MonthlyPaymentsRentContract
Scenario: Pay 4 monthly payments
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
 When a monthly payment is done on day 110
 Then the contract status must be InEffect
  And 4 payments have been done
  And payment month 1 was on day 40
  And payment month 2 was on day 70
  And payment month 3 was on day 100
  And payment month 4 was on day 110


@OneYearPaymentRentContract
Scenario: Terminate a rent contract succeeding
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
  And a monthly payment is done on day 220
  And a monthly payment is done on day 250
  And a monthly payment is done on day 280
  And a monthly payment is done on day 310
  And a monthly payment is done on day 340
 When a monthly payment is done on day 370
  Then the contract status must be SuccessfulTermination
  And the local availability is true

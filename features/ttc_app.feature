Feature: BDD Demo

Scenario: Test order submission
   Given User is on Home Page "http://0.0.0.0:5000/" on browser "chrome"
     When User confirms Address
     And User selects product as "Umbrella"
     And User selects valid payment
     And User clicks on "Request" button
     Then Message displayed is Order Status
     Then close browser

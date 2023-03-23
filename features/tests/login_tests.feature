Feature: User logs in the app

    Scenario Outline: Login with valid credentials
        Given User is in the app
        When User enters username "<NAME>" and password "<PASSWORD>" and cliks login button
        Then User is in main page
        Examples:
            | NAME                    | PASSWORD     |
            | toulouselunde@gmail.com | Toulouse2021 |



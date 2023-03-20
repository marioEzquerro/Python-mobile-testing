Feature: Bodegas torres

    Scenario Outline: Log in using correct credentials
        Given user enters name "<USERNAME>" and password "<PASSWORD>"
        When user click iniciar sesion
        Then user is logged in
        Examples:
            | USERNAME              | PASSWORD |
            | mezquerro@hiberus.com | 12345    |

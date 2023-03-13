Feature: Bodegas torres

    Scenario Outline: Iniciar sesion
        Given user enters name "<USERNAME>"
        Given user enters password "<PASSWORD>"
        When user click iniciar sesion
        Then user is logged in
        Examples:
            | USERNAME              | PASSWORD |
            | mezquerro@hiberus.com | 12345    |

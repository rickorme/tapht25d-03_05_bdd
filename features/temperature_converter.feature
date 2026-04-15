Feature: Temperature Converter

    Scenario: Convert 32 Fahrenheit to Celsius
        Given the temperature is 32 Fahrenheit
        When the temperature is converted to Celsius
        Then the result should be 0 Celsius

    Scenario: Convert 0 Fahrenheit to Celsius
        Given the temperature is 0 Fahrenheit
        When the temperature is converted to Celsius
        Then the result should be -17.77777 Celsius

    Scenario: Convert 100 Fahrenheit to Celsius
        Given the temperature is 100 Fahrenheit
        When the temperature is converted to Celsius
        Then the result should be 37.77777 Celsius     

    Scenario: Convert 212 Fahrenheit to Celsius
        Given the temperature is 212 Fahrenheit
        When the temperature is converted to Celsius
        Then the result should be 100 Celsius     


    Scenario: Convert 0 Celsius to Fahrenheit
        Given the temperature is 0 Celsius
        When the temperature is converted to Fahrenheit
        Then the result should be 32 Fahrenheit

    Scenario: Convert -40 Celsius to Fahrenheit
        Given the temperature is -40 Celsius
        When the temperature is converted to Fahrenheit
        Then the result should be -40 Fahrenheit

    Scenario: Convert -10 Celsius to Fahrenheit
        Given the temperature is -10 Celsius
        When the temperature is converted to Fahrenheit
        Then the result should be 14 Fahrenheit

    Scenario: Convert 37.77777 Celsius to Fahrenheit
        Given the temperature is 37.77777 Celsius
        When the temperature is converted to Fahrenheit
        Then the result should be 100 Fahrenheit

    Scenario: Convert 100 Celsius to Fahrenheit
        Given the temperature is 100 Celsius
        When the temperature is converted to Fahrenheit
        Then the result should be 212 Fahrenheit
    
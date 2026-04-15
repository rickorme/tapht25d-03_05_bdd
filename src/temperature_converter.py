class TemperatureConverter:
    
    def __init__(self):
        pass

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) / 1.8
        return celsius
    

    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit
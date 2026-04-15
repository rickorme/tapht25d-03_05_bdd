import pytest
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from src.temperature_converter import TemperatureConverter

@given(u'the temperature is {fahrenheit} Fahrenheit')
def step_given_fahrenheit(context, fahrenheit):
    context.converter = TemperatureConverter()
    context.fahrenheit = float(fahrenheit)
    # raise StepNotImplementedError(u'Given the temperature is {fahrenheit} Fahrenheit')

@given(u'the temperature is {celsius} Celsius')
def step_given_celsius(context, celsius):
    context.converter = TemperatureConverter()
    context.celsius = float(celsius)
    # raise StepNotImplementedError(u'Given the temperature is {celsius} Celsius')

@when(u'the temperature is converted to Celsius')
def step_when_convert_to_celsius(context):
    context.celsius = context.converter.fahrenheit_to_celsius(context.fahrenheit)
    # raise StepNotImplementedError(u'When the temperature is converted to Celsius')

@when(u'the temperature is converted to Fahrenheit')
def step_when_convert_to_fahrenheit(context):
    context.fahrenheit = context.converter.celsius_to_fahrenheit(context.celsius)
    # raise StepNotImplementedError(u'When the temperature is converted to Fahrenheit')    


@then(u'the result should be {celsius} Celsius')
def step_then_celsius_result(context, celsius):
    celsius = float(celsius)
    assert context.celsius == pytest.approx(celsius), f'Expected {celsius} but got {context.celsius}'
    # raise StepNotImplementedError(u'Then the result should be {celsius} Celsius')


@then(u'the result should be {fahrenheit} Fahrenheit')
def step_then_celsius_result(context, fahrenheit):
    fahrenheit = float(fahrenheit)
    assert context.fahrenheit == pytest.approx(fahrenheit), f'Expected {fahrenheit} but got {context.fahrenheit}'
    # raise StepNotImplementedError(u'Then the result should be {fahrenheit} Fahrenheit')


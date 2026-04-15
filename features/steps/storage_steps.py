
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from src.storage import Stock, StockItem

from behave.api.pending_step import StepNotImplementedError
@given(u'the stock is currently empty')
def step_given_empty_stock(context):
    context.stock = Stock()
    # raise StepNotImplementedError(u'Given the stock is currently empty')


@when(u'I add a product named "{product_name}" with an amount of {amount}')
def step_when_add_product(context, product_name, amount):
    context.product = StockItem(product_name, int(amount))
    context.stock.add_product(context.product)
    # raise StepNotImplementedError(u'When I add a product named "Mac mini M4" with an amount of 20')


@then(u'the stock should contain 1 item')
def step_then_stock_contains_item(context):
    assert len(context.stock.items) == 1, f'Expected stock to contain 1 item but got {len(context.stock)}'


@then(u'the product "{product_name}" should have an amount of {expected_amount}')
def step_then_product_has_amount(context, product_name, expected_amount):
    context.product = context.stock.get_product(product_name)
    assert context.product.name == product_name, f'Expected product name to be "{product_name}" but got "{context.stock.items[0].name}"'
    assert context.product.amount == int(expected_amount), f'Expected product amount to be {expected_amount} but got {context.stock.items[0].amount}'
    # raise StepNotImplementedError(u'Then the product "{product_name}" should have an amount of {expected_amount}')


@given(u'the stock already contains a product named "{product_name}" with an amount of {amount}')
def step_given_existing_product(context, product_name, amount):
    context.stock = Stock()
    context.product = StockItem(product_name, int(amount))
    context.stock.add_product(context.product)
    # raise StepNotImplementedError(u'Given the stock already contains a product named "{product_name}" with an amount of {amount}')


@when(u'I reduce the amount of "{product_name}" by {amount}')
def step_when_reduce_amount(context, product_name, amount):
    context.errors = []
    try:
        context.stock.reduce_stock(product_name, int(amount))
    except ValueError as e:
        context.errors.append(str(e))
    # raise StepNotImplementedError(u'When I reduce the amount of "{product_name}" by {amount}')


@then(u'the product {product_name} should have an amount of {expected_amount}')
def step_then_product_has_amount(context, product_name, expected_amount):
    raise StepNotImplementedError(u'Then the product {product_name} should have an amount of {expected_amount}')

@then(u'I should get an error saying there is not enough in stock')
def step_then_not_enough_in_stock(context):
    assert context.errors[0] == f"Not enough in stock!", f'Expected error message to be "Not enough stock!" but got "{context.errors[0]}"'
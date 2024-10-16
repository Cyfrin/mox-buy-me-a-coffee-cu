import boa

from conftest import SEND_VALUE


def test_can_fund_and_withdraw(coffee, account):
    coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SEND_VALUE

    coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0


def test_can_fund_and_withdraw_two(coffee, account):
    coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SEND_VALUE

    coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0


def test_can_fund_and_withdraw_three(coffee, account):
    coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SEND_VALUE

    coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0


def test_can_fund_and_withdraw_four(coffee, account):
    coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SEND_VALUE
    coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0

import boa

from conftest import SEND_VALUE


def test_can_fund_and_withdraw(coffee, account):
    # Arrange / Act
    coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SEND_VALUE
    coffee.withdraw()

    # Assert
    assert boa.env.get_balance(coffee.address) == 0

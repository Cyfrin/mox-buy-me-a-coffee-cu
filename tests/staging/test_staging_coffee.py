from moccasin.config import get_active_network
import pytest
import boa
from script.deploy import deploy_coffee
from eth_utils import to_wei

active_network = get_active_network()

SENT_VALUE = to_wei(1, "ether")

if not active_network.prompt_live:
    pytest.skip("Skipping this test file", allow_module_level=True)


@pytest.mark.ignore_isolation
def test_can_fund_and_withdraw_live():
    coffee = deploy_coffee()
    account = active_network.get_default_account()
    coffee.fund(value=SENT_VALUE)
    amount_funded = coffee.address_to_amount_funded(account.address)
    assert amount_funded == SENT_VALUE
    coffee.withdraw()
    assert boa.env.get_balance(coffee.address) == 0

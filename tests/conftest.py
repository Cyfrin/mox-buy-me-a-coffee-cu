import pytest
from script.deploy import deploy_coffee
from moccasin.fixture_tools import request_fixtures
from moccasin.config import get_active_network
import boa
from eth_utils import to_wei

SEND_VALUE = to_wei(1, "ether")

request_fixtures([("price_feed", "eth_usd")], scope="session")


@pytest.fixture(scope="session")
def account():
    return get_active_network().get_default_account()


@pytest.fixture(scope="function")
def coffee(eth_usd):
    return deploy_coffee()


@pytest.fixture(scope="function")
def coffee_funded(coffee):
    boa.env.set_balance(coffee.OWNER(), SEND_VALUE * 2)
    with boa.env.prank(coffee.OWNER()):
        coffee.fund(value=SEND_VALUE)
    return coffee

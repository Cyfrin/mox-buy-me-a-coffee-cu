from src.mocks import mock_v3_aggregator
from eth_utils import to_wei


STARTING_DECIMALS = 8
STARTING_PRICE = to_wei(2000, "ether")


def deploy_feed():
    return mock_v3_aggregator.deploy(STARTING_DECIMALS, STARTING_PRICE)


def moccasin_main():
    return deploy_feed()
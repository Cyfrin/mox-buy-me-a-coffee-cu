from src.mocks import mock_v3_aggregator
from eth_utils import to_wei


STARTING_DECIMALS = 8
STARTING_PRICE = to_wei(2000, "ether")


def moccasin_main():
    price_feed = mock_v3_aggregator.deploy(STARTING_DECIMALS, STARTING_PRICE)
    return price_feed

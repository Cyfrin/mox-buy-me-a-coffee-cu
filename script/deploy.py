from src import buy_me_a_coffee
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_coffee() -> VyperContract:
    active_network = get_active_network()
    price_feed = active_network.manifest_contract("price_feed")

    print("Using price feed:", price_feed.address)
    coffee: VyperContract = buy_me_a_coffee.deploy(price_feed.address)

    print("Deployed coffee contract at:", coffee.address)
    return coffee


def moccasin_main() -> VyperContract:
    return deploy_coffee()

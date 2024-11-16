from src import buy_me_a_coffee
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_coffee(price_feed: VyperContract) -> VyperContract:
    print("Using price feed:", price_feed.address)
    coffee: VyperContract = buy_me_a_coffee.deploy(price_feed.address)
    print("Deployed coffee contract at:", coffee.address)
    return coffee


def moccasin_main() -> VyperContract:
    active_network = get_active_network()
    price_feed = active_network.manifest_named("price_feed")
    coffee = deploy_coffee(price_feed)
    if active_network.has_explorer() and active_network.is_local_or_forked_network() is False:
        print("Verifying contract on explorer...")
        result = active_network.moccasin_verify(coffee)
        result.wait_for_verification()
    return coffee

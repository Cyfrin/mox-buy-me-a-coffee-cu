from eth_utils import to_wei
import boa

SEND_VALUE = to_wei(1, "ether")


def test_eth_usd_fixture(eth_usd, coffee):
    assert coffee.price_feed() == eth_usd.address


def test_deploy(coffee, account):
    assert coffee.MINIMUM_USD() == to_wei(50, "ether")
    assert coffee.OWNER() == account.address


def test_price_feed_set_correctly(coffee):
    expected_version = 4
    price_feed_version = coffee.get_version()
    assert price_feed_version == expected_version


def test_fund_fails_without_enough_eth(coffee):
    with boa.reverts():
        coffee.fund()


def test_fund_updates_funded_data_structure(coffee):
    boa.env.set_balance(coffee.OWNER(), SEND_VALUE * 2)
    with boa.env.prank(coffee.OWNER()):
        coffee.fund(value=SEND_VALUE)
    amount_funded = coffee.address_to_amount_funded(coffee.OWNER())
    assert amount_funded == SEND_VALUE


def test_adds_funder_to_array_of_funders(coffee):
    boa.env.set_balance(coffee.OWNER(), SEND_VALUE * 2)
    with boa.env.prank(coffee.OWNER()):
        coffee.fund(value=SEND_VALUE)
    funder = coffee.funders(0)
    assert funder == coffee.OWNER()


def test_withdraw_from_single_funder(coffee_funded):
    starting_fund_me_balance = boa.env.get_balance(coffee_funded.address)
    starting_owner_balance = boa.env.get_balance(coffee_funded.OWNER())
    with boa.env.prank(coffee_funded.OWNER()):
        coffee_funded.withdraw()
    ending_fund_me_balance = boa.env.get_balance(coffee_funded.address)
    ending_owner_balance = boa.env.get_balance(coffee_funded.OWNER())
    assert ending_fund_me_balance == 0
    assert ending_owner_balance == starting_owner_balance + starting_fund_me_balance

# Challenge! Try to implement the following test on your own!
# def test_withdraw_from_multiple_funders(coffee_funded):
#     number_of_funders = 10
#     for i in range(number_of_funders):
#         user = boa.env.generate_address(i)
#         boa.env.set_balance(user, SEND_VALUE * 2)
#         with boa.env.prank(user):
#             coffee_funded.fund(value=SEND_VALUE)
#     starting_fund_me_balance = boa.env.get_balance(coffee_funded.address)
#     starting_owner_balance = boa.env.get_balance(coffee_funded.OWNER())

#     with boa.env.prank(coffee_funded.OWNER()):
#         coffee_funded.withdraw()

#     assert boa.env.get_balance(coffee_funded.address) == 0
#     assert starting_fund_me_balance + starting_owner_balance == boa.env.get_balance(
#         coffee_funded.OWNER()
#     )

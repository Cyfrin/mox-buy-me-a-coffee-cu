from src.example_contracts import fun_with_storage
from moccasin.config import get_active_network
import boa

def deploy_storage():
    fws = fun_with_storage.deploy()

    active_network = get_active_network()
    if active_network.has_explorer():
        print("Verifying contract on explorer...")
        result = active_network.moccasin_verify(fws)
        result.wait_for_verification()

    # You can access private variables!
    print(f"favorite_number is {fws._storage.favorite_number.get()}")
    # You can get the immutables!
    print(f"Immutables: {fws._immutables.IMMUTABLE_NOT_IN_STORAGE}")
    # You can call directly from storage slots!
    print(f"Value at storage slot 0: {boa.env.get_storage(fws.address, 0)}")
    # First element of the fixed array:
    print(f"First element of the fixed array: {boa.env.get_storage(fws.address, 2)}")
    # Length of the dyn array:
    print(f"Length of the dyn array: {boa.env.get_storage(fws.address, 1002)}")
    # First element in dyn array
    print(f"First element in dyn array: {boa.env.get_storage(fws.address, 1003)}")
    # Mapping placeholder
    print(f"Mapping placeholder: {boa.env.get_storage(fws.address, 1103)}")
    # First element of mapping
    slot = 1103  # Slot of mapping
    k = 0        # Key
    location = boa.eval(f"convert(keccak256(concat(convert({slot},bytes32), convert({k}, bytes32))), uint256)")
    print(f"Location: {location}")
    print(f"Storage of element: {boa.env.get_storage(fws.address, location)}")

def moccasin_main():
    deploy_storage()
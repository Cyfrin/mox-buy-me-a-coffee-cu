# pragma version 0.4.0
# pragma enable-decimals
"""
@license MIT
"""

favorite_number: uint256  # Stored at slot 0
some_bool: bool  # Stored at slot 1
my_fixed_array: uint256[1000]  # First element stored at slot 2, no "length" concept
# All elements come after the length
my_dyn_array: DynArray[uint256, 100] # Length stored at slot 1002
my_map: HashMap[uint256, bool]  # Length stored at slot 1103

NOT_IN_STORAGE: constant(uint256) = 123
IMMUTABLE_NOT_IN_STORAGE: immutable(uint256)

@deploy
def __init__():
    self.favorite_number = 25
    self.some_bool = True
    self.my_fixed_array[0] = 222
    self.my_dyn_array.append(333)
    self.my_map[0] = True # Where do you think this stored (check script!)
    IMMUTABLE_NOT_IN_STORAGE = 123

@external
def doStuff():
    new_var: uint256 = self.favorite_number + 1  # SLOAD
    otherVar: bool = self.some_bool  # memory Variable

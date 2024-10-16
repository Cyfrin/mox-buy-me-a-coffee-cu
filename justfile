tests:
    mox test 
    mox test --network sepolia --fork 

test-staging:
    mox test --network sepolia --account default

uvx-tests:
    uvx moccasin test 
    uvx moccasin test --network sepolia --fork

uvx-test-staging:
    uvx moccasin test --network sepolia --account default
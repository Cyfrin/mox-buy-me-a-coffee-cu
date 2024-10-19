# This is a dummy private key, don't worry
deploy:
    mox run deploy --network anvil --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

# This is a dummy private key, don't worry
deploy-zk:
    mox run deploy --network zksync-local --private-key 0x3d3cbc973389cb26f657686445bcc75662b415b656078503592ac8c1abb8810e

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
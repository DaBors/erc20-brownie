from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import OurToken, network, config

initial_supply = Web3.toWei(21_000_000, "ether")

def deploy_token():
    account = get_account()
    token = OurToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed token!")
    return token

def main():
    deploy_token()


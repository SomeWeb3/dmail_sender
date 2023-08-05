import time
from random import randint, shuffle

from eth_account.signers.local import LocalAccount
from loguru import logger
from random_username.generate import generate_username
from web3 import Account, Web3

from config import RANDOM_WALLETS_ORDER, RPC, SLEEP, WALLETS_FILE, ZK_MAIL_ADDRESS


logger.add("log/debug.log")
w3 = Web3(Web3.HTTPProvider(RPC))


def load_wallets() -> list[LocalAccount]:
    """Загрузка кошельков из файла."""

    with open(WALLETS_FILE, "r") as file:
        return [Account.from_key(line.strip()) for line in file.read().split("\n")]


def generate_data(address: str) -> str:
    """Генерация случайно почты получателя и валидных данных для транзакции."""

    mail = generate_username()[0] + "@gmail.com"
    mail = w3.to_hex(text=mail)[2:]
    mail += "0" * (64 - len(mail))
    from_mail = address.lower() + "@dmail.ai"
    data = (
        "0x5b7d7482"
        + "0000000000000000000000000000000000000000000000000000000000000040"
        + "00000000000000000000000000000000000000000000000000000000000000a0"
        + "0000000000000000000000000000000000000000000000000000000000000033"
        + w3.to_hex(text=from_mail)[2:]
        + "00000000000000000000000000"
        + "0000000000000000000000000000000000000000000000000000000000000012"
        + mail
    )

    return data


def send_mail(wallet: LocalAccount) -> None:
    """Отправка письма-транзакции."""

    data = generate_data(wallet.address)
    dict_transaction = {
        "chainId": w3.eth.chain_id,
        "from": wallet.address,
        "to": w3.to_checksum_address(ZK_MAIL_ADDRESS),
        "gasPrice": w3.eth.gas_price,
        "data": data,
        "nonce": w3.eth.get_transaction_count(wallet.address),
    }

    dict_transaction["gas"] = w3.eth.estimate_gas(dict_transaction)
    signed_tx = wallet.sign_transaction(dict_transaction)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    logger.success(
        f"Send email from {wallet.address}. Tx: https://explorer.zksync.io/tx/{tx_hash.hex()}"
    )


def sleep() -> None:
    """Случайная задержка между кошельками."""

    sleep_amount = randint(*SLEEP)
    logger.info(f"Sleep {sleep_amount} sec")
    time.sleep(sleep_amount)


def main() -> None:
    wallets = load_wallets()

    if RANDOM_WALLETS_ORDER:
        shuffle(wallets)

    for wallet in wallets:
        send_mail(wallet)
        if wallet != wallets[-1]:
            sleep()


if __name__ == "__main__":
    main()

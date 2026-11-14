import time


class BankAccount:
    def __init__(self, initial_balance: int):
        self.balance_ = initial_balance

    def deposit(self, amount: int) -> None:
        current = self.balance_
        time.sleep(0.001)
        self.balance_ = current + amount

    def withdraw(self, amount: int) -> bool:
        if self.balance_ < amount:
            return False

        time.sleep(0.001)  # sleep symuluje czas miedzy sprawdzilem saldo a zaktualizowalem balance

        self.balance_ -= amount
        return True

    def getBalance(self) -> int:
        return self.balance_


if __name__ == "__main__":
    ba = BankAccount(10000)
    print(ba.balance_)
    results = []

    start = time.perf_counter()
    for _ in range(10):
        results.append(ba.withdraw(1000))   # jedna po drugiej, bez watkow
    elapsed = time.perf_counter() - start

    print("udane wypłaty:", results.count(True))
    print("saldo:", ba.getBalance())
    print(f"czas: {elapsed:.4f} s")
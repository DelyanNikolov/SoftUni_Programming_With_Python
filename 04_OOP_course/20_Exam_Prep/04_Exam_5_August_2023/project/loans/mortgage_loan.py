from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    LOAN_AMOUNT = 50_000.0
    INTEREST_INCREASE = 0.5

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INTEREST_INCREASE

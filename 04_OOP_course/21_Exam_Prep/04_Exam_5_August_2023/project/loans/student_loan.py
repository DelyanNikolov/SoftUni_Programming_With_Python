from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    LOAN_AMOUNT = 2000.0
    INTEREST_INCREASE = 0.2

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INTEREST_INCREASE

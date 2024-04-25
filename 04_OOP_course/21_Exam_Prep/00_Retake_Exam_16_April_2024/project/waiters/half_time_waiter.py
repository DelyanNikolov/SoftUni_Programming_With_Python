from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    hourly_wage = 12.0

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        earnings = self.hours_worked * self.hourly_wage
        return earnings

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."

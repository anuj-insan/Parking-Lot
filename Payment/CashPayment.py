from Payment.Payment import Payment

class CashPayment(Payment):
    def pay(self, amount):
        print("Cash payment done for amount")
        return True
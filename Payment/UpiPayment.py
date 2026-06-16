from Payment.Payment import Payment

class UpiPayment(Payment):
    def pay(self, amount):
        print("Upi payment done for amount")
        return True
class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >=amount:
            self.account_balance -=amount
            print(f"{amount} Kes sent to {recipient} successfully")
        else:
         print("insufficient funds")

#child classes
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,ID_number):
        super().__init__(account_balance,phone_number)
        self.ID_number = ID_number
    def buyairtime(self,amount):
       if self.account_balance >=amount:
          self.account_balnce -=amount
          print(f"{amount} has successfully been credited")
       else:
           print("insufficient")
class BuisnessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,buisness_name):
     super().__init__(account_balance,phone_number)
     self.buisness_name =buisness_name
    def recieve_payment(self,amount,recipient):

            self.account_balance +=amount
            print(f"{amount} from {recipient}")
Personal=PersonalMpesa(1450,799222344,4555555)
Personal.send_money(1000,799222344)

buisness=BuisnessMpesa(2000,724599206,buisness_name="natax")
buisness.recieve_payment(1000,724599206)



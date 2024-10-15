class ATM:
    def __init__(self):
        self.choice = None
        self.PIN = None
        self.Balance = 0
        self.menu()

    def menu(self):

        print(" 1. Create Pin \n 2. Reset Pin \n 3. Check Balance \n 4. Add balance \n 5. Remove balance \n 6. Exit")
        self.choice = int(input("Enter your choice: "))

        if self.choice == 1:
            print(self.create_pin())
            self.menu()
        elif self.choice == 2:
            print(self.reset_pin())
            self.menu()
        elif self.choice == 3:
            print(self.check_balance())
            self.menu()
        elif self.choice == 4:
            self.add_money()
            self.menu()
        elif self.choice == 5:
            print(self.withdraw_money())
            self.menu()
        elif self.choice == 6:
            print("The program is exited successfully..........")
        else:
            print("Bad choice try again !")
            self.menu()

    def create_pin(self):

        if self.PIN is None:
             self.PIN = input("Enter your PIN: ")
             return "PIN created successfully"
        else:
             return "PIN already exists"


    def reset_pin(self):
       old_PIN = input("Enter existing PIN: ")

       if old_PIN == self.PIN and self.PIN is not None:
           self.PIN = input("Enter your new PIN: ")
           while old_PIN == self.PIN:
              self.PIN =  input("This is your old PIN try with a new PIN: ")
           return 'PIN reset successfully'
       else:
           return 'PIN not matched'



    def check_balance(self):

        if self.PIN == input("Enter PIN: "):
            return f'Your current balance is {self.Balance}'
        else:
            return "PIN not matched"

    def add_money(self):
        money = int(input("Enter the amount you want to deposit: "))
        self.Balance = self.Balance + money


    def withdraw_money(self):

        if self.PIN == input("Enter your PIN: "):
            if self.Balance != 0:
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount <= self.Balance:
                    self.Balance = self.Balance - amount
                else:
                    return "You don't have that much of money"
            else:
               return "Your balance is 0 please recharge!!!"
        else:
            return 'PIN not matched try again!!!'


a1 = ATM()
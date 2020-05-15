########################################
# Team Activity 09, CS241
# Author: Will Brown
# Brother N.Parrish
########################################

class BalanceError(Exception):
    
    def __init__(self, message):
        
        super().__init__(message)
        
        
class OutofChecksError(Exception):
    
    def __init__(self, message):
        
        super().__init__(message)

class CheckingAccount:
    
    def __init__(self, balance, check_count):
        
        if balance < 0.0:
            raise BalanceError("Starting balance cannot be negative")
        
        self.balance = 0.0
        self.check_count =0
        
    def deposit(self, amount):
        
        self.balance += amount
        
    def write_check(self, amount):  
        
        if (self.balance - amount) < 0:
            raise BalanceError("Balance cannot be negative")
        
        if self.check_count <= 0:
            raise OutofChecksError("Insufficient number of checks")
        
        self.balance -= amount
        self.check_count -= 1
        
        
    def display(self):
        
        print()
        print("The current balance is: {:.2f}".format(self.balance))
        print("The current amount of checks is: {}".format(self.check_count))
        
    def apply_for_credit(self):
        
        pass
    
    
def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            acc = CheckingAccount(balance, num_checks)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))
            acc.write_check(amount)
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()
        
        
              
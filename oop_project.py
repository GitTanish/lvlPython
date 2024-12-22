from bank_account import *

Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(100)

Dave.transfer(10,Sara)

Jim = InterestRewardsAcct(1000, 'Jim')
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)

Tabitha = SavingsAcct(1000,'Tabitha')
Tabitha.getBalance()
Tabitha.deposit(100)
Tabitha.transfer(10000, Sara)
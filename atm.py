class Atm:
    
    def _init_(self):
        self.pin=''
        self.balance=0
        
        self.menu()
        
    def menu(self):
        user_input=input('''
                         1.Enter 1 to create pin
                         2.Enter 2 to deposit
                         3.Enter 3 for withdraw
                         4.Enter 4 for check balance
                         5.Enter 5 for Exit
''')
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("exit")  
        
    def create_pin(self):
        self.pin=input("Enter your pin")
        print("pin set successfully") 
    
    def deposit(self):
        temp=input('Enter your pin')
        if temp==self.pin:
           amount=int(input("enter the amount"))
           self.balance=self.balance+amount
           print("deposit successful")
        else:
            print("invalid pin")
    
        
        
            
           
                
                
            
                
       
            
       
    
        
        
            
        
            
            
                                 
                  
sbi=Atm()
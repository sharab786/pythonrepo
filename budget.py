class Budget():
    def __init__(self, balance):
       # self.cateogry = cateogry
        self.balance = balance
        self.origbal = balance
    def __repr__(self):
        return f"This cateogry has a balance of {self.balance}"

    
    def displayfunds(self):
        return self.balance


    def addfunds(self, funds, fileupdate):
        self.balance = (funds + self.balance)
        runningtotal = str(self.balance)
        file = open(fileupdate, "w")
        file.write(runningtotal)
        return funds  
        
        

    def withdrawfunds(self, funds, fileupdate ):
        self.balance = self.balance - funds
        runningtotal = str(self.balance)
        file = open(fileupdate, "w")
        file.write(runningtotal)
        return funds

    def transferfundds(self):
        pass


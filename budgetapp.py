from budget import Budget
from os.path import exists
from time import sleep
import pdb

##### Asks user for type of transaction ############################################
transaction = ""
listvalidoptions = ["d", "w", "t"]

transaction = input("Would you like to deposit(d) or withdraw(w) or transfer(t)? ")
transaction = transaction.lower()  
##### This part is executed if transaction is deposit or withdrawal ################
if transaction == "d" or transaction == "w":
    budtype= input('Please select budget type: ')

    filename = budtype + ".txt"
    #print(filename)
    #sleep(10)


    file_exists = exists(filename)

    inputstr = "Please enter initial budget for " + budtype + ": "

    if file_exists == False:
        budinit = str(int(input(inputstr)))
        file = open(filename, "w")
        file.write(budinit)
        file.close()

    file = open(filename, "r")
    content = int(file.read())
    file.close()
    Food = Budget(content)
    Clothes = Budget(content)
    Entertainment = Budget(content)
    Bills = Budget(content)
    print(Food)


##### Only executed when the transaction is a deposit ####################################
    if transaction == "d":
        amount = int(input("Please enter the amount to deposit: "))
        if budtype == "food":
            Food.addfunds(amount, filename)
        elif budtype == "bills":
            Bills.addfunds(amount, filename)
        elif budtype == "clothes":
            Clothes.addfunds(amount, filename)
        else:
            Entertainment.addfunds(amount, filename)
        file = open(filename, "r")
        print(f" The {budtype} cateogry new balance is {file.read()}")
        file.close()
    elif transaction == "w":
        amount = int(input("Please enter the amount to withdraw: "))
        if budtype == "food":
            Food.withdrawfunds(amount, filename)
        elif budtype == "bills":
            Bills.withdrawfunds(amount, filename)
        elif budtype == "clothes":
            Clothes.withdrawfunds(amount, filename)
        else:
            Entertainment.withdrawfunds(amount, filename)
        file = open(filename, "r")
        print(f" The {budtype} cateogry new balance is {file.read()}")
        file.close()

###### This is executed if the transaction is a transfer ##########################

elif transaction == "t":
    amount = int(input("Please enter the amount: "))
    budsender = input('Please select budget transfer from: ')
    budreceiver =input('Please select budget transfer to: ') 

    filesend = budsender + ".txt"
    filercv = budreceiver + ".txt"
    ## Check for existence of files
    filesend_exists = exists(filesend)
    filereceive_exists = exists(filercv)

    inputstrsend = "No budget yet defined for " + budsender + ". Please enter an opening balance: "
    inputstrrcv = "No budget yet defined for " + budreceiver + ". Please enter an opening balance: "
    
    ## Only executed if no send balance file exists
    if filesend_exists == False:
        budinitsnd = str(int(input(inputstrsend)))
        file = open(filesend, "w")
        file.write(budinitsnd)
        file.close()
    
    ## Only executed if no receive balance file exists
    if filereceive_exists == False:
        budinitrcv = str(int(input(inputstrrcv)))
        file = open(filercv, "w")
        file.write(budinitrcv)
        file.close()
    

    ######   If the sender is food #######
    if budsender == 'food':
        filesd = open(filesend, "r")
        contentsend = int(filesd.read())
        Food = Budget(contentsend)
        filesd.close()
        print(f"Food: {Food}")
        if budreceiver == 'bills':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Bills = Budget(contentrcv)
            filerv.close()
            print(f"Bills: {Bills}")
            Bills.addfunds((Food.withdrawfunds(amount, filesend)), filercv)
            
        elif budreceiver == 'clothes':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Clothes = Budget(contentrcv)
            filerv.close()
            print(f"Clothes: {Clothes}")
            Clothes.addfunds(Food.withdrawfunds(amount, filesend),  filercv)
        else:
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Entertainment = Budget(contentrcv)
            filerv.close()
            print(f"Entertainment: {Entertainment}")
            Entertainment.addfunds(Food.withdrawfunds(amount,  filesend), filercv)
      
    ######   If the sender is clothes #######

    if budsender == 'clothes':
        filesd = open(filesend, "r")
        contentsend = int(filesd.read())
        Clothes = Budget(contentsend)
        filesd.close()
        print(f"Clothes: {Clothes}")
        if budreceiver == 'food':
            print(Food)
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Food = Budget(contentrcv)
            filerv.close()
            Food.addfunds(Clothes.withdrawfunds(amount, filesend), filercv)
        elif budreceiver == 'bills':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Bills = Budget(contentrcv)
            filerv.close()
            print(f"Bills: {Bills}")
            Bills.addfunds(Clothes.withdrawfunds(amount, filesend),  filercv)
        else:
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Entertainment = Budget(contentrcv)
            filerv.close()
            print(f"Entertainment: {Entertainment}")
            Entertainment.addfunds(Clothes.withdrawfunds(amount,  filesend), filercv)  

    ######   If the sender is bills #######

    if budsender == 'bills':
        filesd = open(filesend, "r")
        contentsend = int(filesd.read())
        Bills = Budget(contentsend)
        filesd.close()
        print(f"Bills: {Bills}")
        if budreceiver == 'food':
            print(f"Food: {Food}")
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Food = Budget(contentrcv)
            filerv.close()
            Food.addfunds((Bills.withdrawfunds(amount, filesend)), filercv)
        elif budreceiver == 'clothes':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Clothes = Budget(contentrcv)
            filerv.close()
            print(f"Clothes: {Clothes}")
            Clothes.addfunds((Bills.withdrawfunds(amount, filesend)),  filercv)
        else:
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Entertainment = Budget(contentrcv)
            filerv.close()
            print(f"Entertainment: {Entertainment}")
            Entertainment.addfunds(Bills.withdrawfunds(amount,  filesend), filercv) 

     ######   If the sender is entertainment #######

    if budsender == 'entertainment':
        filesd = open(filesend, "r")
        contentsend = int(filesd.read())
        Entertainment = Budget(contentsend)
        filesd.close()
        print(f"Entertainment: {Entertainment}")
        if budreceiver == 'food':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Food = Budget(contentrcv)
            filerv.close()
            print(f"Food: {Food}")
            Food.addfunds(Entertainment.withdrawfunds(amount, filesend), filercv)
        elif budreceiver == 'clothes':
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Clothes = Budget(contentrcv)
            filerv.close()
            print(f"Clothes: {Clothes}")
            Clothes.addfunds(Entertainment.withdrawfunds(amount, filesend),  filercv)
        else:
            filerv = open(filercv, "r")
            contentrcv = int(filerv.read())
            Bills = Budget(contentrcv)
            filerv.close()
            print(f"Bills: {Bills}")
            Bills.addfunds(Entertainment.withdrawfunds(amount,  filesend), filercv)         

    filesd = open(filesend, "r")
    print(f"The {budsender} cateogry new balance is {filesd.read()}")
    filerv = open(filercv, "r")
    print(f"The {budreceiver} cateogry new balance is {filerv.read()}")

else:
    print("This is an invalid option. Please try again")










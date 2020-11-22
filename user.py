import hashlib
import block
from tabulate import tabulate
class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.ledger=[]


    def register(self):
        print("YOU NEED TO PERFORM YOUR FIRST TRANSACTION TO CREATE A ACCOUNT HERE")
        print()
        self.coin = int(input("HOW MUCH COIN YOU WANT TO PURCHASE FROM COMPANY BLOCK"))
        print()
        self.username = hashlib.sha256(self.username.encode('utf-8')).hexdigest()
        self.password = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        dic[self.username] = self
        block.miningpool(["INITIAL DEPOSIT", self.username, self.coin])
        print("PLEASE WAIT WHILE YOUR TRANSACTION IS IN MINING POOL")

        print("TRANSACTION COMPLETED")
        print()
        print("PLEASE REFER TO THE BLOCK EXPLORER FOR FURTHER CONFIRMATION")
        for i in block.bl[len(block.bl)-1][0].transaction:
            dic[self.username].ledger.append(i)
        print()
        print()

    def ledgerbalance(self):
        print(tabulate(self.ledger, headers=['DEBITACCOUNT', 'CREDITACCOUNT', 'AMOUNT']))
        print()
        print("YOUR BALANCE=",self.coin)
        print()
def signin(u,h):
        uh=hashlib.sha256(u.encode('utf-8')).hexdigest()
        ph = hashlib.sha256(h.encode('utf-8')).hexdigest()
        if uh in dic:
            obj=dic[uh]
            if obj.password==ph:
                c=1
                while(c):
                    print("Signed In")
                    print("DO YOU WANT TO PERFORM SOME TRANSACTION")
                    print("TYPE 1 FOR YES AND 0 TO SEE YOUR LEDGER")
                    x=int(input())
                    if x==1:
                        k=1
                        while k:
                            print("HOW MUCH COIN YOU WANA TRANSFER")
                            coin=int(input())
                            receiver=input("ENTER THE USERNAME OF THE RECEIVER")
                            rh=hashlib.sha256(receiver.encode('utf-8')).hexdigest()
                            if rh in dic:
                                print("PLEASE WAIT TILL WE VERIFY YOUR TRANSACTION")
                                if obj.coin>=coin:
                                    print("YOUR TRANSACTION VERIFIED AND HAS BEEN SENT TO THE MINING POOL")
                                    print()
                                    print("PLEASE REFER TO THE BLOCK EXPLORER FOR FURTHER CONFIRMATION")
                                    print()
                                    block.miningpool([uh,rh,coin])
                                    bl=block.bl
                                    obj.ledger.append([uh,rh,coin])
                                    dic[rh].ledger.append([uh,rh,coin])
                                    obj.coin=obj.coin-coin
                                    dic[rh].coin=dic[rh].coin+coin
                                else:
                                    print("INSUFFICIENT BALANCE")
                            else:
                                print("ENTER VALID USERNAME\n")
                            k=int(input("TYPE 1 FOR ANOTHER TRANSACTION 0 FOR NOT"))
                    else:
                        obj.ledgerbalance()
                    print("TYPE 0 TO LOGOUT 1 TO STAY")
                    c=int(input())
            else:
                print("Oops Wrong Password")
                return
        else:
            print("Oops WRONG USERNAME")
            print()
            return

dic = {}














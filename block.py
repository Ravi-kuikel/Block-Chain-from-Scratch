import random
from hashlib import sha256
from datetime import datetime
import user
from tabulate import tabulate

class block:
    def __init__(self,prevhash):
        self.version=1
        self.prevhash=prevhash
        self.transaction=[]
        self.timestamp=-1
        self.cid=-1
        self.height = len(bl)
    def blockhash(self):
        if len(self.transaction)==2:
            self.timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.cid=self.h(self.timestamp+str(self.prevhash)+str(self.height))
            bl[len(bl)-1][1]=(self.cid)



    def h(self,msg):
        return sha256(msg.encode('utf-8')).hexdigest()

    def blockexplorer(self):
        print("BLOCK HEIGHT:",self.height)
        print("TIMESTAMP:", self.timestamp)
        print("VERSION:",self.version)
        print("BLOCK HASH:", self.cid)
        print("PREVIOUS HASH:", self.prevhash)
        print("                       TRANSACTIONS")
        print()
        print(tabulate(self.transaction, headers=['DEBITACCOUNT', 'CREDITACCOUNT','AMOUNT']))
        print()
        print()
def explore():
    print("***ALL THE BLOCK MINED TILL NOW ARE***")
    for i in range(len(bl)):
        print("BLOCKNO:",i+1)
        print()
        bl[i][0].blockexplorer()
    print()


def miningpool(transaction):
    if len(bl)==0:
        obj=block(-1)
        bl.append([obj,-1])
        obj.transaction.append(transaction)
    else:
        if len(bl[len(bl)-1][0].transaction)==2:
            prev=bl[len(bl)-1][1]
            obj=block(prev)
            bl.append([obj,-1])
            obj.transaction.append(transaction)
        else:
            obj=bl[len(bl)-1][0]
            obj.transaction.append(transaction)
            obj.blockhash()

bl=[]



































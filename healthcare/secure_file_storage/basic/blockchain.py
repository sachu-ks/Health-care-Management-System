# importing the required libraries  
import hashlib  
import simplejson  
from time import time  
import datetime
from  django.core.files.storage import FileSystemStorage
from . models import *
# creating the Block_chain class  
class Block_chain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
        file = open('previous.txt','r')
        x=file.read()
        #file.write(x)

       
        file.close()
        #x="fdsfs44234fdfs"
        self.newBlock(previousHash = x, the_proof = 100)  
        #self.newBlock(previousHash = "", the_proof = 100)  
  
# Creating a new block listing key/value pairs of  
# block information in a simplejson object.  
# Reset the list of pending transactions &  
# append the newest block to the chain.  
    def newBlock(self, the_proof, previousHash = None):  
        the_block = {  
            'index': len(self.chain) + 1,  
            'timestamp': time(),  
            'transactions': self.pendingTransactions,  
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        a=previousHash or self.hash(self.chain[-1]);

        date_time=datetime.datetime.now()
        date_time=str(date_time.date())+"_"+date_time.strftime("%H")+"-"+date_time.strftime("%M")+"-"+date_time.strftime("%S")
        print(date_time)

        file=open("output_"+date_time+".txt","a")

        file.write(a)
        file.write("\n")

        file_to_save = open("output_"+date_time+".txt", 'r').read()
        new_entry = blockchainoutput(output=file_to_save)
        new_entry.save()

        file.close()

        file = open('previous.txt','w')
        file.write(a)

        file.close()
        self.pendingTransactions = []  
        self.chain.append(the_block)  
  
        return the_block  
  
#Searching the blockchain for the most recent block.  
    @property  
    def lastBlock(self):  
   
        return self.chain[-1]  
  
# Adding a transaction with relevant info to the 'blockpool' - list of pending tx's.   
    def newTransaction(self, the_sender, the_recipient, the_amount):  
        the_transaction = {  
            'sender': the_sender,  
            'recipient': the_recipient,  
            'amount': the_amount  
        }  
        self.pendingTransactions.append(the_transaction)  
        return self.lastBlock['index'] + 1  
  
# receiving one block. Turning it into a string, turning that into  
# Unicode (for hashing). Hashing with SHA256 encryption,  
# then translating the Unicode into a hexidecimal string.  
    def hash(self, the_block):  
        stringObject = simplejson.dumps(the_block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        rawHash = hashlib.sha256(blockString)  
        hexHash = rawHash.hexdigest()  
  
        return hexHash  
  

  
# transaction4 = block_chain.newTransaction("Alex", "Lucy", '2 BTC')  
# transaction5 = block_chain.newTransaction("Lucy", "Justin", '1 BTC')  
# transaction6 = block_chain.newTransaction("Justin", "Alex", '1 BTC')  
# block_chain.newBlock(10384)  
  
#print("Genesis block: ", block_chain.chain)  
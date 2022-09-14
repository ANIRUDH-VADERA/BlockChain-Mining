from hashlib import sha256
import datetime
import time

class Block:
    blockNo = 0
    data = None
    nonce = 0
    next = None
    transactions = None
    previousHash = None
    timeStamp = datetime.datetime.now()
    
    def __init__(self,data,transactions):
        self.data = data
        self.transactions = transactions
        
    def SHA256(self,text):
        return sha256(text.encode("ascii")).hexdigest()
    
    def giveHash(self):
        text = str(self.nonce) + str(self.data) + str(self.previousHash) + str(self.timeStamp) + str(self.blockNo) + str(self.transactions)
        return self.SHA256(text)
    
    def printBlock(self):
         print("Block Hash: " + str(self.giveHash()) + "\n" + "BlockNo: " + str(self.blockNo) + "\n" + "Block Data: " + str(self.data) + "\n" + "Hashes: " + str(self.nonce) + "\n" + "Block Transactions: " + str(self.transactions) + "\n" + "Block Previous Hash: " + str(self.previousHash) + "\n" + "Block Time Stamp: " + str(self.timeStamp) + "\n" + "Next Block: " + str(self.next) + "\n--------------")

class Blockchain:
    difficulty = None
    maxNonce = None

    def __init__(self,difficulty,maxNonce):
        self.difficulty = difficulty
        self.maxNonce = maxNonce

    # Origin of BlockChain

    block = Block("Genesis(First Block(Origin))",'''Satoshi Nakamoto->Anirudh:50''')
    dummy = head = block

    def add(self, block):

        block.previousHash = self.block.giveHash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self,block):
        prefix_str = '0'*(self.difficulty)
        start = time.time()
        print("\nStarted mining for next Block to be Added")
        for n in range(self.maxNonce):
            blockHash = block.giveHash()
            if blockHash.startswith(prefix_str):
                self.add(block)
                block.printBlock()
                print(f"Yay! Successfully mined bitcoins with nonce value:{block.nonce}")
                total_time = str((time.time() - start))
                print(f"End mining. Mining took: {total_time} seconds")
                return 1
            else:
                block.nonce += 1

        raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")


if __name__=='__main__':
    difficulty = int(input("Set difficulty (Number of prefix zeros) : ")) # changing this to higher number and you will see it will take more time for mining as difficulty increases
    MAX_NONCE = 2**32
    totalBlocks = int(input("Enter the Number of Blocks : "))
    
    blockchain = Blockchain(difficulty,MAX_NONCE)

    print("\nMining New Blocks: ")    

    for n in range(totalBlocks):
        transactions = input("Enter Transactions for Block "+str(n+1) + " : \n")
        output = blockchain.mine(Block("Block " + str(n+1),transactions))

    print("\nThe BlockChain Currently is: ")

    while blockchain.head != None:
        blockchain.head.printBlock()
        blockchain.head = blockchain.head.next
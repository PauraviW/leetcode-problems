from collections import defaultdict


class Account:
    def __init__(self, id, name='None'):
        self.id = id
        self.name = name
        self.isBlocked = False
    def deleteClass(self):
        pass
    @property
    def isBlocked(self):
        return self.isBlocked
    @isBlocked.setter
    def isBlocked(self,val):
        self.isBlocked = val
    @classmethod
    def getAccount(self, id):
        return self

class Member(Account):
    def __init__(self, id,name):
        super(self,Member).__init__(id, name)
        self.walletAmount = 0
        self.cart = Cart()

    def addItem(self, item):
        # create an instance of the ITem class
        pass
    def deleteItem(self, item):
        # delete self created item
        pass
    def addToCart(self, item):
        self.cart.addItem()
    def delFromCart(self, item):
        self.cart.delItem(item)

class Admin(Account):
    def __init__(self, id, name):
        super(self, Account).__init__(id, name)

    def blockAccount(self, id):
        account = Account.getAccount(id)
        account.isBlocked = True

class Item:
    def __init__(self, id, price, color, vendor, quantity):
        self.id = id
        self.price = price
        self.color = color
        self.vendor = vendor
        self.quantity = quantity



class Cart:
    def __init__(self):
        self.itemDictionary = defaultdict(Item)
        self.memberId = None

    def addItem(self, itemId, memberId, **kwargs):
        member = Account.getAccount(memberId)
        self.itemDictionary[itemId] = Item(itemId, **kwargs)
        self.update_price(1, itemId)
    def deleteItem(self, itemId):
        self.update_price(-1, itemId)
    def update_price(self, operation, itemId):




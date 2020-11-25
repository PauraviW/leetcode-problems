from collections import defaultdict
from datetime import datetime
from enum import Enum


class CD:

    def __init__(self, name, artist, releaseYear, rented=False, category = None):
        self.name = name
        self.artist = artist
        self.releaseYear = releaseYear
        self.rented = rented
        self.category = category

class Account:
    def __init__(self, creationDate, name, address, email):
        self.creationDate = creationDate
        self.name = name
        self.address = address
        self.email = email

    def updateAddress(self, address):
        self.address = address


class Member(Account):
    def __init__(self, creationDate, name, address, email, bill=None):
        super().__init__(creationDate, name, address, email)
        self.bill = bill
        self.rentedDate = datetime.today()
        self.rentedTitle = None

class GenreEnum(Enum):
    MUSIC, MOVIES = 1,2
class CDRentalSystem:
    def __init__(self, id):
        self.id = id
        self.CDquantities = defaultdict(list)
        self.category = defaultdict(set)
        self.memberDetails = defaultdict(Member)
        self.rate = 10
    def printMessage(self, message):
        """
        Function to print all messages
        :param message: notifications from certain activities
        :return: None
        """
        print(message)
    def addMember(self, name, address, email):
        """
        Adding a new member to the syste,
        :param name: name of the member
        :param address: address of the member
        :param email: email of the member
        :return: None
        """
        self.memberDetails[email] = Member(name, datetime.today(), address, email)
        self.printMessage("Member : {} successfully added!".format(name) )
    def updateMemberAddress(self, address , email):
        """
        Updating member address
        :param address: new address
        :param email: member email id
        :return: None
        """
        self.memberDetails[email].updateAddress(address)
        self.printMessage("Member : {}'s  address successfully updated!".format(self.memberDetails[email].name))
    def addCD(self,name, artist, releaseYear, category):
        """
        Add the CD to the database
        :param name: name of the CD
        :param artist: name of the artist
        :param releaseYear: year when the CD released
        :param category: Type of the CD
        :return: None
        """
        cd = CD(name, artist, releaseYear)
        cd.category = category
        self.category[category].add(name)
        self.CDquantities[name].append(cd)
        self.printMessage("CD : {} successfully added!".format(name) )

    def searchByCategory(self, category):
        """
        Returns names of all CDS in that category
        :param category: name of the category
        :return: list of names of titles in this category
        """
        if category not in self.category:
            self.printMessage("Category not found!")
            return []
        else:
            n = self.category[category]
            self.printMessage("{} titles found".format(len(n)))
            return n
    def searchByName(self, name):
        """
        Search Titles by NAmes
        :param name: name of the CD
        :return:
        """

        if name not in self.CDquantities:
            self.printMessage("Title not found!")
        else:
            obj = self.CDquantities[name][0]
            self.printMessage("Title Found : Details: \t Name:{} \t artist \t releaseYear".format(name, obj.artist, obj.releaseYear))
    def rentCD(self, CDname, email):
        if email not in self.memberDetails:
            self.printMessage("Member not present. Creating new. Please provide more input")
            name = input("Name:")
            address= input("Address")
            member = Member(datetime.today(), name, email, address)
            self.memberDetails[email] = member
        else:
            member = self.memberDetails[email]
            if CDname not in self.CDquantities:
                self.printMessage("CD {} not present".format(CDname))
            else:
                l = self.CDquantities[CDname]
                for i in l:
                    if i.rented == False:
                        member.rentedDate = datetime.today()
                        member.rentedTitle = i
                        i.rented = True
                        self.printMessage("Member {} rented {} on {}".format(member.name, CDname, member.rentedDate))
                else:
                    self.printMessage("Sorrt all CDs are rented")
    def returnCD(self, email):
        """
        Return rented CD
        :param email: email id of the memebr
        :return:
        """
        if email not in self.memberDetails:
            self.printMessage("Invalid MEmber")
        else:
            member = self.memberDetails[email]
            amount = (datetime.today() - member.rentedDate)*self.rate
            member.bill += amount
            if datetime.today() - member.rentedDate > 30:
                self.printMessage("Penalty of 10 as a late fee")
                member.bill += 10

            member.rentedTitle.rented = False
    def deleteCD(self, name, category):
        """

        Delete the CD from the database
        :param name: name of the cd
        :return: None
        """
        if name not in self.CDquantities:
            self.printMessage("CD {} not present".format(name))
        else:

            l = self.CDquantities[name]
            for i in l:
                if i.rented == False:
                    return False

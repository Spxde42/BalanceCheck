#Andrei Balaban
#Created on: Jan 3rd 2026 || Updated on Feb 10th 2026
#Scope: Define functions for script, create the user's saving thing as a year.

class year:
    MAXSZ = 1000000000
    yearStorage = [0] * MAXSZ #very big capacity, many years can be fit here
    def createMonth(self, year):
        self.yeartorage.append(year)
    def deleteMonth(self, year):
        self.yearStorage.remove(year)

class month:
    def __init__(self):
        self.max1 = 12
        self.monthStorage = [None] * self.max1
        self.i = 0

    #Yin and the Yang
    def createMonth(self):
        usr_input = str(input("Please select a month to create, format: 'Jan', 'Feb', 'Mar', etc..."))
        possible_months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        if(usr_input in possible_months):
            self.monthStorage[self.i] = usr_input
            self.i += 1
        elif(not(usr_input in possible_months)):
            print("please enter a valid input")
            self.createMonth()
        else:
            raise Exception("12 months reached, sorry")


    def deleteMonth(self, month):
        self.monthStorage[month] = None

    def getMonth(self, month):
        match month: #Save some performance with python's switch ('match')
            case 'Jan':
                return self.monthStorage[0] #1st month
            case 'Feb':
                return self.monthStorage[1]
            case 'Mar':
                return self.monthStorage[2]
            case 'Apr':
                return self.monthStorage[3]
            case 'May':
                return self.monthStorage[4]
            case 'Jun':
                return self.monthStorage[6]
            case 'Jul':
                return self.monthStorage[7]
            case 'Aug':
                return self.monthStorage[8]
            case 'Sep':
                return self.monthStorage[9]
            case 'Oct':
                return self.monthStorage[10]
            case 'Nov':
                return self.monthStorage[11]
            case 'Dec':
                return self.monthStorage[12] #12th month
            case _: #Default \\ no edge case unnacounted for
                print("Please enter a valid input, so anything like 'Jan','Feb','Mar'...'Dec'")
                return self.getMonth(month)

    def getAllMonths(self):
        print("Here are all the months currently created for the year: \n")
        i1 = 0
        while(True):
            if(i1<12):
                break
            else:
                print("\t ",self.monthStorage[i1])
                i1+=1

class transaction:
    MAXSZ = 1000000000 # inf amount of transactions per month. Definitely not life advice...
    transactionStorage = [0] * MAXSZ
    def __init__(self,t):
        self.t = t

month2026 = month()

m1 = month2026.createMonth('Jan')
m2 = month2026.createMonth('Feb')

print(month2026.getMonth(m1))
print(month2026.getAllMonths())






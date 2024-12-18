import time
import random

#global variables
coins = 0
name = ""
charTotal = 0
wordTotal = 0
totalTimeTotal = 0
totalAcc = 0
totalWPM = 0
totalRaces = 0
bestWPM = 0


intro = '''
  *   )            )       *   )
` )  /(  (  (   ( /(     ` )  /((            (
 ( )(_))))\ )(  )\())  (  ( )(_))\ ) `  )   ))\ 
(_(_())/((_|()\((_)\   )\(_(_()|()/( /(/(  /((_)
|_   _|_))( ((_| |(_) ((_|_   _|)(_)|(_)_\(_))
  | | | || | '_| '_ \/ _ \ | | | || | '_ \) -_)
  |_|  \_,_|_| |_.__/\___/ |_|  \_, | .__/\___|  
                                |__/|_| Version 1.0
\n\n\n\nEnter your name: '''
screenClear = "\n\n\n\n\n\n\n\n\n\n\n\n\n"
loading1 = "loading ."+ screenClear
loading2 = "loading .." + screenClear
loading3 = "loading ..." + screenClear

def coolprint(a):
    for i in a:
        print(i, end="", flush=True)
        time.sleep(0.05)


def menu():
    global name
    tabOfCont = "\nHi " + name + ", please choose a number to select an option\n\n1) Race\n2) Profile \n\nNumber: "
    coolprint(tabOfCont)
    choice = input()
    if (choice=="1"):
        coolprint("\nHow many words would you like to race to? (10 is type 10 words)\nEnter: ")
        wordNumStr = input()
        if (wordNumStr.isdigit()):
            wordNum = int(wordNumStr)
            race(wordNum)
        else:
            coolprint(screenClear+"TRY AGAIN"+screenClear)
            menu()
    elif (choice=="2"):
        profile()
    else:
        coolprint(screenClear+"TRY AGAIN"+screenClear)
        menu()

def promptGen(wordNum):
    with open("bank.txt", "rt") as myFile:
        x=""
        part = myFile.read().split()
        for i in range(wordNum):
            y= random.randint(0, 999)
            x = x + str(part[y]) + " " 
        return(x)

def race(wordNum):
    global name
    coolprint("\nPrepare yourself and hit enter when you are ready to start the race")
    x=input()
    coolprint("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n3\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n2\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTYPEEEEEEEEEEEEEEEEEE!")
    x=promptGen(wordNum).strip()
    print("\n\n"+x+"\n\n")
    timeBegin = time.time() 
    y=input() #user typed words
    timeEnd = time.time() 

    #calculations start here
    timeTotal = round((timeEnd-timeBegin),2)
    WPM = round(((len(y)/5.0)/(timeTotal/60.0)),2)
    wordCount = len(y.split())
    z=len(x)
    if len(y)>len(x):
        z=len(y)
    acc = round((((1.0*accuracyV2(x, y))/z)*100),2)
    coinsGained = round(len(y)*(acc/100),0)

    coolprint("\n\nThese are your results:\n\nWords: "+str(wordCount)+"\nCharacters: "+str(len(y))+"\nAccuracy: "+str(acc)+"%\nTime: "+str(timeTotal)+"\nWPM: "+str(WPM)+"\n\nYou made "+str(coinsGained)+" coins!\nHit Enter to move on\n*WPM is not a direct result of words/min")
    
    #calculations for profile
    global totalRaces 
    totalRaces += 1
    global coins
    coins = coins + coinsGained
    global charTotal
    charTotal = charTotal + len(y)
    global wordTotal
    wordTotal = wordTotal + wordCount
    global totalTimeTotal
    totalTimeTotal = totalTimeTotal + timeTotal
    global totalAcc
    totalAcc = totalAcc + acc
    global totalWPM
    totalWPM = totalWPM + WPM

    #calculations for personal bests
    global bestWPM
    if (WPM>bestWPM):
        bestWPM = WPM

    y=input()
    menu()

def profile():
    coolprint("Welcome to your profile: \nWhich page would you like to view?\n\n1) All time stats\n2) Personal Best (WPM)\n3) Exit\n\nSelect a Number: ")
    userIn = input()
    if (userIn=="1"):
        totalHours = int(((totalTimeTotal/60)/60))
        totalMins = int((totalTimeTotal/60)%60)
        totalSecs = round((totalTimeTotal%60)%60)
        WPMavg = int(totalWPM/totalRaces)
        AccAvg = int(totalAcc/totalRaces)
        coolprint("These are your all-time stats: \n\nTotal Races: "+str(totalRaces)+"\nTotal Time Typed: "+str(totalHours)+" hours "+ str(totalMins) +" minutes "+str(totalSecs)+" seconds\nTotal Characters Typed: "+str(charTotal)+"\nTotal Words Typed: "+str(wordTotal)+"\nAverage WPM: "+str(WPMavg)+"\nAverage Accuracy: "+str(AccAvg)+"%\n\nHit Enter to go back to the menu\n")
        x = input()
        menu()
    elif (userIn=="2"):
        global bestWPM
        coolprint("Your personal best is......\n\n")
        numCreator(str(round(bestWPM)))
    elif (userIn=="3"):
        menu()
    else:
        coolprint(screenClear + "TRY AGAIN" + screenClear)
        profile()

def numCreator(x):
    nums = [
        ["┏┓","┃┃","┗┛"],
        [" ┓"," ┃"," ┻"],
        ["┏┓","┏┛","┗━"],
        ["┏┓"," ┫","┗┛"],
        ["  ","┃┃","┗╋"],
        ["┏━","┗┓","┗┛"],
        ["┏┓","┣┓","┗┛"],
        ["━┓"," ┃"," ┃"],
        ["┏┓","┣┫","┗┛"],
        ["┏┓","┗┫","┗┛"]
    ]

    top = ""
    mid = ""
    bot = ""
    for i in x:
        top += nums[int(i)][0]
        mid += nums[int(i)][1]
        bot += nums[int(i)][2]
    
    coolprint(top + "\n" + mid +"\n"+ bot + " WPM\n\nHit Enter to exit the page: ")
    x = input()
    menu()



def accuracy(x, y):
    count = 0
    i = 0
    for i in range (len(x) or len(y)):
        if x[i:i+1]==y[i:i+1]:
            count = count + 1
    return count

def accuracyV2(x, y):
    count = 0
    i = 0

    for i in range(min(len(x.split()), len(y.split()))): # or len(y.split())):
        for j in range (min(len(x.split()[i]), len(y.split()[i]))): # or len(y.split[i])):
            if x.split()[i][j:j+1] == y.split()[i][j:j+1]:
                count = count + 1
    
    if (len(y.split())>=1):
        count = count + len(y.split())-1

    return count


def main():
    d=""
    print("Welcome to TurboType Version 1.0!\nWould you like the cinematic intro? [y/n]\n*DO NOT TYPE WHILE THE COMPUTER IS STILL PRINTING")
    x = input()
    if (x=="n"):
        coolprint("Too bad\n\n\n\n\n")
        d = loading1 + loading2 + loading3 + loading1 + intro
    elif (x=="y"):
        print("\n")
        d = loading1 + loading2 + loading3 + loading1 + intro
    else:
        d = "What is your name: "
        
    
    coolprint(d)
    global name
    name = input()
    menu()

main()
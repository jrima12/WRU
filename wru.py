#TODO:  Make different special characters as separators
#       Change itertools permutation to itertools product for repeating words
#       Make options of common number patterns
#       Add Special Characters to the end

import argparse
import itertools
from pyleetspeak import LeetSpeaker

#Global vars hard coded to make editing easier for user
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
common_specials = ["!","@","#","$","%","&","*","-","_",".","?"]
other_specials = ["=","|","]","}","[","{","'",'"',";",":","/",">",",","<","+","^"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
common_special_combos = []

mode_help = """
    Choose your mode:\n\n
        1) Interactive password generator \n
        2) Interactive username generator\n
        3) Interactive email generator\n
        4) Interactive wordsmith
        5) Generate pin numbers
"""       



def mode1():
    def nameparser(listofnames):
        retlist = []
        for i in listofnames:
            retlist.append(i.upper())
            retlist.append(i.lower())
            retlist.append(i.capitalize())
            retlist.append(i.capitalize().swapcase())
            retlist.append(i.upper()[::-1])
            retlist.append(i.lower()[::-1])
            retlist.append(i.capitalize()[::-1])
            retlist.append(i.capitalize().swapcase()[::-1])
            try:
                retlist.append(i[0].upper())
                retlist.append(i[0].lower())
            except:
                pass
        return retlist

    def wordparser(listofwords):
        retlist = []
        for i in listofwords:
            retlist.append(i.upper())
            retlist.append(i.lower())
            retlist.append(i.capitalize())
            retlist.append(i.capitalize().swapcase())
        return retlist

    def addcomwords(comwords):
        comwordlist = ["password","pass","secret","private"]
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        retlist = []
        if comwords.lower() == "y":
            for i in comwordlist:
                retlist.append(i.upper())
                retlist.append(i.lower())
                retlist.append(i.capitalize())
                retlist.append(i.capitalize().swapcase())
        return retlist
    
    def removeduplicate(inputlist):
        outputlist = []
        for i in inputlist:
            if i not in outputlist:
                outputlist.append(i)
        return outputlist
    
    def makepasswords(WL,num):
        retlist = []
        try:
            number = int(num)
        except:
            number = 2
        for j in range(number+1):
            perms = list(itertools.permutations(WL,j))
            for i in perms:
                retlist.append(''.join(i))
        return retlist
        
    def makepasswordsspecial(WL,num,spec):
        retlist = []
        try:
            number = int(num)
        except:
            number = 2
        for j in range(number+1):
            perms = list(itertools.permutations(WL,j))
            for i in perms:
                for k in spec:
                    retlist.append(k.join(i))
        return retlist
    
    # def addseparator(wordslist, wordcombos, specchar):
    #     retlist = []
    #     for j in range(wordcombos):
    #         perms = list(itertools.permutations(wordslist,j))
    #         for i in perms:
    #             for k in specchar:
    #                 retlist.append(k.join(i)) 
    #     return retlist
    
    def addnums(passwords, yn):
        retlist = []
        if yn.lower() == "y" or yn.lower() == "yes":
            try:
                numbercomobos = int(input("how many digits do you want to include (default = 3)?: "))
            except:
                numbercomobos = 3
            for i in passwords:
                for n in range(numbercomobos+1):
                    for p in itertools.product(numbers, repeat=n):
                        retlist.append(i+''.join(p))
        return retlist

    def makeleetmode(inputlist,yn):
        retlist = []
        if yn.lower() == "y" or yn.lower() == "yes":
            leeter = LeetSpeaker(mode="basic", get_all_combs=True)
            for i in inputlist:
                try:
                    leets = leeter.text2leet(i)
                except:
                    leets = []
                retlist += leets
        return retlist
        
    filename = input("What would you like your file to be called (include extension)(default: file.list)?: ")
    masterlist = []
    firstname = input("What is your target's first name?: ")
    midname = input("What is your target's middle name?: ")
    lastname = input("What is your target's last name?: ")
    nickname = input("What is your target's nick name?: ")
    masterlist += nameparser([firstname,midname,lastname,nickname])

    pet = input("What is your target's pet's name?: ")
    spouse = input("What is your target's spouse's name?: ")
    kid1 = input("What is your target's child's or sibling's name?: ")
    kid2 = input("What is your target's other child's or sibling's name?: ")
    kid3 = input("What is your target's other other child's or sibling's name?: ")
    streetaddress = input("What is your target's street name?: ")
    college = input("What is your target's college?: ")
    highschool = input("What is your target's highschool?: ")
    masterlist += wordparser([pet,spouse,kid1,kid2,kid3,streetaddress,college,highschool])
    
    otherwords = input("Please include other words you want separated by spaces: ").split()
    masterlist += wordparser(otherwords)

    #OPTIONS
    comwords = input("Do you want to include common passwords/password words (y/n)?: ")
    masterlist += addcomwords(comwords)

    wordslist = removeduplicate(masterlist)

    passlist = wordslist
    wordcombos = input("How many combinations of words do you want to use (integer 1-5) (default 2): ")
    try:
        wordcombos = int(wordcombos)
    except:
        wordcombos =  2
    passlist += makepasswords(wordslist, wordcombos)
    passlist = removeduplicate(passlist)

    specchar = input("list characters you want to separate words with (sparate input by spaces): ").split()
    passlist += makepasswordsspecial(wordslist, wordcombos, specchar)

    numatends = input("Would you like to include numbers at the end (y/n)?: ")
    passlist += addnums(passlist,numatends)

    leetmode = input("Would you like to include 1337 mode (y/n)?: ")
    passlist += makeleetmode(passlist,leetmode)

    try:
        f = open(filename, "w")
    except:
        f = open("file.list", "w")

    for item in passlist:
        f.write(item)
        f.write("\n")

        
    
def mode2():
    return("Mode 2")

def mode3():
    return("Mode 3")

def mode4():
    return("Mode 4")

def mode5():
    return("Mode 5")


mode_dict = {
    "1":mode1,
    "2":mode2,
    "3":mode3,
    "4":mode4,
    "5":mode5
}

parser = argparse.ArgumentParser(
    prog='WRU',
    description='Wordlists R Us'
)

parser.add_argument('-m','--mode', help=mode_help, 
                    choices=mode_dict.keys(),
                    required=True, nargs=1,metavar='',
                    default=1)
args = parser.parse_args()

func = mode_dict[args.mode[0]]
func()


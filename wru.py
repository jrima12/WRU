import argparse
import itertools
import re
#Global vars hard coded to make editing easier for user
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
common_specials = ["!","@","#","$","%","^","&","*","-","_","+",".","?",]
other_specials = ["=","|","]","}","[","{","'",'"',";",":","/",">",",","<"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

mode_help = """
    Choose your mode:\n\n
        1) Interactive password generator \n
        2) Interactive username generator\n
        3) Interactive email generator\n
        4) Interactive wordsmith
        5) Generate pin numbers
"""

def make_number_addons():
    addons = []
    for i in numbers:
        for j in range(1,7):
            addons.append(i*j)
    for j in range(0,10):
        string=""
        for i in range(j,j+6):
            try:
                string = string + numbers[i]
                addons.append(string)
                addons.append(string[::-1])
            except:
                pass
        j += 1
    for i in range(0,10):
        string = ""
        for i in range (0,10,2):
            try:
                string=string+numbers[i]
                addons.append(string)
                addons.append(string[::-1])
            except:
                pass
    for i in range(0,10):
        string = ""
        for i in range (1,10,2):
            try:
                string=string+numbers[i]
                addons.append(string)
                addons.append(string[::-1])
            except:
                pass
    numlist = []
    for i in addons:
        if i not in numlist:
            numlist.append(i)
    return numlist

def parsefile(filename):
    filewords = []
    try:
        with open(filename,'r') as f:
            filewords.append(f.split())
    except:
        pass
    return filewords

def leet_mode():
    pass

def getinputs(morewords):
    morewords = morewords.split()
    return morewords

def write_password(filename,target,elements,length,extras,filewords):
    full_items_list = []
    for i in target:
        full_items_list.append(i.lower())
        full_items_list.append(i.upper())
        full_items_list.append(i.capitalize())
        full_items_list.append(i.lower()[::-1])
        full_items_list.append(i.upper()[::-1])
        full_items_list.append(i.capitalize()[::-1])
        full_items_list.append(i[::-1].lower())
        full_items_list.append(i[::-1].upper())
        full_items_list.append(i[::-1].capitalize())
        full_items_list.append(i[0].lower())
        full_items_list.append(i[0].upper())
    for j in elements:
        full_items_list.append(j.lower())
        full_items_list.append(j.upper())
        full_items_list.append(j.capitalize())
    for k in extras:
        full_items_list.append(k.lower())
        full_items_list.append(k.upper())
        full_items_list.append(k.capitalize())
    for l in filewords:
        full_items_list.append(l)
    addons_num = make_number_addons()

    el = []
    for item in full_items_list:
        if item not in el:
            el.append(item)

    if (type(length)==range):
        with open(filename, 'w') as f:
            for i in el:
                for j in el:
                    if (len(i) in length):
                        f.write(i)
                        f.write("\n")
                    if (len(i+j) in length):
                        f.write(i+j)
                        f.write("\n")
                    if extras[0].lower() == "y":
                        for k in addons_num:
                            if (len(i+k) in length):
                                f.write(i+k)
                                f.write("\n")
                            if (len(i+j+k) in length):
                                f.write(i+j+k)
                                f.write("\n")
                    if extras[1].lower() == "y":
                        pass
                    if extras[2].lower() == "y":
                        pass
    else:
        with open(filename, 'w') as f:
            for i in el:
                for j in el:
                    if (len(i) == length):
                        f.write(i)
                        f.write("\n")
                    if (len(i+j) in length):
                        f.write(i+j)
                        f.write("\n")
                    if extras[0].lower() == "y":
                        for k in addons_num:
                            if (len(i+k) in length):
                                f.write(i+k)
                                f.write("\n")
                            if (len(i+j+k) in length):
                                f.write(i+j+k)
                                f.write("\n")
                    if extras[1].lower() == "y":
                        pass
                    if extras[2].lower() == "y":
                        pass 
                          

    # print(full_items_list)
    # print(filename)
    # with open(filename,'rw') as f:
    #     #TODO: Combine 2 words, combine 3 words, first initial of target names, backwards target names, capital first initial, capital whole words
    #     #TODO: Potentially append random numbers and common numbers and special characters
    #     if(type(length)==range):
    #         if(len(itertools.permutations([full_items_list])) in length):
    #             f.write(itertools.permutations([full_items_list]))
    #     else:
    #         if(len(itertools.permutations([full_items_list])) == length):
    #             f.write(itertools.permutations([full_items_list]))

def mode1():
    masterlist = []
    filename = input("What do you want your file to be called (include file extension. (example file.txt) .txt or .list is recommended) default = file.txt: ")
    print("")
    if filename == "":
        filename = "file.txt"
    firstname = input("What's your target's first name?: ")
    nickname = input("What is your target's nickname?: ")
    lastname = input("What's your target's last name?: ")
    middlename = input("What's your target's middle name?: ")
    print("")
    company = input("What's your target's company or website?: ")
    company_acronyms = input("What's your target's company or website acronyms or shortened name?: ")
    print("")
    birthday_month = input("What is your target's birth month? (month number): ")
    birthday_day = input("What is your target's birth day?: ")
    birthday_year = input("What is your target's birth year?: ")
    print("")
    spouse_name = input("What is your target's spouse's name?: ")
    child_name = input("What is your target's child's name? (can add multiple with spaces like 'John Jane Jerry'): ")
    pet_name = input("What is your target's pet's name? (Can add multiple with spaces like 'Boxer Rex Gilgamesh')")
    print("")
    other_words = input("List any other words or characters you want to use like favorite movie, character, website name: ")
    print("")
    password_length = input("What is the min and max password length ('8 12' or just '8' if you want a password of 8 characters) (default 6-18): ")
    print("")
    append_num = input("Do you want to append common numbers to the end? (y/n): ")
    spec_char = input("Do you want to append special characters? (y/n): ")
    leetmode = input("Do you want to use 1337 mode? (y/n): ")
    inputfile = input("Filename to read items from? (words must be separated with new line or space): ")
    filewords = parsefile(inputfile)
    target = []
    for i in getinputs(firstname):
        target.append(i)
    for l in getinputs(nickname):
        target.append(l)
    for j in getinputs(lastname):
        target.append(j)
    for k in getinputs(middlename):
        target.append(k)


    masterlist.append(getinputs(company))
    masterlist.append(getinputs(company_acronyms))
    masterlist.append(getinputs(birthday_month))
    masterlist.append(getinputs(birthday_day))
    masterlist.append(getinputs(birthday_year))
    try:
        masterlist.append(months[int(birthday_month)-1])
    except:
        pass
    masterlist.append(getinputs(spouse_name))
    masterlist.append(getinputs(child_name))
    masterlist.append(getinputs(pet_name))
    masterlist.append(getinputs(other_words))
    wordlist = []
    for i in masterlist:
        for j in i:
            wordlist.append(j)
    password_length = getinputs(password_length)
    try:
        if len(password_length) == 1:
            pass_length = int(password_length[0])
        else:
            pass_length = range(int(password_length[0]),int(password_length[1])+1)
    except:
        pass_length = range(6,19)
    extras = [append_num, spec_char, leetmode]
    write_password(filename, target, wordlist,pass_length,extras,filewords)

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
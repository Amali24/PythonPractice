# get input string
inputString = input("Type a string: ").lower()
# print input for confirmation
print("You entered \"" + inputString + "\"")
# print menu
menu = "Select a fun operation to perform on your string!\n"
menu += "1 - Reverse it!\n2 - Count vowels!\n3 - Is it a palindrome?\n"
menu += "4 - Pig Latinify It!\n5 - Count Words!\n"
#get menu choice
menuchoice = input(menu + "")

# if user entered 1
if menuchoice == "1":
    # create empty string to put reversed string in
    rstring = ""
    # iterator starts at the last letter
    x = len(inputString) - 1
    # while iterator is 0 or higher (i.e. letters remaining)
    while x >= 0:
        # add the last un-added letter to the reversed string
        rstring += inputString[x]
        # move to the previous character
        x -= 1
    # print the string once it's reversed correctly
    print(rstring)

# if user chooses option 2
elif menuchoice == "2":
    # we need a vowel list to check against to count vowels, y is a special case
    vowels = {'a','e','i', 'o', 'u'}
    # iterator
    x = 0
    #counts for vowels and Ys
    vowelsCount = 0
    ycount = 0
    # while we have letters left to check
    while x < len(inputString):
        # if it's a vowel, count it
        if vowels.__contains__(inputString[x]):
            vowelsCount += 1
        # if it's a Y, add it to Y count
        if inputString[x] == 'y':
            ycount += 1
        # move to next layer
        x += 1

    # this is a bit of a lazy implementation of the letter Y
    # I want to do something similar to how it was done in the later piglatin thing
    # but that would require looking at the string word by word instead of going
    # through the whole thing all at once

    print("You have " + str(vowelsCount) + " vowels! And sometimes " + str(ycount) + " more!")

elif menuchoice == "3":
    # if the user has picked 3 we check for palindromity

    e = len(inputString) - 1    # end of the string
    s = 0                       # beginning of the string
    isPalindrome = True         # flag of palindromity
    while s < e and isPalindrome:
        # while the iterators have not overlapped and we haven't found nonmatching pairs
        while inputString[s].isspace():
            # we should ignore white space for multi-word palindromes
            s += 1
        while inputString[e].isspace():
            e -= 1  
        # move to the next pair of letters
        s += 1
        e -= 1
        if inputString[s] != inputString[e]:
            # if the letters don't match print it and flip our flag
            print("That's not a palindrome!")
            isPalindrome = False
    if isPalindrome:
        # if we finish the while loop without flipping the flag, it must be a palindrome
        print("That's a palindrome!")

elif menuchoice == "4":
    # if user chooses 4, it's piglatin time

    vowels = {'a','e','i','o','u'}
    # same vowel list from before

    words = inputString.split()
    # split the string into words delineated by white space

    pigLatin = []
    # empty list to put piglatin words into

    for w in words:
        # for each word found
        suffix = ""
        # reset suffix to empty
        letterCount = 0
        # reset letter count to zero
        if vowels.__contains__(w[0]):
            # if it starts with a vowel (NOT Y), the suffix is just "ay"
            suffix += "ay"
        else:
            # if we start with a consonant (or a y)
            while not (vowels.__contains__(w[0])):
                # while we're not looking at a vowel
                if letterCount == 0 and w[0] == "y":
                    # if we're at the first lettter, and it's a Y, we're good to treat
                    # it as a consonant
                    suffix += w[0]
                    # add the first letter to the suffix
                    w = w[1:]
                    # remove the first letter
                    letterCount += 1
                    # more to the next letter
                elif w[0] == "y":
                    # if we're NOT at the first letter and it's a Y, it's treated as a vowel
                    break
                else:
                    # if it's not a why, we're good to do the same incrementing
                    suffix += w[0]  
                    w = w[1:]
                    letterCount += 1
            suffix += "ay"
            # add "ay" to the end of the suffix
        w += suffix
        # add the suffix to the end of the word
        pigLatin.append(w)
        # put the new Pig Latin word into our list
    for word in pigLatin:
        # print each word
        print(word, end = " ")
    print ("\n")
    # line break after the pig latin
elif menuchoice == "5":
    # easy one if 5 is chosen, just count the words

    words = inputString.split()
    # split the string into words
    wordCount = len(words)
    # get the number of words
    print("You entered " + str(wordCount) + " words!")
    # print the number of words
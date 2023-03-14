# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    check = False
    i , j = 1 , 1 # i is width, j is length
    while check == False: # Loops code if parameters not met
            if (i*2) + (j*2) == perimeter and j * i == area: # Checks for width and height
                check = True
            elif j != area: # Runs code if j is not equal to area
                if i != area: # Checks if i has reached area
                    i += 1 # Increments i
                else:
                    j += 1 # Increments j
                    i = 0 # Resets i to 0
            else:
                return(False) # If no parameters meet, return false
    
    if i > j: # Checks largest w/h 
        return(i)
    else:
        return(j)

def get_index(num, digit):
    """
        >>> get_index(1495, 5)
        1
        >>> get_index(1495, 1)
        4
        >>> get_index(1495423, 4)
        3
        >>> get_index(1495, 7)
        -1
    """
    #- YOUR CODE STARTS HERE
    count = 1
    while(num>0): # Continues loop if num is greater than 0
        compDigit = num % 10 # sets compDigit as right most digit
        if compDigit == digit: # Checks if compDigit is digit
            return(count)
        elif num != 0: # Checks if num is not 0
            num = num // 10 # Removes rigth most digit
            count += 1 # Increases count

    return(-1)

def unique_largest(num):
    """
        >>> unique_largest(123132)
        False
        >>> unique_largest(7264578364)
        True
        >>> unique_largest(2)
        True
        >>> unique_largest(444444)
        False
    """
    #- YOUR CODE STARTS HERE
    maxDigit = 0
    compNum = num
    count = 0
    while(compNum>0):
        if num != 0:
            digit = num % 10 # Checks for digit
            if digit > maxDigit:
                maxDigit = digit # Sets digit to maxDigit, if digit is the largest
            else:
                num = num // 10 # Increments number down
        else: # Continues problem once max digit of num is found
            if compNum != 0:
                compDigit = compNum % 10
                if compDigit == maxDigit:
                    count += 1 # Increments count for each time digit is repeated
                compNum = compNum // 10 # Increments compNum down
    
    '''
    By compressing all the code into two steps
    in an if and else condition I was able to write the code
    in only 1 loop, as per the challenge.
    '''

    if count == 1: # If maxDigit is present once return True
        return True
    else:
        return False
    
def joined_list(n):
    """
        >>> joined_list(5) 
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joined_list(-8) 
        [-8, -7, -6, -5, -4, -3, -2, -1, -1, -2, -3, -4, -5, -6, -7, -8]
    """
    #- YOUR CODE STARTS HERE 

    '''
    lst = [] # Create empty list
    if n >= 1: # Check if positive
        lst = [*range(1,n+1)] # Start adding iterations
        lst += list(reversed(lst)) # Reverse initial list and add it to lst
    if n <= 1:
        lst = [*range(n, 0)] # Start adding iterations
        lst += list(reversed(lst)) # Reverse initial list and add it to lst
    return lst
    
    # New code, I wasn't sure if the method reversed or the * were allowed. So I'm not submitting this one
    '''

    count = 0 # Creates count
    lst = []
    i = 1 # Increment for positive number
    j = 0 # Increment for negative number
    max = abs(n) # Finds max by taking absolute value of n

    if n > 0:
        maxCount = abs(n) * 2 # If n is positive max count is double
    elif n < 0:
        maxCount = (abs(n) * 2) - 1 # If n is negativ max count is double - 1

    while (count < maxCount): # Loop runs double the amount of the number
        if n > 0: # Checks if positive
            count += 1
            if count <= max:
                lst += [i] # Adds to list
                if count != n:
                    i += 1 # Increment n
            elif count >= max: # Checks if count is greater than max
                lst += [i] # Adds to list
                i -= 1
        elif -max < 0: # Checks if negative
            count += 1
            if count <= max:
                lst += [n + j] # Adds to list
                if count != max: # Checks if count is not equal to max
                    j += 1 # Increment j
            if count >= max:
                lst += [n + j] # Adds to list
                j -= 1

    return(lst)

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526,
263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 
1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 
1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 
4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184,
92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 
2, 1]
    """
    #- YOUR CODE STARTS HERE
    check = False
    temp = num # Sets temp to num
    lst = []

    lst += [temp] # Adds original num to lst

    if num == 1:
        return[1]

    while check == False:
        if temp % 2 == 0: # Checks if number is even
            temp = temp / 2 # Does hailstone algorithm
            lst += [int(temp)] # Adds to lst, converts to int
        elif temp % 2 != 0: # Checks if number is not even
            temp = temp * 3 + 1 # Does hailstone algorithm
            lst += [int(temp)] # Adds to lst, converts to int
        
        if temp == 1: # Checks temp == 1
            check = True # Ends while loop

    return(lst)

def is_isomorphic(word1, word2):
    """
        >>> is_isomorphic("egg", "add")
        True
        >>> is_isomorphic ("foo", "car") 
        False
        >>> is_isomorphic ("badc", "baba") 
        False
    """
    #- YOUR CODE STARTS HERE
    dictOne = {}
    dictTwo = {}

    countOne = 1
    for letter in word1: # Iterate by letter
        dictOne[letter] = countOne # Assign number value to key
        countOne += 1 # Increments value

    countTwo = 1
    for letter in word2: # Iterate by letter
        dictTwo[letter] = countTwo # Assign number value to key
        countTwo += 1 # Increments value
    
    lstOne = []
    for letter in word1: # Iterate by letter
        if letter in dictOne:
            lstOne += [dictOne[letter]] # Assigns numerical value to lst of letter
    
    lstTwo = []
    for letter in word2: # Iterate by letter
        if letter in dictTwo: 
            lstTwo += [dictTwo[letter]] # Assigns numerical value to lst of letter

    if lstOne == lstTwo: # Check if number assignments match
        return True
    else:
        return False

def translate(translation_file, msg):
    """
        >>> translate('abbreviations.txt', 'c u in 5.')
        'see you in 5.'
        >>> translate('abbreviations.txt', 'gr8, cu')
        'great, see you'
        >>> translate('abbreviations.txt', 'b4 lunch, luv u!')
        'before lunch, love you!'
    """
    # Open file and read lines into one string all the way to the end of the file
    with open(translation_file) as file:   
        contents = file.read()
    #- YOUR CODE STARTS HERE

    lst = []
    contents = contents.split("\n") # Splits .txt content into a list at \n
    for words in contents:
        a,b = words.split("=") # Splits each word content at =
        lst += [(a,b)]
    translations = dict(lst) # Converts lst to dict

    msg = msg.split() # Splits msg into a list
    
    punc = ['.', '?', '!', ',', ';', ':', ')'] # Punctuation key
    puncList = []
    puncIndex = []
    puncCount = -1

    for word in msg: 
        puncCount += 1 # Counts the index of the word with punc
        for letter in word:
            if letter in punc: # Checks for punc in word
                word = word.replace(letter, "") # Removes punc
                if word in translations:
                    temp = str(translations[word]) + str(letter) # Converts word then adds the punc back
                    puncList += [temp] # Adds word with punc to list
                    puncIndex += [puncCount] # Keeps track of index of punc words
                elif word not in translations:
                    temp = str(word) + str(letter) # Adds punc back to word
                    puncList += [temp] # Adds word with punc to list
                    puncIndex += [puncCount] # Keeps track of index of punc words

    noList = []

    for word in msg: 
            if word in translations:
                noList += [translations[word]] # Adds words that may be translated to normal list
            else:
                noList += [word] # Adds words to normal list

    j = 0 # Keeps track of the index to put the punc word from punc list into
    for i in range(len(noList)):
        if i in puncIndex:
            noList[i] = puncList[j] # Adds correct translated word from puncList to noList
            j += 1 # Iterates index up
    
    noList = " ".join(noList) # Joins list together

    return(noList)
    
def addToTrie(trie, word):
    """      
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' :
True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': 
{'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': 
{'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': 
True}}}}}
    """
    #- YOUR CODE STARTS HERE
    tempTrie = trie # Create temp Trie with same mememory allocation

    for ch in word: # Iterate through word
        if ch not in tempTrie: # Check if ch in trie
            tempTrie[ch] = {} # If not create dictionary spot
        tempTrie = tempTrie[ch] # Changes trie position
    tempTrie['word'] = True # End word

    return trie

def run_tests():
    import doctest
    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. 

    doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True) 
if __name__ == "__main__":
    run_tests()
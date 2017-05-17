import itertools # handy for making permutations
right = 0
# Question 1:
# Given two strings s and t, determine whether some anagram of t is a
# substring of s. For example: if s = "udacity" and t = "ad", then the
# function returns True. Your function definition should look like:
# question1(s, t) and return a boolean True or False.

def make_permutations(t):
    # generate all permutations using all characters in the string t
    perms = [''.join(perm) for perm in itertools.permutations(t)]
    return perms

def question1(s, t):
    # check to see if any of the permutations of t are found in s
    tlist = list(t) # break string t into a list
    anagram = ""
    for i in tlist:
        if i in s:
            anagram = anagram + i
    # do not continue unless at least 2 letters of t are found in s
    if len(anagram) > 1:
        tPerms = make_permutations(anagram)
    else:
        return False
    # test for permutations of t in s - result True on first occurrance
    for q in tPerms:
        if q in s:
            return True
    return False

# Test Cases for Question 1:

print(question1("udacity", "ad"))
# True
print(question1("",""))
# False
print(question1("""
    And upon this act, sincerely believed to be an act of justice, warranted
    by the Constitution, upon military necessity, I invoke the considerate
    judgment of mankind, and the gracious favor of Almighty God.
    ""","Amgtlihy"))
# True

# Question 2:
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def is_palindrome(s):
    return s==s[::-1] # inverts the string and compares to the original

def find_palindrome(s): # checks for odd palindromes
    if is_palindrome(s): # if the whole string is a palindrome, then exit
        return s
    temp = "" # for holding the largest palindrome found
    left=0
    global right
    # check each substring of 3 characters for a palindrome
    while right <= len(s):
        pstr = (s[left:right])
    # if it is, then set it to temp and include the next outlying chars
        if is_palindrome(pstr):
            if len(pstr) > len(temp):
                temp = pstr
            if left > 0:
                left -= 1
            right += 1
        else:
            left += 1
            right += 1
    return temp

def question2(s):
    global right
    right = 3
    t1 = find_palindrome(s)
    right = 4
    t2 = find_palindrome(s)
    if len(t1) > len(t2):
        return t1
    else:
        return t2

# Test Cases for Question 2:

print(question2("abaab"))
#baab
print(question2("aabaab"))
#aabaa
print(question2("hereisareallyyllaerpalindromewithmorethanahterompalindrome"))
#

import itertools # handy for making permutations
import sys # for passing in arguments from the prompt

s = sys.argv[1] # get the first variable passed in from prompt
t = sys.argv[2] # get the second variable passed in from prompt

def make_permutations(t):
    # generate all permutations using all characters in the string t
    perms = [''.join(perm) for perm in itertools.permutations(t)]
    return perms

def question1(s, t):
    # check to see if any of the permutations of t are found in s
    tlist = list(t) # brean string t into a list
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

print(question1(s,t))



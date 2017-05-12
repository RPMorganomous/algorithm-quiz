import itertools # handy for making permutations
import sys # for passing in arguments from the prompt

s = sys.argv[1]
t = sys.argv[2]

def make_permutations(t):
    perms = [''.join(perm) for perm in itertools.permutations(t)]
    return perms

def question1(s, t):
    tlist = list(t)
    anagram = ""
    for i in tlist:
        if i in s:
            anagram = anagram + i
    if len(anagram) > 1:
        tPerms = make_permutations(anagram)
    else:
        return False
    for q in tPerms:
        if q in s:
            return True
    return False

print(question1(s,t))



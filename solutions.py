import collections # great for counting characters

# Question 1:
# Given two strings s and t, determine whether some anagram of t is a
# substring of s. For example: if s = "udacity" and t = "ad", then the
# function returns True. Your function definition should look like:
# question1(s, t) and return a boolean True or False.

def question1(s, t):
    if s and t:
        count_t = collections.Counter(t)
        i = 0
        j = len(t)
        while i <= (len(s)-j):
            substring = (s[i:i+j])
            count_s = collections.Counter(substring)
            if count_s == count_t:
                return True
            i += 1
        return False
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

print(question1("yticadu", "udacity"))
# True

# Question 2:
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

right = 0

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

def question2(s = ""):
    if s:
        global right
        right = 3
        t1 = find_palindrome(s)
        right = 4
        t2 = find_palindrome(s)
        if len(t1) > len(t2):
            return t1
        else:
            return t2
    return("Nothing to see here...")

# Test Cases for Question 2:

print(question2("abaab"))
#baab
print(question2("aabaab"))
#aabaa
print(question2("hereisareallyyllaerpalindromewithmorethanahterompalindrome"))
#morethanahterom
print(question2(""))
#Nothing to see here...
print(question2())
#Nothing to see here...

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}

from collections import defaultdict
import pprint

def question3(graph):

    # test for dictionary
    if type(graph) != dict:
        return "Try using a dictionary next time."

    adj_list = graph

    # create the vertices
    verts = adj_list.keys()

    # create the edges and sort them
    edges = set()
    for vert in verts:
        for edge in adj_list[vert]:
            new_edge = (vert,edge[0],edge[1])
            old_edge = (edge[0],vert,edge[1])
            if old_edge not in edges:
                edges.add((new_edge))
    sorted_edges = sorted(edges, key=lambda edge_value: edge_value[2])

    #go through the sorted edge list and add as long as vert is not already added

    mst_list = []
    mst_list_verts_used1 = set()
    mst_list_verts_used2 = set()

    # check each edge and add to the graph starting from smallest edge to largest
    for edge in sorted_edges:
        if len(mst_list) == 0:
            mst_list.append({edge[0]:(edge[1],edge[2])})
            mst_list_verts_used1.add(edge[0])
            mst_list_verts_used1.add(edge[1])
        else:
            # if the edge has not been used, assign it to the graph and a set
            # sets keep from closing the loop within the graph
            # when one node joins two sets, combine the sets
            if len(mst_list) < (len(adj_list)-1):
                if (edge[0] not in mst_list_verts_used1) or (edge[1] not in mst_list_verts_used1):
                    if (edge[0] or edge[1]) not in mst_list_verts_used2:
                        if (edge[0] or edge[1]) in mst_list_verts_used1:
                            if edge[0] in mst_list_verts_used2 or edge[1] in mst_list_verts_used2:
                                mst_list.append({edge[0]:(edge[1],edge[2])})
                                mst_list_verts_used1.update(mst_list_verts_used2)
                                mst_list_verts_used2.clear()
                            else:
                                mst_list.append({edge[0]:(edge[1],edge[2])})
                                mst_list_verts_used1.add(edge[0])
                                mst_list_verts_used1.add(edge[1])
                        else:
                            mst_list.append({edge[0]:(edge[1],edge[2])})
                            mst_list_verts_used2.add(edge[0])
                            mst_list_verts_used2.add(edge[1])
                    else:
                        break

    # create reciprocal nodes

    vList = (sorted(mst_list))
    out_dict = {}
    for item in vList:
        ((x,y),) = item.items()
        out_dict.setdefault(x, []).append(y)

    # now combine key value entries in dict

    for fnode, info in out_dict.items():
        for node, val in info:
            if node in out_dict and ((fnode, val)) in out_dict[node]:
                break
            else:
                if not node in out_dict:
                    out_dict[node] = [(fnode, val)]
                else:
                    out_dict[node].append((fnode, val))

    return out_dict

graph_in = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]}

pprint.pprint(question3(graph_in))
# {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}

# Kruskal's Algorithm example case found on wikipedia: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
graph_in = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
    'F': [('D', 6), ('E', 8), ('G', 11)],
    'G': [('E', 9), ('F', 11)]}

pprint.pprint(question3(graph_in))
# {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
# {'A': [('B', 7), ('D', 5)],
#  'B': [('E', 7), ('A', 7)],
#  'C': [('E', 5)],
#  'D': [('F', 6), ('A', 5)],
#  'E': [('G', 9), ('C', 5), ('B', 7)],
#  'F': [('D', 6)],
#  'G': [('E', 9)]}

graph_in = "junk"

pprint.pprint(question3(graph_in))
# 'Try using a dictionary next time.'

# Question 4

# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an
# ancestor of both nodes. For example, the root is a common ancestor of all
# nodes on the tree, but if both nodes are descendants of the root's left
# child, then that left child might be the lowest common ancestor. You can
# assume that both nodes are in the tree, and the tree itself adheres to
# all BST properties. The function definition should look like
# question4(T, r, n1, n2), where T is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node
# and a 1 represents a child node, r is a non-negative integer representing
# the root, and n1 and n2 are non-negative integers representing the two nodes
# in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)

def question4(T, r, n1, n2):
    nx1 = -1
    nx2 = -1
    for i, j in enumerate(T[r]):
        if j == 1:
            if nx1 == -1:
                nx1 = i
            else:
                nx2 = i

    if r > max(n1, n2):
        return question4(T, min(nx1, nx2), n1, n2)

    if r < min(n1, n2):
        return question4(T, max(nx1, nx2), n1, n2)

    return r


print "lca =", question4([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]],
    3,
    1,
    4)
# lca = 3

print "lca =", question4([
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]],
    3,
    0,
    2)
# lca = 1

print "lca =", question4([
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]],
    3,
    4,
    6)
# lca = 5

try:
    print "lca = ", question4()
except:
    print "Bad Tree"
# lca = Bad Tree

try:
    print "lca =", question4([
    [0, 0, 0, 0, 0, 0, 0],
    [X, 0, X, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, X, 0, 0, 0, X, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, X, 0, X],
    [0, 0, 0, 0, 0, 0, 0]],
    3,
    4,
    6)
except:
    print "Bad Tree"
# lca = 5

# Question 5
# Find the element in a singly linked list that's m elements
# from the end. For example, if a linked list has 5 elements,
# the 3rd element from the end is the 3rd element. The function
# definition should look like question5(ll, m), where ll is the
# first node of a linked list and m is the "mth number from the
# end". You should copy/paste the Node class below to use as a
# representation of a node in the linked list. Return the value
# of the node at that position.
#
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

def question5(ll, m):
    if m > 0:
        count = ll.getCount()
        item = ll.head
        i = 0
        while (i < (count - m)):
            i += 1
            item = item.next
        return item.data
    else:
        return ("must be greater than 0")
# create the linked list
ll = LinkedList()

# fill the linked list data values = 1-10
for i in range(1, 11):
    ll.push(i)

print(question5(ll, 3))
# 3

print(question5(ll, 5))
# 5

print(question5(ll, 12))
# 10

print(question5(ll, 1))
# 1

print(question5(ll, 0))
# must be greater than 0
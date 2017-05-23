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
    # test for permutations of t in s - result True on first occurrence
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
#morethanahterom

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

# define tree classes and helpers
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

# trace tree beginning with the root node
def find_path(T, r):
    tree = BST(r)
    for i, j in enumerate(T[r]):
        if j==1:
            #print("node ", r, " is parent of node ", i)
            tree.insert(i)
            find_path(T, i)

# search the tree left and right to find the lowest common ancestor
def find_lca(r, n1, n2):

    # if n1 and n2 are less than the root, then lca is to the left
    if (r > n1 and r > n2):
        print r, n1, n2, r.left
        return find_lca(r.left, n1, n2)

    # if n1 and n2 are greater than the root, then lca is to the right
    if (r < n1 and r < n2):
        return find_lca(r.right, n1, n2)
    return r

def question4(T, r, n1, n2):
    find_path(T, r)
    lca = find_lca(r, n1, n2)
    return lca

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
    count = ll.getCount()
    item = ll.head
    i = 0
    while (i < (count - m)):
        i += 1
        item = item.next
    return item.data

# create the linked list
ll = LinkedList()

# fill the linked list data values = 1-10
for i in range(1, 11):
    ll.push(i)

print(question5(ll, 3))
# 3

print(question5(ll, 5))
#5

print(question5(ll, 12))
# 10
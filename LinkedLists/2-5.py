"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295. Output: 2 -) 1 -) 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295. Output: 9 -) 1 -) 2.That is, 912.
"""

def add_lists( n1, n2, carry)
if n1 == None and n2 == None and carry == 0:
    return None

value = carry
if n1 != None:
    value += n1.data 
if n2 != None:
    value += n2.data

result_node = node()
result_node.data = value % 10
if value > 10:
    carry = 1
else:
    carry = 0
if n1 != None or n2 != None:
    add_lists( n1.next, n2.next, carry)

#TODO - Complete exercise with recursion 
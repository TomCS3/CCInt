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
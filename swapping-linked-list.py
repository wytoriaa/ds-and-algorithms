def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node 
    #node1: the node that matches val1
    node2 = input_list.head_node
    #node2: the node that matches val2
    node1_prev = None
    #node1_prev: node1‘s previous node
    node2_prev = None
    #node2_prev: node2‘s previous node

#Finding the Matching and Preceding Nodes
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

#Updating the Preceding Nodes’ Pointers
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)
    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)
#Updating the Nodes’ Next Pointers
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

#Time Complexity = O(n) if both while loops must iterate all the way through to the end
#and new variables O(1).

ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
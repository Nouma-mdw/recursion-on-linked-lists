'''
Define a function called remove_node() that takes in the following parameters:

head - a node that acts as the head of a linked list
i - an integer
The function should remove the ith node of the linked list (index from 0) and return the modified head.

Example:

Input: remove_node(head = "Amber"->"Sapphire"->"Jade"->"Pearl", 1)
Output: head = "Amber"->"Jade"->"Pearl"
The LinkedList class has been implemented for you. You do not need to modify it.
'''

import LinkedList

# # Definition for singly-linked list node.
# class ListNode:
#   def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
  if i < 0:
    return head  
  # base_case
  if head is None:
    return None
  if i == 0:
    return head.next_node
  # recursive step
  head.next_node = remove_node(head.next_node, i - 1)

  return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
# head = remove_node(gemstones.head, 0)
# print(head.flatten())
# print(head.value)

print(gemstones.head.flatten())

# real remove i-th node,
# that actually chanffes the linekd list
# def remove_ith_node(ll, i):
#   current_node = ll.head
#   if i < 0:
#     return None
#   # base case 0
#   if current_node is None:
#     return None
#   # base case 1
#   if i == 0:
#     ll.head = current_node.next_node
#     return current_node.value

#   # while loop
#   prev_node = current_node 
#   while True:
#     target_node = prev_node.next_node
#     if target_node == None:
#       return None
#     i -= 1
#     if i == 0:
#       break
#     prev_node = prev_node.next_node
#   prev_node.next_node = target_node.next_node

#   return target_node.value

# valid tests for change in 
# print("\n\nRemoved Node", remove_ith_node(gemstones, 0))
# print(gemstones.head.flatten())


  ### recursive remove_ith Node
def rec_remove_ith_node(ll, i, current_node = None, prev = None):
  if current_node is None:
    target_node = ll.head
  else:
    target_node = current_node
  if i < 0:
    return None
  # base case 0
  if target_node is None:
    return None
  # base case 1
  if i == 0:
    if prev == None:
      ll.head = target_node.next_node
      return target_node.value
    else:
      prev.next_node = target_node.next_node
      return target_node.value

  # recursive step
  if i != 0 and target_node.next_node != None:
    target_node_value = rec_remove_ith_node(ll, i -1, target_node.next_node, target_node)
    return target_node_value
  else:
    return None

# valid tests for change in 
print("\n\nRemoved Node", rec_remove_ith_node(gemstones, 3))
print(gemstones.head.flatten())
print(gemstones.head.value)
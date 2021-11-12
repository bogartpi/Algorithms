# Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        copy_map = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copy_map[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copy_map[curr]
            copy.next = copy_map[curr.next]
            copy.random = copy_map[curr.random]
            curr = curr.next
        
        return copy_map[head]
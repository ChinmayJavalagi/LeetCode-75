'''
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        if not head or head.next==None:
            return None
        slow=fast = ListNode(next=head)
        while fast.next!=None and fast.next.next!=None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head

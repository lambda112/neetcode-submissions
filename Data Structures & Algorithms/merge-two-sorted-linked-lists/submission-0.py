# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # 0
        trav = dummy # 0

        # [1,4,5]
        # [1,3,6]

        while list1 and list2:
            if list1.val <= list2.val: #(1,1),(4,1),(4,3),(4,6),(5,6)
                trav.next = list1 # 0->1, 4->5
                list1 = list1.next # 4,5,None
            else:
                trav.next = list2 # 0->1, 1->3 
                list2 = list2.next # 3,6,None

            trav = trav.next # 1,1,3,4,5
        
        trav.next = list1 if list1 else list2 #6
        return dummy.next #1,1,3,4,5,6
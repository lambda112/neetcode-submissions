# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []

        while head != None:
            num_list.append(head.val)
            head = head.next
        
        if not num_list: 
            return None

        num_list.reverse()
        new_head = ListNode(num_list[0])
        trav = new_head

        for val in range(1, len(num_list)):
            trav.next = ListNode(num_list[val])
            trav = trav.next

        return new_head

            




        
            





        


        
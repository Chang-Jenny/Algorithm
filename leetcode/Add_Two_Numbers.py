# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 儲存計算結果(建立一Linked list)
        outcome = ListNode()
        cal = outcome
        now = 0
        
        
        # 兩個list開始計算
        while(l1 or l2 or now%10):
            if l1:
                now+=l1.val
                l1 = l1.next
            if l2:
                now+=l2.val
                l2 = l2.next
            
            # 考慮最後一個node的進位
            cal.next = ListNode(now%10)
            cal = cal.next
            now=now//10
        return outcome.next
            

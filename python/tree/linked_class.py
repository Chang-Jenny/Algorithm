class ListNode:
  def __init__(self, val=0, next=None):
    self.val=val
    self.next=next
    
node1 = ListNode()
node2 = ListNode(2)
node1.next=node2

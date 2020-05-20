# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
from common.linkedlist import ListNode
from common.printer import printLinkedList

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            # swap
            swapA = pre.next
            swapB = swapA.next
            pre.next, swapB.next, swapA.next = swapB, swapA, swapB.next
            pre = swapA
        return self.next
        
# Testcase
node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

foo = Solution()
result = foo.swapPairs(node1)

while result:
    print (result.val)
    result = result.next

# Tips
# 这里用到了一个技巧，因为这个技巧导致了之前一直看不懂代码。
# 代码中将pre = self，是利用了self的特性，这里的self相当于js中的{}空对象
# 在循环体外，初始化pre为self，并且给self赋值了一个next属性为head
# 这样写的目的是为了最终可以获取到一个可以返回的结果
# 因此while循环体内就是做swap操作，并且循环一次之后将pre指向了第二个节点确保了current指针是第三个，并且以此类推
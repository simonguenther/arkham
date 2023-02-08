# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        while A.next is not None and B.next is not None:
            

if __name__ == "__main__":
    A = [1,2,3]
    B = [4,5,6]
    x = Solution().mergeTwoLists(A,B)    
            

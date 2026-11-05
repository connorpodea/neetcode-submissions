class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # The intuitive approach to this problem would be to add values to a dict, where
        # the key is the number and the value is the occurance count, to identify the
        # duplicates. However, this requires O(n) space. 

        # According to the solution, this is a non-intuitive algorithm and one that should 
        # ideally be marked as hard. Basically, if this every happens in an interview, you
        # have to know it to solve it, its difficult to organically discover or propose the
        # algorithm in an interview setting.

        # From my initial understanding of the video solution, we will treat this as a linked-list
        # cycle problem. To solve this problem, give the values meaning. For ex, [1,2,3,2] means that
        # Our first node points to 2, our second node points to 3, our third node points to 2, and our
        # fourth node creates a cycle by pointing to 3.
        
        # Given this abstract view, we can solve this problem using slow/fast pointers. Our first iteration
        # will use a slow and fast pointer on our abstracted view of the values, to first determine
        # the initial "intersection" point of the two pointers. After this, we leave our slow pointer at
        # that node, then create another slow pointer at the beginning node, incrementing both of these
        # pointers until they again reach the same intersecting node. This will be the value we return.

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow
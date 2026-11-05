/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    size := 0
	trav := head
	
	for trav != nil {
		size += 1
		trav = trav.Next
	}

	target := size - n
	seen := 0

	// base case
	if target == 0 {
		return head.Next
	}

	trav = head
	for trav != nil {
		seen += 1
		if seen == target {
			trav.Next = trav.Next.Next
			break
		}
		trav = trav.Next
	}
	return head
}

// [1,2,3,4]
// n = 2
// size = 4
// target = 1
// seen = 1
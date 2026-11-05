/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var start *ListNode
	var prev *ListNode

	if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	if list1.Val <= list2.Val {
		start = list1
		prev = list1
		list1 = list1.Next
	} else {
		start = list2
		prev = list2
		list2 = list2.Next
	}

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			prev.Next = list1
			prev = list1
			list1 = list1.Next
		} else {
			mov := list2
			next := list1
			list2 = list2.Next
			prev.Next = mov
			mov.Next = next
			prev = mov
		}
	}

	if list1 != nil {
		prev.Next = list1
	}

	if list2 != nil {
		prev.Next = list2
	}

	return start
}
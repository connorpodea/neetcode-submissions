/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    res := [][]int{}

	if root == nil {
		return res
	}

	q := []*TreeNode{}
	q = append(q, root)
	
	for len(q) > 0 {
		level := []int{}
		size := len(q)
		
		for i := 0; i < size; i += 1 {
			node := q[0]
			q = q[1:]

			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}

			level = append(level, node.Val)
		}
		res = append(res, level)
	}
	return res
}

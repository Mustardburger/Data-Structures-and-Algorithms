def max_depth(root):
    """
    Given a binary tree and a root determine the maximum depth of a tree
    """
    depth = 1

    def trace(root, depth):
        if root == None: return 0
        if root.left == None and root.right == None:
            return depth

        depth_left = 0 if root.left == None else trace(root.left, depth+1) 
        depth_right = 0 if root.right == None else trace(root.right, depth+1)

        return max(depth_left, depth_right)

    return trace(root, depth)

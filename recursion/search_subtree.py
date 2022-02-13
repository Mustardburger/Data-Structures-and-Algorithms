class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_subtree(root, val):
    """
    Return a subtree with of a node that has val
    """
    if root.left == None and root.right == None:
        if root.val == val:
            return [root.val]
        else:
            return None
    if root.val == val:
        return [root.val, root.left.val, root.right.val]

    if root.left != None:
        left = find_subtree(root.left, val)
    if root.right != None:
        right = find_subtree(root.right, val)

    if left != None:
        return left
    elif right != None:
        return right
    else:
        return []

def main():
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2, node1, node2)
    node4 = TreeNode(7)
    root = TreeNode(4, node3, node4)
    print(find_subtree(root, 1))


if __name__ == "__main__":
    main()
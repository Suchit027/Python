class TreeNode:
    def __init__(self, val=0, left=None, right=None, rightthread=False):
        self.val = val
        self.right = right
        self.left = left
        self.rightthread = rightthread

    def inorderSucc(self, root):
        if root.rightthread is True:
            return root.right
        else:
            while root.left is not None:
                root = root.left
            return root

    def inorder(self, root):
        temp = root
        while True:
            temp = self.inorderSucc(temp)
            if temp == root:
                break
            print(temp.val)


def main():
    root = TreeNode(1, rightthread=False)
    r1 = TreeNode(2, rightthread=True)
    r2 = TreeNode(3, rightthread=True)
    root.left = r1
    r1.left = None
    r2.right = root
    root.right = r2
    r2.left = None
    r2.right = root
    root.inorder(root)


if __name__ == '__main__':
    main()

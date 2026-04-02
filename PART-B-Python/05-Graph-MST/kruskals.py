from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            root.count += 1
        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

bst = BST()

while True:
    print("\n1.Insert 2.Delete 3.Search 4.Display 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        bst.insert_key(x)
    elif ch == 2:
        x = int(input("Enter value: "))
        bst.root = bst.delete(bst.root, x)
    elif ch == 3:
        x = int(input("Enter value: "))
        print("Found" if bst.search(bst.root, x) else "Not Found")
    elif ch == 4:
        bst.inorder(bst.root)
        print()
    else:
        break
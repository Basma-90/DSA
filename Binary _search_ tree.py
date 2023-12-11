class Node:
    def __init__(self, key,right=None,left=None):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,node,key):
        
        if node is None:
            return Node(key)
        if key<node.key:
            if node.left is None:
                node.left=Node(key)
            else:
                node.left=self.insert(node.left,key)
        elif key>node.key:
            if node.right is None:
                node.right=Node(key)
            else:
                node.right=self.insert(node.right,key)
        else:
            print("Duplicate values not allowed")
        return node
        


    def search(self,root,key):
        if root is None or root.key==key:
            return root
        if root.key<key:
            return self.search(root.right,key)
        return self.search(root.left,key)


    def successor(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
    
    def predecessor(self,node):
        current=node
        while current.right is not None:
            current=current.right
        return current
    
    def delete(self,root,key):
        if root is None:
            return root
        if key<root.key:
            root.left=self.delete(root.left,key)
        elif key>root.key:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.successor(root.right)
            root.key=temp.key
            root.right=self.delete(root.right,temp.key)
        return root
    
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)
    
    def preorder(self,root):
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)
        
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)
    
    def height(self,root):
        if root is None:
            return -1
        else:
            return 1+max(self.height(root.left),self.height(root.right))
    

if __name__=='__main__':
    bst=BST()
    root=None
    root=bst.insert(root,50)
    root=bst.insert(root,30)
    root=bst.insert(root,20)
    root=bst.insert(root,40)
    root=bst.insert(root,70)
    root=bst.insert(root,60)
    root=bst.insert(root,80)
    print("Inorder traversal of the given tree")
    bst.inorder(root)
    print("\nDelete 20")
    root=bst.delete(root,20)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)
    print("\nDelete 30")
    root=bst.delete(root,30)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)
    print("\nDelete 50")
    root=bst.delete(root,50)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)
    print(bst.height(root))

class Node:
    def __init__(self, key,right=None,left=None):
        self.key = key
        self.left = None
        self.right = None
        self.height=0
    
    def get_child_height(self,node):
        if not node:
            return -1
        return node.height #0
    
    def update_height(self):
        self.height=1+max(self.get_child_height(self.left),self.get_child_height(self.right))
    
    def balance_key(self):
        return self.get_child_height(self.left)-self.get_child_height(self.right)
    
    def is_leaf(self):
        return not self.left and not self.right



class  AVL:
    def __init__(self):
        self.root = None
    

    def right_rotate(self,node):
        lft_node=node.left
        node.left=lft_node.right
        lft_node.right=node
        node.update_height()
        lft_node.update_height()
        return lft_node
    
    def left_rotate(self,node):
        rght_node=node.right
        node.right=rght_node.left
        rght_node.left=node
        node.update_height()
        rght_node.update_height()
        return rght_node
    
    def balance(self,node):
        if node.balance_key()==2:
            if node.left.balance_key()==-1:
                node.left=self.left_rotate(node.left)
            node=self.right_rotate(node)
        elif node.balance_key()==-2:
            if node.right.balance_key()==1:
                node.right=self.right_rotate(node.right)
            node=self.left_rotate(node)
        return node
    
    
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

        node.update_height()
        node=self.balance(node)
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
        root.update_height()
        root=self.balance(root)
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
        
    def valid_BST(self,current):
        lst=[]
        self.inorder(current)
        for idx in range(1, len(lst)):
            if lst[idx - 1] >= lst[idx]:
                return False
        return True
    

if __name__=='__main__':
    
    AVL_TREE = AVL()
    root = None
    # Test 1: Insertion and Deletion Test
    values_to_insert = [10, 20, 30, 15, 5, 25, 35]
    for value in values_to_insert:
        root = AVL_TREE.insert(root, value)
        print(f"Inserted {value}. Tree Height: {AVL_TREE.height(root)}")

    AVL_TREE.inorder(root)

    values_to_delete = [15, 25, 10]
    for value in values_to_delete:
        root = AVL_TREE.delete(root, value)
        print(f"Deleted {value}. Tree Height: {AVL_TREE.height(root)}")

    AVL_TREE.inorder(root)

    # Test 2: Search Test
    print("Search 20:", AVL_TREE.search(root, 20))
    print("Search 50:", AVL_TREE.search(root, 50))

    # Test 3: Traversal Tests
    print("Preorder:")
    AVL_TREE.preorder(root)

    print("Postorder:")
    AVL_TREE.postorder(root)

    # Test 4: Validity Test
    print("Valid BST?", AVL_TREE.valid_BST(root))

    # Test 5: Height Test
    print("Tree Height:", AVL_TREE.height(root))


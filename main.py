class Tree:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root , key):
   # if the tree is empty - return the vlue as a root
   if root is None: 
       return Tree(key)
   #otherwise check for smallest then left or largest then smallest
   if key < root.val: 
       root.left = insert(root.left, key)
   else:
       root.right = insert(root.right, key)
   return root


#function to delete a node from the tree
def delete (root,key):
    #base case
    if root is None:
        return root
    #reccur down the tree to search for the node to be deleted
    if key < root.val:
        root.left = delete(root.left,key)
    elif key > root.val:
        root.right = delete(root.right,key)
    else:
        #case 1 : node with no child node
        if root.left is None and root.right is None:
                return None
        #case 2: node with 1 child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        #case 3: node with 2 child nodes
        #get the inorder successor (smallest in the right in the right subtree)
        temp = findmin(root.right)

        #replace root values with successors value

        root.val = temp.val

        #delete the inorder successor
        root.right = delete(root.right, temp.val)

    return root

#function to find minimum value in the right subtree
def findmin(node):
    current = node
    while current.left is None:
        current = current.left
        return current
    
#inorder traversal(prints the node in sorted order)
def inordertraversal(root):
    if root:
        inordertraversal(root.left)
        print(root.val, end = "-")
        inordertraversal(root.right)

#usage
root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)

root = insert(root,60)
root = insert(root,70)
root = insert(root,80)

print("inorder traversal before deleting:")

inordertraversal(root)

root = delete (root, 70)
print = ("inorder traversal after deleting: ")
inordertraversal(root)


from random import random
from typing import Tuple
 
 
class Node:
    """
    Treap's node
    Treap is a binary tree by value and heap by priority
    """
 
    def __init__(self, value: int = None):
        self.value = value
        self.prior = random()
        self.left = None
        self.right = None
 
    def __repr__(self):
        from pprint import pformat
 
        if self.left is None and self.right is None:
            return f"'{self.value}: {self.prior:.5}'"
        else:
            return pformat(
                {f"{self.value}: {self.prior:.5}": (self.left, self.right)}, indent=1
            )
 
    def __str__(self):
        value = str(self.value) + "\n" "P:"+ str(self.prior)
        left = str(self.left or "")
        right = str(self.right or "")
        return value+"\n" + left + "\n" + right+"\n"
 
 
def split(root: Node, value: int) -> Tuple[Node, Node]:
  
    if root is None:  # dos trees None
        return (None, None)
    elif root.value is None:
        return (None, None)
    else:
        if value < root.value:
        
            left, root.left = split(root.left, value)
            return (left, root)
        else:
            
            root.right, right = split(root.right, value)
            return (root, right)
 
 
def merge(left: Node, right: Node) -> Node:
   
    if (not left) or (not right):  # If one node is None, return the other
        return left or right
    elif left.prior < right.prior:
       
        left.right = merge(left.right, right)
        return left
    else:
       
        right.left = merge(left, right.left)
        return right
 
 
def insert(root: Node, value: int) -> Node:
  
    node = Node(value)
    left, right = split(root, value)
    return merge(merge(left, node), right)
 
 
def erase(root: Node, value: int) -> Node:
    """
    Erase element
 
    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    left, right = split(root, value - 1)
    _, right = split(right, value)
    return merge(left, right)
 
 
def inorder(root: Node):
    """
    Just recursive print of a tree
    """
    if not root:  # None
        return
    else:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
 
 
def interactTreap(root, args):
    """
    Commands:
    + value to add value into treap
    - value to erase all nodes with value
 
        >>> root = interactTreap(None, "+1")
        >>> inorder(root)
        1 
        >>> root = interactTreap(root, "+3 +5 +17 +19 +2 +16 +4 +0")
        >>> inorder(root)
        0 1 2 3 4 5 16 17 19 
        >>> root = interactTreap(root, "+4 +4 +4")
        >>> inorder(root)
        0 1 2 3 4 4 4 4 5 16 17 19 
        >>> root = interactTreap(root, "-0")
        >>> inorder(root)
        1 2 3 4 4 4 4 5 16 17 19 
        >>> root = interactTreap(root, "-4")
        >>> inorder(root)
        1 2 3 5 16 17 19 
        >>> root = interactTreap(root, "=0")
        Unknown command
    """
    for arg in args.split():
        if arg[0] == "+":
            root = insert(root, int(arg[1:]))
 
        elif arg[0] == "-":
            root = erase(root, int(arg[1:]))
 
        else:
            print("Unknown command")
 
    return root
 
 
def main():
    """After each command, program prints treap"""
    root = None
    print(
        "Ingrese cualquier número con el comando de /+/ para agregar un valor al treap y /-/ para eliminar. "
        "Utilice 'q' para cerrar el programa. "
    )
 
    args = input()
    while args != "q":
        root = interactTreap(root, args)
        print(root)
        
        inorder(root)
        #print(self.priority)
        args = input()
 
    print("hasta pronto!")
 
 
if __name__ == "__main__":
    #import doctest
 
    #doctest.testmod()
    main()
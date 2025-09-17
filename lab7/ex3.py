class Node:
    def __init__(self, data, left=None, right=None, balance = 0):
        self.data = data
        self.left = left
        self.right = right
        self.lHeight = 0
        self.rHeight = 0
    def balance(self):
        return self.rHeight - self.lHeight
    def height(self):
        return max([self.lHeight, self.rHeight])
    def calcLHeight(self):
        if self.left == None:
            self.lHeight = 0
        else:
            self.lHeight = max([self.left.calcLHeight(), self.left.calcRHeight()])
        return self.lHeight
    def calcRHeight(self):
        if self.right == None:
            self.rHeight = 0
        else:
            self.rHeight = max([self.right.calcLHeight(), self.right.calcRHeight()])
        return self.rHeight

class AVLTree:
    def __init__(self, array=None):
        self.root = None
        if array:
            for x in array:
                self.insert(x)
    def insert(self, newNode):
        if type(newNode) != Node: newNode = Node(newNode)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            trace = []
            pivot = None
            while True:
                trace.append(curNode)
                if curNode.balance != 0:
                    pivot = curNode
                    trace = [pivot]
                if newNode.data <= curNode.data:
                    if curNode.left is None:
                        curNode.left = newNode
                        curNode.lHeight = 1
                        break
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right is None:
                        curNode.right = newNode
                        curNode.rHeight = 1
                        break
                    else:
                        curNode = curNode.right
            if pivot == None:
                print("Case #1: Pivot not detected")
            else:
                son = newNode
                trace.reverse()
                for curNode in trace:
                    newHeight = max([son.rHeight, son.lHeight])
                    if son == curNode.right:
                        curNode.rHeight = newHeight
                        if curNode.rHeight <= curNode.lHeight:
                            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                            return
                    elif son == curNode.left:
                        curNode.lHeight = newHeight
                        if curNode.lHeight <= curNode.rHeight:
                            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                            return
                    else:
                        raise RuntimeError("son should be a child of curNode")
                    grandson = son #not neccessary for this loop, but needed later
                    son = curNode
                if pivot.balance() in [-1, 0, 1]:
                    raise RuntimeError("pivot was fine when it shouldn't have been")
                #FIXME I'm not sure that the following if/elif block is right
                if son==pivot.right and grandson==son.right:
                    self._left_rotate(pivot)
                elif son==pivot.left and grandson==son.left:
                    self._right_rotate(pivot)
                elif son==pivot.left and grandson==son.right:
                    self._lr_rotate(pivot)
                elif son==pivot.left and grandson==son.left:
                    self._rl_rotate(pivot)
                else:
                    raise RuntimeError("son should be a child of pivot and grandson should be a child of son")
    def _left_rotate(pivot):
        ...
    def _right_rotate(pivot):
        ...
    def _lr_rotate(pivot):
        AVLTree._left_rotate(pivot.left.right)
        AVLTree._right_rotate(pivot)
    def _rl_rotate(pivot):
        AVLTree._right_rotate(pivot.right.left)
        AVLTree._left_rotate(pivot)

def main():
    ...
if __name__ == "__main__":
    main()
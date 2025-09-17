def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def div(x,y): return x/y
op_dict = {'+':add, '-':sub, '*':mul, '/':div}

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, data):
        prev = self.head
        self.head = Node(data, prev)
        self.size += 1
    def pop(self):
        top = self.head
        self.head = self.head.next
        self.size -= 1
        return top
    def peek(self): return self.head
    def getSize(self): return self.size
    def __str__(self):
        curNode = self.head
        string = ""
        while curNode != None:
            string += str(curNode.data)
        return string

def brac_stack(char_list):
    expression = Stack()
    if char_list[0] == '(':
        i = 1
        while i < len(char_list):
            ...
    else:
        value = 0
        i = 0
        while i<len(char_list) and 47 < ord(char_list[i]) and ord(char_list[i]) < 58:
            value *= 10
            value += ord(char_list[i]) - 48
            i += 1
    return value

def S_evaluate(S_expression):
    eval_stack = brac_stack(list(S_expression))
    print(eval_stack)
    val1 = 0
    val2 = 0
    while eval_stack.getSize() > 0:
        expression = eval_stack.pop()
        value = 0
        ...
        i += 1
    return value
    if S_expression[0] == '(':
        op = S_expression[1]
        num1 = S_evaluate(S_expression[3:])
        if S_expression[3] == '(':
            while S_expression[i] != ')': i += 1 #inteded index error for no closing bracket
            i += 1
        else:
            while S_expression[i] != ' ': i += 1
        num2 = S_evaluate(S_expression[i+1:])
        value = op_dict[op](num1, num2)
    else: #should be a number
        value = 0
        while i<len(S_expression) and 47 < ord(S_expression[i]) and ord(S_expression[i]) < 58:
            value *= 10
            value += ord(S_expression[i]) - 48
            i += 1
    if i != 0:
        return value
    else:
        return None

def main():
    S_expression = ""
    while S_expression != "q":
        S_expression = input("Write an S-expression with single spaces between arguments:\n")
        print(S_evaluate(S_expression))
    return 0

if __name__ == "__main__":
    main()
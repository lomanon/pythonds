
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else: return False

    def push(self,item):
        self.items.append(item)

    def pop(self):
        pitem = self.items.pop()
        return pitem

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def convertBase2(number,base):
    remainder_stack = Stack()
    number_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while number > 0:
        remainder = number % base
        remainder_stack.push(remainder)
        number = number // base

    binary_number = ""

    while not remainder_stack.isEmpty():
        binary_number += number_string[remainder_stack.pop()]
    return binary_number


# print(convertBase2(256,16))

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()

    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXY0123456789":
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            while True:
                temptoken = opstack.pop()
                if temptoken == "(":
                    break
                else:
                    postfixlist.append(temptoken)
        else:
            while not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token] ):
                postfixlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)

print(infixToPostfix("A + B * C * Y / ( B + C )"))
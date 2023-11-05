class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def match(a):
    global s
    global i
    if(i >= len(s)):
        return False
    elif(s[i] == a):
        i += 1
        return True
    else:
        return False

def F():
    global i
    node = Node("F")

    if(match("(")):
        node.children.append(Node("("))
        node.children.append(E())
        if(match(")")):
            node.children.append(Node(")"))
    elif(match("i")):
        node.children.append(Node("i"))
    else:
        return node
    return node

def Tx():
    global i
    node = Node("T'")

    if(match("*")):
        node.children.append(Node("*"))
        node.children.append(F())
        node.children.append(Tx())
    elif(match("/")):
        node.children.append(Node("/"))
        node.children.append(F())
        node.children.append(Tx())
    else:
        node.children.append(Node("@"))
    return node

def T():
    global i
    node = Node("T")
    node.children.append(F())
    node.children.append(Tx())
    return node

def Ex():
    global i
    node = Node("E'")

    if(match("+")):
        node.children.append(Node("+"))
        node.children.append(T())
        node.children.append(Ex())
    elif(match("-")):
        node.children.append(Node("-"))
        node.children.append(T())
        node.children.append(Ex())
    else:
        node.children.append(Node("@"))
    return node

def E():
    global i
    node = Node("E")
    node.children.append(T())
    node.children.append(Ex())
    return node

def print_tree(node, level=0):
    if node is not None:
        print("  " * level + node.value)
        for child in node.children:
            print_tree(child, level + 2)

print("\nRecursive Desent Parsing For following grammar :\n")
print("E->E+T/T\nE->E-T/T\nT->T*F/F\nT->T÷F/F\nF->(E)/i\n")

a="E->E+T/T"
b="E->E-T/T"
c="T->T*F/F"
d="T->T÷F/F"
e="F->(E)/i"

if(a[0]==a[3] or b[0]==b[3] or c[0]==c[3] or d[0]==d[3] or e[0]==e[3] ):
    print("Left Recursion Exists!!!\n")
else:
    print("No Left Recursion!!!\n")
print("Removing Left Recursion : [x->xy/z ==> x->zx' & x'->yx'/@]\n")
print("E->TE'\nE'->+TE'/-TE'/@\nT->FT'\nT'->*FT'/÷FT'/@\nF->(E)/i\n")

s = list(input("Enter the string to be checked: "))
i = 0

root = E()  # Parse the input string

if i == len(s):
    print("The given string is accepted")
    print("\nParse Tree:")
    print_tree(root)
else:
    print("The given string is not accepted\n")
from pythonds.basic import Stack
import math

def infixToPostfixEval(expr):
    prec = {} 
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    operandStack = Stack()
    postfixList = []
    tokenList = expr.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789!":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    str = " ".join(postfixList)
    tokenList2 = str.split()


    for token in tokenList2:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return "Cannot be evaluated"
        elif token in "0123456789":
            operandStack.push(int(token))
        elif token == '!':
            operand = operandStack.pop()
            result = math.factorial(operand)
            operandStack.push(result)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
   
    x = str, "Evaluates to: ", operandStack.pop()
    
    return x

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    

#print(infixToPostfixEval("( 2 + 2 ) ! + 8"))
#print(infixToPostfixEval("A * B + C * D"))


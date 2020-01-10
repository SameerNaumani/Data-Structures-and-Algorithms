def evalTree(tree,environment):
    if(tree[0].isdigit()):
        return tree[0]
    
    if (tree[0] == []):
        return
    
    elif(tree[0] in "abcx1"):
        dicts = getDict(environment)
        return dicts.get(tree[0])
        
    elif(tree[0] == "+" or tree[0] =="-" or tree[0] == "*" or tree[0] == "/"):
        a = evalTree(tree[1], environment)
        int(a)
        #print(a)
        b = evalTree(tree[2], environment)
        int(b)
        #print(b)
        result = getResult(a,b,tree[0])
                
        return result
            
                
def getDict(environment):
    dicti={};
    for outside in environment:
        dicti[outside[0]]=outside[1]
    return dicti
        
            
def checkOperator(op):
    if (op=='+' or op=='-' or op=='*' or op=='/'):
        return True
    else:
        return False
  
def getResult(first,second,operator):
    if operator=='+':
        return first+second
    elif operator=='-':
        return first-second
    elif operator=='*':
        return first*second
    elif operator=='/':
        int(first)
        int(second)
        if(second == 0):
            return None
        else:
            return int((first)//(second))


test1Tree=["10",[],[]]
test1Environment=[["a",10],["b",20],["c",30]]
test2Tree=["x1",[],[]]
test2Environment=[["a",10],["x1",22]]
test3Tree=["/",["a",[],[]],["0",[],[]]]
test3Environment=[["a",10],["x1",22]]
test4Tree=["+",["a",[],[]],["*",["b",[],[]],["c",[],[]]]]
test4Environment=[["a",10],["b",20],["c",30]]
test5Tree=["*",["b",[],[]],["c",[],[]]]
test5Environment=[["a",10],["b",20],["c",30]]

#evalTree(test3Tree,test3Environment)


#print(evalTree(test1Tree,test1Environment))
#print(evalTree(test2Tree,test2Environment))
#print(evalTree(test4Tree,test4Environment))
#print(evalTree(test5Tree,test5Environment))

#print(test1Tree[2])
#print(getDict(test1Environment))
#print(getDict(test2Environment))
#print(getDict(test5Environment))            
def create():
    s=[]
    return s

def push(s,a):
    s.append(a)

def pop(s):
    if not isempty(s):
        s.pop()

def isempty(s):
    return len(s)==0

def peek(s):
    if not isempty(s):
        return s[-1]
    return 'no data'

s=create()
push(s,2)
push(s,3)
push(s,4)
push(s,0)
print(peek(s))
print(isempty(s))
print(s)
pop(s)
print(s)

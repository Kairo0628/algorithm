from stack import Stack

t1 = '(()(())()' #F 스택이 남아있음
t2 = '((())))' #F 스택이 비어있음
t3 = '([{()})]' #F 닫는 순서가 틀림
t4 = '({{[]()()}{}})' #S

left = '({['
right = ')}]'

for t in [t1, t2, t3, t4]:
    s = Stack(100)
    check = True

    for i in t:
        if i in left:
            s.push(i)
        else:
            if s.is_empty():
                check = False
                break

            if i == ')' and s.peek() == '(':
                s.pop()
            elif i == '}' and s.peek() == '{':
                s.pop()
            elif i == ']' and s.peek() == '[':
                s.pop()
            else:
                check = False
                break
    
    if s.is_empty() and check:
        print('success')
    else:
        print('fail')

# 20200903

List의 자료구조 형태중 Stack과 Queue 등을 사용하는 문제들을 오늘 본격적으로 쭉 풀어보았다.

오늘 코딩을 하면서 그때 그때 의도했던점들을 정리해보았다.

---

## 계산기3

문자열로 이루어진 계산식이 주어진다.

`(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)`

1. 이렇게 중위표기법으로 되어있는 문자열을 후위표기법으로 변환하고
2. 후위표기법을 계산해서 값을 알려주는 코드를 작성해보았다.

```python
# 우선 중위표기법을 후위표기법으로 변환하는 함수이다. 중위표기법으로 된 'list' 를 입력받는다.
def infixToPostfix(infixLs):
    postfix = [] # 후위표기법으로 반환할 결과를 담을 list이다.
    operators = ['(', '+', '*', ')'] # 연산자들을 담은 리스트를 통해 우선순위를 정하고 숫자를 필터링할 수 있다.
    stack = [] # 연산자들을 임시로 담아줄 스택이다.
    for j in infixLs:
        if j not in operators: # 우선 숫자인 경우 바로 postfix에 저장해준다.
            postfix.append(j)
        elif j == '(': # '('경우 스택에 바로 저장해준다.
            stack.append(j)
        elif j == ')': # ')'인 경우 '('이 나올때까지 연산자스택에서 pop하여 postfix에 넣어준다
            		   # '('와 ')' 사이에 있는 연산자들은, 앞으로 나올 연산들보다 더 우선되어야 하기 때문에 지금 후위표기법에 바로 넣어준다.
            if stack:
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
        else:
            while operators.index(stack[-1]) > operators.index(j): # ')'가 아닌 연산자들중에 * / 처럼 '+','-' 보다 우선되어 연산되어야 하는 연산자들은, 더 먼저 계산되어야하기 때문에 먼저 스택에서 뽑아서 postfix에 넣어준다.
                postfix.append(stack.pop())
            stack.append(j)
 
    while stack: # 지금 스택에는 '(' 과 우선순위에 없던 연산자들이 쭉 들어가 있다. 이렇게 마지막에 계산해줘야하는 연산자들을 다 pop해서 postfix에 넣어준다.
        if stack[-1] != '(':
            postfix.append(stack.pop())
        else:
            stack.pop()
    return postfix
 

# 후위표기법으로된 리스트를 받아 계산결과를 반환하는 함수이다.
def postfixCal(postfix):
    stack = []
    operators = ['(', '+', '*', ')'] # 연산자가 나올때만 계산해주기위해 이렇게 리스트를 만들어준다.
    for nums in postfix:
        if nums not in operators: # 숫자가 나오면 스택에 쌓아준다
            stack.append(nums)
        else:
            if nums == '*': # 곱하기 연산자가 나오면 이전에 쌓인 숫자 2개를 뽑아서 곱해서 반환해준다.
                			# /이 있는 비슷한 문제에서 계속 정답이 틀렸었다. 이건 스택에서 뽑을때, 처음 뽑은게 뒤에 오는 숫자라는 것을 까먹고 있었어서 이런일이 일어났다. 처음뽑은게 분모로 들어간다는것을 명심하자!
                stack.append(int(stack.pop())*int(stack.pop()))
            else:
                stack.append(int(stack.pop())+int(stack.pop()))
 
    return stack[0]
 
for i in range(1, 11):
    N = int(input())
    infix = input()
    postfix = infixToPostfix(infix)
    answer = postfixCal(postfix)
    print(f'#{i} {answer}')
```

---

가위바위보 토너먼트



```python
def win(r, c):
    f = r[1]
    s = c[1]
    if f == 1:
        if s == 2:
            return c
        else:
            return r
    elif f == 2:
        if s == 3:
            return c
        else:
            return r
    else:
        if s == 1:
            return c
        else:
            return r
 
def RPC(stus, l):
    a = (l+1)//2
    b = l - a
    if l == 1:
        return stus[0]
    elif l == 2:
        return win(stus[0],stus[1])
    else:
        return win(RPC(stus[:a],a),RPC(stus[a:],b))
 
 
 
T = int(input())
 
for i in range(1, T+1):
    N = int(input())
    studLs = [[n] for n in range(1, N+1)]
    lsA = list(map(int, input().split()))
    for j in range(N):
        studLs[j].append(lsA[j])
    # print(studLs)
    # print(len(studLs))
    print(f'#{i} {RPC(studLs, N)[0]}')
```

---

## Magnetic

100*100의 테이블에 헬륨풍선과 밤톨이 배치되어있다. 밤톨은 중력에 의해 초당 한칸씩 떨어지고, 풍선은 부력에 의해 한 칸씩 올라간다. 밤톨과 풍선이 만나면 풍선이 터지면서 고무로된 위치에 고정된막이 하나 생긴다. 그 막에 부딛친 밤톨과 풍선은 서로 부딛칠 수 없다. 생성된 총 고무막의 갯수를 구하여라.

```python
def stuck(lis):
    result = 0
    L = len(lis)
    for i in range(L-1):
        if lis[i] == 1:
            if lis[i+1] == 2:
                result += 1
    return result
 
for i in range(1, 11):
    hundred = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for col in range(0, 100):
        stack = []
        for row in range(0, 100):
            if graph[row][col] != 0:
                stack.append(graph[row][col])
 
        ans += stuck(stack)
 
    print(f'#{i} {ans}')
```

---

## 4881 배열 최소 합

```python
def perm(n, k, arr2):
    if k == n:
        result = 0
        for i in range(n):
            result += arr2[i][arr[i]]
        stack.append(result)
        #print(result)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, arr2)
            arr[k], arr[i] = arr[i], arr[k]

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr2 = [list(map(int, input().split())) for _ in range(N)]
    arr = [n for n in range(N)]
    stack = []
    perm(N, 0, arr2)
    print(f'#{i} {min(stack)}')
```


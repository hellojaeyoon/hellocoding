# STACK

### Stack 자료구조의 개념

1. 물건을 쌓아올리듯 자료를 쌓아올린 형태의 자료구조
2. 스택에 저장된 자료는 선형구조를 가짐
3. LIFO (Last In First Out)의 구조를 가짐

---

파이썬에서는 보통 리스트를 사용해서 스택을 구현한다.

- 스택에서 마지막 삽입된 원소의 위치를 `top`이라고 부른다.

- 스택(저장소)에 자료를 저장하고 그 과정을 `push`라고 부른다

- 스택에서 자료를 꺼내는것(즉 맨 마지막에 삽입한 자료를 꺼낼때)을 `pop`이라고 부른다.

  파이썬에선 list에 대한 `pop()`함수가 이미 존재한다.

  `stack.pop()`을 하면 마지막 원소를 return하고 그와 동시에 마지막 원소를 stack에서 없엔다.

- 다음과 같이 push를 정의해서 사용할 수 있다.

```python
def push(item):
    stack.append(item)
```



리스트를 사용해서 스택을 구현하는 경우의 단점

- 리스트의 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간이 소요
- 이를 해결하기 위해서 다음과 같은 방법들이 존재한다(대신 복잡하다)
  - 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
  - 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법

---

## Stack의 응용

주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.


예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.


정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.


print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

```python
def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        #print("Stack is empty!!")
        return
    else:
        return stack.pop()


T = int(input())

for i in range(1, T+1):
    stack = []
    ls = input()
    lista = ['{', '}', ']', '[', '(', ')']
    for elems in ls:
        if elems in lista:
            if elems == '{' or elems == '(' or elems == '[':
                push(elems)
            else:
                popped = pop()
                if elems == '}':
                    if popped == '{':
                        continue
                    else:
                        print("It's wrong!")
                        break
                elif elems == ')':
                    if popped == '(':
                        continue
                    else:
                        print("It's wrong!")
                        break
                elif elems == ']':
                    if popped == '[':
                        continue
                    else:
                        print("It's wrong!")
                        break
                else:
                    continue

    if len(stack) != 0:
        print(f'#{i} 0')
    else:
        print(f'#{i} 1')
```



---

## Memoization

피보나치함수를 살펴보면

```python
def fibo(n):
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(100)
```

다음과 같이 `fibo(100)`을 선언한다면 `fibo(99)`와 `fibo(98)`을, 그에 이어서 `fibo(98)`,`fibo(97)`과 `fibo(97)`와`fibo(96)`을 ... 이와같이 이미 선언했던 함수를 다른곳에서도 끊이없이 선언해야된다는것을 알 수 있다. 이와같은 오래걸리고 효율적이지 못한 일을 줄이고자, 각 순간 값을 저장해두는 Memoization 방법을 적용할 수 있다.

```python
def fibo2(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0,1]
```

---

## DP (Dynamic Programming) 동적계획법

그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다

- 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분문제들을 해결
- 최종적으로 원래 주어진 입력의 문제를 해결

하는 형태이다.

---

1X2, 2X2 두가지 모양의 블록이 무한하게 존재한다고 가정하자.

그 때 2XN 크기의 빈 칸이 있을때 , 존재하는 블록들로 칸을 채우는 가지수를 구해보자.

예를 들어 N = 3인 경우 다음과 같이 5가지가 존재한다.

![image-20200826231228565](20200826[목].assets/image-20200826231228565.png)

---

우선 가로로 N칸이 있다고 가정해보자,

이건 N-1칸을 채운후에 세로로 1X2 를 하나 추가하거나

![image-20200826232058671](20200826[목].assets/image-20200826232058671.png)

N-2칸을 채운후에 세로로 1X2블록을 2개, 혹은 2X2 블록을1개 추가했을 것이다.

![image-20200826232110173](20200826[목].assets/image-20200826232110173.png)

![image-20200826232115457](20200826[목].assets/image-20200826232115457.png)



N-3칸을 채운후 나머지를 채우는건 다 위 두 줄의 경우에 포함이 된다.

즉 f(N)을 가로 N칸의 빈 칸을 채우는 가짓수라 한다면

f(N) = f(N-1) + 2*f(N-2) 가 된다. 다음과 같이 코드를 짰다.

```python
def push(item):
    stack.append(item)

T = int(input())

for i in range(1, T+1):
    stack = [0, 1, 3]
    n = int(input())//10
    for j in range(len(stack), n+1):
        push(stack[j-1]+2*stack[j-2])

    print(f'#{i} {stack.pop()}')
```


## DFS (Depth-First Search)

- 깊이 우선 탐색
- 하나의 정점으로부터 시작하여 갈 수 있는 점들까지 차례대로 모든 정점들을 한 번씩 방문하는 것
- DFS: 스택 or 재귀함수로 구현한다

- 우선 다음과 같은 모양의 무향그래프(일방통행이아닌)가 존재한다고 가정하자.

![image-20200827125335033](20200827.assets/image-20200827125335033.png)

- 위 그래프의 점들에 적혀있는 숫자 순서대로 검색을 하게 된다.

- 위 그래프의 점들의 이름을 편의상 1 ~ 10 으로 정의하고 DFS를 직접 구현해보자.

  #### 우선 그래프를 2가지 방법으로 구현해보자

1. ##### 딕셔너리

```python
#numberOfNodes = 10 (1,2,3,4,5,6,7,8,9,10)
#segmentInput = 1 2 1 5 1 9 2 3 3 4 5 6 5 8 6 7 9 10
# input
# 10
# 1 2 1 5 1 9 2 3 3 4 5 6 5 8 6 7 9 10
#####################################################
n = int(input())
segLs = list(map(int, input().split()))
m = len(segLs)//2
graph = {} #빈 딕셔너리 생성
for i in range(1, n+1): #각 nodes에 연결된 node들을 리스트로 표현하기위해 초기화
    graph[i] = []
for i in range(0, m):
    #segment input을 기반으로 각 key(node)에 해당되는 neighbornode(value)추가
    #1 2 면 1의 neighbor에 2를, 그리고 2의 neighbor에 1을 추가
    graph[segLs[2*i]].append(segLs[2*i+1])
    graph[segLs[2 * i + 1]].append(segLs[2 * i])#유향그래프인경우 이 라인은 삭제
    

print(graph)
```

```python
10
1 2 1 5 1 9 2 3 3 4 5 6 5 8 6 7 9 10

ㅡ> {1: [2, 5, 9], 2: [1, 3], 3: [2, 4], 4: [3], 5: [1, 6, 8], 6: [5, 7], 7: [6], 8: [5], 9: [1, 10], 10: [9]}

{
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
```



2. ##### 2차원 배열

```python
#numberOfNodes = 10 (1,2,3,4,5,6,7,8,9,10)
#segmentInput = 1 2 1 5 1 9 2 3 3 4 5 6 5 8 6 7 9 10
# input
# 10
# 1 2 1 5 1 9 2 3 3 4 5 6 5 8 6 7 9 10
#####################################################
n = int(input())
segLs = list(map(int, input().split()))
m = len(segLs)//2

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    graph[segLs[2 * i + 1]][segLs[2 * i]] += 1
    graph[segLs[2 * i]][segLs[2 * i + 1]] += 1

print(graph)
```

```python
[  # graph[x][y]의 값은
   # node x와 node y가 연결되어 있으면 : 1
   # 그게 아니라면 : 0
   # 아래와 같은 그래프는 node가 1~n까지 일때를 가정하고 1열과 1행을 0으로 준 예시이다.
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]
```

---

그럼 위와 같은 두 그래프가 주어졌을 때 탐색을 시작해보자.

탐색을 돌릴 Graph와 탐색의 출발지점을 인자로 전달받고 탐색을 시작해보자.

```python
def dfs(graph, node):
    #우선 방문지점들을 표시하는 빈 리스트를 하나 생성
    visited = []
    #탐색을 돌리는 대상이 top에 존재하는 stack 하나 생성
    stack = []
    #stack에 node를 넣고 본격적인 탐색시작!
    stack.append(node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.append(graph[node])
```
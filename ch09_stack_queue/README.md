# python-coding-interview

> 3/24 (thu)

<br/>

# 스택, 큐

<br/>

## # 스택 Stack
- LIFO Last-In-First-Out : 후입선출
- 리스트가 스택의 모든 연산 지원
- 예. 잔뜩 쌓아둔 접시, 마지막에 쌓은 접시가 맨 위에 놓일 것이라, 가장 마지막에 쌓은 접시를 제일 먼저 꺼내게 된다.
- 추상 자료형 :
    - push() : 요소를 컬렉션에 추가
    - pop() : 아직 제거되지 않은 가장 최근에 삽입된 요소 제거
- 콜 스택 Call Stack : 컴퓨터 프로긂의 서브 루틴에 대한 정보를 저장하는 자료구조로 활용
    - 컴파일러가 출력하는 에러도 스택처럼 맨 마지막 에러가 가장 먼저 출력되는 순서를 보인다.

## # 큐 Queue
- FIFO First-In-First-Out : 선입선출
- 리스트가 스택의 모든 연산 지원
    - 단점 : 리스트는 동적 배열로 구현되어 있어 큐의 연산을 수행하기에는 효율적이지 않아서, Deque라는 별도의 자료형을 사용해서 좋은 성능을 낸다.
- 예. 가장 먼저 줄 선 사람이 가장 먼저 입장한다.
- 시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.
- Deque나 우선순위 큐 priority Queue 변형들은 여러 분야에서 매우 쓰인다.
- 너비 우선 탐색 Breadth-First Search DFS이나 캐시 등을 구현할 때도 쓴다.

<br/><br/>

# 20. 유효한 괄호 [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
괄호로 된 입력값이 올바른지 판별하라.

<br/>

### # 예제 1
- 입력
```()[]{}```
- 출력
```true```

<br/><br/>

# 21. 중복 문자 제거 [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)
중복된 문자를 제외하고 사전식 순서 Lexicographical Order로 나열하라.

<br/>

### # 예제 1
- 입력
```"bcabc"```
- 출력
```"abc"```

### # 예제 2
- 입력
```"cbacdcbc"```
- 출력
```"acdb"```

<br/>

### 참고 : 사전식 순서 
- 사전에서 가장 먼저 찾을 수 있는 순서를 말한다.
- 중복 문자는 제외하고 순서를 따진다.

<br/><br/>

# 22. 일일 온도 [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
매일의 화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

<br/>

### # 예제 1
- 입력
```T = [73, 74, 75, 71, 69, 72, 76, 73]```
- 출력
```[1, 1, 4, 2, 1, 1, 0, 0]```
- 설명 :
화씨 73도인 첫째 날에서 더 따뜻한 날을 위해서는 하루만 기다리면 된다.

<br/><br/>

# 23. 큐를 이용한 스택 구현 [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
- push(x) : 요소 x를 스택에 삽입한다.
- pop() : 스택의 첫 번째 요소를 삭제한다.
- top() : 스택의 첫 번째 요소를 가져온다.
- empty() : 스택이 비어 있는지 여부를 리턴한다.

```
Mystack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.pop(); // 2 리턴
stack.top(); // 2 리턴
stack.empty(); // false 리턴
```

<br/><br/>

# 24. 스택을 이용한 큐 구현 [Implement Queues using Stack](https://leetcode.com/problems/implement-queues-using-stack/)
스택를 이용해 다음 연산을 지원하는 큐를 구현하라.
- push(x) : 요소 x를 큐 마지막에 삽입한다.
- pop() : 큐 처음에 있는 요소를 삭제한다.
- peek() : 큐 처음에 있는 요소를 조회한다.
- empty() : 큐가 비어 있는지 여부를 리턴한다.

```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.pop(); // 1 리턴
queue.peek(); // 1 리턴
queue.empty(); // false 리턴
```

<br/><br/>

# 25. 원형 큐 디자인 [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
원형 큐를 디자인하라.

```
MyCircularQueue circularQueue = new MyCircularQueue(5); // 크기를 5로지정

ctrcularQueue.enQueue(10); // true 리턴
circularQueue.enQueue(20); // true 리턴
ctrcularQueue.enQueue(30); // true 리턴
circularQueue.enQueue(40); // true 리턴
circularQueue.Rear(); // 40 리턴
circularQueue.isFull(); // false 리턴
circularQueue.deQueue(); // true 리턴
circularQueue.deQueue(); // true 리턴
ctrcularQueue.enQueue(50); // true 리턴
circularQueue.enQueue(60); // true 리턴
circularQueue.Rear(); // 60 리턴
circularQueue.Front(); // 30 리턴
```

<br/>

### 원형 큐 Circular Queue
- FIFO 구조로, 링 버퍼 Ring Buffer라고도 한다.
- 기존의 큐는 공간이 꽉 차게 되면 더 이상 요소를 추가할 수 없었다.
- 앞쪽에 공간이 남아 있다면 동그랗게 연결해 앞쪽으로 추가할 수 있도록 재활용 가능한 구조이다.
- 동작하는 원리는 투 포인터와 비슷하다. 마지막 위치와 시작 위치를 연결하는 원형 구조를 만들고, 요소의 시작점과 끝점을 따라 투 포인터가 움직인다.

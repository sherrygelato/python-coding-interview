# python-coding-interview

> 4/18 (mon)

<br/>

# 트리
- 계층형 트리 구조를 시뮬레이션 하는 추상 자료형으로, 루트 값과 부모-자식 관계의 서브 트리로 구성되며, 서로 연결된 노드의 집합이다.
- 재귀로 정의된 자기 참조 자료구조
    - 자식도 트리고 그 자식도 트리 즉 여러 개의 트리(서브트리)가 쌓아 올려져 큰 트리가 됨
- 트리는 항상 root에서부터 시작된다. 
- 자식child 노드를 가지며,
- 간선edge으로 연결되어 있다. 
- 자식 노드의 개수는 차수Degree라고 하며, 
- 크기size는 자신을 포함한 모든 자식 노드의 개수다.
- 높이Height는 현재 위치에서부터 리프Leaf까지의 거리, 
- 깊이Depth는 루트에서부터 현재 노드까지의 거리다.
- 레벨Level은 0에서부터 시작된다. 
- 트리는 항상 단방향Uni-Directional이기 때문에, 간선의 화살표는 생략 가능하다. 위에서 아래로 향한다.

### # 참고 : 그래프 vs 트리
- "트리는 순환 구조Cyclic를 갖지 않는 그래프이다."
- 그래프는 단방향, 양방향을 모두 가리킬 수 있는 그래프와 달리, 트리는 부모 노드에서 자식 노드를 가리키는 단방향뿐이다. 
- 트리는 하나의 부모 노드를 갖으며, 루트 또한 하나여야 한다.

### # 참고 : 이진 트리
- 각 노드가 m개 이하의 자식을 갖고 있으면 m-ary 트리(다항 트리, 다진 트리)라고 한다.
- 이진 트리는 m=2일 경우, 즉 모든 노드의 차수가 2 이하일 때 Binary Tree 이진트리라고 한다.
- 왼쪽, 오른쪽 최대 2개의 자식을 갖는 매우 단순한 형태로 다진 트리에 비해 훨씬 간결하고, 여러 가지 알고리즘을 구현하는 일도 좀 더 간단하게 처리할 수 있다.

- 정 이진 트리 Full Binary Tree : 모든 노드가 0개 또는 2개의 자식 노드를 갖는다.
- 완전 이진 트리 Complete Binary Tree : 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있다.
- 포화 이진 트리 Perfect Binary Tree : 모든 노드가 2개의 자식 노드를 갖고 있으며, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.

# 42. 이진 트리의 최대 깊이 [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
이진 트리의 최대 깊이를 구하라.

<br/>

### # 예제 
- 입력
```[3, 9, 20, null, null, 15, 7```
- 출력
```3```

<br/><br/>

# 43. 이진 트리의 직경 [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.

<br/>

### # 예제 
- 입력
```[1, 2, 3, 4, 5, None, None]```
- 출력
```3```

### # 문법 : 중첩 함수에서 클래스 변수를 사용한 이유
- 중첩 함수를 사용할 때 왜 longest 변수를 함수 내에서 선언하지 않고, 바깥에 클래스 변수로 선언해서 번거롭게 사용했을까?
- 중첩 함수는 부모 함수의 변수를 자유롭게 읽어들일 수 있다. 그러나 중첩 함수에서 부모 함수의 변수를 재할당하게 되면 참조 ID가 변경되어 별도의 로컬 변수로 선언된다. 
- 숫자나 문자가 아니라 리스트나 딕셔너리 같은 자료형이면 append() 등의 메소드로 재할당 없이 조작이 가능하나 숫자나 문자는 불변 객체이기 때문에 중첩 함수 내에서는 값을 변경할 수 없다. 

<br/><br/>

# 44. 가장 긴 동일 값의 경로 [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
동일한 값을 지닌 가장 긴 경로를 찾아라

<br/>

### # 예제 1
- 입력
```[5, 4, 5, 1, 1, None, 5]```
- 출력
```2```

### # 예제 2
- 입력
```[1, 4, 5, 4, 4, None, 5]```
- 출력
```2```

<br/><br/>

# 45. 이진 트리 반전 [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
중앙을 기준으로 이진 트리를 반전시키라.

<br/>

### # 예제
- 입력
```[4, 2, 7, 1, 3, 6, 9]```
- 출력
```[4, 7, 2, 9, 6, 3, 1]```

<br/><br/>

# 46. 두 이진 트리 병합 [Merge Two Binary Tree](https://leetcode.com/problems/merge-two-binary-tree/)
두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.

<br/>

### # 예제
- 입력
```t1 = [1, 3, 2, 5, None, None, None], t2 = [2, 1, 3, None, 4, None, 7]```
- 출력
```[3, 4, 5, 5, 4, None, 7]```

<br/><br/>

# 47. 이진 트리 직렬화 & 역직렬화 [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라. 트리를 [1, 2, 3, None, None, 4, 5]로 직렬화 할 수 있을 것이다.

<br/>

### # 예제
- 입력
```[1, 2, 3, None, None, 4, 5]```
- 출력
``` ```

<br/>

### # 직렬화
- 이진 트리의 데이터 구조는 논리적인 구조로, 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 하는데, 이를 직렬화라고 한다.
- 파이썬의 pickle이란 직렬화 모듈로 파이썬 객체의 계증 구조를 바이트 스트림으로 변경한다.

<br/><br/>

# 48. 균형 이진 트리 [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
이진 트리가 높이 균형인지 판단하라. (높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.)

<br/>

### # 예제 1
- 입력
```root = [3, 9, 20, null, null, 15, 7]```
- 출력
```true```

### # 예제 2
- 입력
```root = [1, 2, 2, 3, 3, null, null, 4, 4]```
- 출력
```False```

<br/><br/>

# 49. 최소 높이 트리 [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)
노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.

<br/>

### # 예제 1
- 입력
```n1 = 4, edges1 = [[1, 0], [1, 2], [1, 3]] ```
- 출력
```[1]```

### # 예제 2
- 입력
```n2 = 6, edges2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]] ```
- 출력
```[3, 4]```

<br/><br/>

# 50.정렬된 배열의 이진 탐색 트리 변환 [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.

<br/>

### # 예제
- 입력
```[-10, -3, 0, 5, 9] ```
- 출력
```[0, -3, -9, -10, null, 5]```

<br/><br/>
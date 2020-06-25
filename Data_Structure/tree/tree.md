## 트리(Tree)

<center><img src="./images/tree0.svg" alt="tree" width="400"/></center>

트리는 비선형 자료구조이며, 계층적 관계를 표현하는 자료구조이다.

### 노드 주요 용어

- 루트 노드(root node) : 연결된 노드가 한군데로 모이는 최상위 노드
- 차수(degree) : 한 노드에 연결된 서브 트리의 개수
- 부모 노드(parent node) : 현재 노드의 바로 상위노드
- 자식 노드(child node) : 부모 노드의 반대 개념
- 형제 노드(sibling node) : 같은 부모 노드를 갖는 노드 사이
- 리프 노드(leaf node) : 최하위 노드. 단말 노드(terminal node) 라고도 한다.

<br>

### 이진 트리(Binary Tree), 서브 트리(Sub Tree)

<center><img src="./images/tree3.svg" alt="tree3" width="400"/></center>

각 노드가 최대 두 개의 자식 노드를 가지는 트리를 이진트리라고 하고, 큰 트리에 속하는 작은 트리를 서브 트리라고 한다.

<br>

### 포화 이진 트리(Full Binary Tree)

<center><img src="./images/tree1.svg" alt="tree4" width="400"/></center>

포화 이진 트리는 리프 노드를 제외한 모든 노드가 두 개의 자식을 가지고 있는 트리이다. 즉, 모든 레벨이 꽉 찬 이진 트리를 말한다.
<br>

### 완전 이진 트리(Complete Binary Tree)

<center><img src="./images/tree5.svg" alt="tree5" width="400"/></center>

완전 이진 트리는 리프 노드들이 트리의 왼쪽부터 차곡차곡 채워진 트리이다.

<!-- <br>

## 이진트리 구현 -->

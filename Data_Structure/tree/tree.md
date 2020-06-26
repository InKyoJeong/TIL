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

<br>

## 이진트리 순회

둘 이상의 노드로 이뤄진 서브트리를 삭제하려면 모든 노드를 방문해야 한다. 모든 노드를 방문하는 것을 **순회**라고 한다.

순회에는 대표적으로 세 가지 방법이 있다.

<center><img src="./images/tree6.svg" alt="tree6" width="400"/></center>

- 전위 순회(Preorder Traversal) : 루트 노드를 먼저 방문
- 중위 순회(Inorder Traversal) : 루트 노드를 중간에 방문
- 후위 순회(Postorder Traversal) : 루트 노드를 마지막에 방문

<br>

높이가 2 이상인 이진 트리는 순회를 재귀적으로 구현하면 된다.

<center><img src="./images/tree7.svg" alt="tree7" width="400"/></center>

<br>

- 중위 순회 함수

```c
void InorderTraverse(BTreeNode * bt)
{
    InorderTraverse(bt->left);      //왼쪽(1번) 서브트리 순회
    printf("%d \n", bt->data);      //루트노드 방문
    InorderTraverse(bt->right);     //오른쪽(2번) 서브트리 순회
}
```

- 탈출 조건을 추가한 순회

```c
void InorderTraverse(BTreeNode * bt)
{
    if(bt == NULL)
        return;

    InorderTraverse(bt->left);
    printf("%d \n", bt->data);
    InorderTraverse(bt->right);
}
```

전위 순회와 후위 순회함수는 아래와 같다. 루트 노드를 방문하는 문장의 위치만 다르다.

- 전위 순회 함수

```c
void PreorderTraverse(BTreeNode * bt)
{
    if(bt == NULL)
        return;

    printf("%d \n", bt->data);
    InorderTraverse(bt->left);
    InorderTraverse(bt->right);
}
```

- 후위 순회 함수

```c
void PostorderTraverse(BTreeNode * bt)
{
    if(bt == NULL)
        return;

    InorderTraverse(bt->left);
    InorderTraverse(bt->right);
    printf("%d \n", bt->data);
}
```

<br>

## 수식 트리(Expression Tree)

수식 트리는 이진 트리를 이용해 수식을 표현한 것이다.

#### 수식 트리의 연산 과정

수식 트리는 루트 노드에 저장된 연산자의 연산을 하되, 두 개의 자식 노드에 저장된 두 피연산자를 대상으로 연산을 한다.

<center><img src="./images/tree11.svg" alt="tree11" width="400"/></center>

<br>

<center><img src="./images/tree12.svg" alt="tree12" width="400"/></center>

<br>

<center><img src="./images/tree13.svg" alt="tree13" width="400"/></center>

<br>

### 후위 표기법 기반 수식트리 구성

중위 표기법의 수식을 수식 트리로 바로 표현하기는 어려우므로 후위 표기법을 거쳐서 수식 트리로 표현한다.

```c
BTreeNode * MakeExpTree(char exp[]);
```

이 함수는 후위 표기법의 수식을 문자열 형태로 입력받고, 수식 트리를 구성하고 수식트리의 루트 노드의 주소값을 반환한다.

```c
int EvaluateExpTree(BTreeNode * bt);
```

이 함수는 인자로 전달된 수식트리의 수식을 계산해서 결과를 반환한다.

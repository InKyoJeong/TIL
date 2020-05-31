## 1. 트리 개념

### 노드 주요 용어

- 루트 노드(root node) : 연결된 노드가 한군데로 모이는 최상위 노드
- 차수(degree) : 한 노드에 연결된 서브 트리의 개수
- 부모 노드(parent node) : 현재 노드의 바로 상위노드
- 자식 노드(child node) : 부모 노드의 반대 개념
- 형제 노드(sibling node) : 같은 부모 노드를 갖는 노드 사이
- 리프 노드(leaf node) : 최하위 노드

### 이진 트리

자식 노드를 2개 이하만 갖는 트리. 즉, 트리의 차수가 2이하인 트리

- 이진 트리의 노드 정의

```c
typedef struct _Node {
    char data;
    struct _Node *Left;
    struct _Node *Right;
} Node;
```

#### 완전 이진 트리

모든 노드에 자식노드가 없거나 2개의 자식 노드를 갖는 이진 트리

#### 정 이진 트리

리프 노드들의 레벨이 같은 트리.

### 트리의 순회 알고리즘

- 전위 순회
- 중위 순회
- 후위 순회
- 단계 순회

<br>

## 2. 전위 순회 알고리즘

- 전위 순회 알고리즘 함수

```c
void traverse(NODE *ptrNode)
{
    Visit();

    while(!isStackEmpty()){
        ptrNode = Pop();
        Visit(ptrNode);

        if(ptrNode->Right != EndNode)
            Push(ptrNode->Right);

        if(ptrNode->Left != EndNode)
            Push(ptrNode->Left);
    }
}
```

1. Visit() : 현재 가리키는 노드를 방문
2. 스택이 비어있지 않으면 스택에 있는 노드중 하나를 꺼낸다. 그리고 해당 노드를 방문한다.
3. 해당 노드의 오른쪽 노드가 존재하면 오른쪽 노드를 스택에 저장한다.
4. 왼쪽 노드가 있는지 검사해 왼쪽 노드가 존재하면 왼쪽 노드를 스택에 저장한다.
5. 스택이 비워질 때까지 반복한다.

<!--
- node.h : 트리에서 사용하는 노드 자료형 정의파일

```c
#ifndef __NODE_H
#define __NODE_H

#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

typedef struct _NODE {
    char data;
    struct _NODE *Left;
    struct _NODE *Right;
} NODE;
NODE *HeadNode, *EndNode;

#endif
```

- stack.c : 이진 트리에서 사용할 스택코드

```c
#include "node.h"
#define MAX 100

NODE *Stack[MAX];   //스택을 배열로 선언
int Top;

void InitializeStack(void);
void Push(NODE *);
NODE *Pop(void);
int IsStackEmpty(void);

void InitializeStack(void)
{
    Top = 0;
}

void Push(NODE *ptrNode)
{
    Stack[Top] = ptrNode;
    Top = (++Top) % MAX;
}

NODE *Pop(void)
{
    NODE *ptrNode;

    if(!IsStackEmpty()){
        ptrNode = Stack[--Top];

        return ptrNode;
    }
    else
        printf("Stack is Empty\n");

    return NULL;
}

int IsStackEmpty(void)
{
    if(Top == 0)
        return TRUE;

    else
        return FALSE;
}
```

- InitializeStack() : 처음 스택을 초기화하고 스택의 상위 데이터를 가리키는 인덱스 Top 값을 0으로 초기화한다.
- Push() : NODE포인터를 매개변수로 받아 이 포인터가 가리키는 데이터를 스택에 삽입한다.
- Pop() : Push()와 마찬가지로 스택에 저장된 노드를 가리키는 주소 값을 반환한다.
- IsStackEmpty() : 스택 안에 데이터가 있는지 없는지 검사한다. -->

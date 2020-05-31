## 링크드 리스트

- LinkedList.h

```c
#ifndef LinkedList_h
#define LinkedList_h

#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;

typedef struct tagNode
{
    ElementType Data;
    struct tagNode* NextNode;
} Node;

//함수원형선언
Node* SLL_CreateNode(ElementType NewData);
void SLL_DestroyNode(Node* Node);
void SLL_AppendNode(Node** Head, Node* NewNode);
void SLL_InsertAfter(Node* Current, Node* NewNode);
void SLL_InsertNewHead(Node** Head, Node* NewHead);
void SLL_RemoveNode(Node** Head, Node* Remove);
Node* SLL_GetNodeAt(Node* Head, int Location);
int SLL_GetNodeCount(Node* Head);

#endif
```

- LinkedList.c

```c
#include "LinkedList.h"

//노드생성
Node* SLL_CreateNode(ElementType NewData)
{
    Node* NewNode = (Node*)malloc(sizeof(Node));

    NewNode->Data = NewData;    //데이터 저장
    NewNode->NextNode = NULL;   //다음 노드에 대한 포인터는 NULL로 초기화

    return NewNode;             //노드의 주소 반환
}

//노드소멸
void SLL_DestroyNode(Node* Node)
{
    free(Node);
}

//노드추가
void SLL_AppendNode(Node** Head, Node* NewNode)
{
    if((*Head) == NULL)         //헤드노드가 NULL이면 새로운노드가 Head
    {
        *Head = NewNode;
    }
    else{                       //테일을 찾아 NewNode를 연결한다
        Node* Tail = (*Head);
        while(Tail->NextNode != NULL)
        {
            Tail = Tail->NextNode;
        }
        Tail->NextNode = NewNode;
    }
}

//노드삽입
void SLL_InsertAfter(Node* Current, Node* NewNode)
{
    NewNode->NextNode = Current->NextNode;
    Current->NextNode = NewNode;
}

void SLL_InsertNewHead(Node** Head, Node* NewHead)
{
    if(*Head == NULL)
    {
        (*Head) = NewHead;
    }
    else
    {
        NewHead->NextNode = (*Head);
        (*Head) = NewHead;
    }
}

//노드제거
void SLL_RemoveNode(Node** Head, Node* Remove)
{
    if(*Head == Remove)
    {
        *Head = Remove->NextNode;
    }
    else
    {
        Node* Current = *Head;
        while (Current != NULL && Current->NextNode != Remove)
        {
            Current = Current->NextNode;
        }

        if(Current != NULL)
            Current->NextNode = Remove->NextNode;
    }
}

//노드탐색
Node* SLL_GetNodeAt(Node* Head, int Location)
{
    Node* Current = Head;

    while( Current != NULL && (--Location) >= 0)
    {
        Current = Current->NextNode;
    }

    return Current;
}

//노드 수 세기
int SLL_GetNodeCount(Node* Head)
{
    int Count = 0;
    Node* Current = Head;

    while(Current != NULL)
    {
        Current = Current->NextNode;
        Count++;
    }

    return Count;
}
```

- Test_LinkedList.c

```c
#include "LinkedList.h"

int main(void)
{
    int i = 0;
    int Count = 0;
    Node* List = NULL;
    Node* Current = NULL;
    Node* NewNode = NULL;

    for(i=0; i<5; i++)                          //노드 5개 추가
    {
        NewNode = SLL_CreateNode(i);
        SLL_AppendNode(&List, NewNode);
    }

    NewNode = SLL_CreateNode(-1);
    SLL_InsertNewHead(&List, NewNode);

    NewNode = SLL_CreateNode(-2);
    SLL_InsertNewHead(&List, NewNode);

    Count = SLL_GetNodeCount(List);             //리스트 출력
    for(i=0; i<Count; i++)
    {
        Current = SLL_GetNodeAt(List, i);
        printf("List[%d] : %d\n", i , Current->Data);
    }

    printf("\nInserting 3000 After [2]...\n\n");    //리스트의 세번째 노드뒤에 새 노드 삽입

    Current = SLL_GetNodeAt(List, 2);
    NewNode = SLL_CreateNode(3000);

    SLL_InsertAfter(Current, NewNode);

    Count = SLL_GetNodeCount(List);             //리스트 출력
    for(i=0; i<Count; i++)
    {
        Current = SLL_GetNodeAt(List, i);
        printf("List[%d] : %d\n", i, Current->Data);
    }

    printf("\nDestroying List...\n");           //모든노드 메모리에서 제거

    for(i=0; i<Count; i++)
    {
        Current = SLL_GetNodeAt(List, 0);

        if(Current != NULL)
        {
            SLL_RemoveNode(&List, Current);
            SLL_DestroyNode(Current);
        }
    }

    return 0;
}
```

```
//실행결과

List[0] : -2
List[1] : -1
List[2] : 0
List[3] : 1
List[4] : 2
List[5] : 3
List[6] : 4

Inserting 3000 After [2]...

List[0] : -2
List[1] : -1
List[2] : 0
List[3] : 3000
List[4] : 1
List[5] : 2
List[6] : 3
List[7] : 4

Destroying List...
```

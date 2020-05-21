# Array vs Linked List

## 리스트(List)

- 기본적인 연산 : 삽입(insert), 삭제(remove), 검색(search)등
- 리스트를 구현하는 대표적인 두 가지 방법: **베열, 연결리스트**

### 배열의 단점

- 크기가 고정 - reallocation이 필요
- 리스트의 중간에 원소를 삽입하거나 삭제할 경우 다수의 데이터를 옮겨야함

### 연결리스트

- 다른 데이터의 이동없이 중간에 삽입이나 삭제가 가능
- 길이의 제한이 없음
- 그러나 랜덤 엑세스가 불가능

### 노드

- 각각의 노드는 필요한 **데이터 필드**와 하나혹은 그 이상의 **링크 필드**로 구성됨
- 링크 필드는 다음 노드의 주소를 저장
- 첫번째 노드의 주소는 따로 저장해야함
- 마지막 노드의 next필드에는 NULL을 지정하여 연결리스트의 끝임을 표시

#### 노드를 표현하는 구조체

연결리스트에서 하나의 노드를 표현하기 위한 구조체이다. 각 노드에 저장될 데이터는 하나의 문자열이라고 가정하자.

```c
struct node{
    char *data;
    struct node *next;      //다음 노드의 주소를 저장할 필드이다.
}
typedef struct node Node;
Node *head = NULL;          //연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.
```

#### 예제프로그램

```c
int main(){
    head = (Node *)malloc(sizeof(Node));
    head->data = "Tuesday";
    head->next = NULL;

    Node *q = (Node *)malloc(sizeof(Node));
    q->data = "Thursday";
    q->next = NULL;
    head->next = q;


    q = (Node *)malloc(sizeof(Node));
    q->data = "Monday";
    q->next = head;
    head = q;

    Node *p = head;
    while(p!=NULL){
        printf("%s\n", p->data);
        p = p->next;
    }
}
```

## 연결리스트의 맨 앞에 새로운 노드 삽입하기

1. 새로운 노드를 만들고 추가할 데이터를 저장한다.
2. 새로운 노드의 next필드가 현재의 head노드를 가리키도록 한다.
3. 새로운 노드를 새로운 head 노드로 한다.

```c
Node *tmp = (Node *)malloc(sizeof(Node)); // 새로운 노드를 만든다. tmp라는 포인터변수를 임시로 만들어서 이 포인터 변수가 금방 새로 만들어진 주소의 노드를 보관하도록 함
tmp->data = "Ann"; // tmp가 가리키는 노드의 데이터 필드에는 저장할 데이터를 쓴다.
tmp->next = head; // tmp가 가리키는 노드의 next필드에 head를 쓴다.
head = tmp; // head가 새로 만들어진 노드를 가리켜야 하니까 head에 새로만들어진 노드의 주소를 가진 tmp를 쓴다.
```

주의할 점은 이 경우에는 기존의 연결리스트 길이가 0인경우, 즉 head가 NULL인 경우에도 문제가 없는지 확인해야 한다.

<!-- - 첫번째 노드를 가리키는 포인터 head가 전역변수인 경우

만약 맨 앞에 새로운 노드를 삽입하는 일을 하나의 함수를 만들어서 그 함수를 호출하고 싶다면

```c
void add_first(char *item)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = item;
    temp->next = head;
    head = temp;
}
``` -->

## 배열을 사용한 데이터 삽입

```c
#include <stdio.h>

char Data[5] = {'A', 'B', 'D', 'E'};
char c;

void main(){
    int i, temp, temp2;
    c = 'C';

    for(i=0; i<5; i++){
        printf("%2c", Data[i]);
    }
    printf("\n");

    for(i=0; i<5; i++){     //새로운 데이터 C를 넣을 위치를 찾는 코드
        if(Data[i] > c)
        break;
    }

    temp = Data[i];
    Data[i] = c;
    i++;

    for(; i<5; i++){        //데이터 C를 넣은 이후 뒤의 기존데이터들을 한칸씩 이동
        temp2 = Data[i];
        Data[i] = temp;
        temp = temp2;
    }

    for(i = 0; i<5; i++){
        printf("%2c", Data[i]);
    }
}
// 실행결과
// A B D E
// A B C D E
```

이 코드는 데이터가 많아지면 예를들어 1000개이고 두번째 위치에 삽입된다고 하면 999번의 데이터 이동이 필요하다는 점에서 비효율적이다.

### 배열의 삽입 알고리즘의 문제를 해결하는 단일 링크드 리스트의 삽입 알고리즘

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE {
    char Data;
    struct _NODE *Next;
} NODE;

NODE *head, *end, *temp;
NODE *temp1, *temp2, *temp3, *temp4;

void Initialize(void);
void InsertNode(NODE *);

void Initialize(void)
{
    NODE *ptr;
    head = (NODE *)malloc(sizeof(NODE));
    end = (NODE *)malloc(sizeof(NODE));

    temp1 = (NODE *)malloc(sizeof(NODE));
    temp1->Data = 'A';
    head->Next = temp1;
    temp1->Next = end;
    end->Next = end;
    ptr = temp1;

    temp2 = (NODE *)malloc(sizeof(NODE));
    temp2->Data = 'B';
    ptr->Next = temp2;
    temp2->Next = end;
    ptr = temp2;

    temp3 = (NODE *)malloc(sizeof(NODE));
    temp3->Data = 'D';
    ptr->Next = temp3;
    temp3->Next = end;
    ptr = temp3;

    temp4 = (NODE *)malloc(sizeof(NODE));
    temp4->Data = 'E';
    ptr->Next = temp4;
    temp4->Next = end;
    ptr = temp4;
}

void InsertNode(NODE *ptr)
{
    NODE *indexptr;

    for(indexptr = head; indexptr != end; indexptr = indexptr->Next){
        if(indexptr->Next->Data > ptr->Data)
            break;
    }

    //단일 링크드 리스트에서 노드를 삽입하는 코드
    ptr->Next = indexptr->Next;
    indexptr->Next = ptr;
}

void main()
{
    NODE *ptr;
    int i = 0;
    Initialize();

    //링크트 리스트의 노드에 저장한 데이터 출력
    ptr = head->Next;

    for(i = 0; i < 4; i++){
        printf("%2c", ptr->Data);
        ptr = ptr->Next;
    }

    //새로운 노드 생성
    printf("\n");
    temp = (NODE *)malloc(sizeof(NODE));
    temp->Data = 'C';

    //새로 생성한 노드 삽입
    InsertNode(temp);

    //링크드 리스트의 노드에 저장한 데이터 출력
    ptr = head->Next;

    for(i=0; i<5; i++){
        printf("%2c", ptr->Data);
        ptr = ptr->Next;
    }
}

// 실행결과
// A B D E
// A B C D E
```

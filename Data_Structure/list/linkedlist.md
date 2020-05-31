## 배열과 링크드 리스트

배열은 같은 자료형을 갖는 데이터의 집합으로, 연속적인 데이터를 저장한다는 특성이 있다. 배열은 크기가 고정되어 있어 리스트의 중간에 원소를 삽입하거나 삭제할 경우 다수의 데이터를 옮겨야 한다는 단점이 있다.

링크드 리스트는 다른 데이터의 이동없이 중간에 삽입이나 삭제가 가능하다는 것이 장점이다. 그러나 배열은 상수시간에 노드를 얻을 수 있는데 반해 링크드 리스트는 노드의 개수가 n이라면 최악의 경우 n회의 탐색 루프를 실행해야 한다는 단점이 있다.

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

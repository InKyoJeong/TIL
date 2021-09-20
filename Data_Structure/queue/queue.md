## 큐(Queue)

큐(queue)는 대기행렬이라고 볼 수 있다. 역시 스택과 마찬가지로 일종의 리스트이다. 단, 데이터의 삽입은 한쪽 끝에서, 삭제는 반대쪽 끝에서만 일어난다. 삽입이 일어나는 쪽을 **rear**, 삭제가 일어나는 쪽을 **front**라고 부른다.

- **enqueue, insert, put** : 큐의 rear에 새로운 원소를 삽입하는 연산
- **dequeue, remove, get** : 큐의 front에 있는 원소를 큐로부터 삭제하고 반환하는 연산

큐는 **FIFO(First In, First Out)** 방식이다. 처음 저장한 데이터를 처음 사용한다는 뜻이다.

<br>

![queue1](./images/queue1.svg)

<br>

### 큐 구현

```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }
  peek() {
    return this.first;
  }
  enqueue(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      const holdingPointer = this.last;
      holdingPointer.next = newNode;
      this.last = newNode;
    }
    this.length++;
    return this;
  }
  dequeue() {
    if (!this.first) {
      return null;
    }
    // 한개만 있을때
    if (this.first === this.last) {
      this.last = null;
    }
    const holdingPointer = this.first;
    this.first = this.first.next;
    this.length--;
    return holdingPointer; // return this;
  }
}

const myQueue = new Queue();
myQueue.peek();
myQueue.enqueue("AA");
myQueue.enqueue("BB");
// first: Node {value: 'AA', next: Node}
// last: Node {value: 'BB', next: null}
// length: 2
myQueue.dequeue();
```

<!--  -->

<!-- ### 배열을 이용한 큐의 구현

큐는 스택과 달리 배열을 사용하는 것이 좀 더 편하다. 먼저 배열 하나를 정의하여 큐를 위한 자료구조를 준비한다.

```c
int Queue[MAX];
```

<br>

#### 초기화 함수

```c
void InitializeQueue(void)
{
    Front = Rear = 0;
}
```

![queue2](./images/queue2.svg)

큐의 앞과 뒤를 가리키는 **front**와 **rear**변수값을 모두 **0**으로 초기화한다. 100개의 항목을 갖는 배열 Queue에서 front와 rear변수는 첫 번째 인덱스를 가리킨다.

<br>

#### Put() 함수

```c
void Put(int num)
{
    Queue[Rear++] = num;

    if(Rear >= MAX)
        Rear = 0;
}
```

현재 Queue 값에 넣으려는 데이터를 변수 Rear값이 가리키는 곳에 저장하고 Rear 변수값을 하나 증가시킨다. 그러면 Rear는 다음 배열 공간을 가리킨다. 즉 **Put(1)** 함수가 실행되면 1이 Queue[0]에 저장되며 0을 가리키는 변수 Rear는 1증가한다.

![queue3](./images/queue3.svg)

만약 변수 Rear가 배열의 크기(MAX)와 같거나 크면 Rear를 0으로 만들어서 다시 배열 Queue의 인덱스가 0부터 시작하도록 한다.

<br>

#### Get() 함수

```c
int Get(void)
{
    int ret;
    ret = Queue[Front++];

    if(Front >= MAX)
        Front = 0;

    return ret;
}
```

배열 Queue에서 Front가 가리키는 곳의 데이터를 ret에 저장하고 반환한다. 그리고 **Put()** 함수의 Rear에서 처럼 만약 Front변수가 배열의 크기보다 크면 0으로 초기화한다.

![queue4](./images/queue4.svg)

<br>

**Put()** 함수로 1, 2, 8, 10을 큐에 저장하고 저장되면서 Rear값이 바뀐다. 그리고 **Get()** 함수를 호출하면 큐의 처음 데이터인 Front가 가리키는 데이터 1을 반환하고 Front값이 하나 증가한다.

즉, **Put()** 함수는 매개변수로 받은 int자료형 데이터를 Rear가 가리키는 큐에 저장하고 Rear값을 하나 증가시킨다. **Get()** 함수는 반대로 Front가 가리키는 큐 안의 데이터를 가져온다.

<br>

#### 배열을 사용한 큐 알고리즘

배열을 사용한 큐 자료구조를 이용하는 전체 코드는 다음과 같다.

```c
#include <stdio.h>

#define MAX 100

int Queue[MAX];
int Front, Rear;

void InitializeQueue(void);
void Put(int);
int Get(void);
void DisplayQueue(void);

void InitializeQueue(void)
{
    Front = Rear = 0;
}

void Put(int num)
{
    Queue[Rear++] = num;

    if(Rear >= MAX)
        Rear = 0;
}

int Get(void)
{
    int ret;
    ret = Queue[Front++];

    if(Front >= MAX)
        Front = 0;

    return ret;
}

void DisplayQueue(void)
{
    int i;
    printf("Front->");

    for(i = Front; i < Rear; i++)
        printf("%d->", Queue[i]);

    printf("Rear");
}

void main()
{
    int ret;
    InitializeQueue();

    Put(1);
    Put(2);
    Put(8);
    Put(10);
    Put(13);

    printf("다섯 번의 Put() 함수 호출 후 결과\n");
    DisplayQueue();

    ret = Get();
    ret = Get();
    ret = Get();

    printf("\n세 번의 Get() 함수 호출 후 결과\n");
    DisplayQueue();

    printf("\n두 번의 Get() 함수 호출 후 결과\n");

    ret = Get();
    ret = Get();
    DisplayQueue();
}
```

- 실행 결과

```
다섯 번의 Put() 함수 호출 후 결과
Front->1->2->8->10->13->Rear
세 번의 Get() 함수 호출 후 결과
Front->10->13->Rear
두 번의 Get() 함수 호출 후 결과
```

<br>

### 연결리스트를 사용한 큐의 구현

큐는 배열로 사용하는 것이 구현하기도 편하고 관리도 편하지만 연결리스트를 사용하여 만들 수도 있다.

#### 노드 정의

```c
typedef struct _NODE {
    int data;
    struct _NODE *next;
} NODE;
```

링크 하나, 저장할 데이터가 한 개인 구조이다.

<br>

#### 초기화 함수

```c
void InitializeQueue(void)
{
    Front = (NODE *)malloc(sizeof(NODE));
    Rear = (NODE *)malloc(sizeof(NODE));
    Front->next = Rear;
    Rear->next = Rear;
}
```

front와 rear에 메모리를 할당한 뒤 링크를 서로 연결시켜 큐를 초기화한다.

<br>

#### Put() 함수

```c
void Put(int num)
{
    ptrNode = (NODE *)malloc(sizeof(NODE));
    ptrNode->data = num;

    if(Front->next == Rear){
        Front->next = ptrNode;
        ptrNode->next = Rear;
        Rear->next = ptrNode;
    }else {
        Rear->next->next = ptrNode;
        ptrNode->next = Rear;
        Rear->next = ptrNode;
    }
}
```

![queue6](./images/queue6.svg)

큐가 비어있는 경우 (`Front->next`가 Rear를 가리키는 경우) `Front->next`값이 새로 추가되는 노드인 ptrNode를 가리키게 한다. 그리고 `ptrNode->next`는 Rear를 가리키게 하고 `Rear->next`는 ptrNode를 가리키게 한다.

<br>

![queue7](./images/queue7.svg)

기존의 노드가 존재하는 경우는 `Rear->next->next`값이 ptrNode를 가리키게하고(1) `ptrNode->next`는 Rear값을 가리키게 하고(2) `Rear->next`는 새로운 노드 ptrNode를 가리키게 한다(3).

<br>

#### Get() 함수

```c
int Get(void)
{
    int ret;
    NODE *deleteNode;
    printf("\n");

    if(Front->next == Rear)
        printf("Queue is Empty\n");
    else{
        deleteNode = Front->next;
        Front->next = deleteNode->next;
        ret = deleteNode->data;
        printf("get() : %d", ret);

        free(deleteNode);
    }
    return ret;
}
```

![queue8](./images/queue8.svg)

먼저 큐가 비었는지 확인하고 비어있지 않으면 deleteNode값이 `Front->next`값을 가리키게 하고 `Front->next`값이 `deleteNode->next`값을 가리키게 한다. 그리고 deleteNode값의 데이터를 출력하고 free()함수로 노드를 제거한다.

<br>

#### DisplayQueue() 함수

```c
void DisplayQueue(void)
{
    NODE *ptrTemp;

    if(Front->next != Rear){
        for(ptrTemp = Front->next; ptrTemp->next != Rear; ptrTemp = ptrTemp->next){
            printf("%d->", ptrTemp->data);
        }

        printf("%d", ptrTemp->data);
    }
    else if(Front->next == Rear)
        printf("Queue is Empty\n");
}
```

`Front->next`값이 Rear를 가리킬 때까지 연결리스트를 이동하며 각 노드 데이터를 출력한다.

<br>

#### 연결리스트를 사용한 큐 알고리즘

연결리스트를 사용한 큐의 전체 코드는 다음과 같다.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE {
    int data;
    struct _NODE *next;
} NODE;

NODE *Front, *Rear;
NODE *ptrNode;

void InitializeQueue(void);
void Put(int);
int Get(void);
void DisplayQueue(void);

void InitializeQueue(void)
{
    Front = (NODE *)malloc(sizeof(NODE));
    Rear = (NODE *)malloc(sizeof(NODE));
    Front->next = Rear;
    Rear->next = Rear;
}

void Put(int num)
{
    ptrNode = (NODE *)malloc(sizeof(NODE));
    ptrNode->data = num;

    if(Front->next == Rear){
        Front->next = ptrNode;
        ptrNode->next = Rear;
        Rear->next = ptrNode;
    }else {
        Rear->next->next = ptrNode;
        ptrNode->next = Rear;
        Rear->next = ptrNode;
    }
}

int Get(void)
{
    int ret;
    NODE *deleteNode;
    printf("\n");

    if(Front->next == Rear)
        printf("Queue is Empty\n");
    else{
        deleteNode = Front->next;
        Front->next = deleteNode->next;
        ret = deleteNode->data;
        printf("get() : %d", ret);

        free(deleteNode);
    }
    return ret;
}

void DisplayQueue(void)
{
    NODE *ptrTemp;

    if(Front->next != Rear){
        for(ptrTemp = Front->next; ptrTemp->next != Rear; ptrTemp = ptrTemp->next){
            printf("%d->", ptrTemp->data);
        }

        printf("%d", ptrTemp->data);
    }
    else if(Front->next == Rear)
        printf("Queue is Empty\n");
}

void main()
{
    int ret;
    InitializeQueue();
    printf("Put() 함수 호출하기\n");

    Put(1);
    Put(2);
    Put(8);
    Put(10);
    Put(13);

    printf("다섯 번의 Put() 함수 호출 결과: ");
    DisplayQueue();

    ret = Get();
    ret = Get();
    ret = Get();

    printf("\n세 번의 Get() 함수 호출 결과: ");
    DisplayQueue();

    ret = Get();
    ret = Get();

    printf("\n두 번의 Get() 함수 호출 결과: ");
    DisplayQueue();
}
```

- 실행 결과

```
Put() 함수 호출하기
다섯 번의 Put() 함수 호출 결과: 1->2->8->10->13
get() : 1
get() : 2
get() : 8
세 번의 Get() 함수 호출 결과: 10->13
get() : 10
get() : 13
두 번의 Get() 함수 호출 결과: Queue is Empty
``` -->

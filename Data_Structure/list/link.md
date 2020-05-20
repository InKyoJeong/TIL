## 리스트(List)

- 기본적인 연산 : 삽입(insert), 삭제(remove), 검색(search)등
- 리스트를 구현하는 대표적인 두 가지 방법: **배열, 연결리스트**

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
- 마지막 노드의 _**next**_ 필드에는 **_NULL_** 을 지정하여 연결리스트의 끝임을 표시

## 링크드 리스트란?

### Node

> 연결리스트에서 하나의 노드를 표현하기 위한 구조체이다. 각 노드에 저장될 데이터는 하나의 문자열이라고 가정하자.

```c
struct node{
    char *data;
    struct node *next;      //다음 노드의 주소를 저장할 필드이다.
}
typedef struct node Node;
Node *head = NULL;          //연결리스트의 첫 번째 노드의 주소를 저장할 포인터이다.
```

### 예제프로그램

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

- 배열을 사용할때는 미리 배열을 만들어놓고 데이터를 하나씩 필요할때마다 저장하는 형식이다. 데이터를 저장할 메모리를 미리 잡아놓고 데이터를 하나씩 저장해나간다.

- 연결리스트에서는 노드가 10개인 연결리스트를 만든다고해서 노드10개를 미리 만들지 않고 노드가 필요할때 그때그때 노드를 하나씩 만들어서 연결리스트에 추가하는 형식이다.

- 노드는 동적메모리 할당 `malloc` 으로 만든다.

<br>

### #1

```c
    head = (Node *)malloc(sizeof(Node));
    head->data = "Tuesday";
    head->next = NULL;
```

<center><img src="./images/list1.svg" width="800" height="250"></center>

지금은 노드가 하나밖에 없으니까 _**next**_ 노드는 **_NULL_** 이다. 이 하나의 노드가 첫번째 노드가 된다. 그래서 이 블록에서는 _**head**_ 가 첫번째 노드를 가리키게 만들어주는 역할을 한다.

- `head->data = "Tuesday";` : _**head**_ 가 가르키는 노드의 데이터 필드에 "Tuesday" 저장

- `head->next = NULL;` : 첫번째 노드이자 마지막 노드이므로 **_NULL_** 값을 저장해서 이것이 마지막 노드임을 표시

<br>

### #2

그 다음에는 또다른 노드를 만들어서 두번째 노드를 첫번째 노드의 _**next**_ 노드로 (Tuesday 다음에 Thursday가 오도록) 만들어보자.

```c
    Node *q = (Node *)malloc(sizeof(Node));
    q->data = "Thursday";
    q->next = NULL;
    head->next = q;
```

<center><img src="./images/list2.svg" width="800" height="250"></center>

- Thursday를 저장하기위한 노드를 만들고 이 노드의 주소를 q라는 포인터 변수에 저장한다.

- `q->data = "Thursday";`, `q->next = NULL;` : q의 데이터와 _**next**_ 에 "Thursday"와 **_NULL_** 을 각각 저장한다.

- `head->next = q;` : Tuesday의 _**next**_ 필드에 Thursday노드의 주소를 넣어준다. 즉, _**head**_ 가 가리키고있는 노드의 _**next**_ 필드에 q를 저장한다.

<br>

### #3

이번엔 "Monday"라는 노드를 만들어서 "Tuesday"앞에 넣어보자. 연결리스트의 맨 앞에 새로운 노드를 만든다. 아까와 마찬가지로 새로운 노드를 만들고 포인터 변수 q가 새로 만들어진 노드를 가리키도록 한다.

```c
    q = (Node *)malloc(sizeof(Node));
    q->data = "Monday";
    q->next = head;
    head = q;
```

- `q->data = "Monday";` : 먼저 q의 데이터필드에 "Monday"를 저장한다.

<center><img src="./images/list3.svg" width="800" height="250"></center>

- `q->next = head;` : Monday를 앞쪽에 넣으려면 Monday의 _**next**_ 노드가 Tuesday가 되어야한다. 따라서 q가 가리키고있는 노드의 _**next**_ 필드에 Tuesday노드의 주소(포인터변수 _**head**_ )를 쓴다.

<center><img src="./images/list4.svg" width="800" height="250"></center>

- `head = q;` : 이제 더이상 Tuesday가 첫번째 노드가 아니므로 _**head**_ 가 Monday를 가리키도록 바꾼다. Monday의 주소는 q이므로 `head = q;`

<center><img src="./images/list5.svg" width="800" height="250"></center>

<br>

### #4

마지막 부분은 이렇게 만들어진 연결리스트의 각 노드에 저장된 데이터를 순서대로 출력한다.

```c
    Node *p = head;
    while(p!=NULL){
        printf("%s\n", p->data);
        p = p->next;
    }
```

<center><img src="./images/list6.svg" width="800" height="250"></center>

- `Node *p = head;` : p라는 포인터 변수가 선언되고 현재 _**head**_ 에 저장된 값을 p에 쓴다. 따라서 p가 첫번째 노드를 가리키게 된다.

- `while(p!=NULL) {...}` : p가 **_NULL_** 이 아닌 동안 p.data를 출력한다. 현재 p가 "Monday"를 가리키고 있으니까 거기 저장된 데이터 "Monday"를 출력하고 다음 노드로 넘어간다. p가 가리키는 노드의 _**next**_ 필드에 저장된 값이 **_NULL_** 이 되면 `p = NULL`이 되면서 while문을 빠져나온다.

- `p = p->next;` : 그다음 노드로 넘어가는 일을 한다. 현재 p가 가리키고있는 노드의 _**next**_ 필드에 저장된 값(그다음 노드의 주소)을 p에 쓴다.

<br>

## 연결리스트의 맨 앞에 새로운 노드 삽입하기

![insert1](./images/insert1.png)

```c
Node *temp = (Node *)malloc(sizeof(Node));
temp->data = "Mary"
temp->next = head;
head = temp;
```

temp라는 포인터 변수를 임시로 만들어서 새로 만들어진 노드의 주소를 보관하도록 하고, temp가 가리키는 노드의 data필드에 저장할 데이터("Mary")를 넣는다. temp가 가리키는 노드의 next필드에는 head에 보관된 "John"노드의 주소를 넣는다. 따라서 `temp->next = head` 이다. 마지막으로 head가 새로만들어진 노드의 주소(temp)를 가리킨다.

> 만약 노드의 개수가 0개라면, 즉 head가 NULL인 경우에도 문제가 없는지 확인해야 한다.

### 첫번째 노드를 가리키는 포인터 head가 전역변수인 경우

```c
void add_first(char *item)
{
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = item;
    temp->next = head;
    head = temp;
}
```

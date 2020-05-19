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

## 노드

- 각각의 노드는 필요한 **데이터 필드**와 하나혹은 그 이상의 **링크 필드**로 구성됨
- 링크 필드는 다음 노드의 주소를 저장
- 첫번째 노드의 주소는 따로 저장해야함
- 마지막 노드의 next필드에는 NULL을 지정하여 연결리스트의 끝임을 표시

## Node

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

```c
    head = (Node *)malloc(sizeof(Node));
    head->data = "Tuesday";
    head->next = NULL;
```

![list1](./images/list1.svg){: width="100" height="100"}
![list1](./images/list1.png){: width="100" height="100"}

<img src="/images/list1.svg" width="300" height="300">
<img src="/images/list1.png" width="300" height="300">

지금은 노드가 하나밖에 없으니까 next노드는 NULL이다. 이 하나의 노드가 첫번째 노드가 된다. 그래서 이 블록에서는 head가 첫번째 노드를 가리키게 만들어주는 역할을 한다.

- `head->data = "Tuesday"` : head가 가르키는 노드의 데이터 필드에 "Tuesday" 저장

- `head->next = NULL;` : 첫번째 노드이자 마지막 노드이므로 NULL값을 저장해서 이것이 마지막 노드임을 표시

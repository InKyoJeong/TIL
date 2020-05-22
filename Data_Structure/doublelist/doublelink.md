## 이중 연결리스트 (double linked list)

- 단방향 연결리스트 (single linked list)의 한계
  - 어떤 노드의 앞에 새로운 노드를 삽입하기 어려움
  - 삭제의 경우 항상 삭제할 노드의 앞 노드가 필요
  - 단방향의 순회만이 가능
- 이중 연결 리스트
  - 각각의 노드가 다음(next) 노드와 이전(prev) 노드의 주소를 가지는 연결리스트
  - 양방향의 순회(traverse)가 가능

<br>

### Node

> 각 노드에 하나의 문자열이 저장된다고 가정

```c
struct node{
  char *data;
  struct node next;
  struct node prev;
};

typedef struct node Node;

Node *head;
Node *tail;
int size = 0;
```

<br>

## 이중 연결리스트의 삽입 알고리즘

> p가 가리키는 노드 앞에 새로운 노드를 삽입하는 경우

```c
Node *new_node = (Node *)malloc(sizeof(Node));
new_node->data = "Mary";
new_node->next = p;
new_node->prev = p->prev;
p->prev->next = new_node;
p->prev = new_node;
```

![double1](./images/double1.png)

p가 어떤 노드를 가리키고 있을때 그 노드 앞에 새로운 노드를 만든다. 먼저 새로운 노드를 만들고(new_node) 그 노드의 데이터필드에 데이터를 저장한다("Mary").

여기서도 순서가 중요하다. 먼저 새로운노드의 next노드가 p가 되고(1) 새로운노드의 prev노드는 p의 이전노드가 된다(2). 그다음 p의 prev의 next노드가 새로운노드가 되고(3) p의 prev는 새로운노드가 된다(4).

<br>

## 이중 연결리스트의 삭제 알고리즘

> p가 가리키는 노드를 삭제하는 경우

```c
p->prev->next = p->next;
p->next->prev = p->prev;
```

![double2](./images/double2.png)

첫번째 줄은 p의 prev노드의 next노드가 현재는 p인데 그걸 p의 다음 노드로 만든다. 마찬가지로 두번째 줄은 p의 next노드의 prev노드가 현재는 p인데 그걸 p의 이전 노드로 만든다.

<br>

## add_after(Node *pre, char *item) - to empty list

```c
void add_after(Node *pre, char *item)
{
  Node *new_node = (Node *)malloc(sizeof(Node));
  new_node->data = item;
  new_node->prev = NULL;
  new_node->next = NULL;

  if(pre == NULL && head == NULL){
    head = new_node;
    tail = new_node;
  }
  ...
}
```

## add_after(Node *pre, char *item) - at the head

```c
else if (pre == NULL){
  new_node->next = head;
  head->prev = new_node;
  head = new_node;
}
```

## add_after(Node *pre, char *item) - at the tail

```c
else if (pre == tail){
  new_node->prev = tail;
  tail->next = new_node;
  tail = new_node;
}
```

## add_after(Node *pre, char *item) - in the middle

```c
  else{
      new_node->prev = pre;
      new_node->next = pre->next;
      pre->next->prev = new_node;
      pre->next = new_node;
  }
  size++;
}
```

## remove(Node \*p)

> 4가지 경우로 나누어서 처리한다.

1. p가 유일한 노드인 경우
2. p가 head인 경우
3. p가 tail인 경우
4. 그밖의 일반적인 경우

## add_ordered_list(char \*item)

```c
void add_ordered_list(char *item){
  Node *p = tail;
  while (p != NULL && strcmp(item, p->data) < 0)
      p = p->prev;
  add_after(p, item);
}
```

<br>

## 원형 리스트

- 원형 연결 리스트
  - 마지막 노드의 다음 노드가 첫번째 노드가 되는 단순 연결리스트
- 원형 이중 연결 리스트
  - 마지막 노드의 다음 노드가 첫번째 노드가 되고
  - 첫 노드의 이전 노드가 마지막 노드가 됨

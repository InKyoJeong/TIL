## Linked List

```bash
# head(10) -> 4 -> tail(22) -> null
10-->4-->22
```

이런식의 순서로 링크드리스트를 만든다고하면 아래와 같은 형식으로 붙여나간다.

```js
let myLinkedList = {
  head: {
    value: 10,
    next: {
      value: 4,
      next: {
        value: 22,
        next: null,
      },
    },
  },
};
```

#### 구현

- `append()` : 리스트의 끝에 추가
- `prepend()` : 리스트의 시작에 추가

```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }
  insert(index, value) {
    // index가 0일경우 맨앞에, 길이보다 클경우 맨뒤에 추가
    if (index === 0) {
      this.prepend(value);
      return this.printList();
    }
    if (index >= this.length) {
      return this.append(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index - 1); // insert 앞부분 찾기
    const holdingPointer = leader.next; // insert 할곳 뒷부분 기억해놓기
    leader.next = newNode; // insert 앞부분과 새로운 노드 연결
    newNode.next = holdingPointer; // 새로운 노드에 insert 뒷부분 연결
    this.length++;
    return this.printList();
  }

  traverseToIndex(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  remove(index) {
    const leader = this.traverseToIndex(index - 1);
    const wantRemoveNode = leader.next;
    leader.next = wantRemoveNode.next;
    this.length--;
    return this.printList();
  }

  // 반대로 만들어보기
  reverse() {
    if (!this.head.next) {
      return this.head;
    }
    let first = this.head;
    this.tail = this.head;
    let second = first.next; // [1, 10, 4, 22] 이상태라면
    while (second) {
      const temp = second.next; // 4 (세번째)
      second.next = first; // 포인터 바꾸는 부분: 10 다음을 1로 (1<-10), 다시 루프하면 10<-4, 4<-22
      first = second; // 자리 땡기는부분: first는 second로
      second = temp; // 자리 땡기는부분: second는 second.next로 하고
    }
    this.head.next = null;
    this.head = first; // 22가 head로
    return this;
  }
  // reverse 원리 : https://www.youtube.com/watch?v=D7y_hoT_YZI
}

const myLinkedList = new LinkedList(10);
console.log(myLinkedList);
myLinkedList.append(4);
myLinkedList.append(22);
// head: {value: 10, next: {…}}
// length: 3
// tail: {value: 22, next: null}
myLinkedList.prepend(1);
myLinkedList.printList(); // [1, 10, 4, 22]
myLinkedList.insert(2, 77); // [1, 10, 77, 4, 22]
myLinkedList.remove(2); // [1, 10, 4, 22]
myLinkedList.reverse();
```

<br>

#### 시간복잡도

- prepend O(1)
- append O(1)
- lookup O(n)
- insert O(n)
- delete O(n)

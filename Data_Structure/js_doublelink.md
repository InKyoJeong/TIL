## Doubly Linked List

- `append()` : 리스트의 끝에 추가
- `prepend()` : 리스트의 시작에 추가

```bash
10-->4-->22
```

```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null; // +
  }
}

class DoublyLinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
      prev: null, // +
    };
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    const newNode = new Node(value);
    newNode.prev = this.tail; // +
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head.prev = newNode; // +
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
    if (index === 0) {
      this.prepend(value);
      return this.printList();
    }
    if (index >= this.length) {
      return this.append(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index - 1);
    const holdingPointer = leader.next;
    leader.next = newNode;
    newNode.prev = leader; // +
    newNode.next = holdingPointer;
    holdingPointer.prev = newNode; // +
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
    const holdingPointer = wantRemoveNode.next; // +
    holdingPointer.prev = leader; // +
    this.length--;
    return this.printList();
  }
}

const myLinkedList = new DoublyLinkedList(10);
console.log(myLinkedList);
myLinkedList.append(4);
myLinkedList.append(22);
// head: Node {value: 1, next: {…}, prev: null}
// length: 4
// tail: Node {value: 22, next: null, prev: Node}
myLinkedList.prepend(1);
myLinkedList.printList(); // [1, 10, 4, 22]
myLinkedList.insert(2, 77); // [1, 10, 77, 4, 22]
myLinkedList.remove(2); // [1, 10, 4, 22]
```

<br>

#### 시간복잡도

- prepend O(1)
- append O(1)
- lookup O(n)
- insert O(n)
- delete O(n)

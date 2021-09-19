## 배열

- Fast lookups, Fast push/pop
- Slow inserts, Slow deletes

```js
class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return lastItem;
  }

  delete(index) {
    const item = this.data[index];
    this.shiftItems(index);
    return item;
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }
}

const newArray = new MyArray();
newArray.push("AAA"); // 1
newArray.push("BBB"); // 1
newArray.push("CCC"); // 1
// newArray.pop();
newArray.delete(1);
console.log(newArray); // {length: 2, data: {0: 'AAA', 1: 'CCC'}}
```

- `shiftItems` 에서는 지우는 index 기준으로 하나씩 왼쪽으로 땡기는데, 마지막꺼는 남아있으므로 삭제해준다.

<br>

## 문자열 뒤집기 배열로 구현

```js
function reverse(str) {
  if (!str || str.length < 2 || typeof str !== "string") {
    return "That is not good..";
  }

  const backwards = [];
  const totalItems = str.length - 1;
  for (let i = totalItems; i >= 0; i--) {
    backwards.push(str[i]);
  }
  return backwards.join("");
}

reverse("Hi My Name Is KYO"); // 'OYK sI emaN yM iH'
```

#### 메서드 이용

```js
let str = "Hi My Name Is KYO";
str.split("").reverse().join(""); // "OYK sI emaN yM iH"
```

<br>

## 해시 테이블(Hash Table)

- Fast lookup, Fast inserts
- Unordered, Slow key iteration

```js
class HashTable {
  constructor(size) {
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
  }

  set(key, value) {
    let address = this._hash(key);
    if (!this.data[address]) {
      this.data[address] = [];
    }
    this.data[address].push([key, value]);
    return this.data;
  }

  get(key) {
    let address = this._hash(key);
    const currentBucket = this.data[address];
    if (currentBucket) {
      for (let i = 0; i < currentBucket.length; i++) {
        if (currentBucket[i][0] === key) {
          return currentBucket[i][1];
        }
      }
    }
    return undefined;
  }

  keys() {
    const keysArray = [];
    for (let i = 0; i < this.data.length; i++) {
      if (this.data[i]) {
        keysArray.push(this.data[i][0][0]);
      }
    }
    return keysArray;
  }
}

const myHashTable = new HashTable(50);
myHashTable.set("grape", 1000);
myHashTable.set("apple", 54);
myHashTable.get("grape"); // 1000
myHashTable.keys(); // ['apple', 'grape']
```

<br>

## Array vs Hash Table

- Array
  - search O(n)
  - lookup O(1)
  - push O(1)
  - insert O(n)
  - delete O(n)
- Hash Tables
  - search O(1)
  - insert O(1)
  - lookup O(1)
  - delete O(1)

<br>

## 첫 중복 원소 찾기

```js
function solution(arr) {
  let answer = undefined;
  let sH = new Map();
  for (let x of arr) {
    if (sH.get(x)) {
      sH.set(x, sH.get(x) + 1);
    } else {
      sH.set(x, 1);
    }

    for (let [key, value] of sH) {
      if (value >= 2) {
        return key;
      }
    }
  }

  return answer;
}
console.log(solution([2, 5, 1, 2, 3, 5, 1, 2, 4])); //2
```

```js
function firstRecurringCharacter(input) {
  let map = {};
  for (let i = 0; i < input.length; i++) {
    if (map[input[i]] !== undefined) {
      return input[i];
    } else {
      map[input[i]] = i;
    }
  }
  return undefined;
}

firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4]);
```

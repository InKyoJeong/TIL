## this

> this는 함수내에서 함수 호출 맥락(context)을 의미한다(= 상황에따라 달라진다). 즉 함수를 어떻게 호출하느냐에 따라 this가 가리키는 대상이 달라진다.<br>this는 자신이 속해있는 객체를 가리키는 특수한 키워드이다.

```js
const kim = {
  name: "kim",
  age: 20,
  weight: 50,
  sum: function() {
    return kim.age + kim.weight;
  }
};

console.log(kim.sum()); // 70
```

여기서 `const kim`을 `const k`로 바꾼다면 `kim.age`라는 것은 더이상 없기때문에 동작하지않는다.

대신 `this`를 이용해서 바꿔보면 잘 동작한다.

```js
const k = {
  name: "kim",
  age: 20,
  weight: 50,
  sum: function() {
    return this.age + this.weight;
  }
};

console.log(k.sum()); // 70
```

만약 객체의 이름`k`를 다시 `kim`으로 바꾼다 하더라도 이제 잘 동작한다.

```js
const kim = {
  name: "kim",
  age: 20,
  weight: 50,
  sum: function() {
    return this.age + this.weight;
  }
};

console.log(kim.sum()); // 70
```

`this` 덕분에 객체가 내부적으로 가지고 있는 상태를 함수에서 참조할 수 있다.

### 함수호출

> 아래와 같이 함수를 호출했을때 this는 전역객체인 window와 같다.

```js
function func() {
  if (window === this) {
    console.log("window === this");
  }
}

func(); // window === this
```

### 메소드의 호출

> 객체의 소속인 메소드의 this는 그 객체를 가르킨다.

```js
const o = {
  func: function() {
    if (o === this) {
      console.log("o === this");
    }
  }
};

o.func(); // o === this
```

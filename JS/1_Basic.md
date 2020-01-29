#### Variable

변수를 만들때는 기본적으로 이렇게 작동한다.

```
Create : 먼저 변수를 생성하고
Initialize : 다음으로 이걸 초기화하고
Use : 이걸 사용하면 된다.
```

필요에 따라 생성과 초기화를 동시에 할 수 있다.

```js
let a = 221;
let b = a - 5;
a = 4;
console.log(b, a); // 216 , 4
```

const = constant, 상수 = stable (변하지 않는다.)

```js
const a = 22;
a = 4;
console.log(b, a); // TypeError: Assignment to constant variable.
```

const는 변수를 바꿀 수 없다. 변수를 선언할 때는 기본적으로 const를 사용한다.

#### comment (주석)

```js
// 한줄 처리
/* 
여러줄 처리
여러줄 처리
*/
```

#### string

```js
const what = "Github";

console.log(what); //Github
```

만약 숫자를 넣어도 이건 텍스트다.

```js
const what = "1234567";
```

#### Boolean : True or False

```js
const what = true;
```

true/false는 텍스트가 아니다. 소문자로 쓰고, "" 없이 사용한다. 이진법에서 true는 1, false는 0이다.

#### Float : 소숫점이 있는것

```js
const what = 55.1;
```

> Camel case: js에서는 변수명을 소문자로 시작해서 변수명 중간에는 스페이스 대신 대문자로 쓴다. ex) daysOfWeek

#### Array

```js
const monday = "Mon";
const tue = "Tue";
const wed = "Wed";
const thu = "Thu";
const fri = "Fri";

console.log(monday, tue, wed, thu, fri);
//이건 효과적이지 않다. 하나로 묶을 수 있다.
```

Array는 string을 하나로 묶는다.

```js
const daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", true];

console.log(daysOfWeek);
// ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', true];
```

Array는 0부터 시작하기때문에 3번째 요일을 알고싶다고 하면 2로 입력한다.

```js
console.log(daysOfWeek[2]); // Wed
```

#### Object

Array와 Object의 다른점은 Object에는 각 value에 이름을 줄 수 있다는 것이다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true
};

console.log(info); // {name: "Nico", age: 33, gender: "Male", isHandsome: true}
```

gender에만 접근하려면 데이터의 이름만 사용한다.

```js
console.log(info.gender); //Male
```

객체안의 값은 바꿀 수도있다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true
};

console.log(info.gender); //Male

info.gender = "Female";

console.log(info.gender); //Female
```

데이터를 정렬하는데는 두가지 방법이 있는데 하나는 Array, 다른하나는 Object이다.
만약 DB에서 가져온 리스트 데이터라면 Array를 선택하고, 만약 데이터를 합쳐서 만들어야 한다면 Object를 선택한다.

Array와 Object는 서로를 안에 넣을 수도 있다.

```js
const info = {
  name: "Nico",
  age: 33,
  gender: "Male",
  isHandsome: true,
  favMovies: ["Inception", "Notebook"],
  favFood: [
    {
      name: "Kimchi",
      fatty: false
    },
    {
      name: "Burger",
      fatty: true
    }
  ]
};

console.log(info.favFood[0].fatty); //false
```

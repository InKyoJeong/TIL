## 타입스크립트란?

- 자바스크립트에 타입을 부여한 언어. 자바스크립트의 확장된 언어라고 볼 수 있음
- 자바스크립트와 달리 브라우저에서 실행하려면 파일을 한번 변환해줘야함 (= 컴파일(complile))

### 쓰는 이유

- 에러의 사전 방지
- 코드 가이드 및 자동 완성(개발 생산성 향상)

### 설치

```
$ npm install -g typescript
```

### 변환

```
$ tsc filename.ts
```

<br>

## 타입스크립트 설정 파일 (tsconfig.json)

- 타입스크립트를 자바스크립트로 변환할 때의 설정을 정의해놓는 파일
- 프로젝트에서 `tsc` 명령어를 치면 여기에 정의된 내용을 기준으로 변환 작업(컴파일)을 진행함

<br>

## 기본 타입

변수나 함수와 같은 자바스크립트 코드에 타입을 정의할 수 있음. 크게 12가지

- Boolean
- Number
- String
- Object
- Array
- Tuple
- Enum
- Any
- Void
- Null
- Undefined
- Never

```ts
// 문자열
let str: string = "hello";

// 숫자
let num: number = 10;

// 배열
let arr: Array<number> = [1, 2, 3];
let clothes: Array<string> = ["Cap", "Shirts", "Pants"];
let items: number[] = [1, 2, 3];

// 튜플 - 모든 인덱스에 타입이 정의된 배열
let city: [string, number] = ["Seoul", 24];

// 객체
// let obj: object = {};
// let person: object = {
//     name: 'kyo',
//     age: 11
// };
let person: { name: string; age: number } = {
  name: "kyo",
  age: 11,
};

// 진위값
let show: boolean = true;
```

<br>

## 함수

```ts
// TS - 매개변수에 타입지정
function add(a: number, b: number) {
  return a + b;
}

// TS - 함수의 반환값에 타입지정
function add(): number {
  return 11;
}

// 함수에 타입을 정의하는 방식
function add(a: number, b: number): number {
  return a + b;
}
```

### 함수의 옵셔널 파라미터

- 타입스크립트에서는 함수의 인자를 모두 필수 값으로 간주함
  - 하지만 물음표를 이용하여 인자를 필요에따라 생략 가능

```ts
function log(a: string, b?: string) {
  //...
}

log("hello");
log("hello", "world");
```

<br>

## 인터페이스

> 상호 간에 정의한 약속 혹은 규칙

- 객체의 스펙(속성과 속성의 타입)
- 함수의 파라미터
- 함수의 스펙(파라미터, 반환 타입 등)
- 배열과 객체를 접근하는 방식
- 클래스

```ts
interface User{
    age: number;
    name: string;
}

// 변수에 사용
const taeyeon: User = {
    age: 33,
    name: '태연'
}

// 함수의 매개변수에 사용
function getUser(user: User){
    console.log(user);
}
getUser(taeyeon);
```

### 함수의 스펙(구조)에 사용

```ts
interface SumFunction{
    (a: number, b: number): number;
}

var sum: SumFunction;
sum = function(a: number, b: number): number{
    return a+b;
}
```

<br>

## 인덱싱, 딕셔너리 패턴

### 인덱싱

```ts
interface StringArray{
    [index: number]: string;
}

let arr: StringArray = ['a', 'b', 'c'];
arr[0]; //'a'
```

### 딕셔너리 패턴

```ts
interface StringRegexDictionary{
    [key: string]: RegExp;
}

let obj: StringRegexDictionary = {
    cssFile: /\.css$/,
    jsFile: /\.js$/,
}

obj['cssFile'] = 'a';   // 'a'형식은 'RegExp'형식에 할당될수없음
```

<br>

## 인터페이스 확장

```ts
interface Person{
    name: string;
    age: number;
}

interface Developer{
    name: string;
    age: number;
    language: string;
}
```

이렇게 중복된 값들을 다른 인터페이스가 갖고있으면 상속받아 사용가능

```ts
interface Person{
    name: string;
    age: number;
}

interface Developer extends Person{
    language: string;
}

let kyo: Developer = {
    language: 'ts',
    age: 11,
    name: '개발자'
```

<br>

## 타입 별칭

- 특정 타입이나 인터페이스를 참조할 수 있는 타입 변수

```ts
// string 타입을 사용할 때
const name: string = 'kyo';

// 타입 별칭을 사용할 때
type MyName = string;
const name: MyName = 'kyo';
```

- interface 레벨의 복잡한 타입에도 별칭 부여 가능

```ts
type Developer = {
  name: string;
  skill: string;
}
```

<br>

## 타입 별칭과 인터페이스의 차이

- 타입 별칭은 새로운 타입 값을 하나 생성하는 것이 아니라, 정의한 타입에 대해 나중에 쉽게 참고할 수 있게 이름을 부여하는 것과 같음

- **인터페이스는 확장이 가능** / 타입 별칭은 확장이 불가능
- 따라서, 가능한 `type` 보다는 `interface`로 선언해서 사용

<br>

## 유니온(Union) 타입

```ts
//ex) string말고 다른 타입을 쓰고 싶을때

function logMessage(value: string | number){
    console.log(value);
}

logMessage('ssss');
logMessage(100);
```

<br>

### 인터페이스 두개를 연결하면 공통된 속성만 접근가능

```ts
interface Email {
  name: string;
  email: string;
}
interface Phone {
  name: string;
  phone: number;
}
const contactInfo: Email | Phone = {};
contactInfo.name; // 두 타입의 교차점은 name 속성이므로 name만 접근 가능
```

<br>

## 인터섹션 타입

- 두 타입의 합집합

```ts
interface Developer {
  name: string;
  skill: string;
}

interface Person {
  name: string;
  age: number;
}

function askSomeone(someone: Developer & Person){
    someone.name;
    someone.skill;
    someone.age;
  }

askSomeone({name:'개발자', skill: '앱개발'}); //Property 'age' is missing in type ...  
askSomeone({name:'개발자', skill: '앱개발', age: 100});
```

<br>

## 이넘

- 특정 값들의 집합을 의미하는 자료형

### 숫자형

```ts
enum Shoes {
    Nike,
    Adidas
}

let myShoes = Shoes.Nike;
console.log(myShoes); //0
```

- 초기 값 없으면 0부터 차례로 1씩 증가
```ts
enum Direction {
  Up, // 0
  Down, // 1
  Left, // 2
  Right // 3
}
```

### 문자형

```ts
enum Shoes {
    Nike = '나이키',
    Adidas = '아디다스'
}
let myShoes = Shoes.Nike;
console.log(myShoes); //나이키
```

### 예시

```ts
enum Answer{
    Yes = 'Y',
    No = 'N',
}

function askQuestion(answer: Answer){
    if(answer === Answer.Yes){
        console.log('정답');
    }
    if(answer === Answer.No){
        console.log('오답');
    }
}


askQuestion(Answer.Yes);
askQuestion('Yes') //(X) 이넘에서 제공하는 값만 넘길수 있음
```

<br>

## 클래스

```ts
// ES5
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const hulk = new Person('Banner', 33);
```
```ts
// ES6 + 타입스크립트
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}
const capt = new Person('Steve', 100);
```
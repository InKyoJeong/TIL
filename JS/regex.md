## 정규 표현식

> [https://regexr.com/](https://regexr.com/)

- 정규 표현식(regular expression)은 문자열의 패턴을 표현하기 위한 도구
- 각 언어, 응용 프로그램에 내장된 정규 표현식은 기본적인 부분은 같지만 세부적 사양은 차이있음
  - 자바스크립트 정규 표현식은 Perl의 정규 표현식을 받아들인 것

## 정규 표현식 생성

- 자바스크립트 정규표현식은 `RegExp`객체로 표현함
- 정규표현식은 RegExp 생성자 또는 정규 표현식 리터럴로 생성 가능

```js
// RegExp 생성자
const reg = new RegExp("abc");

// 정규 표현식 리터럴
const reg = /abc/;
```

<br>

#### RegExp 객체의 메서드

- js로 정규 표현식을 사용해 문자열 처리하려면 `RegExp.prototype`의 `test`, `exec` 메서드 사용
  - 또는 `String.prototype`의 `match, replace, search, split` 메서드 사용

```js
// test 메서드 : 일치하는지 논리값 반환
const reg = /dog/;
console.log(reg.test("dog and cat")); // true
console.log(reg.test("hello")); // false
```

```js
// exec 메서드 : 일치한 문자열을 배열로 반환. 못찾으면 null
const reg = /Script/;
const result = reg.exec("JavaScript");

console.log(result); // ["Script", index: 4, input: "JavaScript", groups: undefined]
console.log(result[0]); // Script
console.log(result.index); // 4 (가장 처음 일치한 인덱스)
console.log(result.input); // "JavaScript"
```

<br>

## match 사용하기

```js
// [a-z] : 두 문자 사이의 모든 문자
const str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const regexp = /[A-D]/gi;
const match_arr = str.match(regexp);
console.log(match_arr); // ["A", "B", "C", "D", "a", "b", "c", "d"]

// [abc] : 문자 클래스 : 문자 집합 안의 특정 문자 한 개
const str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const regexp = /[abc]/gi;
const match_arr = str.match(regexp);
console.log(match_arr); //["A", "B", "C", "a", "b", "c"]

// abc : 문자열을 포함
const str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const regexp = /abc/gi;
const match_arr = str.match(regexp);
console.log(match_arr); // ["ABC", "abc"]
```

`g`는 글로벌 검색 (일치하는 모든 문자열), `i`는 대소문자 무시 플래그

<br>

## 🏷 태그 구현 해보기

- `/#` #이 선택
- `/#/g` 모든 #이 선택
- `/#.../g` #다음에 세글자(점 개수)가 선택
- `/#.+/g` #다음 모든 글자 선택
  - 이거의 문제점은 `#예시 #아무거나` 이거에서 `예시 #아무거나` 이부분이 하나의 해시태그처럼됨
  - 따라서 공백을 제거해야함
- `/#[]+/g` : 대괄호를`[]`넣으면 안에있는거중에 선택
- `/#[^]+/g` : 캐럿(`^`)을 붙이면 여기안에 들어있는 건 제외
- `/#[^\s]+/g` : `\s`가 공백.
  - 이거의 문제점은 `#첫번쨰#두번쨰` 이렇게 두개 붙어있는게 안됨
  - `/#[^\s#]+/g` : 뒤에 #을 합쳐주면 해결됨

<br>

#### split 으로 확인해보기

- 이렇게 해봤더니 공백이 나옴

```js
"첫번째 게시글 #해시태그 #단플".split(/#[^\s#]+/g);
// ["첫번째 게시글 ", " ", ""];
```

- `#[^\s#]+` 바깥에 괄호를 넣어줘야한다.

```js
"첫 번째 게시글 #해시태그 #단플".split(/(#[^\s#]+)/g);
// ["첫번째 게시글 ", "#해시태그", " ", "#단플", ""];
```

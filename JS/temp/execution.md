## 실행 컨텍스트 (Execution Context)

> 실행 컨텍스트는 실행할 코드에 제공할 환경 정보들을 모아놓은 객체로, 자바스크립트의 동적 언어로서의 성격을 가장 잘 파악할 수 있는 개념

---

### 📌Content

- [실행 컨텍스트란?](#intro)
- [VariableEnvironment](#variable)
- [LexicalEnvironment](#lexical)
  - [Environment Record](#er)
  - [Outer Lexical Environment Reference](#o)
- [thisBinding](#this)

---

### 실행 가능한 코드

- 자바스크립트 엔진은 **실행 가능한 코드(Executable Code)** 를 만나면 그 코드를 평가해서 실행 컨텍스트로 만든다.
- 실행 가능한 코드 유형은 세가지
  - `전역 코드` : 전역 객체 Window 아래에 정의된 함수
  - `함수 코드` : 함수
  - `eval 코드` : eval 함수
- 실행 가능한 코드 유형을 분류하는 이유 : 실행 컨텍스트를 초기화하는 과정이 다르기때문

<br>

### 실행 컨텍스트의 구성

- 실행 컨텍스트(Execution Context)는 **실행 가능한 코드가 실제로 실행되고 관리되는 영역**
- 실행에 필요한 모든 정보를 컴포넌트 여러개가 나눠 관리
- 그 중에 중요한 컴포넌트는 **_렉시컬 환경(LexicalEnvironment) 컴포넌트_**, **_변수 환경(VariableEnvironment) 컴포넌트_**, **_디스 바인딩(This Binding) 컴포넌트_**

<br>

## <a name="intro"></a>실행 컨텍스트란?

실행 컨텍스트는 실행할 코드에 제공할 환경 정보들을 모아놓은 객체이다. 동일한 환경에 있는 코드들을 실행할 때 필요한 환경 정보들을 모아 컨텍스트를 구성하고, 이를 **콜 스택(Call Stack)** 에 쌓았다가, 가장 위에 쌓인 컨텍스트와 관련있는 코드들을 실행하는 식으로 전체 코드의 환경과 순서를 보장한다.

```js
var a = 1;
function outer() {
  function inner() {
    console.log(a); //undefined
    var a = 2;
  }
  inner();
  console.log(a); //1
}
outer();
console.log(a); //1
```

처음 자바스크립트 코드를 실행하면 전역 컨텍스트가 콜 스택에 쌓인다. outer 함수를 호출하면 자바스크립트 엔진은 outer에 대한 환경 정보를 수집해서 outer 실행 컨텍스트를 생성하고 콜 스택에 넣는다. 콜 스택 맨위에 outer 실행 컨텍스트가 쌓였으므로 outer 함수 내부 코드를 순차로 실행한다.

![context1](./images/context1.svg)

다시 inner함수 실행 컨텍스트가 콜 스택 맨위에 쌓이면 outer 컨텍스트 관련 코드실행을 중지하고 inner 함수 내부의 코드를 순서대로 진행한다.

inner 함수 내부에서 변수에 값을 할당하고 inner 함수 실행이 종료되면 inner 실행 컨텍스트가 콜 스택에서 제거된다. 그러면 다시 outer 컨텍스트가 콜 스택 맨위에 있게되고 a 변수가 출력되면 outer 함수 실행이 종료되며 outer 실행 컨텍스트가 제거된다.

![context2](./images/context2.svg)

그리고 콜 스택에 전역 컨텍스트만 남는다. 그리고 다시 a 변수를 출력하면 전역 공간에 더이상 실행할 코드가 없어서 전역 컨텍스트가 제거되고 콜 스택이 비어진다.

한 실행 컨텍스트가 콜 스택의 맨 위에 쌓이는 순간이 현재 실행할 코드에 관여하게 되는 시점이다. 이렇게 어떤 실행 컨텍스트가 활성화될 때 자바스크립트 엔진이 해당 컨텍스트에 관련된 코드들을 실행하는데 필요한 환경 정보들을 수집하고 실행 컨텍스트 객체에 저장한다.

이 객체는 자바스크립트 엔진이 활용할 목적으로 생성할 뿐 개발자가 코드로 확인할 순 없다.

여기 담기는 정보들:

- **_VariableEnvironment_** : 현재 컨텍스트 내의 식별자들에 대한 정보 + 외부 환경 정보, 선언 시점의 _LexicalEnvironment_ 의 스냅샷으로, 변경 사항은 반영되지 않음
- **_LexicalEnvironment_** : 처음에는 _VariableEnvironment_ 와 같지만 변경 사항이 실시간으로 반영됨
- **_ThisBinding_** : _this_ 식별자가 바라봐야할 대상 객체

<br>

즉, 처음 캡쳐떴을때 값만 신경쓰고 그 뒤에 값이 바뀌는건 상관하지않는게 _VariableEnvironment_, 이후에 값이 변경되는것을 계속 반영하고있는게 _LexicalEnvironment_

<br>

## <a name="variable"></a>VariableEnvironment

_VariableEnvironment_ 에 담기는 내용은 _LexicalEnvironment_ 와 같지만 `최초 실행 시의 스냅샷을 유지`한다는 점이 다르다. 실행 컨텍스트를 생성할 때 _VariableEnvironment_ 에 정보를 먼저 담고, 그대로 복사해서 _LexicalEnvironment_ 를 만들고, 이후에는 주로 _LexicalEnvironment_ 를 활용한다. 초기화 과정 중에는 사실상 완전히 동일하다.

<br>

## <a name="lexical"></a>LexicalEnvironment

LexicalEnvironment(렉시컬 환경) 컴포넌트는 자바스크립트 엔진이 자바스크립트 코드를 실행하기 위해 자원을 모아둔 곳이다. 함수 또는 블록의 유효 범위안에 있는 식별자와 그 결과값이 저장된다.

자바스크립트 엔진은 해당 자바스크립트 코드의 유효범위 안에 있는 식별자와 그 식별자가 가리키는 값을 키와 값의 쌍으로 바인드해서 LexicalEnvironment(렉시컬 환경) 컴포넌트에 기록한다.

LexicalEnvironment(렉시컬 환경) 컴포넌트는

- **_Environment Record(환경 레코드)_** 와
- **_Outer Lexical Environment Reference(외부 렉시컬 환경 참조 컴포넌트)_** 로 구성됨.

<br>

### <a name="er"></a>Environment Record(환경 레코드)

**유효 범위 안에 포함된 식별자를 기록**하고 실행하는 영역이다. 자바스크립트 엔진은 유효 범위 안의 식별자와 결과값을 바인드해서 환경 레코드에 기록한다.

#### Environment Record(환경 레코드)와 호이스팅

Environment Record에는 매개변수 이름, 함수 선언, 변수명 등이 담기는데, 컨텍스트 내부 전체를 처음부터 끝까지 훑으면서 순서대로 수집한다. 코드가 실행되기 전이라도 자바스크립트 엔진은 이미 해당 환경에 속한 코드의 변수명들을 알고 있다. 자바스크립트 엔진은 식별자들을 최상단으로 끌어올려놓은 다음 실제 코드를 실행한다고 볼 수 있다.

```js
function a() {
  var x = 1;
  console.log(x);
  var x;
  console.log(x);
  var x = 2;
  console.log(x);
}
a();
```

위 코드는 **_1, undefined, 2_** 로 출력될 것 같지만 그렇지 않다. 이 상태에서 호이스팅을 처리해 보자. Environment Record는 현재 실행될 컨텍스트의 대상 코드 내에 어떤 식별자들이 있는지에만 관심이 있고, 식별자에 어떤 값이 할당될 것인지에는 관심이 없다. 따라서 변수명만 끌어올리고 할당부분은 그대로 남겨보자.

```js
function a() {
  var x;
  var x;
  var x;

  x = 1;
  console.log(x);
  console.log(x);
  x = 2;
  console.log(x);
}
a();
```

코드를 실행해보면 **_1, 1, 2_** 순으로 출력된다.

<br>

```js
function a() {
  console.log(b);
  var b = "bbb";
  console.log(b);
  function b() {}
  console.log(b);
}
a();
```

이번에는 위의 코드를 보면 첫번째 줄에서 b값이 없으니 에러나 undefined가 뜰것 같지만 그렇지 않다. 변수는 선언부와 할당부를 나눠 선언부만 끌어올리지만 `함수 선언은 함수 전체`를 끌어올림.

따라서 다음과같음:

```js
function a() {
  var b;
  function b() {}

  console.log(b);
  b = "bbb";
  console.log(b);
  console.log(b);
}
a();

// ƒ b(){}
// bbb
// bbb
```

<br>

#### 함수 선언식 vs 함수 표현식

함수 선언식의 경우 반드시 함수명이 정의되어 있어야 하고, 함수 표현식은 없어도 된다. 함수명을 정의한 함수 표현식을 '기명 함수 표현식', 정의하지 않은것을 '익명 함수 표현식'이라고 한다.

- 함수 선언식

```js
a(); //실행됨
function a() {
  /*...*/
}
a(); //실행됨
```

- (익명) 함수 표현식

```js
b(); //Error
var b = function () {
  /*...*/
};
b(); //실행됨
```

- (기명) 함수 표현식

```js
var c = function x() {
  /*...*/
};
c(); //실행됨
x(); //Error
```

기명 함수 표현식은 외부에서는 함수명으로 함수를 호출할 수 없고 함수 내부에서만 접근할 수 있다.

<br>

#### 상대적으로 함수 표현식이 안전하다

함수 선언문으로 똑같은 함수를 선언한 예시이다.

```js
function sum(x, y) {
  return x + y;
}

var a = sum(1, 2);
console.log(a); //1+2=3

//...
function sum(x, y) {
  return x + "+" + y + "=" + (x + y);
}

var c = sum(1, 2);
console.log(c); //1+2=3
```

원래 a는 1+2를한 **'3'** 이 출력될것을 의도했지만 아래에 똑같이 선언한 _sum_ 함수 때문에 **'1+2=3'** 이 출력된다.

전역 컨텍스트가 활성화 될때 전역공간에 선언된 함수들이 모두 위로 끌어올려진다. 동일한 변수명에 다른 값을 할당할 경우 나중에 할당한 값이 먼저 할당한 값을 덮어씌운다. 따라서 실제 호출되는 함수는 마지막에 선언된 함수다.

<br>

따라서 아래와 같이 함수 표현식으로 정의하는 것이 상대적으로 더 안전하다.

```js
var sum = function (x, y) {
  return x + y;
};

var a = sum(1, 2);
console.log(a); //3

//...
var sum = function (x, y) {
  return x + "+" + y + "=" + (x + y);
};

var c = sum(1, 2);
console.log(c); //1+2=3
```

<br>

### <a name="o"></a>Outer Lexical Environment Reference(외부 렉시컬 환경 참조 컴포넌트)과 스코프 체인

**스코프체인(scope chain)** 이란 식별자의 유효 범위를 안에서부터 바깥으로 차례로 검색하는 것이다.

자바스크립트는 함수 안에 함수를 중첩해서 정의할 수 있으므로 자바스크립트 엔진은 유효 범위 너머의 유효 범위도 검색할 수 있어야 한다.

중첩된 함수 안에서 바깥 코드에 정의된 변수를 읽거나 써야할때, 자바스크립트 엔진은 외부 렉시컬 환경 참조를 따라 한 단계씩 렉시컬 환경을 거슬러 올라가서 그 변수를 검색한다.

즉, 스코프체인을 가능하게 하는 것이 _Outer Lexical Environment Reference_ 이다.

**_outerEnvironment-Reference_** 는 현재 호출된 함수가 선언될 당시의 **_LexicalEnvironment_** 를 참조한다.

예를들어, A함수 내부에 B함수를 선언, B함수 내부에 C함수를 선언했다고 하자. 함수 C의 **_outerEnvironment-Reference_** 는 함수 B의 **_LexicalEnvironment_** 를 참조한다. 함수 B의 **_LexicalEnvironment_** 에 있는 **_outerEnvironment-Reference_** 는 다시 함수 B가 선언되던 때(A)의 **_LexicalEnvironment_** 를 참조한다.

이렇게 **_outerEnvironment-Reference_** 는 연결리스트 형태를 띈다. 선언 시점의 **_LexicalEnvironment_** 를 따라 올라가다보면 마지막엔 전역 컨텍스트의 **_LexicalEnvironment_** 가 있다.

각 **_outerEnvironment-Reference_** 는 자신이 선언된 시점의 **_LexicalEnvironment_** 만 참조하므로 가장 가까운 요소부터 차례대로 접근할 수 있고 다른순서로 접근은 불가능하다. 이런 구조적 특성으로, 여러 스코프에서 동일 식별자를 선언한 경우 스코프 체인 상에서 가장 먼저 발견된 식별자에만 접근 가능하다.

<br>

```js
var a = 1;
var outer = function () {
  var inner = function () {
    console.log(a); //undefined
    var a = 2;
  };
  inner();
  console.log(a); //1
};
outer();
console.log(a); //1
```

1. 시작: 전역 컨텍스트가 활성화되고 전역 컨텍스트의 **_environmentRecord_** 에 `{ a, outer }` 식별자를 저장함. 전역 컨텍스트는 선언 시점이 없으므로 전역 컨텍스트의 _**outerEnvironment-Reference**_ 에는 아무것도 담기지 않는다.
2. 첫번째와 두번째줄 : 전역 스코프에 있는 변수 `a`에 `1`을, outer에 함수를 할당한다.
3. 끝에서 두번째줄 : outer함수를 호출한다. 전역 컨텍스트 코드는 중단되고, outer 실행 컨텍스트가 활성화되어 두번째줄로 이동한다.
4. 두번째줄 : outer 실행 컨텍스트의 **_environmentRecord_** 에 `{ inner }` 식별자를 저장한다. _**outerEnvironment-Reference**_ 에는 outer 함수가 선언될 당시의 _**LexicalEnvironment**_ 가 담긴다. outer 함수는 전역 공간에서 선언됐으므로, 전역 컨텍스트의 _**LexicalEnvironment**_ 를 참조 복사한다. 이를 `[ Global, { a, outer } ]` 라고 표기하자. 첫번째는 실행 컨텍스트 이름, 두번째는 **_environmentRecord_** 객체이다.
5. 3번째줄 : outer 스코프에 있는 변수 inner에 함수를 할당한다.
6. 7번째줄 : inner 함수를 호출한다. 그러면 outer 실행 컨텍스트 코드는 임시중단되고 inner 실행 컨텍스트가 활성화되어 3번째줄로 이동한다.
7. 3번째줄 : inner 실행 컨텍스트의 **_environmentRecord_** 에 `{ a }` 식별자를 저장한다. _**outerEnvironment-Reference**_ 에는 inner함수가 선언될 당시의 _**LexicalEnvironment**_ 가 담긴다. inner 함수는 outer 함수 내부에서 선언됐으므로 outer 함수의 _**LexicalEnvironment**_ 인 `[ outer, { inner }]`를 참조복사한다.
8. 4번째줄 : 식별자 `a`에 접근한다. 현재 활성화 상태인 inner 컨텍스트의 **_environmentRecord_** 에서 `a`를 검색한다. `a`가 발견됐는데 아직 할당값이 없다.(`undefined` 출력)
9. 5번째줄 : inner 스코프에있는 변수 `a`에 `2`를 할당한다.
10. 6번째줄 : inner 함수 실행이 종료된다. inner 실행 컨텍스트가 콜 스택에서 제거되고, 바로 아래 outer 실행 컨텍스트가 다시 활성화되면서, 중단됐던 7번째줄의 다음으로 이동한다.
11. 8번째줄 : 식별자 `a`에 접근한다. 자바스크립트 엔진은 활성화된 실행 컨텍스트의 _**LexicalEnvironment**_ 에 접근한다. 첫 요소의 **_environmentRecord_** 에 `a`가 있는지 찾고, 없으면 _**outerEnvironment-Reference**_ 에 있는 **_environmentRecord_** 으로 넘어가면서 계속 검색한다. 예제에서는 두번째, 즉 전역 _**LexicalEnvironment**_ 에 `a`가 있으므로 그 `a`에 저장된 `1`을 반환한다.
12. 9번째줄 : outer 함수 실행이 종료된다. outer 실행 컨텍스트가 콜 스택에서 제거되고, 바로 아래 전역 컨텍스트가 다시 활성화되며, 중단했던 끝에서 두번째줄 다음으로 이동한다.
13. 마지막줄 : 식별자 `a`에 접근한다. 현재 활성화 상태인 전역 컨텍스트의 **_environmentRecord_** 에서 `a`를 검색한다. 바로 `a`를 찾을수 있다.(1출력) 모든 코드실행이 완료된다. 전역 컨텍스트가 콜 스택에서 제거되고 종료한다.

![context3](./images/context3.png)

**_L.E_** 는 **_LexicalEnvironment_** 를 나타내고, **e**는 **_environmentRecord_** 를, **o**는 **_outerEnvironment-Reference_** 를 의미한다.

<br>

### <a name="this"></a>ThisBinding

실행 컨텍스트의 thisBinding에는 _this_ 로 지정된 객체가 저장된다. 실행 컨텍스트 활성화 당시에 _this_ 가 지정되지 않은 경우 _this_ 에는 전역 객체가 저정된다. 그밖에는 함수를 호출하는 방법에 따라 _this_ 에 저장되는 대상이 다르다.

<br>

### 정리

- **실행 컨텍스트**는 실행할 코드에 제공할 환경 정보들을 모아놓은 객체
  - 실행 컨텍스트는 전역 공간에서 자동으로 생성되는 전역 컨텍스트, eval, 함수 실행에 의한 컨텍스트 등이 있음
  - 실행 컨텍스트 객체는 활성화되는 시점에 **_VariableEnvironment_**, **_LexicalEnvironment_**, **_ThisBinding_** 세가지 정보를 수집함

* **_VariableEnvironment_** 와 **_LexicalEnvironment_** 는 매개변수명, 변수 식별자, 선언한 함수 함수명 등을 수집하는 `environmentRecord` 와 바로 직전 컨텍스트의 **_LexicalEnvironment_** 정보를 참조하는 `outerEnvironment-Reference` 로 구성됨

- **호이스팅**은 **_environmentRecord_** 의 수집 과정을 추상화한 개념으로, 실행 컨텍스트가 관여하는 코드 집단의 최상단으로 끌어올리는 것
  - 변수 선언과 할당이 동시에 됐으면 '선언부'만 호이스팅하고 할당과정은 자리에 남아서, 함수 선언문과 함수 표현식의 차이 발생

* **스코프**는 변수의 유효범위이고, **_outerEnvironment-Reference_** 는 해당 함수가 선언된 위치의 **_LexicalEnvironment_** 를 참조함
* 코드 상에서 어떤 변수에 접근하려고 하면 현재 컨텍스트의 **_LexicalEnvironment_** 를 탐색해서 발견되면 그값을 반환, 발견하지 못하면 다시 **_outerEnvironment-Reference_** 에 담긴 **_LexicalEnvironment_** 를 탐색
* 전역 컨텍스트의 **_LexicalEnvironment_** 까지 탐색해도 해당 변수를 못찾으면 undefined 반환

- 전역 컨텍스트의 **_LexicalEnvironment_** 에 담긴 변수를 전역변수라고 함
  - 그밖의 함수에 의해 생성된 실행 컨텍스트의 변수들은 지역변수임
  - 안전한 코드 구성을 위해서는 전역변수 사용을 최소화

* _this_ 에는 실행 컨텍스트를 활성화하는 당시에 지정된 _this_ 가 저장됨
  - 함수를 호출하는 방법에 따라 값이 달라지는데, 지정하지 않았으면 전역객체가 저장됨

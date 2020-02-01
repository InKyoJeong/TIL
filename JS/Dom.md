### DOM (Document Object Model)

#### DOM 트리

웹페이지 내용은 Document객체가 관리한다. 웹브라우저가 웹페이지를 읽으면 렌더링엔진은 웹페이지의 HTML 문서 구문을 해석하고 Document객체에서 문서내용을 관리하는 DOM 트리라는 객체의 트리 구조를 만든다.

DOM 트리를 구성하는 객체하나를 `노드(Node)`라고 한다.

```
문서 노드 : 전체 문서를 가리키는 Document 객체. document로 참조할 수 있다.
HTML 요소 노드 : HTML 요소를 가리키는 객체
텍스트 노드 : 텍스트를 기리키는 객체
```

#### 노드 객체 가져오기

js로 HTML요소를 제어하려면 요소 객체를 가져와야한다.

1. id 속성으로 노드 가져오기

```js
document.getElementById("id 값");
```

2. 요소 이름으로 노드 가져오기

```js
document.getElementByTagName("요소의 태그이름");
```

3. class 속성 값으로 노드 가져오기

```js
document.getElementByClassName("class의 이름");
```

4. name 속성 값으로 노드 가져오기

```js
document.getElementsByName("name 속성 값")

ex) ...
    <form>
        <input type="checkbox" name="food" value="potato" />포테이토
    </form>
    <script>
      const foods = document.getElementsByName("food");
      console.log(foods[0].value);      // potato
    </script>
    ...
```

5. CSS선택자로 노드 가져오기
   - `querySelector`는 노드의 첫번째 자식을 반환한다. CSS선택자와 비슷하다

```js
class로 찾고싶으면 document.querySelector(".title")
id는 document.querySelector("#title")
```

### Events and event handlers

`event`란 웹사이트에서 발생하는 것들을 말한다. (click, resize, submit, ...)

```js
function handleResize() {
  console.log("I have been resized");
}
window.addEventListener("resize", handleResize); //I have been resized
```

`handleResize`는 윈도우 사이즈가 변경 될때 `resize`함수를 호출한다.
`handleResize()`라고 적는다면 지금 바로 호출하라는 것이다.

#### DOM if/else Function Practice

- html

```html
...
<body>
	<h1 id="title" class="btn">This works!</h1>
	<script src="index.js"></script>
</body>
</html>
```

- css

```css
.btn {
  cursor: pointer;
}

h1 {
  color: #34495e;
}

.clicked {
  color: #7f8c8d;
}
```

- js

```js
const title = document.querySelector("#title");

const CLICK_CLASS = "clicked";

function handleClick() {
  const currentClass = titile.className;
  if (currentClass !== CLICK_CLASS) {
    title.className = CLICK_CLASS;
  } else {
    titile.className = "";
  }
}

function init() {
  title.addEventListener("click", handleClick);
}

init();
```

이렇게하면 btn class가 제거되어버린다.

따라서 `classList`를 사용해보자. `classList`는 메소드를 가진다. (remove, add, toggle, ...)

```js
const title = document.querySelector("#title");
const CLICK_CLASS = "clicked";

function handleClick() {
  const hasClass = title.classList.contains(CLICK_CLASS);
  if (hasClass) {
    title.classList.remove(CLICK_CLASS);
  } else {
    title.classList.add(CLICK_CLASS);
  }
}

function init() {
  title.addEventListener("click", handleClick);
}

init();
```

`toggle`을 사용하여 짧게 만들어보면

```js
const title = document.querySelector("#title");
const CLICK_CLASS = "clicked";

function handleClick() {
  title.classList.toggle(CLICK_CLASS);
}

function init() {
  title.addEventListener("click", handleClick);
}

init();
```

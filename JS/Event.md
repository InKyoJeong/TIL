<!-- ### Event

이벤트 처리기(이벤트 리스너) : 이벤트가 발생했을때 실행되는 함수

#### addEventListener 메서드

```js
EventTarget.addEventListener(type, listener, useCapture);
```

- `type` : 반응할 이벤트 유형을 나타내는 대소문자 구분 문자열
- `listener` : 이벤트가 발생했을 때 처리를 담당하는 콜백 함수의 참조
- `useCapture` : true=캡쳐링/ false=버블링 (기본값은 `false` ) -->

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

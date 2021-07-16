## Intersection Observer란?

Target Element가 화면에 노출되었는지 여부를 간단히 구독할 수 있는 API

<br>

#### Intersection Observer 필요 예시(MDN)

- 페이지 스크롤시 이미지를 Lazy-loading(지연 로딩)할때
- Infinite Scrolling
- 광고 수익을 계산하기 위한 광고의 가시성을 참고할때
- 사용자가 결과를 볼것인지에 따라 애니메이션 동작 여부를 결정할 때

<br>

#### addEventListener()의 scroll 이벤트

- _scroll_ 이벤트는 단시간에 여러번 호출될수 있고, 동기적으로 실행되어 메인스레드에 영향을 줌
- 한 페이지 내에 여러 _scroll_ 이벤트가 등록되면 엘리먼트마다 등록되어 있기때문에 스크롤시 감지하는 이벤트가 계속해서 호출됨
- 또한 특정 지점 관찰을 위해 `getBoundingClientRect()`를 사용할때, 리플로우(reflow) 현상이 발생
  - `var rect = 요소객체.getBoundingClientRect();`
  - 뷰 포트 좌표계로 측정한 해당 요소의 보더 박스위치와 크기 정보를 담은 객체를 반환함
  - _reflow_ : 브라우저가 웹페이지 일부 또는 전체를 다시 그려야하는 경우 발생

<br>

```js
// ex) 해당 요소가 viewport 내에 있는지 확인하는 함수

function isElementInViewport(el) {
  var rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <=
      (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
// element에 callback 함수 등록
const addEventToEl = (elList) => {
  document.addEventListener("scroll", () => {
    elList.forEach((el) => {
      if (isElementInViewport(el)) {
        el.classList.add("observer");
      } else {
        el.classList.remove("observer");
      }
    });
  });
};
// 이벤트 등록
const boxElList = document.querySelectorAll(".box");
addEventToEl(boxElList);
```

<br>

## Intersection Observer API

```js
let options = {
  root: document.querySelector('#scrollArea'), // 대상 객체의 가시성을 확인할 때 사용되는 뷰포트 요소. 기본값은 브라우저 뷰포트
  rootMargin: '0px', // root 가 가진 여백. 이 속성의 값은 CSS의 margin 속성과 유사 ex)"10px 20px 30px 40px" (상우하좌)
  threshold: 1.0    // observer의 콜백이 실행될 대상 요소의 가시성 퍼센티지. 만일 50%만큼 요소가 보여졌을 때를 탐지하고 싶다면 0.5
}

const io = new IntersectionObserver(callback[, options])
```

<br>

- **[Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver)** 는 `element.getBoundingClientRect`와 달리 `reflow`를 일으키지 않는다.

```js
// ex) Intersection Observer

const io = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    // 관찰 대상이 viewport 안에 들어온 경우 'observer' 클래스 추가
    if (entry.intersectionRatio > 0) {
      entry.target.classList.add("observer");
    } else {
      entry.target.classList.remove("observer");
    }
  });
});

// 관찰할 대상을 선언, 해당 속성을 관찰
const boxElList = document.querySelectorAll(".box");
boxElList.forEach((el) => {
  io.observe(el);
});
```

<br>

#### 참고하기

- MDN - Intersection_Observer_API
  - [https://developer.mozilla.org/ko/docs/Web/API/Intersection_Observer_API](https://developer.mozilla.org/ko/docs/Web/API/Intersection_Observer_API)
- React Intersection Observer
  - [https://github.com/thebuilder/react-intersection-observer#readme](https://github.com/thebuilder/react-intersection-observer#readme)
- Intersection Observer API의 사용법과 활용방법
  - [http://blog.hyeyoonjung.com/2019/01/09/intersectionobserver-tutorial/](http://blog.hyeyoonjung.com/2019/01/09/intersectionobserver-tutorial/)

# CSS Tip

> CSS 팁들을 짧게 기록하는 파일

---

## 1. em과 rem차이

> em과 rem 모두 길이가 유연한 가변 단위로서, 디자인에 설정된 폰트 크기에 따라 브라우저에 의해 픽셀값으로 변환됨

- `rem` 단위를 쓰면, 변환된 픽셀 크기는 페이지 최상위(root) 요소. 즉, html 요소의 폰트 크기가 기준

- `em` 단위를 쓰면 변환되는 픽셀값은 스타일을 지정한 요소의 폰트 크기를 곱한 값

<!-- 참고 : [https://webdesign.tutsplus.com/ko/tutorials/comprehensive-guide-when-to-use-em-vs-rem--cms-23984](https://webdesign.tutsplus.com/ko/tutorials/comprehensive-guide-when-to-use-em-vs-rem--cms-23984) -->

## 2. [scroll-behavior Property](https://www.w3schools.com/cssref/pr_scroll-behavior.asp)

> 부드러운 스크롤 기능을 추가할 수 있다.

```html
html { scroll-behavior: smooth; }
```

### 브라우저 지원상황

- Chrome : 61.0
- IE : Not supported
- FireFox : 36.0
- Safari : Not supported

### Property Value

- auto : Allows a straight jump "scroll effect" between elements within the scrolling box. This is default
- smooth : Allows a smooth animated "scroll effect" between elements within the scrolling box.
- initial : Sets this property to its default value.
- inherit : Inherits this property from its parent element.

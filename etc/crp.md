## Critical Rendering Path

사용자가 참조하고자 하는 웹페이지를 서버에 요청하면 서버로부터 _HTML, CSS, Javascript_, 이미지 파일 등을 응답받는다. 이러한 응답을 받으면 화면에 표시하기 전에 많은 단계를 거쳐야 한다. 브라우저가 페이지의 초기 출력을 위해 실행해야하는 이 단계를 **_Critical Rendering Path(CRP)_** 라고 한다. CRP를 최적화하면 최초 페이지 렌더링에 걸리는 시간을 상당히 단축시킬 수 있다.

CRP는 다음 단계로 진행된다.

- DOM 트리 구축
- CSSOM 트리 구축
- 랜더링 트리 구축
- Layout
- Paint

<br>

## DOM 트리

DOM은 문서 객체 모델(Document Object Model)의 준말이다. 웹브라우저가 웹페이지를 읽으면 렌더링 엔진은 웹페이지의 HTML 문서 구문을 해석하고 Document 객체에서 문서내용을 관리하는 DOM 트리라는 객체의 트리 구조를 만든다.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <link href="style.css" rel="stylesheet" />
    <title>Critical Path</title>
  </head>
  <body>
    <p>Hello <span>web performance</span> students!</p>
    <div><img src="awesome-photo.jpg" /></div>
  </body>
</html>
```

서버에서 응답으로 받은 HTML 데이터를 파싱하고, HTML을 파싱한 결과로 DOM 트리를 만든다. 이 html 문서는 다음과 같은 DOM 트리를 생성한다.

![render](./images/dom.png)

> ##### developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model

<br>

## CSSOM 트리

CSS파일은 HTML을 파싱한 것과 유사한 과정을 거쳐서 역시 트리 형태로 만들어진다. CSS는 rendering의 blocking 요소라고하는데, 먼저 리소스를 완전히 파싱하지 않으면 렌더링 트리를 구성할 수 없다. 자식 노드들이 부모 노드의 특성을 계속 상속 받는 (cascading) 특성때문에 부분적으로 실행될 수 없다.

```css
body {
  font-size: 16px;
}
p {
  font-weight: bold;
}
span {
  color: red;
}
p span {
  display: none;
}
img {
  float: right;
}
```

위 CSS는 다음과 같은 CSSOM 트리를 생성한다

![render](./images/cssom.png)

<br>

## 렌더링 트리

CSSOM을 모두 만들었으면, DOM과 CSSOM를 합쳐 렌더링 트리를 만든다. 페이지에서 최종적으로 렌더링 될 내용을 나타내는 트리이다. 렌더링 트리는 DOM 트리에 있는 것들 중에서 화면에 실제로 보이는 내용만으로 이루어진다. 비시각적 DOM 요소는 렌더 트리에 추가되지 않는다.

예를 들어 `head` 요소와 같은 비시각적 DOM 요소는 렌더 트리에 추가되지 않는다. 또한 display 속성에 `none` 값이 할당된 요소는 트리에 나타나지 않는다.

따라서 아래 렌더링 트리에서 `<head>` 태그와, display속성이 `none`인 `<p>` 태그 하위의 `<span>` 태그가 사라진 것을 확인할 수 있다.

![render](./images/render.png)

> ##### developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction

참고로, `visibility: hidden`은 `display: none`과 다르다. 전자는 요소를 보이지 않게 만들지만, 이 요소는 여전히 레이아웃에서 공간을 차지한다(비어 있는 상자로 렌더링됨). 반면, 후자(_display: none_)는 요소가 보이지 않으며 레이아웃에 포함되지도 않도록 렌더링 트리에서 요소를 완전히 제거한다.

<br>

## Layout

렌더링 트리가 다 만들어지면 렌더링 트리에 있는 각각의 노드들이 화면의 어디에 위치할 지를 계산하는 **Layout**(배치) 과정을 거친다. 이 과정을 _Webkit_ 에서는 layout으로, _Gecko_ 에서는 reflow로 부른다.

<!-- 현재 보이는 뷰포트를 기준으로 실제로 놓으려면 얘가 어디에 가야하는 지는 계산을 또 해야하는 거죠. 여기에서 CSS box model이 쓰이며, position(relative, absolute, fixed..), width, height 등등 틀과 위치에 관련된 부분들이 계산된다. -->

## Paint

이제 렌더링 트리의 각 노드들을 실제로 화면에 그리게 된다.

<br>

### Reference

- [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)

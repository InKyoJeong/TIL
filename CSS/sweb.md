# 5/12

## HTML (Hyper Text Markup Languague)

> 웹에서 기본적인 뼈대를 담당한다.

1. HTML은 '태그'들로 이루어진다.

태그는 `<열린태그>내용</닫힌태그>` 로 구성된다.

<br>

2. HTML의 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <title>제목</title>
  </head>
  <body>
    웹에 표시되는 내용(태그들)
  </body>
</html>
```

<br>

3. 텍스트 관련 태그

- `<h1> ~ <h6>` 태그 : h1이 제일크고 h6이 제일 작다.
- `<p>` 태그 : 주로 문단을 넣을때 쓴다.
- `<textarea>` 태그 : 텍스트 영역을 지정한다.

<br>

4. 목록 관련 태그

- `<ol>` 태그 : 순서가 있는 목록(order list)을 나타낸다. 목록의 아이템은 `<li>`태그를 사용한다.

예시)

```html
<ol>
  <li>사과</li>
  <li></li>
  <li>포도</li>
  <li>오렌지</li>
</ol>
```

- `<ul>` 태그 : 순서가 없는 목록(unorder list)을 나타낸다. 마찬가지로 목록의 아이템은 `<li>`태그를 사용한다.

예시)

```html
<ol>
  <li>사과</li>
  <li></li>
  <li>포도</li>
  <li>오렌지</li>
</ol>
```

<br>

5. 웹 페이지의 영역을 설정할 때 사용하는 태그

- `<div>` 태그 : 뜻이 없는 태그고, 주로 다른 태그들을 감쌀때나 박스를 만들때 쓴다.
- `<span>` 태그도 뜻이 없는 태그이다.

div 태그와 span 태그 차이는 여러개 만들어 나란히 나열하였을 때, div는 줄 바꿈이 일어나면서 세로로, span은 줄바꿈이 일어나지 않고 가로로 나열된다. div 태그를 훨씬더 많이 쓴다.

<br>

6. 이미지태그

- `<img src="이미지 주소" />` : 이미지를 불러올때 쓴다. 닫는태그가 필요없다. 속성값으로 `src`를 받는다.

<br>

7. 링크태그

- `<a href="사이트 주소">표시할 내용</a>` : 사이트주소를 링크할때 쓴다. 속성값으로 `href`를 받는다.

<br>

8. 폼 태그

- `<input>` 태그 : 폼안에 들어가는 항목들을 나타낼때 쓴다. 닫는태그가 필요없다. 속성값으로 `type`을 받고, `placeholder`속성을 사용할 수 있다. `placeholder`는 아무것도 안쳤을때 표시되는 내용이다.

예시)

```html
<input type="email" placeholder="이메일을 입력하세요" />
<input type="text" />
<input type="date" />
<input type="file" />
<input type="checkbox" />
```

<br>

9. 버튼 태그

- `<button>버튼이름</button>`

<br>

## CSS (cascading style sheets)

> 스타일을 적용하는데 쓴다.

css파일에 들어가는 코드들은

```
태그이름 또는 .클래스명{
	속성: 값;
}
```

으로 이루어진다.

html파일의 **head**태그 안에 `<link>` 태그로 연결한다.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>제목</title>
    <link rel="stylesheet" href="./파일이름.css" />
  </head>
  <body>
    태그들(생략)
  </body>
</html>
```

html 태그의 속성에 `class` 또는 `id`로 이름을 붙여서 css에서 제어할 수 있다. `id`는 거의 안쓰고 주로 `class`를 쓴다.

css에서 `class`로 이름을 받아올때는 앞에 마침표(`.`)을 찍고 속성을 지정한다.

예를들어 아래와같은 html 코드에서 `사과`라는 글씨의 색을 빨간색으로로 하려면

```html
<div class="apple">사과</div>
```

css 파일을 이렇게 작성하면 된다.

```
.apple{
	color: red;
}
```

### CSS 속성들

- `font-size : 값(px);`
  글씨 크기를 지정한다.
  <br>
- `width: 값(px 또는 %);`
  넓이를 지정한다.
  <br>
- `height : 값(px 또는 %);`
  높이를 지정한다.
  <br>

* `color : 색이름; 또는 rgb(값,값,값); 또는 #컬러코드;`
* `background-color : 색이름; 또는 rgb(값,값,값); 또는 #컬러코드;`<br>
  색상은 `red`같은 색 이름이나 `rgb(255,255,255);` 같이 `rgb`값이나, `#111FFF`와 같은 16진수로 표현하는법이 있다.

- `justifiy-content : center;`
  항목을 수평에서 중앙정렬한다. `display: flex;` 와 같이 쓰인다.
- `justify-content: space-between;`
  항목을 일정한 간격으로 띄워서 배치한다. `display: flex;` 와 같이 쓰인다.

* `align-items : center;`
  항목을 수직에서 중앙정렬한다. `display: flex;` 와 같이 쓰인다.

- `border-radius: 값(px 또는 %);`
  테두리를 값에따라 둥글게 만든다.
  <br>

- `border : px값 solid 색상;`
  테두리를 직선(solid)으로 설정한 색상으로 픽셀값(px)만큼 지정한다.

<br>

- `opacity : 값(0~1);`
  0~ 1.0 까지 소수점으로 투명도를 지정한다. 0 이면 완전투명, 1이면 기본값

<br>

- `margin` : 경계선(border) 기준 `바깥쪽`의 여백의 크기를 지정한다. (px 또는 %)
  - `margin-top: 20px;`
  - `margin-right: 30px;`
  - `margin-bottom: 40px;`
  - `margin-left: 50px;`

위의 4줄은 `margin: 20px 30px 40px 50px;` 와 같이 한줄로 표현가능하다. (top, right, bottom, left 순서.)

<br>

- `padding` : 경계선(border) 기준 `안쪽`의 여백의 크기를 지정한다. margin과 마찬가지로 (top, right, bottom, left)를 지정가능하고 한줄로 쓸수도 있다.

<br>

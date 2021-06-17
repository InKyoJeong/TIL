## script

- 브라우저는 HTML문서를 처리하다가 `script` 엘리먼트를 만나면 자바스크립트 코드를 실행한다.
- `script` 엘리먼트가 HTML문서 어디에 위치하는지가 웹페이지 로딩 속도에 영향을 줄 수 있다.

<br>

아래 코드는 _one_ 이 출력되고, `script.js` 파일을 받아 코드가 실행되고, _two_ 가 출력된다.

```html
<body>
  <h1>one</h1>
  <script src="./script.js"></script>
  <h1>two</h1>
</body>
```

<br>

- 따라서 딜레이를 최소화하여 최적화된 웹페이지 로딩 경험을 제공하려면 `<script>` 엘리먼트를 `<body>` 엘리먼트의 마지막에 넣는 것이 유리하다.

```html
<body>
  <h1>one</h1>
  <h1>two</h1>
  <script src="./script.js"></script>
</body>
```

<br>

## defer

- 내려받아야할 자바스크립트 파일 크기가 크거나 네트워크 속도가 느리면, `script` 엘리먼트 위치 조정 만으로는 부족할 수 있다.
- `<script>` 엘리먼트에 `defer` 속성을 사용하면, 브라우저는 **HTML 코드를 처리하면서 동시에 자바스크립트 파일도 내려받는다.**
- 따라서 `<script>` 엘리먼트가 HTML 문서 내의 어디에 위치하더라도, `<body>` 엘리먼트 제일 아래 넣은 것처럼, HTML 코드가 모두 처리된 이후에 자바스크립트 코드가 실행된다.

```html
<body>
  <h1>one</h1>
  <script defer src="./script.js"></script>
  <h1>two</h1>
</body>
```

<br>

## async

- `async` 속성을 사용하면 브라우저는 **HTML 코드를 처리하면서 자바스크립트 파일을 내려받고, 다운로드가 끝나자마자 내려받은 자바스크립트 코드를 실행**한다.
- 따라서 자바스크립트 코드양에 따라 HTML 코드처리보다 먼저 끝날수도 있고, 늦게 끝날수도 있다.

```html
<body>
  <h1>one</h1>
  <script async src="./script.js"></script>
  <h1>two</h1>
</body>
```

<br>

## defer vs async

- 서로 연관이 있는 여러 개의 스크립트 파일을 순차적으로 실행해야하는 경우에는 defer 속성이 안전
  - defer는 script가 여러개 있으면 병렬 로드, 순차실행이기 때문
- 여러 개의 독립된 자바스크립트 파일을 삽입하는 경우에는 async 속성을 사용하는 편이 성능에서 유리
  - async는 병렬 로드, 병렬 실행

<br>

## 정리

![script](./script.png)

> 출처: [www.growingwiththeweb.com/2014/02/async-vs-defer-attributes](https://www.growingwiththeweb.com/2014/02/async-vs-defer-attributes.html)

- `<script>` : HTML 파싱이 중단되고 즉시 스크립트가 로드되며 로드된 스크립트가 실행되고 파싱이 재개된다.
- `<script async>` : HTML 파싱과 병렬적으로 로드가 되는데, 스크립트를 실행할 때는 파싱이 중단된다.
- `<script defer>` : HTML 파싱과 병렬적으로 로드가 되는데, 파싱이 끝나고 스크립트를 로드한다.

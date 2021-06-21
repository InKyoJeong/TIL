## Origin 이란

- **Origin** : _scheme (protocol), host (domain), port_ 로 구성된다.
- 출처 내의 포트 번호는 생략이 가능하다.
  - 웹에서 사용하는 HTTP, HTTPS 프로토콜의 기본 포트 번호(80, 443)가 정해져있기 때문

<br>

#### 예를들어, 이런 주소가 있다고하면 _https://www.google.com/maps_

- `Protocol`:<br/>
  - _`https://`www.google.com/maps_
- `Host`:<br/>
  - _https://`www.google.com`/maps_
- `Port`:<br/>
  - _https://www.google.com`:443`/maps_

<br>

## Same Origin Policy

> **Same Origin(동일 출처)** : _scheme, host, port_ 가 모두 같을때를 말한다.

- **같은 출처에서만 리소스를 공유할 수 있다**라는 규칙을 가진 정책이다.
- 만약 다른 출처의 어플리케이션이 서로 통신하는 것에 대해 아무런 제약도 존재하지 않는다면?
  - 악의를 가진 사용자가 소스 코드를 보고 **CSRF(Cross-Site Request Forgery)** 나 **XSS(Cross-Site Scripting)** 와 같은 방법을 사용하여 정보 탈취 가능
- 출처를 비교하는 로직은 **서버에 구현된 스펙이 아니라 브라우저**에 구현되어 있는 스펙이다.
  - 따라서 브라우저를 통하지 않고 **서버 간 통신을 할 때는 이 정책이 적용되지 않음**
    <br>

#### _www.wikipedia.org_ 에서, 각 요청을 한다고 하자.

1. _www.bank.com_ 에 대한자바스크립트 `GET` 요청
2. _www.bank.com_ 에 대한자바스크립트 `POST` 요청
3. _www.bank.com_ 에서 HTML 비디오 링크 클릭

예외가 있을수 있지만 일반적으로,

- 첫번째 요청은 **실패**한다. 교차(다른) 출처 도메인에서 정보를 가져오는 요청은 브라우저가 허락하지 않는다.
  - 브라우저는 _www.wikipedia.org_ 가 _www.bank.com_ 에서 개인 정보를 훔치는 것을 방지하여 개인 정보를 보호하려고 한다.
- 두번째 요청은 **성공**한다. `POST` 요청은 개인정보를 훔칠 가능성이 낮다.
  - `POST`는 데이터를 GET 하는 것이아닌 서버에 데이터를 쓰는데 사용되므로, 응답에 개인정보가 포함될 가능성이 낮다.
- 세번째 요청은 **성공**한다. Same Origin Policy(동일 출처 정책)는 스크립트에만 적용되고 HTML 태그같은 정적 리소스에는 적용되지 않는다.

<br>

## CORS란?

<!-- - 기본적으로 웹 클라이언트 어플리케이션이 다른 출처의 리소스를 요청할 때는 HTTP 프로토콜을 사용하여 요청을 보내는데,
- 이때 브라우저는 요청 헤더에 Origin이라는 필드에 요청을 보내는 출처를 함께 담아보낸다.
- 이후 서버가 이 요청에 대한 응답을 할 때 응답 헤더의 Access-Control-Allow-Origin이라는 값에 “이 리소스를 접근하는 것이 허용된 출처”를 내려주고,
- 이후 응답을 받은 브라우저는 자신이 보냈던 요청의 Origin과 서버가 보내준 응답의 Access-Control-Allow-Origin을 비교해본 후 이 응답이 유효한 응답인지 아닌지를 결정한다. -->

- 클라이언트에서 서버로 요청을 보낼때는, 클라이언트와 서버의 도메인이 일치하지 않으면 기본적으로 요청이 차단된다.
- 이 문제를 CORS(Cross-Origin Resource Sharing) 문제라고 한다.

<br>

<!-- #### 교차 출처 리소스 공유가 동작하는 방식 세가지 시나리오 -->

## 해결 방법

### Access-Control-Allow-Origin 응답 헤더 세팅

- 서버측 응답에서 접근 권한을 주는 헤더를 추가하여 해결

```js
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*"); // 모든 도메인
  res.header("Access-Control-Allow-Origin", "https://example.com"); // 특정 도메인
});
```

### cors 모듈

```js
const cors = require("cors");
const app = express();

app.use(cors());
```

- 아무 옵션없이 설정하면 모든 cross-origin 요청에 대해 응답이므로,
- 특정 도메인이나 특정 요청에만 응답하게 옵션을 설정 가능

#### 특정 도메인 접근 허용

```js
const options = {
  origin: "http://example.com", // 접근 권한을 부여하는 도메인
  credentials: true, // 응답 헤더에 Access-Control-Allow-Credentials 추가
  optionsSuccessStatus: 200, // 응답 상태 200으로 설정
};

app.use(cors(options));
```

#### 특정 요청 접근 허용

```js
app.get("/example/:id", cors(), function (req, res, next) {
  res.json({ msg: "example" });
});
```

<br>

### webpack-dev-server proxy 기능

- 리액트 개발환경에서, 서버쪽 코드를 수정하지 않고 해결가능하다.
- 아래와 같이 프록시 속성을 설정하면, 서버에서 해당 요청을 받아준다.

```js
// 프록시 쓰지 않았을때
// localhost:8080(클라이언트 측) --X (CORS)--> domain.com (서버 측)

// 프록시를 설정 후
// localhost:8080(클라이언트 측) --O 프록시가 설정된 Webpack Dev Server--> domain.com (서버 측)

module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "domain.com",
        changeOrigin: true,
      },
    },
  },
};
```

중간의 프록시 서버 덕분에, domain.com 서버에서는 같은 도메인(domain.com)에서 온 요청으로 인식하여 CORS 에러가 나지 않는다.

<br>

### package.json에 proxy값을 설정

- create-react-app 으로 생성했다면, `package.json`에 `proxy`값을 설정하여 proxy기능을 활성화 가능하다.

```json
"proxy": "http://localhost:4000",
```

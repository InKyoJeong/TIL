# 미들웨어

요청과 응답의 중간에 위치하여 미들웨어라고 한다. 주로 `app.use`와 함께 사용된다.

## 커스텀 미들웨어

```js
//app.js
//...
//추가
app.use(function (req, res, next) {
  console.log(req.url, "저도 미들웨어 입니다.");
  next();
});

app.use(logger("dev"));
//...
```

```js
// npm start => localhost:3000
/ 저도 미들웨어 입니다.
GET / 200 248.630 ms - 170
/stylesheets/style.css 저도 미들웨어 입니다.
GET /stylesheets/style.css 200 3.659 ms - 111
```

각각의 요청이 커스텀 미들웨어를 작동시켰다. 이렇게 서버가 받은 요청은 미들웨어를타고 라우터까지 전달된다. `next()`를 호출해야 다음 미들웨어로 넘어간다.

## morgan

GET / 200 248.630 ms - 170 과 같은 로그는 `morgan`미들웨어에서 나오는것이다. 요청에 대한 정보를 콘솔에 기록한다.

```js
// app.js
//...
const logger = require("morgan");
//...
app.use(logger("dev"));
//...
```

```
GET / 200 248.630 ms - 170 의 의미는..

HTTP요청(GET) 주소(/) HTTP상태코드(200) 응답속도(248.630 ms) 응답바이트( - 170)
```

## helmet

노드앱의 보안에 도움을 준다.

```js
const express = require("express");
const helmet = require("helmet");

const app = express();

app.use(helmet());

// ...
```

<br>

## body-parser

- 요청의 본문을 해석해주는 미들웨어. 폼 데이터나 AJAX요청의 데이터를 처리함

```js
//...
const bodyParser = require("body-parser");
//...
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
//...
```

- 익스프레스 4.16.0 부터는 body-parser일부기능이 내장됐기때문에 설치하지 않고도 다음과같이 할 수 있다.

```js
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
```

**json**은 JSON형식의 데이터 전달방식이고, **URL-encoded**는 주소형식으로 데이터를 보내는 방식이다.

- `extended`옵션 : 내부적으로 `true` 를 하면 `qs` 모듈을 사용하고, `false` 면 `query-string` 모듈사용

- body-parser가 필요한 경우도 있음
  - JSON, URL-encoded 형식의 본문외에도 Raw, Text형식 본문을 해석가능하다.

```js
app.use(bodyParser.raw());
app.use(bodyParser.text());
```

<br>

## cookie-parser

요청에 동봉된 쿠키를 해석해준다.

```js
//app.js
//...
const cookieParser = require("cookie-parser");
//...
app.use(cookieParser());
//...
```

해석된 쿠키들은 `req.cookies`객체에 들어간다.

## static

`static`미들웨어는 정적인 파일들을 제공한다. 익스프레스를 설치하면 따라오므로 따로 설치할 필요없다.

```js
// app.js
//...
app.use(express.static(path.join(__dirname, "public")));
//...
```

함수 인자로 정적파일들이 담겨있는 폴더를 지정한다. 현재 `public`폴더가 지정되어있다.
public/stylesheets/styles.css는 http://localhost:3000/stylesheets/styles.css 로 접근할 수 있다.

보통 `morgan`다음에 배치한다. `static`미들웨어가 더 위에있으면 정적 파일 요청이 기록되지 않기 때문이다.

```js
//...
app.use(logger("dev"));
app.use(express.static(path.join(__dirname, "public")));
//...
```

## express-session

세션관리 미들웨어이다. 로그인 등의 세션을 구현할때 유용하다. 직접설치해야한다.

```
$ npm i express-session
```

```js
//app.js
//...
app.use(cookieParser("secret code"));
app.use(
  session({
    resave: false,
    saveUninitalized: false,
    secret: "secret code",
    cookie: {
      httpOnly: true,
      secure: false,
    },
  })
);
//...
```

- `resave`는 요청이 왔을때 세션에 수정사항이 생기지않아도 세션을 다시 저장할지에 대한 설정
- `saveUninitalized`는 세션에 저장할 내역에 없어도 세션을 다시 저장할지에 대한 설정. 보통 방문자 추적에 사용
- `secret`은 필수항목으로 cookie-parser의 비밀키 같은 역할. 쿠키를 안전하게 전송하려면 쿠키에 서명을 추가해야하고, 쿠키를 서명하는데 `secret`값이 필요
- `cookie`는 세션쿠키에 대한 설정이다. `maxAge, domain, path, expires, sameSite, httpOnly, secure`등 쿠키옵션이 모두 제공된다.

express-session은 `req`객체 안에 `req.session`객체를 만든다.

## connect-flash

일회성 메세지들을 웹 브라우저에 나타낼때 좋다.

```
$ npm i connect-flash
```

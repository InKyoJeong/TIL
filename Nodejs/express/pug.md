# 템플릿 엔진 Pug

```js
//...
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
//...
```

**_app.js_** 에 위의 코드부분이 들어있어야 한다.

- `views`는 템플릿파일들이 위치한 폴더를 지정한다. `res.render`메서드가 이폴더 기준 템플릿엔진을 찾아 렌더링한다. `res.render('index')`이면 _views/index.pug_ 를 렌더링한다.

- `view engine`은 어떤 종류의 템플릿엔진을 사용할지 나타낸다.

## HTML표현

탭 또는 스페이스로 태그의 부모자식관계를 정의한다. 탭한번 또는 스페이스두번이나 네번. 자식태그이면 한단계 들여쓰기 한다. 태그의 속성은 소괄호로 묶어서 적는다.

```pug
<!-- Pug -->
doctype html
html
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
```

```html
<!-- HTML -->
<!DOCTYPE html>
<html>
    <head>
        <title>타이틀<title>
        <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
</html>
```

- id와 class

```pug
<!-- Pug -->
#login-button
.profile-info
span#highlight
p.hidden.full
```

```html
<!-- HTML -->
<div id="login-button"></div>
<div class="profile-info"></div>
<span id="highlight"></span>
<p class="hidden full"></p>
```

- html 텍스트는 태그나 속성뒤에 한칸 띄고 입력한다.

```pug
<!-- Pug -->
p hello world
button(type='submit') 전송
```

```html
<!-- HTML -->
<p>hello world</p>
<button type="submit">전송</button>
```

- 에디터에서 여러줄 입력은 `|`를 사용

```pug
<!-- Pug -->
p
  | Hello
  | World
  br
  | 태그도 중간에 넣을수 있다.
```

```html
<!-- HTML -->
<p>Hello World<br />태그도 중간에 넣을수 있다.</p>
```

- `style`이나 `script`태그로 CSS나 JS코드를 넣으려면 태그뒤에 점`.`을 붙인다.

```pug
<!-- Pug -->
style.
  h1 {
    font-size: 10px;
  }
script.
  var message = "pug";
  alert(message);
```

```html
<!-- HTML -->
<style>
  h1 {
    font-size: 10px;
  }
</style>
<script>
  var message = "pug";
  alert(message);
</script>
```

## 변수

JS변수를 템플릿에 렌더링할 수 있다. `res.render`호출 시 보내는 변수를 Pug가 처리한다.

```js
// routes/index.js
router.get("/", function (req, res, next) {
  res.render("index", { title: "Express" });
});
```

`res.render(템플릿, 변수객체)`는 _index.pug_ 를 HTML로 렌더링하면서 `{ title: 'Express' }`라는 객체를 변수로 집어넣는다. _layout.pug_ 와 _index.pug_ 의 **title** 부분이 모두 **Express**로 치횐된다.

`res.render`메서드의 두번째 인자로 변수 객체를 넣는대신. **_app.js_** 의 에러 처리 미들웨어처럼 `res.locals`객체로 변수를 넣을 수도 있다.

```js
router.get("/", function (req, res, next) {
  res.locals.title = "Express";
  res.render("index");
});
```

이렇게하면 템플릿 엔진이 `res.locals`객체를 읽어서 변수를 집어넣는다. 이 방식은 현재 라우터 뿐만 아니라 다른 미들웨어에서도 `res.locals`객체에 접근할 수 있다는 장점이 있다.

```pug
<!-- Pug -->
h1= title
p Hello #{title}
button(class=title, type='submit') 전송
input(placeholder=title + ' 연습')
```

```html
<!-- HTML -->
<h1>Express</h1>
<p>Hello Express</p>
<button class="Express" type="submit">전송</button>
<input placeholder="Express 연습" />
```

서버로부터 받은 변수는 텍스트로 사용하려면 태그 뒤에 `=`를 붙인다. 속성에도 `=`를 붙이고 사용할 수 있다. 텍스트 중간에 변수를 넣으려면 `#{변수}`를 사용한다.

- 내부에 직접 변수를 선언할 수도 있다. `-`를 이용한다.

```pug
<!-- Pug -->
- var node = 'node.js'
- var js = 'javascript'
p #{node}와 #{js}
```

```html
<!-- HTML -->
<p>node.js와 javascript</p>
```

## 반복문

`each`나 `for`로 반복가능한 변수를 반복할 수 있다.

```pug
<!-- Pug -->
ul
  each fruit in ['사과', '배', '오렌지', '바나나', '복숭아']
    li= fruit
```

```html
<!-- HTML -->
<ul>
  <li>사과</li>
  <li>배</li>
  <li>오렌지</li>
  <li>바나나</li>
  <li>복숭아</li>
</ul>
```

- 인덱스도 가져올 수 있다.

```pug
<!-- Pug -->
ul
  each fruit, index in ['사과', '배', '오렌지', '바나나', '복숭아']
    li= (index + 1) + '번째 ' + fruit

<!-- HTML -->
<ul>
  <li>1번째 사과</li>
  <li>2번째 배</li>
  //...
```

## 조건문

`if`, `else if`, `else`이나 `case`문을 사용할 수 있다.

```pug
<!-- Pug -->
if isLogIn
  div 로그인 완료
else
  div 로그인 필요
```

```pug
<!-- Pug -->
case fruit
  when 'apple'
    p 사과입니다.
  when 'banana'
    p 바나나입니다
    //...
  default
    p 아무것도 아닙니다.
```

## include

> 다른 Pug나 HTML파일을 넣을 수 있다.

```pug
<!-- header.pug -->
header
  a(href='/') Home
  a(href='/about') About
```

```pug
<!-- footer.pug -->
footer
  div 푸터입니다
```

```pug
<!-- main.pug -->
include header
main
  h1 메인파일
  p 다른파일을 include할 수 있다.
include footer
```

## extends와 block

> 공통되는 레이아웃 부분을 따로 관리할 수 있다.

```pug
<!-- layout.pug -->
doctype html
html
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
    block style
  body
    header 헤더입니다.
    block content
    footer 푸터입니다.
    block javascript
```

```pug
<!-- body.pug -->
extends layout

block content
  main
    p 내용입니다.

block javascript
  script(src="/javascripts/main.js")
```

```html
<!-- HTML -->
<html>
  <head>
    <title>Express</title>
    <link rel="stylesheet" href="/stylesheets/style.css" />
  </head>
  <body>
    <header>헤더입니다.</header>
    <main>
      <p>내용입니다.</p>
    </main>
    <footer>푸터입니다.</footer>
    <script src="/javascripts/main.js"></script>
  </body>
</html>
```

페이지마다 달라지는 부분을 `block`으로 비워두고 `block`이 되는 파일에서는 `extends`키워드로 레이아웃 파일을 지정하고 `block`부분을 넣는다.

## Mixins

> 재사용가능한 블럭을 만든다.

- Pug

```pug
//- Declaration
mixin list
  ul
    li foo
    li bar
    li baz
//- Use
+list
+list
```

- HTML

```html
<ul>
  <li>foo</li>
  <li>bar</li>
  <li>baz</li>
</ul>
<ul>
  <li>foo</li>
  <li>bar</li>
  <li>baz</li>
</ul>
```

인자를 받을 수도 있다.

#### 예시1

```pug
mixin pet(name)
  li.pet= name
ul
  +pet('cat')
  +pet('dog')
  +pet('pig')
```

```html
<ul>
  <li class="pet">cat</li>
  <li class="pet">dog</li>
  <li class="pet">pig</li>
</ul>
```

#### 예시2

```pug
//- Declaration
mixin article(title='Default Title')
  .article
    .article-wrapper
      h1= title

//- Use
+article()

+article('Hello world')
```

```html
<div class="article">
  <div class="article-wrapper">
    <h1>Default Title</h1>
  </div>
</div>
<div class="article">
  <div class="article-wrapper">
    <h1>Hello world</h1>
  </div>
</div>
```

## 에러처리 미들웨어

```js
//app.js
//...
//에러핸들러
app.use(function (err, req, res, next) {
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  res.status(err.status || 500);
  res.render("error");
});
```

에러처리 미들웨어는 `error`라는 템플릿 파일을 렌더링한다. 렌더링 시 `res.locals.message`와 `res.locals.error`에 넣어준 값을 함께 렌더링한다.

`res.render`에 변수를 대입하는것 외에도 이렇게 `res.locals`속성에 값을 대입해 템플릿 엔진에 변수를 넣을 수 있다.

`error`객체는 시스템환경이 development인 경우만 표시. 배포환경인 경우 에러메세지가 표시되지 않는다.

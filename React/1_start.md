## 리액트란

- 어떤 데이터가 변할때마다 어떤 변화를 줄지 고민하는게 아니라, 기존 뷰를 날리고 처음부터 새로 렌더링하는 방식
- V(view)만 신경쓰는 라이브러리
- 컴포넌트(component) : 리액트에서 특정 부분이 어떻게 생길지 정하는 선언체
  - 재사용이 가능한 API로 수많은 기능 내장
- 렌더링 : 사용자 화면에 뷰를 보여주는 것
  - 리액트가 뷰를 어떻게 렌더링 하는가는 **초기 렌더링**과 **리렌더링**을 이해해야함

<br>

### 초기 렌더링

맨 처음 어떻게 보일지 정하는 초기 렌더링. 리액트에서는 `render`함수.

```js
render() {...}
```

- 이 함수는 컴포넌트가 어떻게 생겼는지 정의함
- `render`함수가 실행되면 그 내부의 컴포넌트들도 재귀적으로 렌더링함
- 최상위 컴포넌트 렌더링이 끝나면 HTML 마크업을 만들고, 실제 페이지의 DOM 요소 안에 주입함

<br>

### 조화 과정

- 리액트에서 뷰를 업데이트할때는 업데이트보다 조화 과정(reconciliation)이라는 표현이 더 정확함
- 뷰가 변형되는 것처럼 보이지만, 사실은 새로운 요소로 갈아끼우는것
- 컴포넌트는 업데이트한 값을 수정하는 것이 아니라, 새로운 데이터로 `render`함수를 다시 호출함
- `render`함수가 반환하는 결과를 바로 DOM에 반영하지 않고 이전에 `render`함수가 만든 컴포넌트와 현재 `render`함수가 만든 컴포넌트를 비교함
- 둘의 차이를 알아내 최적의 연산으로 업데이트함

<br>

## Virtual DOM

- 리액트의 주요특징 중 하나는 virtual DOM을 이용한다는 것
- DOM (Document Object Model)은 객체로 문서 구조를 표현하는 것
  - 웹 브라우저는 DOM을 활용해서 객체에 js나 css를 적용함
  - DOM은 트리 형태라서 특정 노드를 찾거나 수정,제거,삽입할 수 있음
- DOM을 조작할 떄마다 엔진이 웹페이지를 새로 그려서 너무 자주 업데이트가 발생시 성능 저하
- 리액트는 Virtual DOM 방식으로 DOM을 최소한으로 조작하여 효율적

#### 리액트에서 DOM을 업데이트하는 과정

1. 데이터를 업데이트하면 전체 UI를 Virtual DOM에 리랜더링함
2. 이전 Virtual DOM에 있던 내용과 현재 내용을 비교
3. 바뀐 부분만 실제 DOM에 적용함

<br>

## create-react-app

`create-react-app`은 리액트 프로젝트를 생성할때 필요한 웹팩, 바벨의 설치 및 설정을 생략하고 프로젝트 작업환경을 구축해준다.

```
$ yarn create react-app <프로젝트_이름>
```

#### cf) yarn 설치

> Home brew로 yarn 설치하기 (mac)

```
$ brew update
$ brew install yarn
$ yarn config set prefix ~/.yarn
$ echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.zshrc
```

기본 쉘이 _zsh_ 이면 (echo \$SHELL 해보면 /bin/zsh)

```
$ echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.bash_profile
```

대신에 `/.zshrc`로 설정한다.

<br>

### src/App.js

```js
import React from "react";
```

- 리액트를 불러와서 사용할 수 있게 한다. (`node_modules`에 react모듈이 설치됨)
- 모듈을 불러오는것은 브라우저에 없는 기능인데, 브라우저에서도 사용하기 위해 번들러를 사용한다.
- 번들러는 모듈을 모두 합쳐 하나의 파일을 생성해준다. 웹팩, Parcel 등이 있다.
- 파일들을 불러오는 것은 **로더(loader)** 가 해준다.
  - `css-loader` : css파일을 불러오게함
  - `file-loader` : 웹폰트, 미디어파일 등을 불러오게함
  - `babel-loader` : 최신코드를 es5문법으로 변환해줌 (구버전 웹브라우저와 호환을 위함)
- `create-react-app` 으로 프로젝트를 만들 경우에는 별도 설정이 필요없다.

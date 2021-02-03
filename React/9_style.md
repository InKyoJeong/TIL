## 리액트 컴포넌트 스타일링

- 컴포넌트 스타일링에 정해진 방식은 없음
- 스타일링 방식들
  - 일반 CSS
  - Sass
  - CSS Module
  - styled-components

## Sass

> Sass를 사용하려면 라이브러리 설치

```
$ yarn add node-sass
```

- Sass를 CSS로 변환해줌

### 변수 사용하기

```css
$red: #fa5252;
```

```css
background: $red;
```

### mixin 사용하기

```css
@mixin square($size) {
  $calculated: 32px * $size;
  width: $calculated;
  height: $calculated;
}
```

```css
&.red {
  @include square(1);
}
```

### scss 불러오기

> 다른 scss 불러올때는 @import

```css
@import "./styles/utils";
```

<br>

### sass-loader

- `@import './../../styles/utils` 와 같이 파일 구조가 깊어지면 웹팩의 `sass-loader`의 설정을 커스터마이징해서 해결할 수 있음
- 커스터마이징하려면 먼저 기본적으로 Git 설정되어있기 때문에 Git에 커밋하고 `yarn eject` 해야함

```
$ git add .
$ git commit -m "Commit before yarn eject"
$ yarn eject
```

- webpack.config.js 파일이 생기면 `Ctrl+F`로 `sassRegex`를 찾아 수정

```js
//webpack.config.js
{
    test: sassRegex,
    exclude: sassModuleRegex,
    use: getStyleLoaders(
    {
        importLoaders: 3,
        sourceMap: isEnvProduction && shouldUseSourceMap,
    },
    'sass-loader'
    ),
    sideEffects: true,
},

```

```js
//webpack.config.js

//...
            {
              test: sassRegex,
              exclude: sassModuleRegex,
              use: getStyleLoaders({
                importLoaders: 3,
                sourceMap: isEnvProduction && shouldUseSourceMap,
              }).concat({
                loader: require.resolve("sass-loader"),
                options: {
                  sassOptions: {
                    includePaths: [paths.appSrc + "/styles"],
                  },
                  sourceMap: isEnvProduction && shouldUseSourceMap,
                },
              }),
              // Don't consider CSS imports dead code even if the
              // containing package claims to have no side effects.
              // Remove this when webpack adds a warning or an error for this.
              // See https://github.com/webpack/webpack/issues/6571
              sideEffects: true,
            },
```

이제 `@import "utils.scss"` 로 수정해도 적용됨

<br>

### node_modules에서 라이브러리 불러오기

- yarn으로 설치한 라이브러리 불러오기

```css
@import "../../../node_modules/library/styles";
```

- 물결문자 `~`를 사용하면 간단하게 가능

```css
@import "~library/styles";
```

<br>

## CSS Module

- 컴포넌트 스타일 클래스 이름이 중첩되는것을 방지해줌
- 고유 클래스를 사용하려면 `className={styles.[클래스이름]}`을 사용하고, `:global`로 전역으로 선언한 클래스는 기존처럼 문자열로 넣음

```js
import React from "react";
import styles from "./CSSModule.module.css";

const CSSModule = () => {
  return (
    <div className={styles.wrapper}>
      Hi, I'm
      <span className="something"> CSS Module!</span>
    </div>
  );
};
export default CSSModule;
```

```css
/* CSSModule.module.css */
.wrapper {
  background: black;
  padding: 1rem;
  color: white;
  font-size: 2rem;
}

:global .something {
  font-weight: 600;
  color: aqua;
}
```

<br>

- CSS Module을 이용한 클래스 이름 두개이상일때는 **템플릿 리터럴**사용

```js
const CSSModule = () => {
  return (
    <div className={`${styles.wrapper} ${styles.border}`}>

// className={[styles.wrapper, styles.border].join('')} 와 같음
// ...
```

```css
.wrapper {
  background: black;
  padding: 1rem;
  color: white;
  font-size: 2rem;
}

.border {
  color: black;
  background-color: blue;
  border: 2px solid red;
}
```

<br>

## styled-components

- 자바스크립트 파일 안에 스타일 선언하는 방식 (CSS-in-JS)

```
$ yarn add styled-components
```

### 사용방식

- `styled.태그명`

```js
const MyComponent = styled.div`
  font-size: 10px;
`;
```

- 컴포넌트 자체에 스타일링

```js
const StyledLink = styled(Link)`
  color: red;
`;
```

- 스타일에서 props 조회

```js
const Box = styled.div`
  background: ${(props) => props.color || "red"};
  padding: 1rem;
  display: flex;
`;
```

`props`를 조회해서 `props.color`값을 사용하고, 값이 주어지지않으면 `red`를 사용

```js
<Box color="black">...</Box>
```

<br>

### props 조건부 스타일링

```js
import styled, { css } from "styled-components";

const Button = styled.button`
  background: white;
  color: black;
  padding: 0.5rem;
  //(생략)

  /* inverted 값이 true일때 특정 스타일 부여 */
  ${(props) =>
    props.inverted &&
    css`
      background: none;
      color: white;
    `};
`;

// ...

<Button inverted={true}>테두리</Button>;
```

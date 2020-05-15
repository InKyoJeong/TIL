# Sass

> CSS pre-processor로서, 코드의 재활용성과 가독성을 높여주어 유지보수를 쉽게해준다.

주로 Node.js 환경에서 작업을 할때 [node-sass](https://www.npmjs.com/package/node-sass)를 이용한다.

# SCSS

기존의 Sass는 `{}`대신 들여쓰기를 사용하였으며 세미콜론(`;`)을 사용하지 않는 문법이였다. Sass버전 3 이상부터는 주 문법이 `.scss` 로 변경되었다.

<br>

## Variables (변수)

Sass는 `$`기호를 이용하여 재사용 가능한 변수를 만들 수 있다.

- SCSS

```scss
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

- CSS

```css
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}
```

<br>

## Nesting (중첩)

- SCSS

```scss
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li {
    display: inline-block;
  }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}
```

- CSS

```css
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
```

<br>

## Parent Selector (부모선택자)

> **_parent selector_** `&`는 **_nested selector_** 에서 사용된다.

내부선택자에서 부모선택자가 사용되면 해당 외부선택자로 대체된다.

- SCSS

```scss
.alert {
  &:hover {
    font-weight: bold;
  }
}
```

- CSS

```css
.alert:hover {
  font-weight: bold;
}
```

<br>

### Adding Suffixes (접미사 추가)

부모선택자를 사용하여 외부선택자에 접미사를 추가할 수도 있다. [BEM](http://getbem.com/) 방법론 등을 사용할 때 유용하다.

- SCSS

```scss
.accordion {
  max-width: 600px;
  margin: 4rem auto;
  width: 90%;
  font-family: "Raleway", sans-serif;
  background: #f4f4f4;

  &__copy {
    display: none;
    padding: 1rem 1.5rem 2rem 1.5rem;
    color: gray;
    line-height: 1.6;
    font-size: 14px;
    font-weight: 500;

    &--open {
      display: block;
    }
  }
}
```

- CSS

```css
.accordion {
  max-width: 600px;
  margin: 4rem auto;
  width: 90%;
  font-family: "Raleway", sans-serif;
  background: #f4f4f4;
}
.accordion__copy {
  display: none;
  padding: 1rem 1.5rem 2rem 1.5rem;
  color: gray;
  line-height: 1.6;
  font-size: 14px;
  font-weight: 500;
}
.accordion__copy--open {
  display: block;
}
```

<br>

## Partials

Partial은 `_partial.scss`처럼 밑줄이 붙은 Sass파일이다. CSS를 모듈화하고 쉽게 ​​유지보수할 수 있다. `@use`와 함께 사용된다.

<br>

## Modules

모든 Sass를 하나의 파일로 작성할 필요는 없다. `@use`를 사용하여 분할할 수 있다. `@use`는 다른 Sass 파일을 모듈로 로드하므로 변수, mixin, 함수를 참조할 수 있다.

```scss
// _base.scss
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

```scss
// styles.scss
@use 'base'; //확장자명을 쓰지않아도 된다.

.inverse {
  background-color: base.$primary-color;
  color: white;
}
```

- CSS

```css
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}

.inverse {
  background-color: #333;
  color: white;
}
```

<br>

## Reference

[https://sass-lang.com/guide](https://sass-lang.com/guide)

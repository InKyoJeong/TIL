## CSS 선택자(Selector)에서 '+', '>', '~'

```html
<div id="container">
  <p>First</p>
  <div>
    <p>Child Paragraph</p>
  </div>
  <p>Second</p>
  <p>Third</p>
</div>
```

### 1. space

```css
div#container p {
  font-weight: bold;
}
```

위의경우 `container div`안의 모든 `p`태그가 해당된다.

<br>

### 2. >

> 특정 요소의 DIRECT children

```css
div#container > p {
  border: 1px solid black;
}
```

![selector](./images/selector.jpg)

위의 경우 `container div`의 **_direct children_** 들이 해당된다. (`div`의 children은 아님)

<br>

### 3. +

> 인접 선택자로 부르는 선택자. 앞의 요소 바로 뒤에 있는 요소만 선택한다.

```css
div + p {
  color: green;
}
```

![selector2](./images/selector2.jpg)

위의 경우 `div` 바로 다음의 `<p>Second</p>`만 해당한다.

<br>

### 4. ~

> 이 형제 선택자는 '+' 와 유사하지만 덜 엄격하다. 인접 선택자 '+'는 앞의 선택자 바로 뒤에 오는 첫 번째 요소만을 선택하지만, 이 선택자는 모든 요소를 선택한다.

```css
div ~ p {
  background-color: blue;
}
```

![selector3](./images/selector3.jpg)

<br>

### Reference

[https://techbrij.com/css-selector-adjacent-child-sibling](https://techbrij.com/css-selector-adjacent-child-sibling)

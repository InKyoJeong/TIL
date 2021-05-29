## React Style

## CSS classes dynamically

```jsx
<div className={`form-control ${!isValid ? "invalid" : ""}`}>
```

```css
.form-control.invalid input {
  border-color: red;
}
```

<br>

## Styled Components & Dynamic Props

```
$ npm install --save styled-components
```

```js
const FormControl = styled.div`
  margin: 0.5rem 0;

  & label {
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
    color: ${(props) => (props.invalid ? "red" : "black")};
  }

  & input {
    display: block;
    width: 100%;
    border: 1px solid ${(props) => (props.isValid ? "red" : "#ccc")};
    background: ${(props) => (props.invalid ? "#ffd7d7" : "transparent")};
    font: inherit;
    line-height: 1.5rem;
    padding: 0 0.25rem;
  }
`;

// 생략

return (
  <form onSubmit={formSubmitHandler}>
    <FormControl invalid={!isValid}>
      <label>Course Goal</label>
      <input type="text" onChange={goalInputChangeHandler} />
    </FormControl>
    <Button type="submit">Add Goal</Button>
  </form>
);
```

<br>

## CSS Module

- newly generated class name

```js
import styles from "./Button.module.css";

const Button = (props) => {
  return (
    <button type={props.type} className={styles.button} onClick={props.onClick}>
      {props.children}
    </button>
  );
};
```

<br>

#### Dynamic Styles with CSS Modules

- className이 `.form-control`일 경우 `styles.form-control`이 아니라

```js
<div className={styles["form-control"]}>...</div>
```

- Dynamic class

```js
<div className={`${styles["form-control"]} ${!isValid && styles.invalid}`}>
  ...
</div>
```

```css
//...

.form-control.invalid input {
  border-color: red;
}

.form-control.invalid label {
  color: red;
}
```

#### media query

```css
//...

.button:focus {
  outline: none;
}

.button:hover,
.button:active {
  background: #ac0e77;
  border-color: #ac0e77;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.26);
}

@media (min-width: 768px) {
  .button {
    width: auto;
  }
}
// styled component와 다르게 class명 써야함
```

<br>

## Modal with React Portal

- index.html

```html
//...생략
<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="overlays"></div>
  <div id="root"></div>

  //...생략
</body>
```

- Modal.js

```js
const portalElement = document.getElementById("overlays");

const Modal = (props) => {
  return (
    <Fragment>
      {ReactDOM.createPortal(<Backdrop />, portalElement)}
      {ReactDOM.createPortal(
        <ModalOverlay>{props.childeren}</ModalOverlay>,
        portalElement
      )}
    </Fragment>
  );
};

export default Modal;
```

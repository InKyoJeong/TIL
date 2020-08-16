## ref

> HTML에서 id를 이용해서 DOM에 이름을 다는 것처럼 리액트 프로젝트 내부에서 DOM에 이름을 다는 개념

- DOM을 직접 조작할때 사용
  - state 만으로 해결할수 없는 기능들도 있음
    - 특정 input에 포커스 적용
    - 스크롤박스 조작
    - Canvas 요소에 그림그리기 등
- 쓰는 이유
  - `id`를 사용할 수는 있지만, 같은 컴포넌트를 여러번 사용할 경우 유일해야하는 `id` 중복이 발생가능
  <!-- ## 클래스형 컴포넌트에서 ref -->

### ref 사용

#### 콜백함수를 통한 ref 설정

- ref를 달 요소에 ref라는 콜백함수를 `props`로 전달함

```html
<input ref={(ref) => {this.input=ref}} />
```

- 버튼 눌렀을때 포커스가 다시 input으로 넘어가게하기

```js
import React, { Component } from "react";
import "./ValidationSample.css";

class ValidationSample extends Component {
  state = {
    password: "",
    clicked: false,
    validated: false,
  };

  handleChange = (e) => {
    this.setState({
      password: e.target.value,
    });
  };

  handleButtonClick = () => {
    this.setState({
      clicked: true,
      validated: this.state.password === "0000",
    });
    this.input.focus();
  };

  render() {
    return (
      <div>
        <input
          ref={(ref) => (this.input = ref)}
          type="password"
          value={this.state.password}
          onChange={this.handleChange}
          className={
            this.state.clicked
              ? this.state.validated
                ? "success"
                : "fail"
              : ""
          }
        />
        <button onClick={this.handleButtonClick}>확인</button>
      </div>
    );
  }
}

export default ValidationSample;

// className은 누르기전 비어있는 문자열이고 누른후에는 검증후 sucess또는 fail 설정
```

#### createRef

- 리액트 내장 함수 `createRef`를 사용
  - 컴포넌트 내부에서 `React.createRef()`를 담고 해당 멤버 변수를 `ref`를 달 요소에 `ref props`로 넣으면됨
  - 나중에 `ref`를 설정한 DOM에 접근하려면 `this.input.current`를 조회

```js
import React, { Component } from "react";

class RefExample extends Component {
  input = React.createRef();

  handleFocus = () => {
    this.input.current.focus();
  };

  render() {
    return (
      <div>
        <input ref={this.input} />
      </div>
    );
  }
}

export default RefExample;
```

<br>

### 컴포넌트에 ref 달기

- 컴포넌트에 `ref`를 달수 있음
- 컴포넌트 내부에있는 DOM을 컴포넌트 외부에서 쓸때 사용

```js
<NewComponent
  ref={(ref) => {
    this.newComponent = ref;
  }}
/>
```

<!--
#### 컴포넌트에 메서드 생성

- `scrollTop` : 세로 스크롤바 위치
- `scrollHeight` : 스크롤이 있는 박스 안의 div 높이
- `clientHeight` : 스크롤이 있는 박스의 높이 -->

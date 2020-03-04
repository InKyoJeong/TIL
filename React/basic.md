> [velopert - 누구든지 하는 리액트](https://velopert.com/) 를 읽고 정리한 글입니다.

## JSX

### 감싸져 있는 엘리먼트

> 두개 이상의 엘리먼트는 무조건 하나의 엘리먼트로 감싸져있어야 함

단순히 감싸기 위해서 새로운 `div` 를 사용하는 것은 스타일 관련 설정을 하면서 코드가 꼬이게 될 수도 있고, table 관련 태그를 작성 할 때 번거로워질 수도 있다. 그럴경우 `Fragment`를 사용한다. (v16.2 에 도입됨)

```js
import React, { Component, Fragment } from "react";

class App extends Component {
  render() {
    return (
      <Fragment>
        <div>Hello</div>
        <div>Bye</div>
      </Fragment>
    );
  }
}

export default App;
```

### JSX 안에 자바스크립트 값 사용하기

> JSX 내부에서 자바스크립트 값을 사용 할 땐 이렇게 할 수 있다.

```js
import React, { Component } from "react";

class App extends Component {
  render() {
    const name = "react";
    return <div>hello {name}!</div>;
  }
}

export default App;
```

### 조건부 렌더링

> JSX 내부에서 조건부 렌더링을 할 때는 보통 **삼항 연산자**를 사용하거나, AND 연산자를 사용. if문을 쓸수 없다.

```js
import React, { Component } from "react";

class App extends Component {
  render() {
    return <div>{1 + 1 === 2 ? <div>맞아요!</div> : <div>틀려요!</div>}</div>;
  }
}

export default App;
```

## props와 state

props 는 부모 컴포넌트가 자식 컴포넌트에게 주는 값. 자식 컴포넌트에서는 props 를 받아오기만하고, 받아온 props 를 직접 수정 할 수 는 없다.

반면 state 는 컴포넌트 내부에서 선언하며 내부에서 값을 변경 할 수 있다.

### 컴포넌트 만들기

> 받아온 props 값은 this. 키워드를 통하여 조회 할 수 있다.

```js
//MyName.js
import React, { Component } from "react";

class MyName extends Component {
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

export default MyName;
```

```js
//App.js
import React, { Component } from "react";
import MyName from "./MyName";

class App extends Component {
  render() {
    return <MyName name="리액트" />;
  }
}

export default App;
```

### defaultProps

가끔씩은 실수로 `props` 를 빠트려먹을때가 있다. 혹은, 특정 상황에 props 를 일부러 비워야 할 때도 있다. 그러한 경우에, props 의 기본값을 설정해줄 수 있는데, 그것이 바로 `defaultProps`이다.

```js
import React, { Component } from "react";

class MyName extends Component {
  static defaultProps = {
    name: "기본이름"
  };
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

export default MyName;
```

이렇게 하면 만약에 `<MyName />` 이런식으로 name 값을 생략해버리면 `“기본이름”` 이 나타난다. `defaultProps` 는 다음과 같은 형태로도 설정 할 수 있다.

```js
import React, { Component } from "react";

class MyName extends Component {
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

MyName.defaultProps = {
  name: "기본이름"
};

export default MyName;
```

### 함수형 컴포넌트

props 만 받아와서 보여주기만 하는 컴포넌트의 경우엔 더 간편한 문법으로 작성할 수 있는 방법이 있다. 바로, 함수형태로 작성하는 것. `MyName`컴포넌트를 다시작성해보면

```js
import React from "react";

const MyName = ({ name }) => {
  return <div>안녕하세요! 제 이름은 {name} 입니다.</div>;
};

export default MyName;
```

함수형 컴포넌트와 클래스형 컴포넌트의 주요 차이점은, `state` 와 `LifeCycle` 이 빠져있다는 점이다.

### state

동적인 데이터를 다룰 땐 `state` 를 사용한다.

```js
//Counter.js
import React, { Component } from "react";

class Counter extends Component {
  state = {
    number: 0
  };

  handleIncrease = () => {
    this.setState({
      number: this.state.number + 1
    });
  };

  handleDecrease = () => {
    this.setState({
      number: this.state.number - 1
    });
  };

  render() {
    return (
      <div>
        <h1>카운터</h1>
        <div>값: {this.state.number}</div>
        <button onClick={this.handleIncrease}>+</button>
        <button onClick={this.handleDecrease}>-</button>
      </div>
    );
  }
}

export default Counter;
```

`state`는 내부에서 변경할 수 있다. 변경할 때는 어제나 `setState`함수를 사용한다.

```js
 handleIncrease() {
    this.setState({
      number: this.state.number + 1
    });
  }

  handleDecrease() {
    this.setState({
      number: this.state.number - 1
    });
  }
```

이렇게 하면, 나중에 버튼에서 클릭이벤트가 발생 했을 때, `this` 가 `undefined` 로 나타나서 제대로 처리되지 않게 된다. 이는 함수가 버튼의 클릭이벤트로 전달이 되는 과정에서 `this` 와의 연결이 끊겨버리기 때문인데, 이를 고쳐주려면 `constructor` 에서

```js
constructor(props) {
super(props);
this.handleIncrease = this.handleIncrease.bind(this);
this.handleDecrease = this.handleDecrease.bind(this);
}
```

처럼 해주거나, 이전에 작성한 코드처럼 아예 화살표 함수 형태로 하면 this 가 풀리지 않는다.

## LifeCycle API

> 이 API 는 컴포넌트가 브라우저에서 나타날때, 사라질때, 그리고 업데이트 될 때, 호출되는 API 이다.

### 컴포넌트 초기 생성

일단, 컴포넌트가 브라우저에 나타나기 전, 후에 호출되는 API 들이 있다.

#### constructor

```js
constructor(props) {
super(props);
}
```

이 부분은 컴포넌트 생성자 함수다. 컴포넌트가 새로 만들어질 때마다 이 함수가 호출된다.

#### componentWillMount

```js
componentWillMount() {

}
```

이 API 는 컴포넌트가 화면에 나타나기 직전에 호출되는 API. , 이 API 에 대해선 별로 신경쓰지 않아도 된다. 원래는 주로 브라우저가 아닌 환경에서 (서버사이드)도 호출하는 용도로 사용했었는데, 이 API 가 더 이상 필요하지 않게 되어 리액트 v16.3 에서는 해당 API 가 deprecated 되었으니, 옛날엔 이러한 API가 사용됐었구나 하고 알아만 두자. v16.3 이후부터는 `UNSAFE_componentWillMount()` 라는 이름으로 사용된다. 기존에 이 API 에서 하던 것들은 위에 있는 `constructor` 와 아래의 `componentDidMount` 에서 충분히 처리 할 수 있다.

#### componentDidMount

```js
componentDidMount() {
  // 외부 라이브러리 연동: D3, masonry, etc
  // 컴포넌트에서 필요한 데이터 요청: Ajax, GraphQL, etc
  // DOM 에 관련된 작업: 스크롤 설정, 크기 읽어오기 등
}
```

이 API 는 컴포넌트가 화면에 나타나게 됐을 때 호출된다. 여기선 주로 D3, masonry 처럼 DOM 을 사용해야하는 외부 라이브러리 연동을 하거나, 해당 컴포넌트에서 필요로하는 데이터를 요청하기 위해 axios, fetch 등을 통하여 ajax 요청을 하거나, DOM 의 속성을 읽거나 직접 변경하는 작업을 진행한다.

### 컴포넌트 업데이트

컴포넌트가 업데이트는 props 의 변화, 그리고 state 의 변화에 따라 결정된다. 업데이트가 되기 전과 그리고 된 후에 어떠한 API 가 호출 되는지 살펴보자.

#### componentWillReceiveProps

```js
componentWillReceiveProps(nextProps) {
  // this.props 는 아직 바뀌지 않은 상태
}
```

이 API 는 컴포넌트가 새로운 props 를 받게됐을 때 호출됨. 이 안에서는 주로, `state` 가 `props` 에 따라 변해야 하는 로직을 작성한다. 새로 받게될 props 는 nextProps 로 조회 할 수 있으며, 이 때 this.props 를 조회하면 업데이트 되기 전의 API이다. 이 API 또한 v16.3 부터 deprecate 됨. v16.3 부터는 `UNSAFE_componentWillReceiveProps()` 라는 이름으로 사용

#### static getDerivedStateFromProps()

이 함수는, v16.3 이후에 만들어진 라이프사이클 API이다. props 로 받아온 값을 state 로 동기화 하는 작업을 해줘야 하는 경우에 사용

```js
static getDerivedStateFromProps(nextProps, prevState) {
  // 여기서는 setState 를 하는 것이 아니라
  // 특정 props 가 바뀔 때 설정하고 설정하고 싶은 state 값을 리턴하는 형태로
  // 사용됩니다.
  /*
  if (nextProps.value !== prevState.value) {
    return { value: nextProps.value };
  }
  return null; // null 을 리턴하면 따로 업데이트 할 것은 없다라는 의미
  */
}
```

#### shouldComponentUpdate

```js
shouldComponentUpdate(nextProps, nextState) {
  // return false 하면 업데이트를 안함
  // return this.props.checked !== nextProps.checked
  return true;
}
```

이 API 는 컴포넌트를 최적화하는 작업에서 매우 유용하게 사용된다. 리액트에서는 변화가 발생하는 부분만 업데이트를 해줘서 성능이 잘나오는데, 변화가 발생한 부분만 감지해내기 위해서는 Virtual DOM 에 한번 그려줘야한다.

즉, 현재 컴포넌트의 상태가 업데이트되지 않아도, 부모 컴포넌트가 리렌더링되면, 자식 컴포넌트들도 렌더링 된다. 여기서 `렌더링` 된다는건, `render()` 함수가 호출된다는 의미입니다.

변화가 없으면 물론 DOM 조작은 하지 않게 된다. 그저 `Virutal DOM` 에만 렌더링 할 뿐이다. 이 작업은 그렇게 부하가 많은 작업은 아니지만, 컴포넌트가 무수히 많이 렌더링된다면 CPU 자원을 어느정도 사용하고 있는 것이기 때문에 낭비되고 있는 이 CPU 처리량을 줄여주기 위해서 Virtual DOM 에 리렌더링 하는것도,불필요할경우엔 방지하기 위해서 `shouldComponentUpdate` 를 작성한다.

이 함수는 기본적으로 `true` 를 반환한다. 우리가 따로 작성을 해주어서 조건에 따라 false 를 반환하면 해당 조건에는 render 함수를 호출하지 않습니다.

#### componentDidUpdate

```js
componentDidUpdate(prevProps, prevState, snapshot) {

}
```

이 API는 컴포넌트에서 `render()` 를 호출하고난 다음에 발생한다. 이 시점에선 this.props 와 this.state 가 바뀌어있다. 그리고 파라미터를 통해 이전의 값인 prevProps 와 prevState 를 조회 할 수 있다. 그리고, getSnapshotBeforeUpdate 에서 반환한 snapshot 값은 세번째 값으로 받아온다.

### 컴포넌트 제거

컴포넌트가 더 이상 필요하지 않게 되면 단 하나의 API 가 호출된다.

#### componentWillUnmount

```js
componentWillUnmount() {
  // 이벤트, setTimeout, 외부 라이브러리 인스턴스 제거
}
```

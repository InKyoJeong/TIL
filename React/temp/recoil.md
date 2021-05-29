## Recoil 이란

Facebook 에서 만든 React 상태 관리 라이브러리

## React 에서의 상태 관리

- 복잡한 React 웹 앱에서는 상태 관리가 개발자의 주요 과제이자 어려운 작업
- 어떤 상태 변경이 하나이상의 다른 컴포넌트에 영향을 끼칠 수 있기 때문
- 예를 들어, 인스타그램을 클론한다고 하면 '좋아요' 동작을 취하는 순간
  - 해당 사진의 좋아요 개수 1증가
  - 해당 사진을 업로드한 유저에게 알림 보내기
  - 해당 사진에 좋아요 누른 유저 기록
- 이런 식으로 하나의 변경이 단순히 하나의 변경으로 끝나지 않아서, **Redux, MobX** 와 같은 상태 관리 라이브러리가 등장함

<br>

## Recoil의 등장 배경

- Redux와 MobX의 API는 단순하지 않고, 근본적으로 React에서 사용하기 위해 나온 것이 아님
- 그래서 Recoil 개발자들은 API와 동작 방식을 가능한 React 스럽게 가져가면서 현상을 해결하려고 Recoil을 제작

<br>

## 핵심 개념

- **Atom** 으로 부터 시작해서 **Selector** 를 거쳐 React 컴포넌트까지 전달되는 하나의 Data-Flow Graph를 만들게함

- **Atom** 은 컴포넌트들이 구독(subscribe)할 수 있는 단위이고, **Selector** 는 동기적 혹은 비동기적으로 상태를 변환

<br>

### Atom

- Atom은 상태의 단위.
- Atom이 업데이트되면 해당 Atom을 구독하고 있던 모든 컴포넌트들이 새로운 값으로 리렌더됨
- 또 여러 컴포넌트에서 같은 Atom을 구독하고 있으면 그 컴포넌트들이 상태를 동일하게 공유함

### Selector

- Selector는 다른 Atom들 혹은 Selector들을 받아 사용하는 순수 함수
- 받은 Atom들 혹은 Selector들 중 어떤 것이 업데이트되면, Selector 함수는 다시 평가(re-evaluate)됨
- Atom처럼 컴포넌트에서 구독할 수 있으며, Selector 함수가 다시 평가될 때 컴포넌트가 리렌더됨

<br>

### reference

- [Recoil 알아보기 — 1편](https://medium.com/humanscape-tech/recoil-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-285b29135d8e)
- [recoiljs.org/docs/introduction/getting-started](https://recoiljs.org/docs/introduction/getting-started)

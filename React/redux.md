## Redux vs React Context API

### 📌Contents

- Redux란 무엇인가?
- Context API란 무엇인가
- React의 Context API가 Redux를 대체할까?

---

### Redux란 무엇인가?

<hr/>

Redux는 중앙에서 React 앱의 상태를 관리하는 데 사용된다. "상태(State)"는 사용자 인터페이스를 올바르게 렌더링하는 데 필요한 데이터를 나타낸다. 예시는 다음과 같다:

- 장바구니의 제품
- 사용자가 HTTP요청이 완료되기를 기다리고 있는지에 대한 정보

Redux는 React에 기술적으로 종속되는 라이브러리가 아니고, 다른 기술에서도 사용되지만 Redux는 특히 React에서 많이 사용된다.

Redux는 4개의 주요 빌딩 블록으로 구성된다.

1. 직접 액세스하거나 변경할 수 없는 **단일 중앙 집중식 상태**(single, centralized state). 즉, 전역객체(global JS object)라고 말할 수 있다.
2. 전역 상태를 변경하고 업데이트하는 로직이 포함된 **리듀서(Reducer)함수**. (필요한 모든 변경 사항과 함께 이전 상태의 새 복사본을 반환해서)
3. 리듀서 함수가 실행되도록 트리거 하기 위해 디스패치(dispatch)될 수 있는 **액션(Action)**
4. 전역 상태에서 데이터를 가져오기 위한 구독(Subscriptions)

![redux](./images/redux.jpg)

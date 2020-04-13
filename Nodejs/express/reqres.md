## 라우트 요청(req), 응답(res) 객체

- 요청 객체 (request)

  - **req.params** : 주소에 포함된 변수를 담는다. `:id`이면 `req.params.id` 로, `:type`이면 `req.params.type` 으로 조회할 수 있다.
  - **req.query** : GET 방식으로 넘어오는 쿼리스트링 파라미터를 담고 있다. 쿼리스트링의 키-값 정보. 주소 바깥 `?` 이후의 변수를 담는다.

  > 예를들어 _/users/123?limit=5&skip=11_ 이라는 주소의 요청이 들어왔을때 **req.params**와 **req.query**객체는 다음과 같다. `{ id: '123'} { limit: '5', skip: '11'}`

  - **req.body** : POST 방식으로 넘어오는 파라미터를 담고 있다. HTTP의 BODY 부분에 담겨져있는데, 이 부분을 파싱하기 위해 _body-parser_ 와 같은 패키지가 필요하다. (express 4.16부터는 body-parser를 따로 임포트하지 않아도 된다.)

  > 예를들어 JSON 형식으로 `{ name: 'mary', book: 'nodejs' }` 를 본문으로 보낸다면 req.body에 그대로 들어간다. URL-encoded 형식으로 _name=mary&book=nodejs_ 를 본문으로 보낸다면 req.body에 `{ name: 'mary', book: 'nodejs' }` 가 들어간다.

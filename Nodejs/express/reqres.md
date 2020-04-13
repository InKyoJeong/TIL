# 라우트 요청(req), 응답(res) 객체

## 요청 객체 (request)

- **req.params** : 주소에 포함된 변수를 담는다. `:id`이면 `req.params.id` 로, `:type`이면 `req.params.type` 으로 조회할 수 있다.
- **req.query** : GET 방식으로 넘어오는 쿼리스트링 파라미터를 담고 있다. 쿼리스트링의 키-값 정보. 주소 바깥 `?` 이후의 변수를 담는다.

  - 예를들어 _/users/123?limit=5&skip=11_ 이라는 주소의 요청이 들어왔을때 **req.params**와 **req.query**객체는 다음과 같다. `{ id: '123'} { limit: '5', skip: '11'}`

- **req.body** : POST 방식으로 넘어오는 파라미터를 담고 있다. HTTP의 BODY 부분에 담겨져있는데, 이 부분을 파싱하기 위해 _body-parser_ 와 같은 패키지가 필요하다. (express 4.16부터는 body-parser를 따로 임포트하지 않아도 된다.)

  - 예를들어 JSON 형식으로 `{ name: 'mary', book: 'nodejs' }` 를 본문으로 보낸다면 req.body에 그대로 들어간다. URL-encoded 형식으로 _name=mary&book=nodejs_ 를 본문으로 보낸다면 req.body에 `{ name: 'mary', book: 'nodejs' }` 가 들어간다.

- **req.cookies** : 클라이언트가 전달한 쿠키 값을 가진다. 예를들어 _name=mary_ 쿠키를 보냈다면 req.cookies는 `{ name: 'mary' }`가 된다.

## 응답 객체 (response)

- **res.render** : jade, pug 같은 템플릿 엔진을 사용하여 뷰를 렌더링한다.
- **res.send(버퍼 또는 문자열 또는 HTML또는 JSON)** : 클라이언트에 응답을 보낸다.
- **res.sendFile(파일경로)** : 파일을 응답으로 보내준다.
- **res.redirect(주소)** : 응답을 다른 라우터로 보냄. 예를 들어 로그인 완료 후 다시 메인화면으로 돌릴때 res.redirect(메인주소)를 하면 된다.
- **res.json** : 클라이언트로 JSON 값을 보낸다.
- **res.status(code)** : HTTP 응답 코드를 설정한다. 응답 코드가 redirect(30x)라면 res.redirect를 쓰는게 낫다.
  - 기본적으로는 200 HTTP 상태코드를 응답하지만 (res.redirect는 302), 직접 바꿀수도 있다. status메서드를 먼저 사용하면 된다. `res.status(404).send('Not Found')`

## 인터넷 리소스 탐색

- URI(통합 자원 식별자, Uniform Resource Identifier)는 두가지 부분집합으로 구성됨
  - URN : 현재 그 리소스가 어디에 존재하든 이름만으로 리소스를 식별함
  - URL : 리소스가 어딨는지 설명해서 리소스를 식별함
- 대부분의 URL은 `스킴://서버위치/경로` 구조
- 예를들어, `http://www.naver.com/seasonal/index-fall.html` 이라는 URL을 불러올때
  - `http`는 URL의 `스킴`. 스킴은 웹 클라이언트가 리소스에 어떻게 접근하는지 알려줌. 이 경우 HTTP프로토콜 사용
  - `www.naver.com`은 `서버의 위치`. 웹 클라이언트가 리소스가 어디에 호스팅되어 있는지 알려줌
  - `/seasonal/index-fall.html`은 `리소스 경로`. 서버에 존재하는 로컬 리소스 중에서 요청 받은 리소스가 무엇인지 알려줌
- URL은 HTTP프로토콜이 아닌 다른 프로토콜을 사용할 수도 있음. ex) `mailto:...`, `ftp://...`, `rtsp://...`

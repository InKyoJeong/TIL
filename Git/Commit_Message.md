## Git 커밋 메세지 작성법

커밋 메세지 제목은 타입 라벨을 앞에 붙여 `타입(Type): 제목` 형식으로 작성한다.

- **feat**: 새로운 기능
- **fix**: 버그 수정
- **docs**: 문서 수정
- **style**: 코드 포맷 변경, 세미 콜론 누락, 코드 변경 없음
- **refactor**: 프로덕션 코드 리팩터링
- **test**: 테스트 추가, 테스트 리팩터링 (프로덕션 코드 변경 없음)
- **chore**: 빌드 테스크 업데이트, 패키지 매니저 설정 (프로덕션 코드 변경 없음)

제목은 50자 이내이며, 대문자로 시작하고 마지막에 마침표 `.`를 붙이지 않는다.
**"Changed"**, **"Fixed"** 등 과거형이 아닌 **"Change"**, **"Fix"** 와 같이 명령문으로 시작한다.

예시 1) `docs: Edit README.md to include ...`<br>
예시 2) `feat: Summarize changes in around 50 characters or less`

### Reference

> [Udacity Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/)

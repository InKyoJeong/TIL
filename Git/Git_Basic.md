# Git Tip

> git 명령어들을 짧게 기록하는 파일

### 1. 저장소 초기화

> 새로운 디렉토리를 만들고 저장소를 초기화하는 과정을 한꺼번에 처리할 수 있다.

```
$ git init [directory]
```

### 2. 스테이징과 커밋 한꺼번에 처리하기

> 한 번 커밋한 이력이 있는 파일이라면 스테이지에 올리고 커밋하는 과정을 한꺼번에 처리할 수 있다.

```
$ git commit -am "[message]"
```

### 3. 로그 확인하기

```
$ git log --oneline
$ git log --oneline --branches
$ git log --oneline --branches --graph
```

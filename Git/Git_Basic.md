# Git Tip

> git 기본 팁들을 짧게 기록하는 파일

---

## 1. 저장소 초기화

> 새로운 디렉토리를 만들고 저장소를 초기화하는 과정을 한꺼번에 처리할 수 있다.

```
$ git init [directory]
```

## 2. 스테이징과 커밋 한꺼번에 처리하기

> 한 번 커밋한 이력이 있는 파일이라면 스테이지에 올리고 커밋하는 과정을 한꺼번에 처리할 수 있다.

```
$ git commit -am "[message]"
```

## 3. 로그 확인하기

```
$ git log --oneline
$ git log --oneline --branches
$ git log --oneline --branches --graph
```

## 4. status 짧게 확인하기

```
$ git status -s
```

<!-- 원격저장소로부터 clone을 받으면 로컬저장소로 모든 브랜치를 다 가져오는게 아니라 master 브랜치만 가져온다 -->

## 5. 브랜치 전환하기

> checkout 명령에 -b 옵션을 넣으면 브랜치 작성과 체크아웃을 한꺼번에 실행할 수 있다.

```
$ git checkout -b <branch>
```

## 6. 브랜치 삭제하기

> 브랜치를 삭제하려면 branch 명령에 -d 옵션을 지정하여 실행한다.

```
$ git branch -d <branchname>
```

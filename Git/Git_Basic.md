# Git Tip

> git 기본 팁들을 짧게 기록하는 파일

---

<br>

## 저장소 초기화

> 새로운 디렉토리를 만들고 저장소를 초기화하는 과정을 한꺼번에 처리할 수 있다.

```bash
$ git init [directory]
```

<br>

## 스테이징과 커밋 한꺼번에 처리하기

> 한 번 커밋한 이력이 있는 파일이라면 스테이지에 올리고 커밋하는 과정을 한꺼번에 처리할 수 있다.

```
$ git commit -am "[message]"
```

<br>

## 로그 확인하기

```bash
$ git log
$ git log --oneline
$ git log --oneline --branches
$ git log --oneline --branches --graph
```

<br>

## status 짧게 확인하기

```bash
$ git status -s
```

<br>

<!-- 원격저장소로부터 clone을 받으면 로컬저장소로 모든 브랜치를 다 가져오는게 아니라 master 브랜치만 가져온다 -->

## 브랜치 생성&전환하기

> checkout 명령에 -b 옵션을 넣으면 브랜치 작성과 체크아웃을 한꺼번에 실행할 수 있다.

```bash
$ git checkout -b <branch>
```

<br>

## 브랜치 삭제하기

> 브랜치를 삭제하려면 branch 명령에 -d 옵션을 지정하여 실행한다.

```bash
$ git branch -d <branchname>
```

<br>

## 작업 디렉토리 + 스테이징 영역에서 파일 삭제

```
$ git rm <fileName>
```

## 스테이징 영역에서만 파일 삭제

> 작업 디렉토리나 저장소에서는 삭제되지 않음

```bash
$ git rm --cached <fileName>
```

### github올린 파일 삭제하고 .gitignore 재설정

```bash
$ git rm -r --cached .
$ git add .
$ git commit -m "Apply .gitignore"
$ git push
```

<br>

## PR(pull request)을 merge 하지 않고 local로 받기

```bash
$ git pull origin pull/[PR_NUM]/head:pr-[PR_NUM]
```

<br>

## stash: commit하지 않고 잠시 저장했다가 나중에 다시 꺼내기

```bash
$ git stash
$ git stash list
# 목록 확인
$ git stash apply
# 최근의 stash를 가져와서 적용
$ git stash apply [stash 이름]
# stash 이름(ex. stash@{2})에 해당하는 stash를 적용
```

<br>

## 로컬 Git 저장소 브랜치 이름을 변경하기

```bash
$ git branch -m [OLD_BRANCH] [NEW_BRANCH]
```

## GitHub 저장소 브랜치 이름을 변경하기

- 먼저 새로 변경한 브랜치 푸시

```bash
$ git push origin new_branch
```

- origin의 _old branch_ 를 삭제

```bash
$ git push origin --delete old_branch

# 또는
$ git push origin :old_branch
```

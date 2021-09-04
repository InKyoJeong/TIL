## git lfs

- 100Mb부터 push error발생하므로 git repo에 포함시켜야할때 사용

#### 설치

- homebrew로 설치

```bash
$ brew install git-lfs
```

#### 사용법

```bash
$ git lfs install
$ git lfs track "*.psd" # track으로 파일 추적
$ git add .gitattributes
```

- gitattributes 부터 커밋/푸시하고 나서 파일 커밋/푸시해야한다.

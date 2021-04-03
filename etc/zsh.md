## zsh를 기본 쉘로 변경하기

- zsh가 설치되었는지 확인

```
$ zsh --version
```

- 설치가 안되어있는 경우

```
$ brew update
$ brew install zsh
```

- 쉘의 기본 위치 확인, 위치를 이용하여 기본쉘을 변경

```
$ which zsh
$ chsh -s /bin/zsh
```

- 터미널 재시작 후, 기본쉘 확인

```
$ echo $SHELL
```

zsh로 기본쉘을 적용한 뒤에는 `~/.bash_profile`대신 `~/.zshrc`에 설정값을 저장해야한다.

<br>

## zshrc

- **vscode** 에서 `zshrc` 열기

```
$ code ~/.zshrc
```

<br>

## homebrew로 yarn 설치

```
$ brew update
$ brew install yarn
$ yarn config set prefix ~/.yarn
$ echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.zshrc
```

기본 쉘이 zsh인 경우 `echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.bash_profile` 대신에 `~/.zshrc`로 설치

#### 공식 문서에서는 global로 권장

```
$ npm install --global yarn
```

<!-- 현재 맥에 이걸로 재설치(2021/04) -->

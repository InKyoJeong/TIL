## MySQL

> MySQL은 SQL언어를 사용하는 관계형 데이터베이스 관리 시스템이다.

## 데이터베이스란?

데이터베이스는 관련성을 가지며 중복이 없는 데이터들의 집합이다. 데이버베이스를 관리하는 시스템을 DBMS(데이터베이스 관리 시스템)이라 한다.<br>
보통 서버의 하드디스크나 SSD등의 저장매체에 데이터를 저장한다. 서버 종료와 상관없이 데이터를 계속 사용할 수 있다.

데이터베이스를 관리하는 DBMS 중에는 RDBMS(관계형 DBMS)가 많이 사용되고 대표적인 RDBMS로는 Oracle, MySQL, MSSQL 등이 있다.

### 설치

> Homebrew로 설치하기

```
$ brew install mysql@5.7
$ brew services start mysql@5.7
```

zsh를 사용중이면 아래명령으로 PATH추가해야한다.

```
$ echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.zshrc
```

이제 이 명령어로 root 비밀번호를 설정한다.

```
$ mysql_secure_installation
```

- validate_password 플러그인 설치 (n)
- 비밀번호 설정
- 익명사용자 삭제 (y)
- 원격 접속 허용 (n)
- 테스트DB삭제 (n)
- 수정할 것이 있는가? (y or n) : 하나라도 권한 변경을 했다면 (y)

#### 접속

```
$ mysql -uroot -p
Enter password: [비밀번호 입력]
mysql>

//다시 콘솔로 돌아가려면
mysql> exit(입력)
```

### 워크벤치

> 콘솔로는 데이터를 한눈에 보기 어려우므로 워크벤치를 사용하면 데이터베이스 내부에 저장된 데이터를 시각적으로 관리할 수 있다.

[https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)

### 데이터베이스 생성하기

```
mysql> CREATE SCHEMA [데이터베이스명]
```

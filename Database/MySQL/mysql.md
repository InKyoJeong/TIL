## MySQL

> MySQL은 SQL언어를 사용하는 관계형 데이터베이스 관리 시스템이다.

## 데이터베이스란?

데이터베이스는 관련성을 가지며 중복이 없는 데이터들의 집합이다. 데이버베이스를 관리하는 시스템을 DBMS(데이터베이스 관리 시스템)이라 한다.<br>
보통 서버의 하드디스크나 SSD등의 저장매체에 데이터를 저장한다. 서버 종료와 상관없이 데이터를 계속 사용할 수 있다.

데이터베이스를 관리하는 DBMS 중에는 RDBMS(관계형 DBMS)가 많이 사용되고 대표적인 RDBMS로는 Oracle, MySQL, MSSQL 등이 있다.

### 설치(mac)

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

```sql
mysql> CREATE SCHEMA [데이터베이스명]

mysql> use [데이터베이스명]
```

SQL구문을 입력할때는 마지막에 세미콜론`;`을 붙여야 실행된다.

```sql
mysql> CREATE SCHEMA nodejs;
//Query OK, 1 row affected (0.00 sec)

mysql> use nodejs;
//Database changed
```

### 테이블 생성하기

> 테이블이란 데이터가 들어갈 수 있는 틀이다.

```sql
mysql> CREATE TABLE nodejs.users (
    -> id INT NOT NULL AUTO_INCREMENT,
    -> name VARCHAR(20) NOT NULL,
    -> age INT UNSIGNED NOT NULL,
    -> married TINYINT NOT NULL,
    -> comment TEXT NULL,
    -> created_at DATETIME NOT NULL DEFAULT now(),
    -> PRIMARY KEY(id),
    -> UNIQUE INDEX name_UNIQUE (name ASC))
    -> COMMENT = '사용자 정보'
    -> DEFAULT CHARSET=utf8
    -> ENGINE=InnoDB;
Query OK, 0 rows affected (0.01 sec)
```

콤마로 구분해서 컬럼 id, name, age, married, comment, created_at(로우생성일)을 만들었다.

- 자료형
  - `INT`는 정수를 의미한다. 소수까지 표시하려면 **FLOAT**나 **DOUBLE**형을 이용한다.
  - `VARCHAR(자릿수)`는 가변 길이이다. **CHAR(자릿수)** 는 고정길이이다.
  - `TEXT`는 긴 글을 저장한다.
  - `TINYINT`는 -127 ~ 128 까지 정수를 저장한다. 0이나 1만 저장하면 boolean같은 역할을 한다.
  - `DATETIME`은 날짜와 시간에 대한 정보를 담는다. **DATE**나 **TIME**만 쓸수도 있다.

* 옵션
  - `NULL`은 빈칸을 허용할지 여부이다. `NOT NULL`은 비허용.
  - id컬럼에 추가로 붙은 `AUTO_INCREMENT`는 숫자를 저절로 올리는 역할이다.
  - `UNSIGNED`는 음수는 무시되고 음수만큼 양수를 더 표현한다.
  - `ZEROFILL`은 숫자의 자릿수가 고정되어있을때 쓴다. ex) INT(4)로 표현하는경우 숫자1을 넣으면 0001이 된다.
  - `DEFAULT now()`는 데이터베이스 저장시 해당 컬럼에 값이 없을 때 MySQL이 기본값을 넣어준다. `now()`는 현재시각을 넣는다. 대신에 `CURRENT_TIMESTAMP`를 넣어도 된다.
  - `PRIMARY KEY`옵션은 해당 컬럼이 기본키(로우를 대표하는 고유값)임을 나타낸다. 위에서는 PRIMARY KEY(id)로 id컬럼을 기본키로 했다.
  - `UNIQUE INDEX`는 해당값이 고유해야하는지 옵션이다. name_UNIQUE는 인덱스이름, name컬럼을 오름차순(ASC)으로 기억한다. id도 고유하지만 PRIMARY KEY는 자동으로 UNIQUE INDEX를 포함한다.

- 테이블 자체 설정
  - `COMMENT`는 테이블 보충 설명이다. (필수X)
  - `DEFAULT CHARSET=utf8`은 한글 설정
  - `ENGINE`은 **MyISAM**과 **InnoDB**가 많이 사용된다.

#### 생성된 테이블 확인

> DESC [테이블명] 명령어는 만든 테이블을 확인할 수 있다.

```sql
mysql> DESC users;
+------------+------------------+------+-----+-------------------+----------------+
| Field      | Type             | Null | Key | Default           | Extra          |
+------------+------------------+------+-----+-------------------+----------------+
| id         | int(11)          | NO   | PRI | NULL              | auto_increment |
| name       | varchar(20)      | NO   | UNI | NULL              |                |
| age        | int(10) unsigned | NO   |     | NULL              |                |
| comment    | text             | YES  |     | NULL              |                |
| created_at | datetime         | NO   |     | CURRENT_TIMESTAMP |                |
+------------+------------------+------+-----+-------------------+----------------+
```

### 테이블 제거

> DROP TABLE [테이블명] 명령어는 만든 테이블을 삭제할 수 있다.

```
mysql> DROP TABLE users;
```

### 테이블 생성하기 2

```sql
mysql> CREATE TABLE nodejs.comments (
    -> id INT NOT NULL AUTO_INCREMENT,
    -> commenter INT NOT NULL,
    -> comment VARCHAR(100) NOT NULL,
    -> created_at DATETIME NOT NULL DEFAULT now(),
    -> PRIMARY KEY(id),
    -> INDEX commenter_idx (commenter ASC),
    -> CONSTRAINT commenter
    -> FOREIGN KEY (commenter)
    -> REFERENCES nodejs.users (id)
    -> ON DELETE CASCADE
    -> ON UPDATE CASCADE)
    -> COMMENT = '댓글'
    -> DEFAULT CHARSET=utf8
    -> ENGINE=InnoDB;
```

commenter컬럼에는 댓글을 작성한 사용자의 id를 저장하려고 한다. 다른 테이블의 기본 키를 저장하는 컬럼을 **외래 키(foreign key)** 라고 한다.

- `CONSTRAINT [제약조건명]`, `FOREIGN KEY [컬럼명]`, `REFERENCES [참고하는 컬럼명]`을 이용해서 외래키를 지정할 수 있다. commenter컬럼과 users테이블의 id컬럼을 연결했다.
- `ON DELETE`와 `ON UPDATE`를 `CASCADE`로 설정하면, 사용자 정보가 수정,삭제되면 연결된 댓글 정보도 같이 수정,삭제된다.

#### 테이블 생성 확인

> SHOW TABLES;

```sql
mysql> SHOW TABLES;
+------------------+
| Tables_in_nodejs |
+------------------+
| comments         |
| users            |
+------------------+
```

### CRUD 작업

> CRUD란 Create, Read, Update, Delete를 의미한다.

#### Create(생성)

> Create는 데이터를 생성해서 데이터베이스에 넣는다.

데이터는 `INSERT INTO [테이블명] ([컬럼1], [컬럼2], ...) VALUES ([값1], [값2], ...)` 명령으로 넣는다.

```sql
mysql> INSERT INTO nodejs.users (name, age, married, comment) VALUES ('zero', 24, 0, '자기소개1');
// Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO nodejs.users (name, age, married, comment) VALUES ('nero', 44, 1, '자기소개2');
// Query OK, 1 row affected (0.00 sec)
```

```sql
mysql> INSERT INTO nodejs.comments (commenter, comment) VALUES (1, '안녕하세요. 제로의  댓글입니다.');
// Query OK, 1 row affected (0.00 sec)
```

_users_ 와 _comments_ 테이블에 데이터를 넣어보았다. `use nodejs;`명령어를 사용했으면 nodejs.users대신 users만 해도 된다.

#### Read(조회)

> Read는 데이터베이스의 데이터를 조회힌다.

`SELECT * FROM [테이블명]` 형식이다.

```sql
mysql> SELECT * FROM nodejs.users;
+----+------+-----+---------+---------------+---------------------+
| id | name | age | married | comment       | created_at          |
+----+------+-----+---------+---------------+---------------------+
|  1 | zero |  24 |       0 | 자기소개1       | 2020-04-09 16:14:22 |
|  2 | nero |  44 |       1 | 자기소개2       | 2020-04-09 16:16:12 |
+----+------+-----+---------+---------------+---------------------+
```

```sql
mysql> SELECT * FROM nodejs.comments;
+----+-----------+---------------------------------------------+---------------------+
| id | commenter | comment                                     | created_at          |
+----+-----------+---------------------------------------------+---------------------+
|  1 |         1 | 안녕하세요. 제로의 댓글입니다.                     | 2020-04-09 16:20:09 |
+----+-----------+---------------------------------------------+---------------------+
```

`SELECT [컬럼1, 컬럼2,...] FROM [테이블명]`으로 특정 컬럼만 조회할 수도 있다.

```sql
mysql> SELECT name, married FROM nodejs.users;
+------+---------+
| name | married |
+------+---------+
| zero |       0 |
| nero |       1 |
+------+---------+
```

`WHERE`을 이용해서 특정 조건의 데이터만 조회할 수도 있다. `AND`로 조건을 묶어 모두 만족하는 데이터를 찾을 수도 있다. `OR`도 가능하다. 어느하나라도 만족하는 데이터를 찾는다.

```sql
mysql> SELECT name, age FROM nodejs.users WHERE married = 1 AND age > 30;
+------+-----+
| name | age |
+------+-----+
| nero |  44 |
+------+-----+
```

`ORDER BY [컬럼명] [ASC 또는 DESC]`로 정렬할 수 있다.

```sql
mysql> SELECT id, name FROM nodejs.users ORDER BY age DESC;
+----+------+
| id | name |
+----+------+
|  2 | nero |
|  1 | zero |
+----+------+
```

`LIMIT [숫자]`로 조회할 로우개수를 설정할 수 있다.

```sql
mysql> SELECT id, name FROM nodejs.users ORDER BY age DESC LIMIT 1;
+----+------+
| id | name |
+----+------+
|  2 | nero |
+----+------+
```

`OFFSET [건너뛸 숫자]`로 건너뛰고 조회도 가능하다.

```sql
mysql> SELECT id, name FROM nodejs.users ORDER BY age DESC LIMIT 1 OFFSET 1;
+----+------+
| id | name |
+----+------+
|  1 | zero |
+----+------+
```

#### Update(수정)

> Update은 데이터베이스에 있는 데이터를 수정한다.

`UPDATE [테이블명] SET [컬럼명=바꿀값] WHERE [조건]` 명령어로 수정한다.

```sql
mysql> UPDATE nodejs.users SET comment = '바꿀내용입니다.' WHERE id = 2;
// Query OK, 1 row affected (0.00 sec)
// Rows matched: 1  Changed: 1  Warnings: 0
```

comment가 바뀐것을 확인할 수 있다.

```sql
mysql> SELECT * FROM nodejs.users;
+----+------+-----+---------+------------------------+---------------------+
| id | name | age | married | comment                | created_at          |
+----+------+-----+---------+------------------------+---------------------+
|  1 | zero |  24 |       0 | 자기소개1                | 2020-04-09 16:14:22 |
|  2 | nero |  44 |       1 | 바꿀내용입니다.            | 2020-04-09 16:16:12 |
+----+------+-----+---------+------------------------+---------------------+
```

#### Delete(삭제)

> Delete는 데이터베이스 데이터를 삭제한다.

`DELETE FROM [테이블명 WHERE [조건]`명령어로 삭제한다.

```sql
mysql> DELETE FROM nodejs.users WHERE id = 2;
// Query OK, 1 row affected (0.00 sec)
```

id가 2인 로우가 삭제된 것을 확인할 수 있다.

```sql
mysql> SELECT * FROM nodejs.users;
+----+------+-----+---------+---------------+---------------------+
| id | name | age | married | comment       | created_at          |
+----+------+-----+---------+---------------+---------------------+
|  1 | zero |  24 |       0 | 자기소개1       | 2020-04-09 16:14:22 |
+----+------+-----+---------+---------------+---------------------+
```

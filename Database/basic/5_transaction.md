## 트랜잭션이란

- 복수 쿼리를 한 단위로 묶은 것
- MySQL 에서는 트랜잭션을 사용할 수 없는 MyISAM형과 **트랜잭션 구조를 사용할 수 있는 InnoDB형** 2종류의 테이블을 이용 가능

#### 트랜잭션 4가지 특성

- 원자성(Atomicity)
- 일관성(Consistency)
- 고립성 or 격리성(Isolation)
- 지속성(Durability)

<br>

## 1. 원자성

- 데이터의 변경(INSERT/DELETE/UPDATE)을 수반하는 일련의 데이터 조작이 전부 성공할지 전부 실패할지 보증하는 구조
- 모두 정상적으로 실행되거나 하나도 실행되지 않아야함
  - 전부 성공후 **COMMIT**, 또는 전부 되돌리기 **ROLL BACK**

## 2.일관성

- 일련의 데이터 조작 전후에 그 상태를 유지하는 것
- 트랜잭션이 성공적으로 완료되면 일관적인 DB상태를 유지해야함

## 3.고립성(격리성)

- 일련의 데이터 조작을 복수 사용자가 **동시**에 실행해도 **각각의 처리가 모순없이 실행**되는 것을 보증
- 잠금(Lock)을 걸어서 후속 처리를 블록(Block)하는 방법이 있음
  - 잠금 단위에는 테이블, 블록, 행 등이 있는데 주로 행 단위 사용

### 모순 없는 상태란

- 복수의 트랜잭션이 순서대로 실행되는 경우와 같은 결과를 얻을 수 있는 상태
- 즉, 병렬이 아닌 직렬로 실행되는 상태

### 격리 수준

- 다른 트랜잭션의 영향을 받는것을 허용하는 4개 단계 (ANSI에서 정의)

```
- 커밋되지 않은 읽기
- 커밋된 읽기
- 반복 읽기
- 직렬화 가능
```

- 커밋되지 않은 읽기가 가장 완화된 격리수준, 직렬화 가능이 가장 엄격한 수준

<br>

### 격리 수준을 완화했을때 일어나는 현상

- **더티 읽기**(Dirty Read)
  - 어떤 트랜잭션이 커밋되기 전, 다른 트랜잭션에서 데이터를 읽는 현상
  - 더럽혀진(Dirty) 데이터를 읽는것
    - ex) A가 값을 변경하고 아직 커밋하지 않았는데 B가 변경한 후의 값을 읽음
- **애매한 읽기**(Fuzzy Read / 반복 불가능한 읽기, NonRepeatable Read)
  - 어떤 트랜잭션이 이전에 읽은 데이터를 다시 읽을때, 2회 이후의 결과가 1회때와 다른 현상
  - 최초에 읽은 값이 2회 이후의 SELECT에서 보증되지 못하고 애매(Fuzzy)하게 되는 것
    - ex) A가 '10'을 읽고 B가 그걸'9'로 변경해서 커밋했을때, A가 SELECT를 다시 실행하면 최초에 SELECT했던 '10'이 아닌 변경후의 '9'를 읽는다.
- **팬텀 읽기**(Phantom Read)
  - 어떤 트랜잭션을 읽을때, 선택할 수 있는 데이터가 나타나거나 사라지는 현상
    - ex) A가 범위검색 실행후 3행을 읽음 -> B가 1행을 INSERT하고 커밋함 -> A가 다시 같은 SELECT문 실행 후, 최초에 SELECT해서 얻은 3행이 아닌 4행이 선택됨

<br>

## 4. 지속성

- 일련의 데이터 조작(트랜잭션)을 완료하고 완료통지를 사용자가 받는 시점에서, 그 조작이 영구적이 되어 그 결과를 잃지 않는 것
  - MySQL 포함 많은 데이터베이스 구현에서는 트랜잭션 조작을 하드디스크에 **로그**로 기록하고, 이상이 발생하면 **로그를 사용해 이전 상태로 복원하여 지속성을 실현함**

<br>

## 다른 커넥션에서 작성한 테이블 보기

- 기본적으로는, 데이터 정의어(DDL)와 데이터 조작어(DML)에 의한 데이터 저장은 트랜잭션이 커밋되기전까지 다른 커넥션에서 보이지 않음
  - 그러나 MySQL이나 Oracle에서는 `CREATE TABLE` 같은 DDL 실행시 암묵적 커밋 발생
  - 따라서 한 커넥션에서 실행된 `CREATE TABLE`이 성공하면 이후 다른 커넥션에서도 참조가능

<br>

## DDL, DML, DCL

> SQL 명령은 3가지로 구분됨

- DDL (데이터 정의어)
  - 데이터를 저장하는 그릇인 스카마 또는 테이블을 작성 or 제거
  - `CREATE`, `DROP`, `ALTER`(CREATE로 작성한 것 변경) 등
- DML (데이터 조작어)
  - 테이블의 행을 검색하거나 변경
  - 실무에서 사용하는 SQL문의 대부분
  - `SELECT, INSERT, UPDATE, DELETE` 등
- DCL (데이터 제어어)
  - 데이터베이스에서 실행한 변경을 확정하거나 취소
  - `COMMIT`이나 `ROLLBACK`

<br>

## 복수 커넥션에서 읽기/쓰기

- 트랜잭션 다룰 테이블 준비

```sql
mysql> CREATE SCHEMA test210612;
-- Query OK, 1 row affected (0.00 sec)
mysql> use test210612;
-- Database changed
mysql> CREATE TABLE t1(i1 INT NOT NULL PRIMARY KEY, v2 VARCHAR(20)) engine = innodb;
mysql> INSERT INTO t1 values(1, 'JS');
mysql> SELECT * FROM t1;
+----+------+
| i1 | v2   |
+----+------+
|  1 | JS   |
+----+------+
```

- 2개의 MySQL 커맨드라인 클라이언트 실행 (_test0612_ 스키마, _t1_ 테이블 생성)

```sql
mysql> prompt Transaction A>
-- PROMPT set to 'Transaction A>'
Transaction A>use test210612;
-- Database changed
Transaction A>start transaction;
-- Query OK, 0 rows affected (0.00 sec)

Transaction A>
```

```sql
mysql> prompt Transaction B>
-- PROMPT set to 'Transaction B>'
Transaction B>use test210612;
-- Database changed
Transaction B>start transaction;
-- Query OK, 0 rows affected (0.00 sec)

Transaction B>
```

- (_t1_ 테이블 조회)

```sql
Transaction A>SELECT * FROM t1;
+----+------+
| i1 | v2   |
+----+------+
|  1 | JS   |
+----+------+
-- 1 row in set (0.00 sec)
Transaction A>rollback;
-- Query OK, 0 rows affected (0.00 sec)
```

```sql
Transaction B>SELECT * FROM t1;
+----+------+
| i1 | v2   |
+----+------+
|  1 | JS   |
+----+------+
-- 1 row in set (0.00 sec)
Transaction B>rollback;
-- Query OK, 0 rows affected (0.00 sec)
```

<br>
<!-- 
#### 다른 트랜잭션의 갱신(INSERT)을 자신의 트랜잭션 읽기(SELECT)에서 확인 -->

#### 다른 트랜잭션과 자신의 트랜잭션이 중복됐을때

```sql
Transaction B>start transaction;

Transaction B>INSERT INTO t1 values (2, 'SAME-A');
-- Query OK, 1 row affected (0.00 sec)
```

```sql
Transaction A>start transaction;

Transaction A>INSERT INTO t1 values (2, 'SAME-B');
-- 에러발생
-- ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

<br>

## 트랜잭션 격리수준 확인

```sql
mysql> SELECT @@GLOBAL.transaction_isolation;
+--------------------------------+
| @@GLOBAL.transaction_isolation |
+--------------------------------+
| REPEATABLE-READ                |
+--------------------------------+

mysql> SELECT @@SESSION.transaction_isolation;
+---------------------------------+
| @@SESSION.transaction_isolation |
+---------------------------------+
| REPEATABLE-READ                 |
+---------------------------------+
```

<br>

## 트랜잭션 격리수준 변경

#### 방법1 : mysql.conf 또는 mysql.ini 등의 파일에 명시

```sql
[mysqld]
transaction-isolation = REPEATABLE-READ
transaction-read-only = OFF
```

#### 방법2 : 문장으로 변경

```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

- MySQL 트랜잭션 격리수준 기본값은 `반복 읽기(Repeatable Read)`

<br>

## 격리수준 실습

- 한개의 커넥션에서 쓰기를 해서, 트랜잭션 격리 수준이 다른 2개의 커넥션에서 어떻게 보이는지 확인하기

1. A 격리수준 반복읽기로 변경(기본)

```sql
Transaction A>SET SESSION TRANSACTION ISOLATION LEVEL repeatable read; start transaction;

-- 변경 확인
Transaction A>SELECT @@SESSION.transaction_isolation;
+---------------------------------+
| @@SESSION.transaction_isolation |
+---------------------------------+
| REPEATABLE-READ                 |
+---------------------------------+
```

2. B 격리수준 커밋된 읽기로 변경

```sql
Transaction B>SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;start transaction;

-- 변경 확인
Transaction B>SELECT @@SESSION.transaction_isolation;
+---------------------------------+
| @@SESSION.transaction_isolation |
+---------------------------------+
| READ-COMMITTED                  |
+---------------------------------+
```

3. C 준비하고 명령입력

```sql
mysql> prompt Transaction C>
-- PROMPT set to 'Transaction C>'
Transaction C>use test210612;
-- Database changed
Transaction C>start transaction;

Transaction C>UPDATE t1 SET v2='MySQL' WHERE i1 = 1;commit;start transaction;
```

4. A,B 에서 확인

```sql
Transaction A>SELECT * FROM t1 WHERE i1=1;
+----+-------+
| i1 | v2    |
+----+-------+
|  1 | MySQL |
+----+-------+
-- 1 row in set (0.00 sec)

Transactioni B>SELECT * FROM t1 WHERE i1=1;
+----+-------+
| i1 | v2    |
+----+-------+
|  1 | MySQL |
+----+-------+
-- 1 row in set (0.00 sec)
```

5. 다시 C에 명령 입력

```sql

Transaction C>UPDATE t1 SET v2='PostgreSQL' WHERE i1 = 1;commit;start transaction;
-- Query OK, 1 row affected (0.00 sec)
-- Rows matched: 1  Changed: 1  Warnings: 0

Transaction C>UPDATE t1 SET v2='Oracle' WHERE i1=1;
-- Query OK, 1 row affected (0.00 sec)
-- Rows matched: 1  Changed: 1  Warnings: 0
```

6. ABC 순으로 확인

```sql
Transaction A>SELECT * FROM t1 WHERE i1=1;
+----+-------+
| i1 | v2    |
+----+-------+
|  1 | MySQL |
+----+-------+
-- 1 row in set (0.00 sec)

Transaction B>SELECT * FROM t1 WHERE i1=1;
+----+------------+
| i1 | v2         |
+----+------------+
|  1 | PostgreSQL |
+----+------------+
-- 1 row in set (0.00 sec)

Transaction C>SELECT * FROM t1 WHERE i1=1;
+----+--------+
| i1 | v2     |
+----+--------+
|  1 | Oracle |
+----+--------+
-- 1 row in set (0.00 sec)

```

<br>

#### 결과

- _(트랜잭션 A)_ 반복읽기 (Repeatable Read)
  - 최초 쿼리를 실행한 시점에 커밋된 데이터를 읽는다.
  - 같은 쿼리를 복수 회 실행시 최초 읽은 내용의 결과가 반환
  - 복수 회의 쿼리 실행 사이에 다른 트랜잭션이 COMMIT 했어도 반영되지 않음
- _(트랜잭션 B)_ 커밋된 읽기 (Read Committed)
  - 쿼리를 실행한 시점에서 커밋된 데이터를 읽는다.
  - 같은 쿼리를 복수회 실행하면, 도중에 다른 트랜잭션에서 커밋할때, 최신 쿼리 실행개시 시점에서 커밋된 데이터를 읽음
- _(트랜잭션 C)_ 갱신을 수행하는 트랜잭션 자신
  - 트랜잭션 격리 수준이나 _COMMIT/ROLLBACK_ 에 상관없이 갱신을 즉시 볼 수 있음

<br>

#### 커밋되지 않은 읽기를 사용하지 않는이유?

- MySQL(innodb형 )은 **MVCC**(Multi Versioning Concurrency Control)를 사용함
  - 읽기를 수행할 경우 갱신중이라도 블록되지 않음
  - 따라서 커밋되지 않은 읽기가 필요없음

## 잠금 타임아웃

- 갱신과 참조는 서로 블록하지 않음
- **갱신과 갱신이 부딪치면 나중에 온 갱신이 잠금 대기 상태가 된다**
- 잠금 해제를 기다리는 쪽은 잠금을 기다리지 않거나, 어느정도 기다릴지 설정 가능
  - MySQL 에서는 `innodb_lock_wait_timeout` (유효값은 1초 이상)

```sql
Transaction B>start transaction;

Transaction B>INSERT INTO t1 values (2, 'SAME-A');
-- Query OK, 1 row affected (0.00 sec)
```

```sql
Transaction A>start transaction;

Transaction A>INSERT INTO t1 values (2, 'SAME-B');
-- 잠금 타임 아웃 발생
-- ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

<br>

## 교착 상태

- 서로 잠금을 건 자원에 잠금이 필요한 처리(**_INSERT/UPDATE/DELETE_**)를 실행했을때
  - 아무리 기다려도 상황이 바뀌지 않는 상태 = 교착상태

```sql
Transaction A>CREATE TABLE a(i1 INT NOT NULL PRIMARY KEY, v2 VARCHAR(20)) engine = innodb;
Transaction A>CREATE TABLE b(i1 INT NOT NULL PRIMARY KEY, v2 VARCHAR(20)) engine = innodb;
Transaction A>set innodb_lock_wait_timeout = 50;start transaction;

Transaction B>start transaction;
-- Query OK, 0 rows affected (0.00 sec)

Transaction A>INSERT INTO a values(1,'React');
-- Query OK, 1 row affected (0.00 sec)

Transaction B>INSERT INTO b values(1,'Vue');
-- Query OK, 1 row affected (0.00 sec)

Transaction A>INSERT INTO b values(1,'React');
-- Query OK, 1 row affected (14.80 sec)

Transaction B>INSERT INTO a values(1,'Vue');
-- 교착 상태 발생
-- ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

<br>

### 교착 상태 빈도를 낮추려면

- 교착 상태는 상황이 개선될 수 없음
- 따라서 일반적으로, 교착상태를 검출하여 보고
- MySQL은 교착상태시 시스템에 영향이 작은쪽은 트랜잭션을 트랜잭션 개시 시점까지 롤백함

#### 전반적인 DBMS 대책

- 트랜잭션을 자주 커밋하여 교착상태 가능성을 낮추기
- 정해진 순서로 테이블에 액세스하기
- 필요없는 경우에는 읽기 잠금 획득 (SELECT ~ FOR UPDATE 등)의 사용 피하기
- 쿼리에 의한 잠금 범위를 좁히거나 잠금 정도를 더 작은것으로 하기 (ex. MySQL에서 격리수준을 '커밋된 읽기'로 변경)

#### MySQL 대책

- 테이블에 적절한 인덱스를 추가해 쿼리가 이걸 사용하게 하기

<br>

## 주의할 트랙잭션

- 오토커밋
  - 오토커밋은 쿼리 단위로 커밋하는 설정
  - 커맨드라인 같은 간단한 쿼리실행과 테스트는 편리하지만, 애플리케이션 잠금을 실행하는데는 커밋 부하가 높음
  - 주의해서 사용하지 않으면 성능에 악영향
- 긴 트랜잭션
  - 긴 트랜잭션은 데이터베이스 트랜잭션의 동시성이나 자원의 유효성을 저하시킴

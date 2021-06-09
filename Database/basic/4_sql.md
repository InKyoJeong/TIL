## SQL 기본

- SQL은 DBMS에 저장된 테이블을 조작하기 위해 사용
- 테이블은 스키마에 저장되어 있음
- MySQL에서는 스키마=데이터베이스
  - 1개의 데이터베이스에 복수의 테이블이 저장되어 있음
  - 관리 명령 (SQL이 아님)
    - `show databases;` : 데이터베이스를 살펴볼때
    - `use 데이터베이스명;` : 디폴트(현재) 데이터베이스 지정
    - `show tables` : 데이터베이스 내의 테이블 리스트를 얻을때

#### SQL 기술 규칙

- 마지막에 딜리미터 붙인다. (보통 세미콜론)
- 키워드의 대소문자 구분하지 않는다. (select = SELECT)
- 정수는 그대로, 문자열이나 날짜 시각은 작음따옴표(`''`)로 감싼다.

<br>

## 실습

> [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html) > _world database_ 다운 > _WorkBench_ 로 열어서 쿼리 후 Refresh

- 데이터베이스 항목 표시

```sql
mysql> show databases;
+----------------------+
| Database             |
+----------------------+
| information_schema   |
| mysql                |
| performance_schema   |
| sys                  |
| world                |  -- ✅
+----------------------+
```

- 사용할 데이터베이스 선택, 테이블 조회

```sql
mysql> use world
Database changed
mysql> show tables;
+-----------------+
| Tables_in_world |
+-----------------+
| city            |
| country         |
| countrylanguage |
+-----------------+
3 rows in set (0.00 sec)
```

<br>

## SELECT 문 응용조작

#### SELECT : 데이터 선택

- `FROM 테이블명` 또는 `데이터베이스명.테이블명`으로 지정가능
- 별표 (`*`)는 전체 열

```sql
SELECT * FROM city;
SELECT * FROM world.city;
```

#### WHERE : 조건 추가

```sql
mysql> SELECT * FROM city where countrycode = 'KOR';
+------+------------+-------------+---------------+------------+
| ID   | Name       | CountryCode | District      | Population |
+------+------------+-------------+---------------+------------+
| 2331 | Seoul      | KOR         | Seoul         |    9981619 |
| 2332 | Pusan      | KOR         | Pusan         |    3804522 |
| 2333 | Inchon     | KOR         | Inchon        |    2559424 |
-- ...
| 2399 | Tonghae    | KOR         | Kang-won      |      95472 |
| 2400 | Mun-gyong  | KOR         | Kyongsangbuk  |      92239 |
+------+------------+-------------+---------------+------------+
70 rows in set (0.00 sec)
```

```sql
mysql> SELECT * FROM city where district = 'Kyonggi';
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
| 2338 | Songnam    | KOR         | Kyonggi  |     869094 |
| 2339 | Puchon     | KOR         | Kyonggi  |     779412 |
| 2340 | Suwon      | KOR         | Kyonggi  |     755550 |
| 2341 | Anyang     | KOR         | Kyonggi  |     591106 |
--  ...
| 2392 | Hanam      | KOR         | Kyonggi  |     115812 |
| 2396 | Uiwang     | KOR         | Kyonggi  |     108788 |
+------+------------+-------------+----------+------------+
```

<br>

- AND 또는 OR 연산자 사용

```sql
mysql> SELECT * FROM city whcity where district = 'Kyonggi' AND population > 300000;
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
| 2338 | Songnam    | KOR         | Kyonggi  |     869094 |
| 2339 | Puchon     | KOR         | Kyonggi  |     779412 |
| 2340 | Suwon      | KOR         | Kyonggi  |     755550 |
| 2341 | Anyang     | KOR         | Kyonggi  |     591106 |
| 2344 | Koyang     | KOR         | Kyonggi  |     518282 |
| 2345 | Ansan      | KOR         | Kyonggi  |     510314 |
| 2349 | Kwangmyong | KOR         | Kyonggi  |     350914 |
| 2353 | Pyongtaek  | KOR         | Kyonggi  |     312927 |
+------+------------+-------------+----------+------------+
```

<br>

#### DISTINCT : 중복 배제

```sql
mysql> SELECT district from city where countrycode = 'KOR';
+---------------+
| district      |
+---------------+
| Seoul         |
| Pusan         |
| Inchon        |
| Taegu         |
| Taejon        |
| Kwangju       |
| Kyongsangnam  |
| Kyonggi       |
| Kyonggi       |
| Kyonggi       |
| Chollabuk     |
| Chungchongbuk |
| Kyonggi       |
| Kyonggi       |
| Kyongsangbuk  |
| Kyongsangnam  |
| Kyongsangnam  |
| Kyonggi       |
-- ...
```

- 중복 행을 제외해서 구하기 : `SELECT` 구문에서 `DISTINCT` 키워드 사용

```sql
mysql> SELECT DISTINCT district from city where countrycode = 'KOR';
+---------------+
| district      |
+---------------+
| Seoul         |
| Pusan         |
| Inchon        |
| Taegu         |
| Taejon        |
| Kwangju       |
| Kyongsangnam  |
| Kyonggi       |
| Chollabuk     |
| Chungchongbuk |
| Kyongsangbuk  |
| Chungchongnam |
| Cheju         |
| Chollanam     |
| Kang-won      |
+---------------+
15 rows in set (0.00 sec)
```

```sql
-- 이렇게해도 위와 같다
mysql> SELECT district from city where countrycode = 'KOR' GROUP BY district;
```

<br>

#### ORDER BY : 검색 결과 정렬

```sql
mysql> SELECT * FROM city WHERE countrycode = 'KOR' ORDER BY population;
+------+------------+-------------+---------------+------------+
| ID   | Name       | CountryCode | District      | Population |
+------+------------+-------------+---------------+------------+
| 2400 | Mun-gyong  | KOR         | Kyongsangbuk  |      92239 |
| 2399 | Tonghae    | KOR         | Kang-won      |      95472 |
| 2398 | Namwon     | KOR         | Chollabuk     |     103544 |
-- ...
| 2332 | Pusan      | KOR         | Pusan         |    3804522 |
| 2331 | Seoul      | KOR         | Seoul         |    9981619 |
+------+------------+-------------+---------------+------------+
```

- `DESC` : 내림차순 정렬 (기본값 ASC)

```sql
mysql> SELECT * from city where countrycode = 'KOR' ORDER BY population DESC;
+------+------------+-------------+---------------+------------+
| ID   | Name       | CountryCode | District      | Population |
+------+------------+-------------+---------------+------------+
| 2331 | Seoul      | KOR         | Seoul         |    9981619 |
| 2332 | Pusan      | KOR         | Pusan         |    3804522 |
-- ...

| 2398 | Namwon     | KOR         | Chollabuk     |     103544 |
| 2399 | Tonghae    | KOR         | Kang-won      |      95472 |
| 2400 | Mun-gyong  | KOR         | Kyongsangbuk  |      92239 |
+------+------------+-------------+---------------+------------+
```

<br>

#### 테이블 집약

- 행수를 카운트 하려면 `select count(*)`

```sql
mysql> select count(*) from city where countrycode = 'KOR';
+----------+
| count(*) |
+----------+
|       70 |
+----------+
1 row in set (0.00 sec)
```

- 최소 최대 총수 평균 등을 구하려면 콤마로 구분해 지정

```sql
mysql> select min(population), max(population), sum(population), avg(population) from city where countrycode ='KOR';
+-----------------+-----------------+-----------------+-----------------+
| min(population) | max(population) | sum(population) | avg(population) |
+-----------------+-----------------+-----------------+-----------------+
|           92239 |         9981619 |        38999893 |     557141.3286 |
+-----------------+-----------------+-----------------+-----------------+
1 row in set (0.00 sec)
```

<br>

#### GROUP BY : 테이블을 그룹으로 구분

```sql
-- district 별로 그룹 나눠서 몇개 도시가 있는지 확인

mysql> SELECT district, count(*) from city where countrycode = 'KOR' GROUP BY district;
+---------------+----------+
| district      | count(*) |
+---------------+----------+
| Cheju         |        1 |
| Chollabuk     |        6 |
| Chollanam     |        5 |
| Chungchongbuk |        3 |
| Chungchongnam |        6 |
| Inchon        |        1 |
| Kang-won      |        4 |
| Kwangju       |        1 |
| Kyonggi       |       18 |
| Kyongsangbuk  |       10 |
| Kyongsangnam  |       11 |
| Pusan         |        1 |
| Seoul         |        1 |
| Taegu         |        1 |
| Taejon        |        1 |
+---------------+----------+
15 rows in set (0.00 sec)
```

- `HAVING` : 조건을 지정해 그룹 구분

```sql
mysql> SELECT district, count(*) from city where countrycode = 'KOR' GROUP BY district HAVING count(*) = 6;
+---------------+----------+
| district      | count(*) |
+---------------+----------+
| Chollabuk     |        6 |
| Chungchongnam |        6 |
+---------------+----------+
2 rows in set (0.00 sec)
```

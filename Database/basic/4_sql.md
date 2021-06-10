- SQL 기본
  - [SELECT (검색)](#select-r)
  - [UPDATE (갱신)](#update-u)
  - [INSERT (등록)](#insert-c)
  - [DELETE (제거)](#delete-d)
- [뷰, 서브쿼리](#view)
- [결합](#join)

---

<br>

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

## <a name="select-r"></a>SELECT 문 응용조작

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

mysql> SELECT district, count(*) from city WHERE countrycode = 'KOR' GROUP BY district;
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
mysql> SELECT district, count(*) from city WHERE countrycode = 'KOR' GROUP BY district HAVING count(*) = 6;
+---------------+----------+
| district      | count(*) |
+---------------+----------+
| Chollabuk     |        6 |
| Chungchongnam |        6 |
+---------------+----------+
2 rows in set (0.00 sec)
```

<br>

## <a name="update-u"></a>데이터 갱신

#### UPDATE 문 : 데이터 변경

- `UPDATE 테이블명 SET 열명 = 값`
- `SET`으로 지정한 열 이외의 것은 변경되지않음

Kyonggi(경기) 도시를 검색해보면

```sql
mysql> SELECT * from city WHERE countrycode = 'KOR' AND district = 'Kyonggi';
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
-- ...
| 2383 | Shihung    | KOR         | Kyonggi  |     133443 |
| 2392 | Hanam      | KOR         | Kyonggi  |     115812 |
| 2396 | Uiwang     | KOR         | Kyonggi  |     108788 |
+------+------------+-------------+----------+------------+
```

잘못되어 있는 Shihung(시흥)을 Siheung으로 바꾸기

```sql
mysql> UPDATE city SET name = 'Siheung' WHERE countrycode = 'KOR' AND district = 'Kyonggi' AND name = 'Shihung';
-- Query OK, 1 row affected (0.00 sec)
-- Rows matched: 1  Changed: 1  Warnings: 0
```

다시 조회해보면 시흥이 _Siheung_ 으로 바뀜

```sql
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
-- ...
| 2383 | Siheung    | KOR         | Kyonggi  |     133443 |
| 2392 | Hanam      | KOR         | Kyonggi  |     115812 |
| 2396 | Uiwang     | KOR         | Kyonggi  |     108788 |
+------+------------+-------------+----------+------------+
```

- 복수열 동시 갱신

name 열 외에 population 열도 동시에 갱신하기

```sql
UPDATE city SET name = 'Siheung', population = 429390 WHERE countrycode = 'KOR' AND district = 'Kyonggi' AND name = 'Shihung';
```

<br>

## <a name="insert-c"></a>데이터 삽입

#### INSERT 문 : 데이터 입력

- INSERT 는 행 단위로 수행되므로 **행을 구성하는 열 정보를 포함한 "테이블의 정의"를 잘 알아야한다**
- MySQL 에서는 `show create table 테이블명\G`로 알 수 있다. (`\G`는 `;` 대신 사용하면 결과를 세로로 보기 쉽게 표시)

```sql
mysql> show create table city\G
*************************** 1. row ***************************
Table: city
Create Table: CREATE TABLE `city` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(35) NOT NULL DEFAULT '',
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `District` char(20) NOT NULL DEFAULT '',
  `Population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)
) ENGINE=InnoDB AUTO_INCREMENT=4080 DEFAULT CHARSET=utf8mb4
1 row in set (0.00 sec)
```

- 테이블 정의가 아닌 **열의 정보만 보려면** `desc 테이블명`

```sql
mysql> desc city;
+-------------+----------+------+-----+---------+----------------+
| Field       | Type     | Null | Key | Default | Extra          |
+-------------+----------+------+-----+---------+----------------+
| ID          | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name        | char(35) | NO   |     |         |                |
| CountryCode | char(3)  | NO   | MUL |         |                |
| District    | char(20) | NO   |     |         |                |
| Population  | int(11)  | NO   |     | 0       |                |
+-------------+----------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
```

<br>

#### 기본키(Primary Key)

- 테이블의 행을 유일하게 특정할 수 있는 **유니크한 값을 저장하는 열**
- 테이블 하나당 하나만 가능
- 데이터자체에 특정 유니크 정보가 있으면 그걸 기본키로, 없이 기계적으로 할당하려면 `auto_increment`속성 사용

<br>

#### INSERT 문의 기본 구문

```sql
INSERT INTO 테이블명(열1, 열2, ...) VALUES (값1, 값2, ...)
```

<br>

- 경기도(Kyonggi)에 김포(Gimpo)시를 추가
  - 모든 열에대해 `VALUES` 값 설정하면, 테이블명의 **열 리스트 생략 가능**

```sql
mysql> INSERT INTO city VALUES (DEFAULT, 'Gimpo', 'KOR', 'Kyonggi', 359865);
-- Query OK, 1 row affected (0.00 sec)
```

```sql
mysql> SELECT * FROM city WHERE countrycode = 'KOR' AND district = 'Kyonggi';
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
| 2338 | Songnam    | KOR         | Kyonggi  |     869094 |
-- ...
| 2396 | Uiwang     | KOR         | Kyonggi  |     108788 |
| 4080 | Gimpo      | KOR         | Kyonggi  |     359865 |
+------+------------+-------------+----------+------------+
19 rows in set (0.00 sec)
```

<br>

- 복수 행 입력 : VALUES 뒤에 괄호를 콤마로 연결하여 작성

```sql
mysql> INSERT INTO city (name, countrycode, district, population) VALUES ('Test11', 'KOR','Kyonggi', 19191919), ('Test22', 'KOR', 'Kyonggi', 29292929);
-- Query OK, 2 rows affected (0.01 sec)
-- Records: 2  Duplicates: 0  Warnings: 0
```

```sql
mysql> SELECT * FROM city WHERE countrycode = 'KOR' AND district = 'Kyonggi';
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
| 2338 | Songnam    | KOR         | Kyonggi  |     869094 |
-- ...
| 4083 | Test11     | KOR         | Kyonggi  |   19191919 |
| 4084 | Test22     | KOR         | Kyonggi  |   29292929 |
+------+------------+-------------+----------+------------+
```

<br>

## <a name="delete-d"></a>데이터 제거

#### DELETE 문

```sql
DELETE FROM 테이블명;        --전체행이 제거되므로 주로 아래 처럼 사용
DELETE FROM 테이블명 WHERE 조건;
```

```sql
-- 마지막에 추가한 TEST22 를 삭제

mysql> DELETE FROM city WHERE id = 4084;
-- Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM city WHERE countrycode = 'KOR' AND district = 'Kyonggi';
+------+------------+-------------+----------+------------+
| ID   | Name       | CountryCode | District | Population |
+------+------------+-------------+----------+------------+
| 2338 | Songnam    | KOR         | Kyonggi  |     869094 |
-- ...
| 4083 | Test11     | KOR         | Kyonggi  |   19191919 |
+------+------------+-------------+----------+------------+
```

<br>

## <a name="view"></a>뷰

- 테이블과 동일하지만 데이터는 가지고 있지 않음
  - 복잡한 SELECT 문을 일일이 매번 기술할 필요가 없다
  - 필요한 열과행만 보여주고, 갱신 시에도 뷰 정의에 따른 갱신으로 한정 가능
  - 위의 두가지를 데이터 저장없이 실현 가능. 뷰를 제거해도 참조하는 테이블은 영향을 받지않음

#### CREATE VIEW : 뷰 작성

```sql
CREATE VIEW 뷰 명 (열명1, 열명2, ...) AS SELECT 문;
```

<br>

- 경기도의 _id, name, population_ 을 표시하는 뷰 _(citykyonggi)_ 작성

```sql
mysql> CREATE VIEW citykyonggi AS SELECT id, name, population from city where countrycode = 'KOR' AND district = 'Kyonggi';
-- Query OK, 0 rows affected (0.03 sec)

mysql> SELECT * FROM citykyonggi;
+------+------------+------------+
| id   | name       | population |
+------+------------+------------+
| 2338 | Songnam    |     869094 |
| 2339 | Puchon     |     779412 |
| 2340 | Suwon      |     755550 |
| 2392 | Hanam      |     115812 |
-- ...
| 4082 | Test22     |      22222 |
| 4083 | Test11     |   19191919 |
+------+------------+------------+
22 rows in set (0.00 sec)
```

- 인구 _(population)_ 가 700만 보다 많은 도시 뷰 _(largecity)_ 작성
- _WITH CHECK OPTION_ 은 뷰에 참조된 테이블에 행을 _INSERT_ 또는 _UPDATE_ 하는 것을 제약

```sql
mysql> CREATE VIEW largecity AS SELECT * FROM city WHERE population > 7000000 WITH CHECK OPTION;
-- Query OK, 0 rows affected (0.03 sec)
```

- 작성한 뷰 확인

```sql
mysql> SELECT * FROM largecity;
+------+-------------------+-------------+------------------+------------+
| ID   | Name              | CountryCode | District         | Population |
+------+-------------------+-------------+------------------+------------+
|  206 | São Paulo         | BRA         | São Paulo        |    9968485 |
-- ...
| 2331 | Seoul             | KOR         | Seoul            |    9981619 |
-- ...
| 3793 | New York          | USA         | New York         |    8008278 |
| 4083 | Test11            | KOR         | Kyonggi          |   19191919 |
+------+-------------------+-------------+------------------+------------+
```

<br>

## 서브쿼리 실행

> 서브쿼리란 부모 쿼리 안에 작성하는 내부의 SELECT 쿼리

- SELECT 문의 결과를 데이터처럼 다루거나 수치처럼 취급해서 조건문에 이용 가능하다.
- 이런 쿼리를 메인 쿼리와 대비하여 **서브 쿼리**라고 함

```sql
-- 한국 도시만을 가진 뷰 작성

mysql> CREATE VIEW citykorea AS SELECT id, name, district, population FROM city WHERE countrycode = 'KOR';
-- Query OK, 0 rows affected (0.02 sec)

-- 한국 도시중 인구가 평균 이상인 도시 수
mysql> SELECT count(*) FROM citykorea WHERE population > (SELECT avg(population) FROM citykorea);
+----------+
| count(*) |
+----------+
|        9 |
+----------+
```

<br>

## <a name="join"></a>결합(JOIN)

- SQL은 **2개 이상의 테이블을 대상으로 실행**하는 것도 가능
- 결합은 하나의 테이블에 있는 열만으로 데이터가 충족되지 않는 경우, 열을 가지고 오는 조작
- 2개 테이블의 행을 결합시키기 위한 **결합조건**을 지정
  - **내부결합과 외부결합** 등이 있음

<br>

#### 내부 결합(Inner Join)

```sql
SELECT 선택하고 싶은 열리스트 FROM 첫번째 테이블명 INNER JOIN 두번째 테이블명 ON 결합조건;
```

(_country_ 테이블 예시)

```sql

mysql> SELECT * FROM country;
+------+----------------------------------------------+---------------+---------------------------+-------------+-----------+------------+----------------+------------+------------+----------------------------------------------+----------------------------------------------+--------------------------------------+---------+-------+
| Code | Name                                         | Continent     | Region                    | SurfaceArea | IndepYear | Population | LifeExpectancy | GNP        | GNPOld     | LocalName                                    | GovernmentForm                               | HeadOfState                          | Capital | Code2 |
+------+----------------------------------------------+---------------+---------------------------+-------------+-----------+------------+----------------+------------+------------+----------------------------------------------+----------------------------------------------+--------------------------------------+---------+-------+
| ABW  | Aruba                                        | North America | Caribbean                 |      193.00 |      NULL |     103000 |           78.4 |     828.00 |     793.00 | Aruba                                        | Nonmetropolitan Territory of The Netherlands | Beatrix                              |     129 | AW    |
| AFG  | Afghanistan                                  | Asia          | Southern and Central Asia |   652090.00 |      1919 |   22720000 |           45.9 |    5976.00 |       NULL | Afganistan/Afqanestan                        | Islamic Emirate                              | Mohammad Omar                        |       1
-- ...
```

_countrylanguage_ 테이블에는 각 국가에서 사용하는 언어가 등록되어 있음

```sql
mysql> SELECT * FROM countrylanguage where countrycode = 'KOR';
+-------------+----------+------------+------------+
| CountryCode | Language | IsOfficial | Percentage |
+-------------+----------+------------+------------+
| KOR         | Chinese  | F          |        0.1 |
| KOR         | Korean   | T          |       99.9 |
+-------------+----------+------------+------------+
```

전세계에서 한국어를 사용하는 국가 조회

```sql
mysql> SELECT * FROM countrylanguage WHERE language = 'Korean';
+-------------+----------+------------+------------+
| CountryCode | Language | IsOfficial | Percentage |
+-------------+----------+------------+------------+
| GUM         | Korean   | F          |        3.3 |
| JPN         | Korean   | F          |        0.5 |
| KOR         | Korean   | T          |       99.9 |
| MNP         | Korean   | F          |        6.5 |
| PRK         | Korean   | T          |       99.9 |
| USA         | Korean   | F          |        0.3 |
+-------------+----------+------------+------------+
```

위에서 GUM, MNP등의 국가 코드가 어느 국가인지 알기 힘드므로, 국가코드에서 국가명을 검색하여 추가하기

```sql
mysql> SELECT countrylanguage.*, country.name FROM countrylanguage INNER JOIN country ON countrylanguage.countrycode = country.code WHERE countrylanguage.language = 'Korean';
+-------------+----------+------------+------------+--------------------------+
| CountryCode | Language | IsOfficial | Percentage | name                     |
+-------------+----------+------------+------------+--------------------------+
| GUM         | Korean   | F          |        3.3 | Guam                     |
| JPN         | Korean   | F          |        0.5 | Japan                    |
| KOR         | Korean   | T          |       99.9 | South Korea              |
| MNP         | Korean   | F          |        6.5 | Northern Mariana Islands |
| PRK         | Korean   | T          |       99.9 | North Korea              |
| USA         | Korean   | F          |        0.3 | United States            |
+-------------+----------+------------+------------+--------------------------+
```

<br>

#### 외부 결합(Outer Join)

```sql
SELECT 선택하고 싶은 열리스트 FROM 첫번째 테이블명 LEFT OUTER JOIN 두번째 테이블명 ON 결합조건;
```

- 내부 결합은 2개의 테이블에서 결합 조건에 일치하는 것을 얻어내지만
- **외부 결합**은 2개의 테이블 중 **왼쪽 테이블(첫번째)의 전체행이 표시**되고, **다른 테이블 행 데이터는 결합조건과 일치할때** 그 값이 되고, 일치하는것 없으면 _NULL_ 이 됨

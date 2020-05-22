# 몽고디비(MongoDB)

몽고디비는 자바스크립트 문법을 사용한다. RDBMS가 아니라 SQL을 사용하지 않는 NoSQL 이다.

NoSQL은 고정된 테이블이 없고 컬렉션이라는 개념이 있다. 컬럼을 따로 정의하지 않는다. 또한 몽고디비에는 MySQL과 달리 JOIN 기능이 없다.

몽고디비를 사용하는 이유는 확잘성과 가용성 때문이다. 데이터의 일관성을 보장해주는 기능이 약한 대신 데이터를 빠르게 넣고, 쉽게 서버에 데이터 분산이 가능하다.

MySQL의 **테이블, 로우, 컬럼**을 몽고디비에서는 **컬렉션, 다큐먼트, 필드** 라고 한다.

## 설치/실행(mac)

[https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

To run MongoDB manually as a background process, issue the following:

```
mongod --config /usr/local/etc/mongod.conf --fork
```

To verify that MongoDB is running, search for mongod in your running processes:

```
ps aux | grep -v grep | grep mongod
```

```
$ brew services start mongodb-community

$ mongo

> use admin
switched to db admin
> db.createUser({ user: 'ingg', pwd: '비밀번호', roles: ['root']})
Successfully added user: { "user" : "ingg", "roles" : [ "root" ] }
```

`db.createUser`메서드로 계정 생성

```
$ brew services stop mongodb-community
$ code /usr/local/etc/mongod.conf
```

몽고디비가 인증을 사용하도록 설정

```
//(vscode)    /usr/local/etc/mongod.conf

...
security:
    authorization: enabled
```

다시 mongod 실행하고, `mongo admin -u [이름] -p [비밀번호]`로 접속

```
$ brew services start mongodb-community
$ mongo admin -u ingg -p 비밀번호
```

### 컴퍼스 설치

몽고디비 관리도구 [컴퍼스](https://www.mongodb.com/download-center/compass)를 사용하면 GUI를 통해 시각적으로 관리할 수 있다. 필수적인것은 아니고 콘솔로 같은 작업이 가능하다.

## 데이터베이스 컬렉션 생성

- 데이터베이스를 만드는 명령어는 `use [데이터베이스명]`이다.

```
> use nodejs
switched to db nodejs
```

- 데이터베이스 목록을 확인하는 명령어는 `show dbs`이다.

```
> show dbs
admin    0.000GB
config   0.000GB
in-tube  0.000GB
local    0.000GB
```

데이터를 한개 이상 넣어야 목록에 표시된다.

- 현재 사용중인 데이터베이스를 확인하는 명령어는 `db`이다.

```
> db
nodejs
```

- 다큐먼트를 넣으면 컬렉션도 생성되기 때문에 컬렉션을 따로 생성하지 않아도 되지만, 직접 넣을수도 있다.

```
> db.createCollection('users')
{ "ok" : 1 }
> db.createCollection('comments')
{ "ok" : 1 }
```

- `show collections`는 생성한 컬렉션 목록을 확인할 수 있다.

```
> show collections
comments
users
```

## CRUD

### Create(생성)

몽고디비는 기본적으로 자바스크립트 자료형을 따른다. 추가로 `Binary Data, ObjectId, Timestamp` 등이 있다.

- `db.컬렉션명.save(다큐먼트)`로 다큐먼트를 생성할 수 있다.

```
> use nodejs;
switched to db nodejs

> db.users.save({ name: 'john', age: 25, married: false, comment: '자기소개 1', createdAt: new Date()});
WriteResult({ "nInserted" : 1 })
> db.users.save({ name: 'Mary', age: 32, married: true, comment: '자기소개 2', createdAt: new Date()});
WriteResult({ "nInserted" : 1 })
```

`new Date()`는 현재 시간을 입력하라는 뜻이다. 명령이 성공적으로 수행되면 다큐먼트 한개가 생성되었다는 `WriteResult({ "nInserted" : 1 })` 응답이 나온다.

```
> db.users.find({name: 'john'}, {_id: 1})
{ "_id" : ObjectId("5e92a026b7d1397e3f40c4a5") }

> db.comments.save({commenter: ObjectId('5e92a026b7d1397e3f40c4a5'), comment: 'John의 댓글이다.', createdAt: new Date()});
WriteResult({ "nInserted" : 1 })
```

John의 아이디를 조회한후 commnets 컬렉션에도 데이터를 넣었다.

### Read(조회)

- `find({})` : 컬렉션 내의 모든 다큐먼트를 조회한다.

```
> db.users.find({})
{ "_id" : ObjectId("5e92a026b7d1397e3f40c4a5"), "name" : "john", "age" : 25, "married" : false, "comment" : "자기소개 1", "createdAt" : ISODate("2020-04-12T04:59:18.405Z") }
{ "_id" : ObjectId("5e92a065b7d1397e3f40c4a6"), "name" : "Mary", "age" : 32, "married" : true, "comment" : "자기소개 2", "createdAt" : ISODate("2020-04-12T05:00:21.542Z") }

> db.comments.find({})
{ "_id" : ObjectId("5e92a70eb7d1397e3f40c4a7"), "commenter" : ObjectId("5e92a026b7d1397e3f40c4a5"), "comment" : "John의 댓글이다.", "createdAt" : ISODate("2020-04-12T05:28:46.404Z") }
```

- 특정 필드만 가져오기 : `find`메서드 두번째 인자로 조회할 필드를 넣는다. `1`이나 `true`로 표시한 필드만 가져온다.

```
> db.users.find({}, {_id: 0, name: 1, married: 1});
{ "name" : "john", "married" : false }
{ "name" : "Mary", "married" : true }
```

`_id`는 기본적으로 가져오므로 `0`이나 `false`로 가져오지 않게 한다.

- 연산자 : `$gt(초과)`, `$gte(이상)`, `$lt(미만)`, `$lte(이하)`, `$ne(같지 않음)`, `$or(또는)`, `$in(배열 요소 중 하나)`

```
> db.users.find({ age: { $gt: 30 }, married: true }, {_id: 0, name: 1, age: 1});
{ "name" : "Mary", "age" : 32 }
```

age가 30 초과이거나 married가 true인 다큐먼트의 이름과 나이를 조회한 예시이다.

```
> db.users.find({ $or: [{ age: { $gt: 30} }, { married: false }] }, {_id: 0, name: 1, age: 1});
{ "name" : "john", "age" : 25 }
{ "name" : "Mary", "age" : 32 }
```

`$or`에 주어진 조건을 하나라도 만족하는 다큐먼트를 조회한 예시이다.

- `sort` 메서드 : 정렬 (`-1`은 내림차순, `1`은 오름차순)

```
> db.users.find({}, {_id: 0, name: 1, age: 1}).sort({ age: -1 })
{ "name" : "Mary", "age" : 32 }
{ "name" : "john", "age" : 25 }
```

- `limit` 메서드 : 조회할 다큐먼트 개수를 설정

```
> db.users.find({}, {_id: 0, name: 1, age: 1}).sort({ age: -1 }).limit(1)
{ "name" : "Mary", "age" : 32 }
```

- `skip` 메서드 : 몇 개를 건너뛸지 설정

```
> db.users.find({}, {_id: 0, name: 1, age: 1}).sort({ age: -1 }).limit(1).skip(1)
{ "name" : "john", "age" : 25 }
```

### Update(수정)

- `db.컬렉션명.update(다큐먼트)` : 첫번째는 수정할 다큐먼트를 지정하는 객체, 두번째는 수정할 내용을 입력하는 객체다.

- `$set` 은 어떤 필드를 수정할지 정하는 연산자이다. 일부 필드만 수정하려면 이 연산자를 지정한다. 이 연산자가 없으면 다큐먼트가 통째로 두번째 인자로 주어진 객체로 수정된다.

```
> db.users.update({ name: 'Mary'}, {$set: {comment: '이 필드를 수정한다.'} });
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

### Delete(삭제)

- `db.컬렉션명.remove(다큐먼트)` : 첫 번째 인자는 삭제할 다큐먼트에 대한 정보이다.

```
> db.users.remove({ name: 'Mary'})
WriteResult({ "nRemoved" : 1 })
```

## 몽구스(Mongoose)

MySQL에 시퀄라이즈가 있다면 몽고디비에는 몽구스(mongoose)가 있다. 몽구스는 시퀄라이즈와 달리 ODM(Object Document Mapping)이다. 몽고디비는 릴레이션이 아니라 다큐먼트를 사용한다.

ES2015 프로미스와 가독성이 높은 쿼리빌더를 지원한다.

```
$ express [프로젝트명] --view=pug

$ cd [프로젝트명]
$ npm install
$ npm i mongoose
```

### 몽고디비 연결

아래와 같은 형식의 주소를 사용해서 노드와 몽고디비를 연결한다.

```
mongodb://[username:password@]host[:port]/[database][?options]]
```

`[]`부분은 있어도되고 없어도된다. `username`과 `password`에 몽고디비 계정이름과 비밀번호, `host`에 localhost, `port`에 27017, `database`에 admin을 넣는다.

## Mongoku

[https://github.com/huggingface/Mongoku](https://github.com/huggingface/Mongoku)

```
$ mongoku start
```

설치하면 localhost:3100 에서 mongoDB를 관리할 수 있다.

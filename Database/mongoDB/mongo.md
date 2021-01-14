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

#### 관리자 계정 추가

```
$ brew services start mongodb-community@4.4

$ mongo

> use admin
switched to db admin
> db.createUser({ user: 'ingg', pwd: '비밀번호', roles: ['root']})
Successfully added user: { "user" : "ingg", "roles" : [ "root" ] }
```

`db.createUser`메서드로 계정 생성

```
$ brew services stop mongodb-community@4.4
$ code /usr/local/etc/mongod.conf
```

몽고디비가 인증을 사용하도록 설정

```
$ code /usr/local/etc/mongod.conf
//아래 두줄추가
...
security:
    authorization: enabled
```

다시 mongod 실행하고, `mongo admin -u [이름] -p [비밀번호]`로 접속

```
$ brew services start mongodb-community
$ mongo admin -u ingg -p 비밀번호
```

<Br>

> 업데이트

```
$ brew upgrade mongodb/brew/mongodb-community
```

<br>

#### 데이터베이스별 관리자 계정 생성

예를 들어, 도서관 관리자 계정을 추가한다고하면

- 먼저 접속

```
$ mongo -u ingg
```

- use 명령으로 데이터베이스를 선택

```
use library
```

- 데이터베이스의 관리자 계정을 추가하고 비밀번호입력
  - role: `readWrite` - 읽기만허용, `dbOwner` - 모든 수정/삭제 권한 등
  - [다른 권한 참고 mongodb: built-in-roles](https://docs.mongodb.com/manual/reference/built-in-roles/)

```
db.createUser({
    user: "subadmin",
    pwd: passwordPrompt(),
    roles: [ { role: "readWrite", db: "library" } ]
})
```

- 사용자 계정 조회는 `db.getUsers()`로 가능하다.
  - 삭제는 `db.dropUser('아이디')`

```
> db.getUsers()
[
	{
		"_id" : "library.subadmin",
		"userId" : UUID("3663cd92-3bff-4f76-b7ed-411b5afeb0ee"),
		"user" : "subadmin",
		"db" : "library",
		"roles" : [
			{
				"role" : "readWrite",
				"db" : "library"
			}
		],
		"mechanisms" : [
			"SCRAM-SHA-1",
			"SCRAM-SHA-256"
		]
	}
]
>
```

- 종료하고 다시 접속
- root 접속과 다른 점은 **뒤에 DB명을 써야함**. (안쓰면 권한문제로 오류)

```
> exit
$ mongo -u subadmin library
```

- `db` : 현재 사용중인 DB확인

```
> db
library
```

- 자료 추가해보면

```
> db.book.insert({ name:'로빈훗의 대모험' })
WriteResult({ "nInserted" : 1 })
> show dbs
library  0.000GB
```

<br>

### 컴퍼스 설치

몽고디비 관리도구 [컴퍼스](https://www.mongodb.com/download-center/compass)를 사용하면 GUI를 통해 시각적으로 관리할 수 있다. 필수적인것은 아니고 콘솔로 같은 작업이 가능하다.

## 데이터베이스 컬렉션 생성

- 데이터베이스를 만드는 명령어는 `use [데이터베이스명]`이다.

```
> use nodejs
switched to db nodejs
```

- 데이터베이스 목록을 확인하는 명령어는 `show dbs`이다.
  - 데이터를 한개 이상 넣어야 목록에 표시된다.

```
> show dbs
admin    0.000GB
config   0.000GB
in-tube  0.000GB
local    0.000GB
```

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

<br>

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

<br>

#### insert 와 save 차이

- `save()`는 **동일 id값이 들어오면 update**를 한다

```
> db.user.insert({ "_id" : 4, "name" : "ingg", "job" : "studen"})
> db.user.insert({ "_id" : 4, "name" : "ingg", "job" : "student"})

> db.user.save({ "_id" : 5, "name" : "taru", "job" : "studen"})
> db.user.save({ "_id" : 5, "name" : "taru", "job" : "student"})
```

```
> db.user.find()
{ "_id" : 4, "name" : "ingg", "job" : "studen"}
{ "_id" : 4, "name" : "ingg", "job" : "studens"}
```

<br>

### Read(조회)

- `db.collection.findOne()` : 한 객체만 조회
- `db.collection.find()` : 컬렉션 내의 모든 다큐먼트를 조회한다.

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

<br>

- 연산자 : `$gt(초과)`, `$gte(이상)`, `$lt(미만)`, `$lte(이하)`, `$ne(같지 않음)`, `$or(또는)`, `$in(배열 요소 중 하나)`, `$nin:{[ ... ]} (=not $in)`

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

<br>

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

<br>

### Update(수정)

- `db.collection.update(다큐먼트)`
  - 첫번째는 수정할 다큐먼트를 지정하는 객체
  - 두번째는 수정할 내용을 입력하는 객체
- `$set` : 어떤 필드를 수정할지 정하는 연산자. 필드가 없으면 추가한다.
  - 일부 필드만 수정하려면 이 연산자를 지정한다. 이 연산자가 없으면 다큐먼트가 통째로 두번째 인자로 주어진 객체로 수정된다.

```
> db.users.update({ name: 'Mary'}, {$set: {comment: '이 필드를 수정한다.'} });
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

<br>

### Delete(삭제)

- `db.collection.remove(다큐먼트)` : 첫 번째 인자는 삭제할 다큐먼트에 대한 정보이다.

```
> db.users.remove({ name: 'Mary'})
WriteResult({ "nRemoved" : 1 })
```

- `db.collection.deleteOne({ ... })` : 하나만
- `db.collection.deleteMany({})` : 전부삭제

<br>

## 몽구스(Mongoose)

> [https://mongoosejs.com/](https://mongoosejs.com/)

MySQL에 시퀄라이즈가 있다면 몽고디비에는 몽구스(mongoose)가 있다. 몽구스는 시퀄라이즈와 달리 ODM(Object Document Mapping)이다. 몽고디비는 릴레이션이 아니라 다큐먼트를 사용한다.

ES2015 프로미스와 가독성이 높은 쿼리빌더를 지원한다.

```
$ npm i mongoose
```

```js
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/test", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(()>{
//...
}).catch(()=>{
//...
})

```

<br>

#### Schema Types

- String
- Number
- Date
- Buffer
- Boolean
- Mixed
- ObjectId
- Array
- Decimal128
- Map
- Schema

<br>

### 몽고디비 연결

아래와 같은 형식의 주소를 사용해서 노드와 몽고디비를 연결한다.

```
mongodb://[username:password@]host[:port]/[database][?options]]
```

`[]`부분은 있어도되고 없어도된다. `username`과 `password`에 몽고디비 계정이름과 비밀번호, `host`에 localhost, `port`에 27017, `database`에 admin을 넣는다.

```js
//ex)

mongoose
  .connect("mongodb://subadmin:비밀번호@localhost:27017/library", {...}
```

<br>

## repl

```
$ node
> .load index.js

```

### Find with mongoose

- `find`

```
//모두
> Movie.find({}).then(data=>console.log(data)

//특정
> Movie.find({rating:'PG-13'}).then(data =>console.log(data))

//이상($gte)
> Movie.find({year: {$gte:2010 } }).then(data =>console.log(data))
```

- `FindByID`

```

> Movie.findById('5ffffbb0401f90eeefffdd83').then(m => console.log(m))
```

<br>

### Update with mongoose

- `updateOne`, `updateMany`

```
//title이 Amadeus인 데이터의 year을 변경
> Movie.updateOne({title: 'Amadeus'}, {year:1984}).then(res => console.log(res))
// updateMany
> Movie.updateMany({title: {$in: ['Amadeus' , 'Stand By Me']} }, {score:10}).then(res=>console.log(res))

```

- `findOneAndUpdate`
  - `updateOne` 이랑 차이 : `findOneAndUpdate`는 문서를 반환

```
// 7.0 으로 업뎃했는데 7.8나옴 (이전데이터)

> Movie.findOneAndUpdate({ title: 'The Iron Giant'}, { score: 7.0 }).then(m => console.log(m))

Promise { <pending> }
> (node:61167) DeprecationWarning: Mongoose: `findOneAndUpdate()` and `findOneAndDelete()` without the `useFindAndModify` option set to false are deprecated. See: https://mongoosejs.com/docs/deprecations.html#findandmodify
(Use `node --trace-deprecation ...` to show where the warning was created)
{
  _id: 5fffecb1bfb275e0ff8f59e3,
  title: 'The Iron Giant',
  year: 1999,
  score: 7.5,
  rating: 'PG',
  __v: 0
}
```

- 업데이트된 데이터를 return 하려면 세번째 인자로 `new` 넣는다

```
> Movie.findOneAndUpdate({ title: 'The Iron Giant'}, { score: 7.8 }, {new: true}).then(m => console.log(m))

Promise { <pending> }
> {
  _id: 5fffecb1bfb275e0ff8f59e3,
  title: 'The Iron Giant',
  year: 1999,
  score: 7.8,
  rating: 'PG',
  __v: 0
}
```

<br>

### Delete with mongoose

- `remove` (deprecated)

```
> Movie.remove({title: 'Amelie'}).then(msg => console.log(msg))
Promise { <pending> }
> (node:61167) DeprecationWarning: collection.remove is deprecated. Use deleteOne, deleteMany, or bulkWrite instead.
{ n: 2, ok: 1, deletedCount: 2 }
```

- `deleteMany`

```
// 1999이상 모두제거
> Movie.deleteMany({ year: {$gte: 1999}}).then(msg => console.log(msg))
```

- `findOneAndDelete` : 삭제한 data 반환

```
> Movie.findOneAndDelete({ title: 'Alien' }).then(m => console.log(m))

Promise { <pending> }
> {
  _id: 5fffecb1bfb275e0ff8f59e2,
  title: 'Alien',
  year: 1979,
  score: 8.1,
  rating: 'R',
  __v: 0
}
```

<br>

## [SchemaType Options](https://mongoosejs.com/docs/schematypes.html#schematype-options)

```js
const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    maxLength: 20,
  },
  price: {
    type: Number,
    required: true,
    min: 0,
  },
  onSale: {
    type: Boolean,
    default: false,
  },
  categories: [String], // string 배열. ex) ["AAA", "BBB"]
  // type: [String]
  qty: {
    online: {
      type: Number,
      default: 0,
    },
    inStore: {
      type: Number,
      default: 0,
    },
  },
  size: {
    type: String,
    enum: ["S", "M", "L"],
  },
});
```

- All Schema Types
  - `required` : true면, 필수
  - `default` : default로 값을 추가
- String
  - `maxLength` : 최대길이
  - `enum`: 검사할 배열.
- Number
  - `min`, `max`

```js
//...

const bike = new Product({
  name: "Mountain Bike",
  price: 599,
  categories: ["AAA", "BBB"],
  size: "XS", //'XS' is not valid enum
});
```

- Validation이 적용되게 하려면 세번째인자에 `runValidators:true` 추가

```js

Product.findOneAndUpdate(
  { name: "Mountain Bike" },
  { price: -9 },    //error (min:0)
  { new: true, runValidators: true }
)
  .then( ...)
```

<br>

## Mongoku

[https://github.com/huggingface/Mongoku](https://github.com/huggingface/Mongoku)

```
$ mongoku start
```

설치하면 localhost:3100 에서 mongoDB를 관리할 수 있다.

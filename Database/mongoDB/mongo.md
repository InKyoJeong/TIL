## 몽고디비(MongoDB)

몽고디비는 자바스크립트 문법을 사용한다. RDBMS가 아니라 SQL을 사용하지 않는 NoSQL 이다.

NoSQL은 고정된 테이블이 없고 컬렉션이라는 개념이 있다. 컬럼을 따로 정의하지 않는다. 또한 몽고디비에는 MySQL과 달리 JOIN 기능이 없다.

몽고디비를 사용하는 이유는 확잘성과 가용성 때문이다. 데이터의 일관성을 보장해주는 기능이 약한 대신 데이터를 빠르게 넣고, 쉽게 서버에 데이터 분산이 가능하다.

MySQL의 **테이블, 로우, 컬럼**을 몽고디비에서는 **컬렉션, 다큐먼트, 필드** 라고 한다.

### 설치/실행(mac)

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

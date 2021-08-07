## 시퀄라이즈(Sequelize)

> 시퀄라이즈는 ORM(Object-relational Mapping)으로 분류된다. ORM은 자바스크립트 객체와 데이터베이스의 릴레이션을 매핑해준다.

시퀄라이즈를 쓰는이유는 자바스크립트 구문을 알아서 SQL로 바꿔주기 때문이다.

Express-generator로 프로젝트를 생성하고 시퀄라이즈를 설치한다.

```
$ express learn-sequelize --view=pug

$ cd learn-sequelize
$ npm install
```

```
$ npm i sequelize mysql2
$ npm i -g sequelize-cli
$ sequelize init
```

config, models, migrations, seeders 폴더가 생성된다. models/index.js를 수정한다.

```js
// models/index.js
const path = require("path");
const Sequelize = require("sequelize");

const env = process.env.NODE_ENV || "development";
const config = require(__dirname + "/../config/config.json")[env];
const db = {};

const sequelize = new Sequelize(
  config.database,
  config.username,
  config.password,
  config
);

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
```

<br>

## MySQL 연결하기

시퀄라이즈로 익스프레스와 MySQL을 연결하기위해 app.js에 코드를 추가한다.

```js
//...
var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");
var sequelize = require("./models").sequelize;

var app = express();
sequelize.sync();
//...
```

**_require("./models")_** 는 **_require("./models/index.js")_** 와 같다. 폴더내의 index.js파일은 require시 이름을 생략할 수 있다. `sync`메서드는 서버실행시 MySQL과 연동되게 해준다.

<br>

## 모델 정의하기

MySQL에서 정의한 테이블을 시퀄라이즈에서도 정의해야한다.

```js
// models/user.js(추가)
module.exports = (sequelize, DataTypes) => {
  return sequelize.define(
    "user",
    {
      name: {
        type: DataTypes.STRING(20),
        allowNull: false,
        unique: true,
      },
      age: {
        type: DataTypes.INTEGER.UNSIGNED,
        allowNull: false,
      },
      married: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
      },

      comment: {
        type: DataTypes.TEXT,
        allowNull: true,
      },
      created_at: {
        type: DataTypes.DATE,
        allowNull: false,
        defaultValue: DataTypes.NOW,
      },
    },
    {
      timestamps: false,
    }
  );
};
```

시퀄라이즈는 알아서 id는 기본키로 연결한다. `sequelize.define`메서드로 테이블명과 각 컬럼의 스펙을 연결한다. MySQL 테이블과 컬럼 내용이 일치해야 정확히 대응한다.

- 시퀄라이즈 자료형은 MySQL 자료형과 조금 다르다.
  - **VARCHAR**은 `STRING`으로
  - **INT**는 `INTEGER`로
  - **TINYINT**은 `BOOLEAN`으로
  - **DATETIME** 은 `DATE`로 적는다.
  - `INTEGER.UNSIGNED`는 UNSIGNED옵션이 적용된 INT이다. ZEROFILL옵션도 이어서 붙일수 있다.
  - `defaultValue`는 기본값이다. `DataTypes.NOW`로 현재 시간을 기본값으로 설정할 수 있다. SQL의 **now()** 와 같다.
  - `allowNull`은 **NOT NULL**과 같다. `unique`는 **UNIQUE**와 같다.

define 메서드의 **세번째 인자는 테이블 옵션**이다. `timestamps`속성이 `true`면 시퀄라이즈는 `createdAt`과 `updatedAt` 컬럼을 추가한다. (로우의 생성,수정 시간이 자동으로 입력)

예제에서는 직접 **created_at** 컬럼을 만들었으므로 false로 한다.

```js
// models/comment.js(추가)
module.exports = (sequelize, DataTypes) => {
  return sequelize.define(
    "comment",
    {
      comment: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
      created_at: {
        type: DataTypes.DATE,
        allowNull: true,
        defaultValue: DataTypes.NOW,
      },
    },
    {
      timestamps: false,
    }
  );
};
```

Comment 모델에 users 테이블과 연결된 commenter 컬럼이 없는 이유는, 모델을 정의할때 넣어도 되지만 시퀄라이즈 자체에서 관계를 따로 정의할 수 있기 때문이다.

이렇게 user, comment 모델을 생성한 후 _models/index.js_ 와 연결한다.

```js
// models/index.js
//...
db.sequelize = sequelize;
db.Sequelize = Sequelize;

db.User = require("./user")(sequelize, Sequelize);
db.Comment = require("./comment")(sequelize, Sequelize);

module.exports = db;
```

db 객체에 User와 Comment 모델을 담았다.

```js
// config/config.json
{
  "development": {
    "username": "root",
    "password": "MySQL 비밀번호",
    "database": "nodejs",
//...
```

development.password와 development.databse를 MySQL 커넥션과 일치하게 수정한다. test와 production은 테스트와 배포용이므로 나중에 사용한다.

<br>

## 관계 정의하기

> 1:N 관계, 일대일, 다대다 관계가 있다.

#### 1:N

시퀄라이즈에서 1:N 관계는 `hasMany`라는 메서드로 표현한다. 반대로 불러올땐 `belongsTo`메서드를 사용한다.

```
User    ---(hasMany)--->   Comment
User    <---(belongsTo)---   Comment
```

모델을 연결해준 곳 밑에 추가로 넣는다.

```js
// models/index.js
//...
db.User = require("./user")(sequelize, Sequelize);
db.Comment = require("./comment")(sequelize, Sequelize);

db.User.hasMany(db.Comment, { foreignKey: "commenter", sourceKey: "id" });
db.Comment.belongsTo(db.User, { foreignKey: "commenter", targetKey: "id" });

module.exports = db;
```

User 모델의 `id`가 Comment 모델의 `commenter` 컬럼에 들어간다.

`npm start` 명령으로 스퀄라이즈가 실행하는 SQL문을 확인할 수 있다.

```
Executing (default): CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER NOT NULL auto_increment , `name` VARCHAR(20) NOT NULL UNIQUE, `age` INTEGER UNSIGNED NOT NULL, `married` TINYINT(1) NOT NULL, `comment` TEXT, `created_at` DATETIME NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB;
Executing (default): SHOW INDEX FROM `users` FROM `nodejs`
Executing (default): CREATE TABLE IF NOT EXISTS `comments` (`id` INTEGER NOT NULL auto_increment , `comment` VARCHAR(100) NOT NULL, `created_at` DATETIME, `commenter` INTEGER, PRIMARY KEY (`id`), FOREIGN KEY (`commenter`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE=InnoDB;
Executing (default): SHOW INDEX FROM `comments` FROM `nodejs`
```

`IF NOT EXISTS`는 테이블이 존재하지않으면 실행된다는 뜻이다. 지금은 콘솔로 테이블을 만들어뒀으므로 실행되지않는다.

#### 1:1

1:1 관계는 `hasMany`메서드 대신 `hasOne`메서드를 사용한다.

```js
//ex)
db.User.hasOne(db.Info, { foreignKey: "user_id", sourceKey: "id" });
db.Info.belongsTo(db.User, { foreignKey: "user_id", targetKey: "id" });
```

1:1 관계이므로 belongsTo와 hasOne이 반대여도 상관없다.

#### N:M

다대다 관계는 `belongsToMany` 메서드가 있다. `through`속성에 이름을 적는다.

```js
//ex)
db.Post.belongsToMany(db.Hashtag, { through: "PostHashtag" });
db.Hashtag.belongsToMany(db.Hashtag, { through: "PostHashtag" });
```

해시태그를 찾으면 그 해시태그에서 `get + 모델이름의 복수형` 메서드를 바로 사용할 수 있다.

```js
//노드 해시태그를 사용한 게시물을 조회하는 예시
async (req, res, next) => {
  const tag = await Hashtag.find({ where: { title: "노드" } });
  const posts = await tag.getPosts();
};
```

`add + 모델 이름의 복수형` 메서드도 있다. 두 테이블 간 N:M 관계를 추가해준다.

```js
//title이 노드인 해시태그와 게시글 아이디가 3인 게시글을 연결하는 코드
async (req, res, next) => {
  const tag = await Hashtag.find({ where: { title: "노드" } });
  await tag.addPosts(3);
};
```

<Br>

## 쿼리

시퀄라이즈로 CRUD 작업을 하려면 시퀄라이즈 쿼리에 대해 알아야한다.

### create: 로우를 생성하는 쿼리

```js
//MySQL:
INSERT INTO nodejs.users (name, age, married, comment) VALUES ('zero', 24, 0, '자기소개1');

//시퀄라이즈 쿼리:
const { User} = require('../models')
User.create({
    name: 'zero',
    age: 24,
    married: false,
    comment: '자기소개1'
})
```

models 모듈에서 User 모델을 불러와 `create` 메서드를 사용한다. 데이터를 넣을때는 시퀄라이즈 모델에 정의한 자료형대로 넣어야한다.

#### findOrCreate: 특정 요소를 검색하거나, 존재하지 않으면 새로 생성

- `findOrCreate` 메서드는 DB에 특정 요소가 존재하는지 검사
- 만약 존재한다면 해당하는 인스턴스를 반환, 그렇지 않으면 새로 생성

#### `findOrCreate` 메서드는 검색되었거나 또는 생성된 객체를 포함한 배열, 그리고 boolean값을 반환한다.

```bash
# ex)
[ { name:’xxx’,age:’21’}, true ]
```

<br>

### find, findAll: 로우를 조회하는 쿼리

```js
// users테이블의 모든 데이터 조회하는 SQL
//MySQL:
SELECT * FROM nodejs.users;
//시퀄라이즈 쿼리:
User.findAll({});

// users 테이블의 데이터를 하나만 가져오는 SQL
//MySQL:
SELECT * FROM nodejs.users LIMIT 1;
//시퀄라이즈 쿼리:
User.find({});

// 원하는 컬럼만 가져오기
//MySQL:
SELECT name, married FROM nodejs.users;
//시퀄라이즈 쿼리:
User.findAll({
    attributes: ['name', 'married'],
})
```

데이터를 하나만 가져올때는 `find` 메서드, 여러개 가져올때는 `findAll` 메서드를 사용한다.

```js
// 조건들을 나열하기
//MySQL:
SELECT name, age, FROM nodejs.users WHERE married = 1 AND age > 30;
//시퀄라이즈 쿼리:
const {
  User,
  Sequelize: { Op },
} = require("../models");

User.findAll({
  attributes: ["name", "age"],
  where: {
    married: 1,
    age: { [Op.gt]: 30 },
  },
});
```

```js
//MySQL:
SELECT id, name FROM users WHERE married = 0 OR age > 30;
//시퀄라이즈 쿼리:
const {
  User,
  Sequelize: { Op },
} = require("../models");
User.findAll({
  attributes: ["id", "name"],
  where: {
    [Op.or]: [{ married: 0 }, { age: { [Op.gt]: 30 } }],
  },
});
```

`where`옵션이 조건들을 나열하는 옵션이다. Sequelize 객체 내부의 `Op` 객체를 불러와 사용한다.

자주쓰이는 연산자는 `Op.gt(초과)`, `Op.gte(이상)`, `Op.lt(미만)`, `Op.lte(이하)`, `Op.ne(같지않음)`, `Op.or(또는)`, `Op.in(배열 요소중 하나)`, `Op.notIn(배열요소와 모두다름)`이 있다.

```js
//정렬 방식
//MySQL:
SELECT id, name, FROM users ORDER BY age DESC;
//시퀄라이즈 쿼리:
User.findAll({
  attributes: ["id", "name"],
  order: [["age", "DESC"]],
});
```

`order`옵션으로 정렬하는 방식이다.

```js
// 조회할 로우 개수를 설정하기
//MySQL:
SELECT id, name FROM users ORDER BY age DESC LIMIT 1;
//시퀄라이즈 쿼리:
User.findAll({
  attributes: ["id", "name"],
  order: ["age", "DESC"],
  limit: 1,
});
```

`offset`속성도 사용할 수 있다.

```js
//MySQL:
SELECT id, name FROM users ORDER BY age DESC LIMIT 1 OFFSET 1;
//시퀄라이즈 쿼리:
User.findAll({
  attributes: ["id", "name"],
  order: ["age", "DESC"],
  limit: 1,
  offset: 1,
});
```

### update: 로우를 수정하는 쿼리

`update`메서드로 수정할 수 있다. **첫번째 인자**는 수정할 내용, **두번째 인자**는 수정 대상 로우를 찾는조건이다. `where`옵션에 조건을 적는다.

```js
//MySQL:
UPDATE nodejs.users SET comment = '바꿀 내용' WHERE id = 2;
//시퀄라이즈 쿼리:
User.update(
  {
    comment: "바꿀 내용",
  },
  {
    where: { id: 2 },
  }
);
```

### destroy: 로우를 삭제하는 쿼리

```js
//MySQL:
DELETE FROM nodejs.users WHERE id = 2;
//시퀄라이즈 쿼리:
User.destroy({
  where: { id: 2 },
});
```

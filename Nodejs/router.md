## Router

```js
const express = require("express");
const router = express.Router();
```

- 요청 메서드와 주소별로 분기 처리하면 코드가 복잡해짐
  - Router로 라우팅을 깔끔하게 관리할 수 있음

```js
// routes/shelters.js
router.get("/", (req, res) => {
  res.send("All Shelters");
});

router.post("/", (req, res) => {
  res.send("Create posts");
});

router.get("/:id", (req, res) => {
  res.send("View one shelter");
});

router.get("/:id/edit", (req, res) => {
  res.send("Edit one shelter");
});
```

```js
// routes/dogs.js
router.get("/", (req, res) => {
  res.send("All Shelters");
});

router.get("/:id", (req, res) => {
  res.send("View one dog");
});

router.get("/:id/edit", (req, res) => {
  res.send("Edit one dog");
});
```

```js
// index.js
const shelterRoutes = require("./routes/shelters");
const dogRoutes = require("./routes/dogs");

app.use("/shelters", shelterRoutes);
app.use("/dogs", dogRoutes);

//localhost:3000/dogs         => All Shelters
//localhost:3000/dogs/1       => View one dog
//localhost:3000/dogs/1/edit  => Edit one dog
```

<br>

## Middleware

```js
// admin.js

router.use((req, res, next) => {
  if (req.query.isAdmin) {
    next();
  }
  res.send("Sorry Not Admin");
});

router.get("/secret", (req, res) => {
  res.send("This is Secret!");
});

router.get("/deleteeverything", (req, res) => {
  res.send("Deleted ALL!!");
});
```

```js
//index.js
app.use("/shelters", shelterRoutes);
app.use("/dogs", dogRoutes);
app.use("/admin", adminRoutes);
```

```
.../admin/secret                => Sorry Not Admin
.../admin/secret?isAdmin=true   => This is Secret!
```

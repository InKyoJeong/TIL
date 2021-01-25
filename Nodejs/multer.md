## Multer

- 파일 업로드를 위해 사용되는 `multipart/form-data`를 다루기 위한 node.js의 미들웨어

### 설치 & 사용

#### Install

```
$ npm i multer
```

<br>

#### Usage

- app.js

```js
const express = require("express");
const multer = require("multer");
const upload = multer({ dest: "uploads/" });
//파일이 uploads/ 폴더 내에 저장됨
```

- html

```html
<input type="file" name="image" id="" />
```

- router
  - `input name`과 매치시켜야함 (_"image"_)

```js
app.post("/profile", upload.single("image"), (req, res) => {
  // req.file 은 `image` 라는 필드의 파일 정보
  // 텍스트 필드가 있는 경우, req.body가 이를 포함
  console.log(req.body, req.file);
  //  [Object: null prototype] {
  //   campground: [Object: null prototype] {
  //     title: 'testtest',
  //     location: 'testtest',
  //     price: '11',
  //     description: 'testtest'
  //   }
  // } {
  //   fieldname: 'image',
  //   originalname: '이미지파일이름.png',
  //   encoding: '7bit',
  //   mimetype: 'image/png',
  //   destination: 'uploads/',
  //   filename: 'f283374335287ad76ebba76dcc28ea30',
  //   path: 'uploads/f283374335287ad76ebba76dcc28ea30',
  //   size: 1127827
  // }
  res.send("It works!!");
});
```

<br>

- 다수 이미지 : `.array`메서드 사용

```html
<input type="file" name="image" id="" multiple />
```

```js
app.post(upload.array("image"), (req, res) => {
  console.log(req.body, req.files);
  res.send("It works!!");
});
```

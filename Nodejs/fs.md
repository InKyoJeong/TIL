## 파일 시스템

- `fs` 모듈은 파일 시스템에 접근하는 모듈
  - 폴더 생성/삭제, 파일 생성/삭제/읽거나 쓸수 있다.

```js
fs.readFile("./kepler_data.csv", (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data);
  // $ node index.js
  // <Buffer 23 20 54 68 69 73 20 66 69 6c 65 20 77 61 73 20 70 72 6f 64 75 63 65 64 20 62 79 20 74 68 65 20 4e 41 53 41 20 45 78 6f 70 6c 61 6e 65 74 20 41 72 63 ... 3650420 more bytes>
  console.log(data.toString());
  // 제대로 출력됨
});
```

- `readFile` 결과물은 버퍼라는 형식으로 제공됨
- 파일을 변환해야 하는 이유는 data가 버퍼이기 때문
- `toString()`으로 문자열로 변환하면 제대로 출력됨

## 버퍼와 스트림

- 파일을 읽거나 쓰는 방식에는 크게 버퍼, 스트림을 이용하는 두가지 방식이 있다.
- 노드는 파일 읽을때 메모리에 파일크기 공간만큼 마련해두고, 파일 데이터를 메모리에 저장한뒤 사용자가 조작할 수 있게 해준다.
  - **메모리에 저장된 데이터**가 바로 버퍼

<br>

#### readFile() 방식의 버퍼의 문제점

- 만약 용량이 100메가면, 메모리에 100메가 버퍼를 만들어야한다. 이작업을 동시에 열개만 해도 1기가 메모리가 사용됨.
- 또한 모든 내용을 다 써야 다음으로 넘어가서, 매번 전체 용량을 버퍼로 처리해야 함

#### 스트림

- 버퍼의 크기를 작게 만들어서 여러번 나눠 보내는 방식
  - ex) 버퍼 1메가 만든후 100메가 파일을 백번에 걸쳐 보낸다.
  - 그러면 메모리 1메가로 100메가 파일을 전송할 수 있다.
- `createReadStream` : 파일을 읽는 스트림 메서드
- `pipe` : 읽기 가능한 스트림의 출력과 쓰기 가능한 스트림의 입력을 파이프로 연결. `readable.pipe(writable)`

```
   (createReadStream)
csv     ---->   ==(pipe)==   ---->   변환(객체 배열)
                            (parse)
```

```js
const parse = require("csv-parse");
const fs = require("fs");

const results = [];

fs.createReadStream("kepler_data.csv")
  .pipe(
    parse({
      comment: "#",
      columns: true,
    })
  )
  .on("data", (data) => {
    results.push(data);
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    console.log(results);
    console.log("done");
  });
```

```bash
$ node index.js
...(생략)
   koi_srad_err2: '-0.0340',
    ra: '285.283630',
    dec: '38.947281',
    koi_kepmag: '15.403'
  },
  ... 9464 more items
]
done
```

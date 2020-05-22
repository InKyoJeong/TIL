# 파일에 문자열 쓰기, 읽기

## 파일에 문자열 쓰기

> 파일에 문자열을 쓸 때는 `open`함수로 파일을 열어서 파일 객체(file object)를 얻은 뒤 `write`메서드를 사용한다.

- `파일객체 = open(파일이름, 파일모드)`
- `파일객체.write('문자열')`
- `파일객체.close()`

```py
>>> file = open('hello.txt','w')
>>> file.write('Hellllllllllll')
>>> file.close()
```

## 파일에서 문자열 읽기

- 파일을 읽을 때도 `open`함수로 파일을 열어 파일 객체를 얻은 뒤 `read`메서드로 파일의 내용을 읽는다.
- 단, 이때는 파일 모드를 읽기모드 `'r'`로 지정한다.
- `변수 = 파일객체.read()`

```py
>>> file = open('hello.txt','r')
>>> s = file.read()
>>> print(s)
Hellllllllllll
>>> file.close()
```

### 자동으로 파일 객체 닫기

- 파이썬에서는 `with as`를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫아준다.

```py
>>> with open('hello.txt', 'r') as file:
        s = file.read()
        print(s)

Hellllllllllll
```

- `read`로 파일을 읽고나서 `close`를 사용하지 않음
- `with as`를 사용하면 파일 객체를 자동으로 닫아준다.

<br>

# 문자열 여러 줄을 파일에 쓰기, 읽기

## 반복문으로 문자열 여러 줄을 파일에 쓰기

> 문자열 여러 줄을 쓰려면 간단하게 반복문을 사용하면 됨

```py
>>> with open('hello.txt', 'w') as file:
        for i in range(3):
            file.write('Helllllooooooo {0}\n'.format(i))
```

- `py`파일이 있는 폴더의 `hello.txt`파일을 열어보면 다음과같이 저장되어있다.

```
Helllllooooooo 0
Helllllooooooo 1
Helllllooooooo 2
```

## 리스트에 들어있는 문자열을 파일에 쓰기

- `파일객체.writelines(문자열리스트)`

```py
>>> lines = ['안녕하세요.\n', '제 이름은\n', '파이썬입니다.\n']
>>> with open('hello.txt', 'w') as file:
    	file.writelines(lines)

# hello.txt
안녕하세요.
제 이름은
파이썬입니다.
```

## 파일의 내용을 한 줄씩 리스트로 가져오기

- `read`는 파일의 내용을 읽어서 문자열로 가져오지만 `readlines`는 파일의 내용을 한 줄씩 리스트 형태로 가져온다.

## 파일의 내용을 한 줄씩 읽기

- 파일의 내용을 한 줄씩 순차적으로 읽으려면 `readline`을 사용한다.

<br>

# 파이썬 객체를 파일에 저장하기, 가져오기

- 파이썬은 객체를 파일에 저장하는 `pickle`모듈을 제공한다.
- 파이썬 객체를 파일에 저장하는 과정을 피클링, 파일에서 객체를 읽어오는 과정을 언피클링 이라고 한다.

## 파이썬 객체를 파일에 저장하기

- 피클링은 `pickle`모듈의 `dump`메서드를 사용한다.

## 파일에서 파이썬 객체 읽기

- 언피클링은 `pickle`모듈의 `load`를 사용한다.
- 언피클링을 할때는 파일 모드를 바이너리 읽기모드 `'rb'`로 지정해야한다.

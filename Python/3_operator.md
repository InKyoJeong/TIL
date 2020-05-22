# 불과 비교 연산자

## 불과 비교 연산자 사용

불은 `True, False`로 표현하면 값의 일종이다.

```py
>>> True
True
>>> False
False
```

## 비교 연산자 판단 결과

- 파이썬에서는 비교연산자와 논리연산자의 판단 결과로 `True, False`를 사용
- 부등호 `>`로 두 숫자를 비교

```py
>>> 3 > 1
True
```

## 숫자가 같은지 다른지 비교

두 숫자가 같은지 비교할 때는 `==` 다른지 비교할 때는 `!=`사용

```py
>>> 9 == 9
True
>>> 9 != 9
False
```

## 문자열 비교

숫자뿐만 아니라 문자열도 비교할 수 있다. 대소문자를 구분한다.

```py
>>> 'Hello' == 'Hello'
True
>>> 'HELLO' == 'hello'
False
```

## 객체가 같은지 다른지 비교

`==`, `!=`는 값 자체를 비교하고, `is`, `is not`은 객체를 비교한다.

```py
>>> 1 == 1.0
True
>>> 1 is 1.0
False
```

`is`로 했을때 `False`가 나오는 것은 `1`은 정수 객체, `1.0`은 실수 객체이므로 두 객체는 다르기 때문이다.

### 정수 객체와 실수 객체가 서로 다른것을 확인하기

`id`는 객체의 고유한 값(메모리 주소)를 구한다. (이 값은 파이썬을 실행하는 동안에는 유지되나 다시실행하면 달라짐)

```py
>>> id(1)
4321631024
>>> id(1.0)
4358703152
```

`1`과 `1.0`은 두 객체의 고유한 값이 다르므로 서로 다른 객체이다.

### 값 비교에 is를 쓰지말자

변수 `a`에 `-5`를 할당한 뒤 `a is -5`를 실행하면 `True`가 나오지만 다시 `-6`을 할당하고 `a is -6`을 실행하면 `False`가 나온다.

```py
>>> a = -5
>>> a is -5
True
>>> a = -6
>>> a is -6
False
```

변수 `a`가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 때문이다.<br>따라서 값(숫자)를 비교할때는 `is`가 아닌 비교연산자를 사용한다.

## 논리 연산자 사용

논리 연산자는 `and`, `or`, `not`이 있다.

### and

```py
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>>
```

`and`는 두 값이 모두 `True`여야 `True`이다.

### or

```py
>>> True or True
True
>>> True or False
True
>>> False or False
False
```

`or`는 두 값 중 하나라도 `True`면 `True`이다.

### not

```py
>>> not True
False
>>> not False
True
```

`not`은 논리값을 뒤집는다.

- `and, or, not` 논리 연산자가 식 하나에 들어있으면 `not`, `and`, `or`순으로 판단한다.

```py
>>> not True and False or not False
True
```

## 논리 연산자와 비교 연산자를 함께 사용

```py
>>> 10 == 10 and 7 != 3
True
>>> 10 != 10 or 7 == 7
True
>>> 10 > 5 or 10 < 5
True
>>> not 1 is 1.0
True
```

비교 연산자`(is, is not, ==, !=, <, >)`를 먼저 판단하고 논리 연산자`(not, and, or)`를 판단한다.

### 정수, 실수 , 문자열을 불로 만들기

- 정수 `1`은 `True`, `0`은 `False`이다.
- 정수 `0`, 실수 `0.0`이외의 모든 숫자는 `True`이다.
- 빈 문자열 `''`, `""`를 제외한 모든 문자열은 `True`이다.

```py
>>> bool(1)
True
>>> bool(0)
False
>>> bool(1234354657)
True
>>> bool('Hi')
True
```

## 단락 평가

- 논리 연산에서 중요한 부분이 단락 평가(short-circuit evalution)이다.
- 단락 평가는 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인(평가)하지 않는 방법이다.
- `and`연산자는 두 값이 모두 참이어야 참이므로 첫 번째 값이 `False`면 두 번째 값은 확인하지 않고 바로 `False`로 결정한다.

```py
print(False and True)   # False
```

```py
>>> False and 'Python'
False
>>> 0 and 'Python'      # 0은 False이므로 두번째 값을 평가X
0
```

<br>

- `or`연산자는 두 값중 하나만 참이여도 참이므로 첫 번째 값이 `True`면 두 번째 값은 확인하지않고 바로 `True`로 결정한다.

```py
print(True or True)     # True
```

- 파이썬에서 논리 연산자는 이 단락 평가에 따라 반환하는 값이 결정된다.

```py
>>> True and 'Python'
'Python'
```

- 문자열 `'Python'` 도 불로 따지면 `True`라서 `True and True`가 되어 `True`가 나올것 같지만 `'Python'`이 나온다.

- 파이썬에서 논리 연산자는 **마지막으로 단락 평가를 실시한 값**을 그대로 반환하기 때문이다.

  <br>

```py
>>> 'Python' and True
True
```

물론 마지막으로 단락 평가를 실시한 값이 이렇게 불이면 불을 반환한다.

## 문자열 사용하기

### 여러줄로 된 문자열 사용

`'''(작음따옴표 3개)` 로 시작하고 엔터를 누르고 마지막줄에서 `'''`로 닫는다.

```py
>>> hello = '''Hello
my name
is'''
>>> print(hello)
Hello
my name
is
```

### 문자열 안에 작은따옴표나 큰따옴표 포함하기

- 문자열 안에 `'(작은따옴표)`를 넣고 싶다면 문자열을 `"(큰따옴표)`로 묶어준다.

```py
>>> hi = "Python isn't difficult"
>>> hi
"Python isn't difficult"
```

- 반대로 `"(큰따옴표)`를 넣고 싶다면 문자열을 `'(작은따옴표)`로 묶어준다.

```py
>>> hi = 'He said "Hi"'
>>> hi
'He said "Hi"'
```

#### 따옴표를 포함하는 다른 방법

> 작은따옴표 안에 작은따옴표를 넣을 수 있다. 작은따옴표 앞에 역슬래시를 붙인다.

```py
>>> 'Python isn\'t difficult'
"Python isn't difficult"
```

문자열 안에 특수문자를 포함하기 위에 앞에 `\`를 붙이는 방법을 `이스케이프`라고 한다.

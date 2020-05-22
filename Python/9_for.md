# for, while 반복문과 중첩

## 1. for와 range사용하기

```py
for 변수 in range(횟수):
    반복할 코드
```

```py
>>> for i in range(10):
	    print('Hello')

# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
```

### 시작하는 숫자와 끝나는 숫자 지정하기

```py
>>> for i in range(5,12):
    	print('Hello', i)

# Hello 5
# Hello 6
# Hello 7
# Hello 8
# Hello 9
# Hello 10
# Hello 11
```

### 증가폭 사용하기

```py
>>> for i in range(0,12,2):
    	print('Hello', i)

# Hello 0
# Hello 2
# Hello 4
# Hello 6
# Hello 8
# Hello 10

>>> for i in range(5,0,-1):
    	print('Hello', i)

# Hello 5
# Hello 4
# Hello 3
# Hello 2
# Hello 1
```

## 숫자를 감소시키기

> 증가폭을 음수로 지정하는 방법 외에도 reversed를 사용하면 숫자의 순서를 뒤집을 수 있다.

```py
>>> for i in reversed(range(5)):
    	print('Hello', i)

# Hello 4
# Hello 3
# Hello 2
# Hello 1
# Hello 0

```

## 시퀀스 객체로 반복하기

- for에 range대신 리스트를 넣으면 리스트의 요소를 꺼내면서 반복한다.

```py
>>> a = [10,20,30,40,50]
>>> for i in a:
    	print(i)

# 10
# 20
# 30
# 40
# 50
```

- 튜플도 튜플의 요소를 꺼내면서 반복한다.

```py
>>> fruits = ('apple', 'kiwi', 'orange')
>>> for i in fruits:
    	print(i)

# apple
# kiwi
# orange
```

- 문자열도 문자를 하나씩 꺼내면서 반복한다.

```py
>>> for letter in 'Python':
	    print(letter)

# P
# y
# t
# h
# o
# n

>>> for letter in 'Python':
	    print(letter, end=' ')


# P y t h o n

>>> for letter in reversed('Python'):
    	print(letter, end=' ')

# n o h t y P
```

## 2. while 반복문

```py
초기식
while 조건식:
    반복할 코드
    변화식
```

- while문으로 반복출력하기

```py
>>> i = 0
>>> while i < 5:
    	print('Hi')
    	i += 1

# Hi
# Hi
# Hi
# Hi
# Hi
```

- 입력한 횟수대로 반복하기

```py
>>> count = int(input('반복할 횟수를 입력 :'))

>>> i = 0
>>> while i < count:
	    print('Hello', i)
	    i += 1

# 반복할 횟수를 입력 :5
# Hello 0
# Hello 1
# Hello 2
# Hello 3
# Hello 4
```

## 반복 횟수가 정해지지 않은 경우

- 난수(random number)란 규칙없이 무작위로 나열되는 수
- 파이썬에서 난수를 생성하려면 `random`모듈이 필요함
- `import`키워드로 가져올 수 있다.

```py
>>> import random
>>>
>>> random.random()
0.9717721666844628
```

### 난수 범위 지정

- `randint`함수는 난수를 생성할 범위를 지정한다. 범위에 지정한 숫자도 난수에 포함한다.

```py
>>> random.randint(1, 6)
3
>>> random.randint(1, 6)
6
```

<br>

- 1과 6사이의 난수를 생성한 뒤 3이 나오면 반복을 끝내는 예제

```py
>>> import random
>>> i = 0
>>> while i != 3:
	    i = random.randint(1,6)
	    print(i)

# 4
# 6
# 6
# 1
# 4
# 2
# 3
```

## while 반복문으로 무한루프 만들기

- `True`또는 True로 취급하는 값을 사용하면 무한루프로 동작한다.

```py
>>> while True:
	    print('Hello')


# Hello
# Hello
# Hello
# Hello
# Hello
# ...
```

## break로 반복문 끝내기

- 변수 i가 5일때 반복문 끝내는 예제

```py
>>> i = 0
>>> while True:
    	print(i)
	    i += 1
	    if i == 5:
	    	break

# 0
# 1
# 2
# 3
# 4
```

### for에서 break로 반복문 끝내기

- while뿐만 아니라 for에서도 동작은 같다.

```py
>>> for i in range(100):
	    print(i)
	    if i == 5:
	    	break

# 0
# 1
# 2
# 3
# 4
# 5
```

## continue로 코드 실행 건너뛰기

`break`는 반복문을 완전히 빠져나오지만 `continue`는 아래의 명령을 수행하지 않으면서 반복문을 다시 시작한다.

- 0부터 99까지 for로 반복하면서 홀수만 출력하기

```py
>>> for i in range(100):
	    if i % 2 == 0:      # 짝수가 아니면 출력, 짝수면 다시 반복
	    	continue
	    print(i)


# 1
# 3
# 5
# ...(생략)
# 95
# 97
# 99
```

## 3. 중첩 루프 사용하기

```
for i in range(횟수):
    for j in range(횟수):
        가로 처리 코드
    세로 처리 코드
```

## 사각형으로 별 출력

```py
>>> for i in range(5):                 # 바깥루프는 세로방향
	    for j in range(5):         # 안쪽루프는 가로방향
	    	print('*', end='')     # end에 ''를 지정하여 줄바꿈 하지않음
    	print()

# *****
# *****
# *****
# *****
# *****
```

## 계단식으로 별 출력

```py
>>> for i in range(5):
    	for j in range(5):
	    	if j <= i:
		    	print('*', end='')
	    print()

# *
# **
# ***
# ****
# *****
```

## 대각선으로 별 출력

```py
>>> for i in range(5):
	    for j in range(5):
	    	if i == j:
	    		print('*', end='')
	    	else:
	    		print(' ', end='')
    	print()

# *
#  *
#   *
#    *
#     *
```

## FizzBuzz 문제

> FizzBuzz는 간단한 프로그래밍 규칙이며 규칙은 다음과 같다.

1. 1에서 100까지 출력
2. 3의배수는 Fizz 출력
3. 5의배수는 Buzz 출력
4. 3과 5의 공배수는 FizzBuzz 출력
   <br>

- 1부터 100까지 숫자 출력하기

```py
>>> for i in range(1,101):
    	print(i)

# 1
# 2
# 3
# ... (생략)
# 99
# 100
```

- 3의 배수일 때와 5의 배수일 때 처리하기

```py
>>> for i in range(1,101):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# 1
# 2
# Fizz
# ... (생략)
# 97
# 98
# Fizz
# Buzz
```

- 3과 5의 공배수 처리하기

```py
>>> for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else
            print(i)

# 1
# 2
# Fizz
# ... (생략)
# FizzBuzz
# 91
# 92
# Fizz
# ...
# 98
# Fizz
# Buzz
```

`and`를 사용하지 않고 `i % 15 == 0` 으로 바로 처리해도 된다.

### 코드 단축하기

위의 코드는 이렇게 단축시킬 수도 있다.

```py
>>> for i in range(1,101):
    	print('Fizz' * (i % 3 ==0) + 'Buzz' * (i % 5 == 0) or i)

# 결과는 위와 같다.
```

### 코드 골프

> 소스코드의 문자 수를 최대한 줄여서 작성하는 놀이

- 문자열을 곱하면 문자열이 반복되고, 문자열을 더하면 두 문자열이 연결된다.
- 문자열에 `True`를 곱하면 문자열이 그대로 나오고, `False`를 곱하면 문자열이 출력되지 않는다.

```py
>>> 'Fizz' + 'Buzz'
'FizzBuzz'
>>> 'Fizz' * True
'Fizz'
>>> 'Buzz' * False
''
```

#### 코드 골프 - 코드 단축하기

- 문자열 곱셉으로 3의 배수일 때 'Fizz'를 출력

  ```
  'Fizz' * (i % 3 == 0)`
  ```

- 문자열 덧셈으로 3과 5의 공배수일때는 'FizzBuzz'를 출력

  ```
  'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
  ```

- 3또는 5의 공배수가 아닐때는 `'Fizz' * False + 'Buzz' * False`가 되고 그 결과 `''`(빈문자열) 이 되는데, 이때는 `or`연산자를 사용
  ```
  'Fizz' * (i % 3 ==0) + 'Buzz' * (i % 5 == 0) or i
  ```

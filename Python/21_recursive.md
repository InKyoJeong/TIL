# 1. 함수에서 재귀호출 사용하기

- 함수안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 한다.
- 재귀호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할때 매우 유용하다.
- 보통 알고리즘에 따라서 반복문으로 구현한 코드보다 재귀호출로 구현한 코드가 좀 더 직관적이고 이해하기 쉬운 경우가 많다.

## 재귀호출에 종료 조건 만들기

```py
>>> def hello(count):
        if count == 0:          # 종료조건 만듦. count가 0이면 끝냄
            return

        print('Hello, world', count)

        count -= 1              # count를 1감소시킨뒤
        hello(count)            # 다시 hello에 넣음


>>> hello(5)                    # hello함수 호출
# Hello, world 5
# Hello, world 4
# Hello, world 3
# Hello, world 2
# Hello, world 1
```

## 재귀호출로 팩토리얼 구하기

- 팩토리얼은 1부터 n까지 양의 정수를 차례로 곱한 값이며 `!`기호로 표기

```py
>>> def factorial(n):
        if n == 1:
            return 1            # 1을 반환하고 재귀호출을 끝냄
        return n * factorial(n - 1)

>>> factorial(5)
# 120
```

# 2. 람다 표현식 사용하기

- 람다 표현식은 식 형태로 되어 있다고 해서 람다 표현식(lambda expression)이라고 부른다.
- 람다 표현식은 함수를 간편하게 작성할 수 있어 다른 함수의 인수로 넣을때 주로 사용한다.
- `lambda 매개변수들: 식`

```py
>>> def plus_ten(x):
	    return x + 10

>>> plus_ten(1)
# 11
>>> lambda x: x +10
# <function <lambda> at 0x10792a050>
```

## 람다 표현식으로 함수 만들기

- 람다표현식은 이름이 없는 함수를 만들기 때문에 이 상태로는 함수를 호출할 수 없다.
- 람다표현식을 익명함수(anonymous function)로 부르기도 한다.
- lambda로 만든 익명함수를 호출하려면 람다표현식을 변수에 할당해주면 된다.

```py
>>> plus_ten = lambda x: x + 10
>>> plus_ten(2)
# 12
```

### 람다 표현식 자체를 호출하기

- 람다 표현식은 변수에 할당하지 않고 람다 표현식 자체를 바로 호출할 수 있다.
- `(lambda 매개변수들: 식)(인수들)`

```py
>>> (lambda x: x + 10)(1)
# 11
```

### 람다 표현식 안에는 변수를 만들 수 없다.

- 변환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야함
- 변수가 필요한 코드일 경우 `def`로 함수를 작성하는 것이 좋음
- 람다 표현식 바깥에 있는 변수는 사용할 수 있음

```py
>>> y = 10
>>> (lambda x: x + y)(1)
# 11
```

매개변수 `x`와 람다표현식 바깥에 있는 변수 `y`를 더해서 반환함

## 람다 표현식을 인수로 사용하기

- 람다 표현식을 사용하기 전에 먼저 `def`로 함수를 만들어서 `map`을 사용해 보자

```py
>>> def plus_ten(x):
	return x + 10

>>> list(map(plus_ten, [1,2,3]))
# [11, 12, 13]
```

- 람다 표현식으로 함수를 만들어서 `map`에 넣어보자

```py
>>> list(map(lambda x: x + 10, [1,2,3]))
# [11, 12, 13]
```

# 3. 람다표현식과 map, filter, reduce 함수

## 람다 표현식에 조건부 표현식 사용하기

- `lambda 매개변수들: 식1 if 조건식 else 식2`

- `map`을 사용하여 리스트 `a`에서 `3`의 배수를 문자열로 변환하기

```py
>>> a = [1,2,3,4,5,6,7,8,9,10]
>>> list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
```

- 람다표현식 안에서 조건부 표현식 if, else를 사용할때는 `:`을 붙이지 않는다.
- 람다표현식에서 `if`를 사용했다면 반드시 `else`를 사용해야한다.
- 람다표현식 안에서는 `elif`를 사용할 수 없다.

## map에 객체를 여러 개 넣기

- 두 리스트의 요소를 곱해서 새 리스트 만들기

```py
>>> a = [1,2,3,4,5]
>>> b = [2,4,6,8,10]
>>> list(map(lambda x, y: x * y, a, b))
# [2, 8, 18, 32, 50]
```

## filter 사용하기

- `filter`는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, `filter`에 지정한 함수의 반환값이 `True`일 때만 해당 요소를 가져온다.
- `filter(함수, 반복가능객체)`

```py
>>> def f(x):
    	return x > 5 and x < 10

>>> a = [8,3,2,10,15,7,1,8,9,11]
>>> list(filter(f, a))
# [8, 7, 8, 9]
```

### 함수 f를 람다표현식으로 만들어서 filter에 넣기

```py
>>> a = [8,3,2,10,15,7,1,8,9,11]
>>> list(filter(lambda x: x > 5 and x < 10, a))
# [8, 7, 8, 9]
```

## reduce 사용하기

- `reduce`는 반복가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
- `reduce`는 파이썬3 부터 내장함수가 아니다. 따라서 `functools`모듈에서 `reduce`함수를 가져와야 한다.

  - `from functools import reduce`
  - `reduce(함수, 반복가능객체)`

- 리스트에 저장된 요소를 순서대로 더하고 누적결과를 반환하기

```py
>>> def f(x, y):
	    return x + y

>>> a = [1,2,3,4,5]
>>> from functools import reduce
>>> reduce(f, a)
# 15
```

### 함수 f를 람다표현식으로 만들어서 reduce에 넣기

```py
>>> a = [1,2,3,4,5]
>>> reduce(lambda x,y: x + y, a)
15
```

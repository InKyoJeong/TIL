# 클로저

> 클로저는 개념이 어려운 부분이므로 변수의 사용범위 부터 알아본다.

## 1. 변수의 사용 범위 알아보기

1. 전역변수

```py
>>> x = 10      # 전역변수
>>> def foo():
	    print(x)


>>> foo()
>>> print(x)
10
10
```

- 함수를 포함하여 스크립트 전체에서 접근할 수 있는 변수를 `전역변수(global variable)`이라고 한다.
- 전역변수에 접근할 수 있는 범위를 `전역범위(global scope)`라고 한다.

<br>

2. 지역변수

```py
>>> def foo():
        x = 11      # foo의 지역변수
        print(x)    # foo의 지역변수 출력


>>> foo()
# 11
>>> print(x)        # 에러. foo의 지역변수는 출력할 수 없음
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     print(x)
# NameError: name 'x' is not defined
```

- 변수 `x`는 함수 `foo`안에서 만들었기 때문에 `foo`의 `지역변수(local variable)`이다.
- 지역변수는 변수를 만든 함수 안에서만 접근할 수 있다. 함수바깥에서는 접근할 수 없다.
- 지역변수를 접근할 수 있는 범위를 `지역범위(local scope)`라고 한다.

### 함수 안에서 전역 변수 변경하기

- 전역변수 `x`가 있고, `foo`에서 지역변수 `x`를 새로 만들었다.

```py
>>> x = 10          # 전역변수
>>> def foo():
        x = 20      # x는 foo의 지역변수
        print(x)    # foo의 지역변수 출력


>>> foo()
# 20
>>> print(x)        # 전역변수 출력
# 10
```

<br>

- 함수안에서 전역 변수 값을 변경하려면 `global`키워드를 사용한다.

```py
>>> x = 10
>>> def foo():
        global x        # 전역변수 x를 사용하겠다고 설정
        x = 20          # x는 전역변수
        print(x)        # 전역변수 출력


>>> foo()
# 20
>>> print(x)            # 전역변수 출력
# 20
```

기존의 `x = 10`은 사라졌다.

## 2. 함수 안에서 함수 만들기

- 다음과 같이 `def`로 함수를 만들고 그 안에서 다시 `def`로 함수를 만들면 됨

```py
def 함수이름1():
    코드
    def 함수이름2():
        코드
```

## 지역 변수의 범위

- 안쪽 함수 `print_message`에서는 바깥쪽 함수 `print_hello`의 지역변수 `hello`를 사용할 수 있다.

```py
def print_hello():
    hello = 'Heeeellllloooo'
    def print_message():
	    print(hello)        # 바깥쪽 함수의 지역 변수를 사용
    print_message()


>>> print_hello()
# Heeeellllloooo
```

- 즉, 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있다.

### 지역변수 변경하기

> 파이썬에서는 함수에서 변수를 만들면 항상 현재 함수의 지역변수가 됨

```py
>>> def A():
        x = 10          # A의 지역변수 x
        def B():
            x = 20      # x 에 20 할당

        B()
        print(x)        # A의 지역변수 x출력


>>> A()
10
```

<br>

- 현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하려면 `nonlocal`키워드를 사용한다.

```py
>>> def A():
        x = 10      # A의 지역변수 x
        def B():
            nonlocal x      # 현재함수의 바깥쪽에 있는 지역변수 사용
            x = 20          # A의 지역변수 x에 20할당

        B()
        print(x)            # A의 지역변수 x출력


>>> A()
20
```

### nonlocal이 변수를 찾는 순서

- `nonlocal`은 현재 함수의 바깥쪽에 있는 지역변수를 찾을때 가장 가까운 함수부터 찾음

```py
>>> def A():
        x = 10
        y = 100
        def B():
            x = 20
            def C():
                nonlocal x
                nonlocal y
                x = x + 30
                y = y + 200
                print(x)
                print(y)
            C()
        B()

>>> A()
50
300
```

<br>

### global로 전역변수 사용하기

- 함수가 몇단계든 상관없이 `global`키워드를 사용하면 무조건 전역변수를 사용하게 됨

```py
>>> x = 1
>>> def A():
        x =10
        def B():
            x = 20
            def C():
                global x
                x = x + 30
                print(x)
            C()
        B()

>>> A()
31
```

- 전역변수는 가급적 사용하지 않는다.

<br>

## 3. 클로저

- 함수 바깥쪽에 있는 지역변수 `a,b`를 사용하여 `a * x + b` 를 계산하는 함수 `mul_add`를 만들고 함수 `mul_add`자체를 반환하기

```py
>>> def calc():
        a = 3
        b = 5
        def mul_add(x):
            return a * x + b        # 함수 바깥쪽에 있는 지역변수 a,b를 사용하여 계산
        return mul_add

>>> c = calc()
>>> print(c(1), c(2), c(3), c(4))
# 8 11 14 17
```

### 클로저 사용하기

- 함수를 둘러싼 환경(지역변수, 코드 등)을 유지하다가, 함수를 호출할때 다시 꺼내서 사용하는 함수를 `클로저(closure)`라고 한다.
- 위에서는 `c`에 저장된 함수가 클로저 이다.

  - 클로저를 사용하면 프로그램의 흐름을 변수에 저장할 수 있다.
  - 클로저는 지역변수와 코드를 묶어서 사용하고 싶을때 활용함
  - 클로저에 속한 지역변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을때 활용함

### lambda로 클로저 만들기

```py
>>> def calc():
        a = 3
        b = 5
        return lambda x: a * x + b

>>> c = calc()
>>> print(c(1), c(2), c(3), c(4))
# 8 11 14 17
```

- 람다는 이름이 없는 익명함수를 뜻하고, 클로저는 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수를 뜻함

### 클로저의 지역변수 변경하기

> 클로저의 지역변수를 변경하려면 `nonlocal`을 사용

- `a * x + b`결과를 함수 `calc`의 지역변수 `total`에 누적하기

```py
>>> def calc():
        a = 3
        b = 5
        total = 0
        def mul_add(x):
            nonlocal total
            total = total + a * x + b
            print(total)
        return mul_add

>>> c = calc()
>>> c(1)
# 8
>>> c(2)
# 19
>>> c(3)
# 33
```

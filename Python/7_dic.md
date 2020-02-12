# 딕셔너리

- 파이썬에서는 **연관된 값을 묶어서 저장**하는 용도로 딕셔너리라는 자료형을 제공함
- 딕셔너리는 값마다 이름을 붙여서 저장하는 방식
- `딕셔너리 = {키1: 값1, 키2: 값2, ...}`
- 키 이름이 중복되면 뒤에 있는 값만 사용한다.

```py
>>> human = {'age': 25, 'age': 50, 'height':100, 'weight':55}
>>> human['age']
50
```

- 문자열뿐만 아니라 정수, 실수, 불도 사용가능하다.

```py
>>> x = {100: 'hundred', False: 0, 3.1: [4.5, 6.6]}
>>> x
{100: 'hundred', False: 0, 3.1: [4.5, 6.6]}
```

- `키`에는 **리스트와 딕셔너리 사용 불가능**하다.
- `값`에는 리스트, 딕셔너리를 포함해 모든 자료형을 사용 가능하다.

```py
>>> y = {[10, 20]: 100}
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     y = {[10, 20]: 100}
# TypeError: unhashable type: 'list'

>>> z = {{'a': 100}: 200}
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     z = {{'a': 100}: 200}
# TypeError: unhashable type: 'dict'
```

## 빈 딕셔너리 만들기

- `딕셔너리 = {}`
- `딕셔너리 = dict()`

```py
>>> x = {}
>>> x
{}
>>> y = dict()
>>> y
{}
```

## dict로 딕셔너리 만들기

- `dict`는 키와 값을 연결하거나 리스트,튜플,딕셔너리로 딕셔너리를 만들때 사용한다.

1. 딕셔너리 = `dict(키1=값1, 키2=값2, ...)`

```py
>>> human = dict(age=22, height=100, weight=55)
>>> human
{'age': 22, 'height': 100, 'weight': 55}
```

`키`는 딕셔너리를 만들고 나면 문자열로 바뀐다.

2. 딕셔너리 = `dict(zip([키1,키2], [값1,값2], ...))`

```py
>>> human2 = dict(zip(['age','height','weight'],[10,90,20]))
>>> human2
{'age': 10, 'height': 90, 'weight': 20}
```

키와 값을 리스트가 아닌 튜플에 저장해서 `zip`에 넣어도 된다.

3. 딕셔너리 = `dict([(키1,값1), (키2,값2), ...])`

```py
>>> human3 = dict([('age',25), ('height',160), ('weight',44)])
>>> human3
{'age': 25, 'height': 160, 'weight': 44}
```

4. 딕셔너리 = `dict({키1:값1, 키2:값2, ...})`

```py
>>> human4 = dict({'age':27, 'height':165, 'weight':48})
>>> human4
{'age': 27, 'height': 165, 'weight': 48}
```

## 딕셔너리의 키에 접근하고 값 할당하기

- 딕셔너리 키에 접근할때는 딕셔너리 뒤에 `[]`를 사용하고 그 안에 키를 지정한다.

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> x['age']
11
>>> x['health']
400
```

- 딕셔너리는 `[]`로 키에 접근하고 값을 할당한다.

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> x['grade'] = 4
>>> x['health'] = 333
>>> x
{'age': 11, 'grade': 4, 'health': 333}
```

- 기존에 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당된다.

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> x['add'] = 99999
>>> x
{'age': 11, 'grade': 4, 'health': 333, 'add': 99999}
```

- 없는 키에서 값을 가져올 수는 없다.

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> x['hello']
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     x['hello']
# KeyError: 'hello'
```

## 딕셔너리에 키가 있는지 확인하기

- `키 in 딕셔너리`

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> 'age' in x
True
>>> 'speed' not in x
True
```

## 딕셔너리의 키 개수 구하기

- `len(딕셔너리)`

```py
>>> x = {'age':11, 'grade': 5, 'health':400}
>>> len(x)
3

# 직접 딕셔너리를 그대로 넣어도 된다.
>>> len({'age':11, 'grade': 5, 'health':400})
3
```

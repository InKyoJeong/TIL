# 회문 판별과 N-gram 만들기

- 회문은 유전자 염기서열 분석에서 많이 쓰고, N-gram은 빅 데이터 분석, 검색 엔젠에서 많이 쓰임
- 구글은 책들을 스캔해서 N-gram viewer를 만들었는데 사람들의 언어 패턴을 시대별로 분석하기도 했다.
  - https://books.google.com/ngrams

## 회문 판별하기

- 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장

### 반복문으로 문자 검사하기

```py
>>> word = input('단어를 입력하세요: ')

>>> is_palindrome = True                # 회문 판별값을 저장할 변수, 초깃값은 True
>>> for i in range(len(word) // 2):     # 0부터 문자열 길이의 절반만큼 반복
        if word[i] != word[-1 - i]:     # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            is_palindrome = False       # 회문이 아니다.
            break

    print(is_palindrome)

# 단어를 입력하세요: level
# True
```

### 시퀀스 뒤집기로 문자 검사하기

- 회문은 시퀀스 객체의 슬라이스를 활용하면 간단하게 판별할 수 있다.

```py
>>> word = input('단어를 입력하세요: ')

>>> print(word == word[::-1])       # 원래 문자열과 반대로 뒤집은 문자열을 비교

# 단어를 입력하세요: level
# True
```

### 리스트와 reversed 사용하기

- 반복 가능한 객체의 요소 순서를 반대로 뒤집는 `reversed`를 사용해도 된다.
- `list`에 문자열을 넣으면 문자 하나하나가 리스트의 요소로 들어간다.

```py
>>> list(word)
['l', 'e', 'v', 'e', 'l']
>>> list(reversed(word))
['l', 'e', 'v', 'e', 'l']
```

<br>

## N-gram 만들기

- N-gram은 문자열에서 N개의 연속된 요소를 추출하는 방법
- 만약 `Hello` 라는 문자열을 문자(글자) 단위 `2-gram`으로 추출하면 다음과 같다.

```
He
el
ll
lo
```

## 반복문으로 N-gram 출력하기

```py
>>> for i in range(len(text) - 1):
    	print(text[i], text[i + 1], sep='')

# He
# el
# ll
# lo
```

### 3-gram 출력하기

- `3-gram`이면 반복 횟수는 `range(len(text) - 2)`이고, 문자열 끝에서 두 글자 앞까지 반복하면 된다.

### zip으로 2-gram 만들기

```py
>>> text = 'hello'
>>> two_gram = zip(text, text[1:])
>>> for i in two_gram:
    	print(i[0], i[1], sep='')

# he
# el
# ll
# lo
```

- 지금까지 `zip`함수는 리스트 두 개를 딕셔너리로 만들 때 사용했는데, `zip`함수는 반복 가능한 객체의 각 요소를 튜플로 묶어준다.

```py
>>> list(zip(text, text[1:]))
[('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]
```

## zip과 리스트 표현식으로 N-gram 만들기

```py
>>> list(zip(*['hello', 'ello', 'llo']))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

>>> list(zip(*[text[i:] for i in range(3)]))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]
```

## 연결리스트 - 다항식만들기(1)

### 구조체 Term

```c
struct term {
    int coef;       //계수
    int expo;       //지수(차수)
    struct term *next;
};

typedef struct term Term;
```

### 구조체 Polynomial

```c
typedef struct polynomial{
    char name;      //다항식의 이름(f, g, h..)
    Term *first;    //이 다항식을 구성하는 첫번째 항의 주소
    int size = 0;
} Polynomial;

Polynomial *polys[MAX_POLYS];       //polys는 다항식들에 대한 포인터의 배열
int n = 0;      //저장된 다항식의 개수
```

### create instance

```c
Term *create_term_instance(){
    Term *t = (Term *)malloc(sizeof(Term));
    t->coef = 0;
    t->expo = 0;
    return t;
}

Polynomial *create_polynomial_instance(char name){
    Polynomial *ptr_poly = (Polynomial *)malloc(sizeof(Polynomial));
    ptr->poly->name = name;
    ptr->poly->size = 0;
    ptr->poly->first = NULL;
    return ptr_poly;
}
```

동적으로 생성된 객체를 적절하게 초기화해주지 않는 것이 종종 프로그램의 오류를 야기한다. 이렇게 객체를 생성하고 기본값으로 초기화해주는 함수를 따로 만들어 사용하는 것은 좋은 방법이다.

### add_term(int c, int e, Polynomial \*poly)

- poly가 가리키는 다항식에 새로운 하나의 항 (c,e)를 추가하는 함수
- 두가지 경우
  - 추가하려는 항과 동일 차수의 항이 이미 있는 경우 : 기존 항의 계수만 변경
  - 그렇지 않은 경우 : 새로운 항을 삽입 (항들은 차수의 내림차순으로 항상 정렬됨)

```c
void add_term(int c, int e, Polynomial *poly){
    if (c == 0)
        return ;
    Term *p = poly->first, *q = NULL;
    while(p != NILL && p->expo > e){
        q = p;
        p = p->next;
    }
    if (p! = NULL && p->expo == e){
        p->coef += c;
        if(p->coef == 0){
            if(q == NULL)
                poly->first = p->next;
            else
                q->next = p->next;
            poly->size--;
            free(p);
        }
        return;
    }

// 동일한 차수의 항이 없는경우
    Term *term = create_term_instance();
    term->coef = c;
    term->exop = e;

    if(q == NULL){              //맨 앞에 삽입하는 경우
        term->next = poly->first;
        poly->first = term;
    }
    else {                      //q의 뒤, p의 앞에 삽입
        term->next = p;
        q->next = term;
    }
    poly->size++;
}
```

1. 만약 c가 0이면 이 항은 존재하지 않으므로 아무것도 할필요없이 그냥 return하면 끝, 그렇지 않다면 두개의 포인터 p,q를 이용해서 p는 첫번째 노드에서 출발하고 q는 p의 한칸뒤를 따라온다. p가 가리키는 항의 차수가 내가 삽입하려는 차수보다 큰 동안 p는 한칸씩 전진한다.

2. p가 가리키는 항이 삽입하려는 항과 차수가 같을 수도 있다. 그러면 그 항의 계수만 증가시키면 된다. 그런데 계수를 더했을때 0이라면 이 항 자체를 다항식에서 제거해야 한다.

3. 여기서 만약 p가 첫번째 노드를 가리키면 q는 NULL이다. 그러면 첫번째 노드를 삭제해야한다. first가 p다음 노드를 가리키게하면 된다. 그렇지 않다면 (q가 NULL이 아니라면) p가 첫번째 노드가 아니므로 q.next가 p.next를 가리키게하면 된다.

4. 다항식의 size를 하나 감소시키고 p가 가리키는 노드를 free시켜서 불필요해진 노드를 없애준다.

#### 새로운 항을 삽입해야하는 경우 : 예를들어 5x를 삽입한다고 가정

```c
Term p = first, q = null;
while(p != null && p.expo > e){
    q = p;              //q는 항상 p의 한칸 뒤를 따라감
    p = p.next;
}
```

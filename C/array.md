### 배열요소 출력하기

```c
// 0번째 학생의 점수는 10입니다
// 1번째 학생의 점수는 20입니다
// 2번째 학생의 점수는 30입니다
// 3번째 학생의 점수는 40입니다
// 4번째 학생의 점수는 50입니다

#include <stdio.h>
#define STUDENTS 5

int main(void){
    int score[STUDENTS];
    int i;

    score[0] = 10;
    score[1] = 20;
    score[2] = 30;
    score[3] = 40;
    score[4] = 50;

    for(i=0; i<STUDENTS; i++){
        printf("%d번째 학생의 점수는 %d입니다\n", i, score[i]);
    }

    return 0;
}
```

#### 사용자입력을 배열요소에 저장하기

```c
// 입력
// 성적을 입력하시오: 10
// 성적을 입력하시오: 20
// 성적을 입력하시오: 30
// 성적을 입력하시오: 40
// 성적을 입력하시오: 50

// 출력
// 평균성적은 30.000000이다.

#include <stdio.h>
#define STUDENTS 5

int main(void){
    int score[STUDENTS];
    int i;
    int sum = 0;
    double avg;

    for(i=0; i<STUDENTS; i++){
    printf("성적을 입력하시오: ");
    scanf("%d", &score[i]);
    }

    for(i=0; i<STUDENTS; i++){
        sum = sum + score[i];
    }
    avg = sum / STUDENTS;
    printf("평균성적은 %f이다.", avg);
    return 0;
}
```

### sizeof연산자

> 배열의 요소의 개수를 자동으로 계산하기

`size = sizeof(score) / sizeof(score[0])` (배열의크기 / 배열요소의 크기)

sizeof연산자는 자료형이나 변수크기를 바이트단위로 계산하는 연산자이다.

```c
#include <stdio.h>
int main(void){
    int score[] = {1,3,5,6,7,11,22,44,566,777};
    int i, size;

    size = sizeof(score) / sizeof(score[0]);

    for(i=0; i<size; i++){
        printf("score[%d]=%d\n", i, score[i]);
    }
    return 0;
}

//결과
// score[0]=1
// score[1]=3
// score[2]=5
// score[3]=6
// score[4]=7
// score[5]=11
// score[6]=22
// score[7]=44
// score[8]=566
// score[9]=777
```

#### 최솟값 구하기

```c
#include <stdio.h>
#define SIZE 10

int main(void){
    int x[SIZE] = {11,3,44,4,6,13,12,3,1,19};
    int i, minimum;
    minimum = x[0];

    for(i=1; i<SIZE; i++){
        if(x[i] < minimum){
            minimum = x[i];
        }
    }
    printf("최솟값은 %d이다.",minimum);
    return 0;
}

```

#### 히스토그램 그리기

```c
// 요소	 값	 히스토그램
// 0	11	************
// 1	3	****
// 2	4	*****
// 3	7	********
// 4	9	**********
// 5	2	***
// 6	1	**
// 7	6	*******

#include <stdio.h>
#define SIZE 8

int main(void){
    int x[SIZE] = {11,3,4,7,9,2,1,6};
    int i, j;
    printf("요소\t값\t히스토그램\n");
    for(i=0; i<SIZE; i++){
        printf("%d\t%d\t", i, x[i]);
        for(j=0; j<=x[i]; j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
```

#### 문자열 입출력

```c
//Is Seoul the Capital city of Korea?(y or n)n
//틀렸음

#include <stdio.h>
int main(void){
    char question[] = "Is Seoul the Capital city of Korea?(y or n)";
    char answer[100];

    printf("%s", question);
    scanf("%s", answer);

    if(answer[0] == 'y'){
        printf("맞았음\n");
    }
    else{
        printf("틀렸음\n");
    }
    return 0;
}
```

배열의 이름은 바로 배열의 주소이기 때문에 문자열의 경우 scanf("%s", &answer); 같이 하면 안된다. (`&`를 넣지않음)

#### 문자열 길이 구하기

```c
// 문자열을 입력하세요 : university
// 문자열의 길이 : 10

#include <stdio.h>
int main(void){
    char n[10], i;

    printf("문자열을 입력하세요 : ");
    scanf("%s", n);

    i = 0;
    while( n[i] != '\0')
        i++;

    printf("문자열의 길이 : %d", i);
    return 0;
}
```

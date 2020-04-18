# 전화번호부 예제연습

## 실행 예

```
//프로그램을 실행하면 화면에 프롬프트($)를 출력하고 명령을 기다린다.
$ add John 01078789898      //새로운 사람을 추가한다.
John was added successfully.
$ add David 01033334444
David was added successfully.
$ find Henry                //이름으로 전화번호를 검색한다.
No person named 'Herny' exists.
$ status                    //전화번호부에 저장된 모든 사람 출력한다.
John 01078789898
David 01033334444
$ delete Jim
No person named 'Jim' exists.
$ delete John               //전화번호부에서 삭제한다.
John was deleted successfully.
$ status
David 01033334444
$ exit                      //프로그램을 종료한다.
```

```c
#include <stdio.h>
#include <string.h>

#define CAPACITY 100
#define BUFFER_SIZE 100

char *names[CAPACITY];
char *numbers[CAPACITY];

int n = 0;

void add();
void find();
void status();
void remove();

int main(){
    char command[BUFFER_SIZE];
    while(1){
        printf("$ ");
        scanf("%s", command);

        if(strcmp(command, "add") == 0){
            add();
        }else if(strcmp(command, "find") == 0){
            find();
        }else if(strcmp(command, "status") == 0){
            status();
        }else if(strcmp(command, "delete") == 0){
            remove();
        }else if(strcmp(command, "exit") == 0)
            break;
    }
    return 0;
}

void add(){
    char buf1[BUFFER_SIZE], buf2[BUFFER_SIZE];
    scanf("%s", buf1);
    scanf("%s", buf2;

    names[n] = strdup(buf1);
    numbers[n] = strdup(buf2);
    n++;

    printf("%s was added successfully.\n", buf1);
}
```

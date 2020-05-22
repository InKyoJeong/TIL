## 전화번호부 v1

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
void del();

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
            del();
        }else if(strcmp(command, "exit") == 0)
            break;
    }
    return 0;
}

void add(){
    char buf1[BUFFER_SIZE], buf2[BUFFER_SIZE];
    scanf("%s", buf1);
    scanf("%s", buf2);

    names[n] = strdup(buf1);
    numbers[n] = strdup(buf2);
    n++;

    printf("%s was added successfully.\n", buf1);
}

void find(){
    char buf[BUFFER_SIZE];
    scanf("%s", buf);

    int i;
    for (i=0; i<n; i++){
        if (strcmp(buf, names[i]) == 0){
            printf("%s\n", numbers[i] );
            return;
        }
    }
    printf("No person named '%s' exists.\n", buf);
}
// strcmp는 같으면 0 리턴

void status(){
    int i;
    for(i=0; i<n; i++){
        printf("%s %s\n", names[i], numbers[i]);
    }
    printf("Total %d persons.\n", n);
}

void del(){
    char buf[BUFFER_SIZE];
    scanf("%s", buf);

    int i;
    for(i=0; i<n; i++){
        if(strcmp(buf, names[i]) == 0){
            names[i] = names[n-1];      // 맨 마지막 사람을 삭제된 자리로 옮긴다.
            numbers[i] = numbers[n-1];
            n--;
            printf("'%s' was delete successfully. \n", buf);
            return;
        }
    }
    printf("No person named '%s' exists.\n", buf);
}
```

## 전화번호부 v2

```
//항상 알파벳순으로 정렬된 상태를 유지한다.
$ read directory.txt        //파일로부터 데이터를 읽어온다.
$ status
Mary 01055556666
John 01033334444
$ add Anderson 0103232323
Aderson was added successfully.
$ status
Anderson 0103232323
Mary 01055556666
John 01033334444
$ save as directory.txt     //파일에 데이터를 저장한다.
$ exit
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
void del();
void load();
void save();

int main(){
    char command[BUFFER_SIZE];
    while(1){
        printf("$ ");
        scanf("%s", command);

        if(strcmp(command, "read") == 0){
            load();
        }else if(strcmp(command, "add") == 0){
            add();
        }else if(strcmp(command, "find") == 0){
            find();
        }else if(strcmp(command, "status") == 0){
            status();
        }else if(strcmp(command, "delete") == 0){
            del();
        }else if(strcmp(command, "save") == 0){
            save();
        }else if(strcmp(command, "exit") == 0)
            break;
    }
    return 0;
}

void load(){
    char fileName[BUFFER_SIZE];
    char buf1[BUFFER_SIZE];
    char buf2[BUFFER_SIZE];

    scanf("%s", fileName);      //파일 이름을 입력받는다.

    FILE *fp = fopen(fileName, "r");
    if(fp == NULL){
        printf("Open failed.\n");
        return;
    }
    while ((fscanf(fp, "%s", buf1) !=EOF)){     //파일의 끝에 도달할때까지 반복해서 이름,전화번호를 읽어서 배열에 저장
        fscanf(fp, "%s", buf2);
        names[n] = strdup(buf1);
        numbers[n] = strdup(buf2);
        n++;
    }
    fclose(fp);
}

void save(){
    int i;
    char fileName[BUFFER_SIZE];
    char tmp[BUFFER_SIZE];

    scanf("%s", tmp);
    scanf("%s", fileNmae);

    FILE *fp = fopen(fileNmae, "w");
    if(fp == NULL){
        printf("Open failed.\n");
        return;
    }
    for (i=0; i<n; i++){
        fprintf(fp, "%s %s\n", names[i], numvers[i]);
    }
    fclose(fp);
}

void add(){
    char buf1[BUFFER_SIZE], buf2[BUFFER_SIZE];
    scanf("%s", buf1);
    scanf("%s", buf2);

    int i = n-1;
    while(i >= 0 && strcmp(names[i], buf1) > 0){
        names[i+1] = names[i];
        numbers[i+1] = numbers[i];
        i--;
    }

    names[n] = strdup(buf1);
    numbers[n] = strdup(buf2);
    n++;

    printf("%s was added successfully.\n", buf1);
}

void del(){
    char buf[BUFFER_SIZE];
    scanf("%s", buf);
    int index = search(buf);
    if (index == -1){
        printf("No person named '%s' exists. \n", buf);
        return;
    }
    int j = index;
    for(; j<n-1; j++){
        names[j] = names[j+1];
        numbers[j] = numbers[j+1];
    }
    n--;
    printf("'%s' was deleted successfully.\n", buf);
}

void find(){
    char buf[BUFFER_SIZE];
    scanf("%s", buf);
    int index == search(buf);
    if (index == 1)
        printf("No person named '%s' exists.\n", buf);
    else
        printf("%s\n", numbers[index]);
}

int search(char *name){
    int i;
    for(i =0; i<n; i++){
        if (strcmp(name, names[i]) == 0){
            return i;
        }
    }
    return -1;
}

void status(){
    int i;
    for(i=0; i<n; i++){
        printf("%s %s\n", names[i], numbers[i]);
    }
    printf("Total %d persons.\n", n);
}
```

### 데이터를 정렬된 상태로 유지하려면

- bubblesort 등의 정렬(sorting) 알고리즘을 사용하는 방법
  - 새로운 데이터가 계속 추가되는 상황에서는 부적절
- 새로운 데이터가 추가될때마다 제자리를 찾아서 삽입하는 방법

```
B C D F K M P  //E를 추가하려면 맨 뒤에서부터 검사해서 E보다 큰 것들을 전부 한칸씩 뒤로 이동
B C D E F K M P  //E보다 작은것이 나오거나 배열의 시작을 지나치면 그 다음자리에 E를 저장한다.
```

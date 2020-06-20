## 퀵 정렬 알고리즘

```c
void QuickSort(int data[], int left, int right)
{
    int num, i, j, temp;

    if(right > left){
        num = data[right];
        i = left - 1;
        j = right;

        for(; ;){
            while(data[++i] < num);
                while(data[--j] > num);
                    if(i >= j)
                        break;

            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }
        temp = data[i];

        data[i] = dadta[right];
        data[right] = temp;

        QuickSort(data, left, i-1);
        QuickSort(data, i+1, right);
    }
}
```

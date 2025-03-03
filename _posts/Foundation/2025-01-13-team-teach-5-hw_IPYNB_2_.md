---
layout: post
title: HW Numero Cinco
permalink: /hw_5
comments: True
---

```java
import java.util.Random;

public void repopulate(){
    for (int i = 0; i < grid.length; i++){
        for (int j = 0; j < grid[0].length; j++){
            Random rand = new Random();
            int random_int1 = rand.nextInt(MAX)+1;
            while (random_int1 % 10 || random_int1 % 100){
                random_int1 = rand.nextInt(MAX)+1;
            }
            grid[i][j] = random_int1;
        }
    }
}
```


```java
public int countIncreasingCols(){
    int num = 0;
    for (int j = 0; j < grid[0].length; j++){
        boolean flag = true;
        for (int i = 1; i < grid.length; i++){
            if (grid[row-1][col] > grid[row][col]){
                flag = false;
            }
        }
        if (flag){
            num++;
        }
    }
    return num;
}
```

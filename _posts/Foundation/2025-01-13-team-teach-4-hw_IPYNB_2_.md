---
layout: post
title: HW Numero Cuatro
permalink: /hw_4
comments: True
---

```java
public void cleanData(double lower, double upper) {
    int length = temperatures.size();
    for (int i = length-1, i >= 0, i--){
        if (temperatures.get(i) < lower || temperatures.get(i) > upper){
            temperatures.remove(i);
        }
    }
}
```

## PART A EXPLANATION

- iterate through the for loop backwards, since removing elements will make the arraylist change. Compare each temperature to the lower and upper to determine wether you remove it.


```java
public int longestHeatWave(double threshold) {
    int current = 0;
    int max = 0;
    for (double i : temperatures){
        if (i <= threshold){
            curent = 0;
        }
        else {
            current++;
            if (current > max){
                max = current;
            }
        }
    }
    return max;
}
```

## PART B Explanation

- if the temperatrue value is less than the threshold reset the chain, if greater, add 1 and compare to the max.

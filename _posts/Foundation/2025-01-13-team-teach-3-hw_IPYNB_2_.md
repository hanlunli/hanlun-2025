---
layout: post
title: HW Numero Tres
permalink: /hw_3
comments: True
---

```java
public class CombinedTable {
    private SingleTable t1;
    private SingleTable t2;
    public CombinedTable(t1, t2){
        this.t1 = t1;
        this.t2 = t2;
    }
    public boolean canSeat(int seats){
        if (seats <= t1.getNumSeats() + t2.getNumSeats()){
            return true;
        }
        return false;
    }
    public double getDesirability(){
        if (t1.getHeight() == t2.getHeight()){
            return (t1.getViewQuality()+t2.getViewQuality())/2;
        }
        else {
            return (t1.getViewQuality()+t2.getViewQuality())/2 - 10.00;
        }
    }
}
```

## SELF SCORING:
Declares class and constructor headers properly: 0/1 (failed to use SingleTable object in constructor)

Declares appropriate private instance variables including at least two SingleTable references: 1/1

Constructor initializes instance variables using parameters: 1/1

Declares method header public boolean canSeat(int ___): 1/1

Calls getNumSeats on SingleTable objects: 1/1

canSeat(int) returns true if and only if sum of seats of two tables - 2 >= n: 0/1 (instead of using >=, i used <=)

Declares method header public double getDesirability(): 1/1

Calls getHeight and getViewQuality on SingleTable objects: 1/1

getDesirability computes the average desirability correctly: 1/1

## CORRECTED CODE:


```java
public class CombinedTable {
    private SingleTable t1;
    private SingleTable t2;
    public CombinedTable(SingleTable t1, SingleTable t2){
        this.t1 = t1;
        this.t2 = t2;
    }
    public boolean canSeat(int seats){
        if (seats >= t1.getNumSeats() + t2.getNumSeats()){
            return true;
        }
        return false;
    }
    public double getDesirability(){
        if (t1.getHeight() == t2.getHeight()){
            return (t1.getViewQuality()+t2.getViewQuality())/2;
        }
        else {
            return (t1.getViewQuality()+t2.getViewQuality())/2 - 10.00;
        }
    }
}
```

---
layout: post
title: HW Numero Dos
permalink: /hw_2
comments: True
---

```java
public class Game   
{
    private Level levelOne;
    private Level levelTwo;
    private Level levelThree;
    public Game(){

    }
    public boolean isBonus(){
        
    }
    public void play(){

    }
    public int getScore(){


    }
    public int playManyTimes(int num){

    }
}
```


```java
public int getScore(){
    int gameScore = 0;
    if (levelOne.goalReached()){
        gameScore += levelOne.getPoints()
        if (levelTwo.goalReached()){
            gameScore += levelTwo.getPoints(){
                if (levelThree.goalReached()){
                    gameScore += levelThree.getPoints()
                }
            }
        }
    }

    if (isBonus())
        gameScore *= 3;
        
    return gameScore;
}
```


```java
public int playManyTimes(int num){
    int returnScore = 0;
    for (int i = 0; i < num; i++){
        play();
        if (getScore() > returnScore){
            returnScore = getScore();
        }
    }
    return returnScore;
}
```

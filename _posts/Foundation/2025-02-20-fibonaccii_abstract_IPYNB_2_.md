---
toc: False
layout: post
title: Abstract Fibonaccii Hack
description: A Fibonacci algorithm that runs using an abstract parent class.
courses: {'csa': {'week': 25}}
type: ccc
image: /images/data_structures/fibonacci.png
---

![abstract]({{site.baseurl}}/images/data_structures/fibonacci.png)

## Introduction

This notebook uses Class definitions, ArrayLists, and Hash Maps.   My hypothosis is these data structures are probably the most widely used in the Java language.

### Popcorn Hacks

- Provide some reasons why you agree with my hypothesis?

- Provide some data structures that you think might rival my hypothesis?

- Categorize data structure mentioned, tested by college board tested, widely used, fast.



```Java
/*
 * Creator: Nighthawk Coding Society
 * Mini Lab Name: Fibonacci sequence, featuring a Stream Algorithm
 * 
*/

import java.util.ArrayList;  
import java.util.HashMap;
import java.util.stream.Stream;

/* Objective will require changing to abstract class with one or more abstract methods below */
abstract class Fibo {
    String name;
    int size;
    int hashID;
    ArrayList<Long> list;
    HashMap<Integer, Object> hash;

    public Fibo() {
        this(8);
    }

    public Fibo(int nth) {
        this.size = nth;
        this.list = new ArrayList<>();
        this.hashID = 0;
        this.hash = new HashMap<>();
        
        long start = System.nanoTime();
        this.calc();
        long end = System.nanoTime();
        System.out.println(this.getClass().getSimpleName() + " computed Fibonacci in " + (end - start) + " ns");
    }

    protected abstract void calc();

    public void setData(long num) {
        list.add(num);
        hash.put(this.hashID++, list.clone());
    }

    public long getNth() {
        return list.get(this.size - 1);
    }

    public Object getNthSeq(int i) {
        return hash.get(i);
    }

    public void print() {
        System.out.println("Calculation method = " + this.name);
        System.out.println("Fibonacci Number " + this.size + " = " + this.getNth());
        System.out.println("Fibonacci List = " + this.list);
    }
}
```


```Java

public class FiboFor extends Fibo {

    public FiboFor() {
        super();
    }

    public FiboFor(int nth) {
        super(nth);
    }

    @Override
    protected void calc() {
        super.name = "FiboFor extends Fibo";
        long limit = this.size;
        // for loops are likely the most common iteration structure, all the looping facts are in one line
        for (long[] f = new long[]{0, 1}; limit-- > 0; f = new long[]{f[1], f[0] + f[1]})
            this.setData(f[0]);
    }

    /*
    Tester class method.
     */
    static public void main(int... numbers) {
        for (int nth : numbers) {
            Fibo fib = new FiboFor(nth);
            fib.print();
            System.out.println();
        }
    }
}

FiboFor.main(2, 5, 8);

```

    FiboFor computed Fibonacci in 118065 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 2 = 1
    Fibonacci List = [0, 1]
    
    FiboFor computed Fibonacci in 73718 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 5 = 3
    Fibonacci List = [0, 1, 1, 2, 3]
    
    FiboFor computed Fibonacci in 53510 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 8 = 13
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13]
    



```Java
public class FiboStream extends Fibo {

    public FiboStream() {
        super();
    }

    public FiboStream(int nth) {
        super(nth);
    }

    @Override
    protected void calc() {
        super.name = "FiboStream extends Extends";

        // Initial element of stream: new long[]{0, 1}
        // Lambda expression calculate the next fibo based on the current: f -> new long[]{f[1], f[0] + f[1]}
        Stream.iterate(new long[]{0, 1}, f -> new long[]{f[1], f[0] + f[1]})
            .limit(super.size) // stream limit
            .forEach(f -> super.setData(f[0]) );  // set data in super class
    }

    /*
    Tester class method.
     */
    static public void main(int... numbers) {
        for (int nth : numbers) {
            Fibo fib = new FiboFor(nth);
            fib.print();
            System.out.println();
        }
    }
}

FiboStream.main(2, 5, 8);
```

    FiboFor computed Fibonacci in 42715 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 2 = 1
    Fibonacci List = [0, 1]
    
    FiboFor computed Fibonacci in 58457 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 5 = 3
    Fibonacci List = [0, 1, 1, 2, 3]
    
    FiboFor computed Fibonacci in 65654 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 8 = 13
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13]
    


## Popcorn Hacks
Objectives of these hacks are ...

1. Understand how to fullfill abstract class requirements using two additional algoritms.
2. Use inheritance style of programming to test speed of each algorithm.  To test the speed, a.) be aware that the first run is always the slowest b.) to time something, my recommendation is 12 runs on the timed element, through out highest and lowest time in calculations.
3. Be sure to make a tester and reporting methods.

.85 basis for text based comparison inside of Jupyter Notebook lesson

## Hacks
Assign in each Team to build a Thymeleaf UI for portfolio_2025 using this example https://thymeleaf.nighthawkcodingsociety.com/mvc/fibonacci as basis.  Encorporate into Algorithms menu.

Since there are three teams, one team can do Fibo, others Pali and Factorial.  Assign this to people that are struggling for contribution and presentation to checkpoints.

.90 basis for FE presentation in Thymmeleaf to BE call in Spring


```Java

class FiboWhile extends Fibo {
    public FiboWhile(int nth) {
        super(nth);
    }

    @Override
    protected void calc() {
        super.name = "FiboWhile";
        long a = 0, b = 1;
        int count = super.size;
        while (count-- > 0) {
            super.setData(a);
            long temp = a;
            a = b;
            b = temp + b;
        }
    }
}

class FiboRecursion extends Fibo {
    public FiboRecursion(int nth) {
        super(nth);
    }

    @Override
    protected void calc() {
        super.name = "FiboRecursion";
        for (int i = 0; i < super.size; i++) {
            super.setData(fib(i));
        }
    }

    private long fib(int n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
}

public class Test {
    public static void main(String[] args) {
        int[] testCases = {10, 20, 30};
        new FiboFor(10).print();
        new FiboWhile(10).print();
        new FiboStream(10).print();
        new FiboRecursion(10).print();
    }
}
Test.main(new String[]{});

```

    FiboFor computed Fibonacci in 83218 ns
    Calculation method = FiboFor extends Fibo
    Fibonacci Number 10 = 34
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    FiboWhile computed Fibonacci in 77052 ns
    Calculation method = FiboWhile
    Fibonacci Number 10 = 34
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    FiboStream computed Fibonacci in 244825 ns
    Calculation method = FiboStream extends Extends
    Fibonacci Number 10 = 34
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    FiboRecursion computed Fibonacci in 279187 ns
    Calculation method = FiboRecursion
    Fibonacci Number 10 = 34
    Fibonacci List = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


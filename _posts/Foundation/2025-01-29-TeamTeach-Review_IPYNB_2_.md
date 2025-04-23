---
layout: post
title: TeamTeach Retrospective
permalink: /CSA_Teamteach_Retrospective
comments: True
---

## Primitive Types
- Topics include variables, data types (int, double, boolean), arithmetic operators, type casting, and constants.
- Common issues: Integer division confusion, precision with double, and incorrect casting

KEY LEARNING POINTS:
- Understand how data is stored and manipulated.
- Always remember integer division truncates; use casting for accurate results.
- Know the limits of each primitive type and when to use them.

## Recursion
- ONLY EXIST ON THE MC
- Definition: when a function calls itself to solve small instances of the same problem
- Base Case: Essential for stopping recursion; without it, the function will cause a stack overflow.
- Recursive Case: The function reduces the problem into a smaller instance of itself.
- Stack Usage: Recursive calls use the call stack, leading to higher memory usage compared to iteration.
- Efficiency: Some problems (like tree traversal and backtracking) are naturally suited for recursion.
- Risk of Infinite Recursion: If the base case is missing or incorrect, recursion will not terminate.
Concept: A divide-and-conquer sorting algorithm that splits, sorts, and merges arrays.

- MERGE SORT:
   - Concept: A divide-and-conquer sorting algorithm that splits, sorts, and merges arrays.
   - Recursive Splitting: The array is split into left and right halves recursively until each sub-array has one element.
   - Time Complexity: Always O(n log n), making it faster than O(n²) sorting algorithms like bubble sort.
   - Merge Function Details: Uses two temporary arrays (leftArray and rightArray), then merges them back into the original array.

KEY LEARNING POINTS: 

- For the collegeboard exam, recursion is tested in multiple-choice questions, focusing on understanding return values and tracing recursive calls. Key concepts include base cases, recursive cases, and stack usage, with common problems like factorial, sum of digits, binary search (O(log n)), and merge sort (O(n log n)). 

## Methods and Control Structures
- Importance: 
   - Reusable code that performs specific tasks
   - Helps break down programs into manageable parts.
- Modifier: Describes the method’s properties.
- Access Modifiers:
   - public: Accessible everywhere.
   - private: Accessible only within the class.
   - protected: Accessible within the package and subclasses.
- Non-Access Modifiers:
   - static: Belongs to the class, not the object.
   - final: Cannot be overridden.
- Return Type: Specifies what the method returns (int, void, etc.).
- Instance Methods: Belongs to objects (e.g., myObject.method()).
- Static Methods: Belongs to the class (e.g., ClassName.method()).

KEY LEARNING POINTS:

- Be sure modifiers are correct along with return type, these are common errors collegeboard looks for. Ensure understanding of method calls in order to avoid silly mistakes.

## Classes
- Blueprint for Objects: A class is essentially a blueprint for creating objects in Java. It defines both the data (fields) and the behaviors (methods) that an object will have.
- Encapsulation: Classes allow you to bundle data (fields) and methods that operate on the data into a single unit. This also helps in keeping the data safe by restricting access to it via access modifiers like private.
- Inheritance: Classes support inheritance, meaning that one class (subclass) can inherit fields and methods from another class (superclass), allowing for code reuse.
- Polymorphism: This principle allows for the use of the same method name in different contexts, like method overloading (same method name, different parameters) and method overriding (subclass providing specific implementation).
- Access Modifiers: Classes use access modifiers (private, public, protected, etc.) to define the visibility of fields and methods. Private means accessible only within the class, public means accessible everywhere.
- Mutators and Accessors: Methods like getters (accessor) and setters (mutator) are often used to read and modify private fields of a class.
- Easy Points in FRQs: In class-related Free Response Questions (FRQs), focus on getting the easy points. For example, correctly declaring the class header and private instance variables can already earn you up to 4 points.
- Destruction of Data: Be mindful of modifying persistent data, especially when passing objects as parameters. This can lead to unintended side effects.
- Constructor Initialization: Constructors are responsible for initializing the state of objects. Make sure to properly initialize instance variables within your constructors.

KEY LEARNING POINTS:

- A class in Java is a blueprint for creating objects, encapsulating data and behaviors. Key concepts include encapsulation, inheritance, polymorphism, and abstraction, which help organize and reuse code efficiently. When tackling AP CSA FRQs, focus on following instructions carefully, avoiding unnecessary code, and ensuring correct method signatures and variable declarations to earn points.

## Arrays/Arraylists
- ArrayList Creation: Use ArrayList<Type> list = new ArrayList<Type>(); to create an ArrayList.
- Common Methods: Methods like add(), get(), set(), remove(), size(), and contains() are frequently used to modify and interact with ArrayLists.
- Adding Elements: list.add(value); appends a value, while list.add(index, value); inserts a value at a specific index.
- Accessing Elements: Use list.get(index); to access an element by index.
- Removing Elements: list.remove(index); or list.remove(value); to remove elements by index or value.
- Nested Loops: Nested loops can be used to compare elements of an ArrayList against each other.
- Declare Class Header: Always start with a correctly formatted class declaration, such as public class ClubMembers {}.
- Constructor: Ensure that the constructor initializes key variables like memberList = new ArrayList<>();.
- Check Method Signatures: Pay attention to method headers and ensure you include the correct return type and parameters.
- Return Correct Data: Ensure that any method with a return type returns the correct data—like an updated list of graduated members in good standing.

KEY LEARNING POINTS:
- In FRQs, it's important to correctly declare variables, iterate through lists with proper logic, and ensure that return types and conditions, such as graduation year and standing, are handled accurately. Also, make sure elements of arraylists are being accessed in a proper fashion. (.get())


## 2D Arrays
- Declaring 2D Arrays: Use int[][] array = new int[2][3]; to declare and initialize a 2D array with specific dimensions (2 rows and 3 columns).
- Iterating with Enhanced For Loops: Use nested enhanced for loops (for (int[] row : array) { for (int value : row) { ... } }) to iterate through each element of a 2D array.
- Accessing Elements: To access an element, use array[row][col], where row and col represent the index positions.
- Finding Dimensions: Use array.length for the number of rows and array[0].length for the number of columns. <- only works for non-jagged arrays
- Jagged Arrays: To find the number of columns in a jagged 2D array, use array[row].length since not all rows may have the same number of columns.
- Misusing .get() vs [].: .get() is for accessing elements in ArrayLists, not arrays. Use [] for arrays.
- Correct Initialization Format: Always initialize 2D arrays as int[][] arr = new int[a][b], where a is the row count and b is the column count.
- Avoiding Misassumptions: Don’t assume all rows of a 2D array have the same number of columns unless you’re working with a non-jagged (rectangular) array.

KEY LEARNING POINTS:
- When working with 2D arrays in Java, ensure correct initialization using int[][] array = new int[rows][cols], and iterate through elements using nested enhanced for loops. Be mindful of common pitfalls, such as index out of bounds exceptions, jagged array structures, and improper copying methods. Always use proper syntax and avoid misusing array-specific methods like .get().

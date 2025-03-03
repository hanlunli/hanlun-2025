---
layout: post
title: Team Teach Blog
type: issues
comments: True
hide: True
permalink: /teamteachblog
---

<style>
  .modal {
    display: none; /* Hidden by default */
    position: fixed;
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto; /* Enable scroll if needed */
    background-color: rgba(0, 0, 0, 0.5); /* Black with opacity */
  }

  /* Modal Content */
  .modal-content {
    background-color: #fff;
    margin: 10% auto; /* 10% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Adjust as needed */
    border-radius: 5px;
    position: relative;
  }

  /* Close Button */
  .close {
    color: #aaa;
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
  }

  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
  }

  /* Open Modal Buttons */
  .open-modal-btn {
    padding: 10px 20px;
    margin: 10px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
    background-color: #7e92d6;
    color: white;
  }

  .open-modal-btn:hover {
    background-color: #7e92d6;
  }

  /* Optional: Styling for the definition lists */
  dl {
    margin: 0;
  }

  dt {
    font-weight: bold;
    margin-top: 10px;
  }

  dd {
    margin-left: 20px;
  }
</style>

<!-- Buttons to Open Modals -->
<div style="text-align: center; margin-top: 50px;">
  <button class="open-modal-btn" onclick="openModal('unit2Modal')">Open Unit 2</button>
  <button class="open-modal-btn" onclick="openModal('unit3Modal')">Open Unit 3</button>
  <button class="open-modal-btn" onclick="openModal('unit4Modal')">Open Unit 4</button>
  <button class="open-modal-btn" onclick="openModal('unit5Modal')">Open Unit 5</button>
  <button class="open-modal-btn" onclick="openModal('unit6Modal')">Open Unit 6</button>
  <button class="open-modal-btn" onclick="openModal('unit7Modal')">Open Unit 7</button>
  <button class="open-modal-btn" onclick="openModal('unit8Modal')">Open Unit 8</button>
  <button class="open-modal-btn" onclick="openModal('unit9Modal')">Open Unit 9</button>
</div>

<!-- Unit 2 Modal -->
<div id="unit2Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 2</h2>
    <dl>
      <dt>Objects</dt>
      <dd>- Initializing objects using constructors</dd>
      <dd>- Call methods on objects to perform actions</dd>
      <dt>Wrapper</dt>
      <dd>- Wrapping and unwrapping primitive data types</dd>
    </dl>
  </div>
</div>

<!-- Unit 3 Modal -->
<div id="unit3Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 3</h2>
    <dl>
      <dt>Boolean Expressions</dt>
      <dd>- Expressions like "==" or "<=" return true if conditions are met, otherwise false</dd>
      <dd>- Allows for comparison operations</dd>
      <dt>If, If/Else, Else If Statements</dt>
      <dd>- Execute code if certain conditions are met</dd>
      <dd>- Support "nested" conditions for complex logic</dd>
    </dl>
  </div>
</div>

<!-- Unit 4 Modal -->
<div id="unit4Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 4</h2>
    <dl>
      <dt>Loops/Iteration</dt>
      <dd>- For loops, while loops, enhanced for loops (for each)</dd>
      <dd>- Allows running code a set number of times or until a condition is false</dd>
      <dd>- Nested for loops enable loops within loops</dd>
      <dt>String Iteration</dt>
      <dd>- Methods like `length()` or `substring()` allow for flexible manipulation of strings</dd>
    </dl>
  </div>
</div>

<!-- Unit 5 Modal -->
<div id="unit5Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 5</h2>
    <dl>
      <dt>Classes</dt>
      <dd>- Modifiers like public/static to protect data</dd>
      <dd>- Define classes with methods and attributes</dd>
      <dd>- Overload methods by writing different methods with the same name but different parameters</dd>
    </dl>
  </div>
</div>

<!-- Unit 6 Modal -->
<div id="unit6Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 6</h2>
    <dl>
      <dt>Arrays</dt>
      <dd>- Store multiple values and use loops to process them</dd>
      <dd>- Nested loops handle more complex structures</dd>
    </dl>
  </div>
</div>

<!-- Unit 7 Modal -->
<div id="unit7Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 7</h2>
    <dl>
      <dt>ArrayList</dt>
      <dd>- A flexible, resizable list with helpful methods like `add()` and `get()`</dd>
      <dd>- Use for-each loops to easily iterate through items</dd>
    </dl>
  </div>
</div>

<!-- Unit 8 Modal -->
<div id="unit8Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 8</h2>
    <dl>
      <dt>2D Arrays</dt>
      <dd>- Think of it as a table: rows and columns of data</dd>
      <dd>- Use nested loops to iterate through each element</dd>
    </dl>
  </div>
</div>

<!-- Unit 9 Modal -->
<div id="unit9Modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Unit 9</h2>
    <dl>
      <dt>Inheritance</dt>
      <dd>- One class inherits methods and fields from another</dd>
      <dd>- Subclasses can override methods from the parent class</dd>
      <dd>- Polymorphism lets you treat objects as their parent type</dd>
    </dl>
  </div>
</div>

<script>
  // Get all modal elements
  const modals = document.querySelectorAll('.modal');
  // Get all close buttons
  const closeButtons = document.querySelectorAll('.close');

  // Function to open a specific modal
  function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.style.display = 'block';
    }
  }

  // Function to close all modals
  function closeModal() {
    modals.forEach(modal => {
      modal.style.display = 'none';
    });
  }

  // Add event listeners to all close buttons
  closeButtons.forEach(button => {
    button.addEventListener('click', closeModal);
  });

  // Close the modal when clicking outside of the modal content
  window.addEventListener('click', function(event) {
    modals.forEach(modal => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  });

  // Optional: Close modal with the Esc key
  window.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      closeModal();
    }
  });
</script>


| **Assignment**             | **Points**    | **Grade** | **Evidence** |
|----------------------------|---------------|-----------|--------------|
| Pull Request (Integration) | 2             |   1.69     |   [link](https://github.com/nighthawkcoders/portfolio_2025/pulls?q=is%3Apr+is%3Aclosed+author%3Ahanlunli)        |
| Relevancy Checklist (Peer) | 2             |     1.66      |[link](http://127.0.0.1:4100/hanlun-2025/sprint2)|
| Lesson (Group)             | 1             |    0.9       |              |
| Homework, Popcorn Hacks    | 1 x 8         |   5.46/6 (not all graded yet)        | 0.9+0.9+0.91+0.95+0.9+0.9             |
| Individual Contribution    | 1             |     0.9      |[link](https://github.com/hanlunli/portfolio_2025/commits/main/?author=hanlunli)|
| Personal Notebooks / Blogs | 1             |0.9|[link]({{site.baseurl}}/teamteachblog)|
| Total                      | 15 (13 so far)            |11.51|              |


| **Skill**                  | **Points**    | **Grade** | **Evidence** |
|----------------------------|---------------|-----------|--------------|
| Work Habits (Analytics)    |   1           |0.9|I have very many commits that add relevant changes ![image of analytics]({{site.baseurl}}/images/analytics.png)|
| Team Planning (Issue)      |   1           |0.85|our team could work on planning more [link to planning document](https://docs.google.com/document/d/1HmLY5Y8AhCI-ywkJN--SPko2PLmuIy6ZeAN53ms-5Vw/edit?usp=sharing)|
| Presentation Memories      |   1           |0.9|I think our presentation was pretty engaging and reasonable. My individual part was [link](https://nighthawkcoders.github.io/portfolio_2025/csa/unit4-p1/unit4-2)|
| Grading and Feedback       |   1           |0.9|grading matched criteria|
| Beyond Perfunctory         |   1           |0.9|I went above and beyond on bricking pull requests ![image]({{site.baseurl}}/images/pullrequests.png)| 
| Total                      |   5           |4.45|              |

## Relevancy Checklist

| **Assignment**          | **Weightage** | **Grade** | **Comments** |
|-------------------------|---------------|-----------|--------------|
| College Board Coverage  | 20            | 18       | he included all collegeboard sections, and also added more content          |
| Java Examples           | 30            |29| included good examples for syntax          |
| Popcorn Hack Usage      | 10            | 9       | popcorn hacks seem pretty engaging and interesting, some of them are relatively challenging, which is good|
| Homework                | 10            |9    | a good amount of homework, seems like it meets the time requirement. I think the extra credit hack is pretty fun/challenging.|
| Grading Plan            | 10            | 9|Not a lot of planning for grading, however all grading seems to be done|
| Original an Creative    | 10            |9|This teamteach looks a little bland, but at least it has original elements in the hacks/content.|
| Total                  | **90**        |83|Overall, your it seems pretty good. I like the original elements like the animation, but overall, the teamteach could have been themed in a more engaging way, as well as having even more interactive elements.|

-Akhil Singamneni


```java
import java.util.ArrayList;

class Person {
    private String name;
    private int age;

    Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    public String getName(){ return name; }

    public void displayInfo(){
        System.out.println(name + " (Age: " + age + ")");
    }
}

class Student extends Person {
    private int[] grades;
    private boolean[][] attendance;

    Student(String name, int age, int[] grades, boolean[][] attendance){
        super(name, age);
        this.grades = grades;
        this.attendance = attendance;
    }

    public double getAverageGrade(){
        int sum = 0;
        for(int grade : grades) sum += grade;
        return sum / (double) grades.length;
    }

    @Override
    public void displayInfo(){
        super.displayInfo();
        System.out.println("Average Grade: " + getAverageGrade());
        System.out.print("Attendance: ");
        for(int week = 0; week < attendance.length; week++){
            for(int day = 0; day < attendance[week].length; day++){
                System.out.print(attendance[week][day] ? "P " : "A ");
            }
            System.out.print("| ");
        }
        System.out.println();
    }
}

class Teacher extends Person {
    private String subject;

    Teacher(String name, int age, String subject){
        super(name, age);
        this.subject = subject;
    }

    @Override
    public void displayInfo(){
        super.displayInfo();
        System.out.println("Teaches: " + subject);
    }
}

class School {
    private ArrayList<Person> people = new ArrayList<>();

    public void addPerson(Person p){
        if(p != null){
            people.add(p);
            System.out.println("Added: " + p.getName());
        }
    }

    public Person findPerson(String name){
        for(Person p : people){
            if(p.getName().equalsIgnoreCase(name)){
                return p;
            }
        }
        return null;
    }

    public void displayPeople(){
        for(Person p : people){
            p.displayInfo();
            System.out.println();
        }
    }
}

public class Main {
    public static void main(String[] args){
        School school = new School();
        int[] grades1 = {85, 90, 78};
        boolean[][] attendance1 = {
            {true, true, false, true, true},
            {true, true, true, true, true}
        };
        int[] grades2 = {92, 88, 95};
        boolean[][] attendance2 = {
            {true, true, true, true, true},
            {true, false, true, true, false}
        };
        Student s1 = new Student("Alice", 16, grades1, attendance1);
        Student s2 = new Student("Bob", 17, grades2, attendance2);
        Teacher t1 = new Teacher("Mr. Lee", 40, "Physics");
        Teacher t2 = new Teacher("Ms. Kim", 35, "Chemistry");
        school.addPerson(s1);
        school.addPerson(s2);
        school.addPerson(t1);
        school.addPerson(t2);
        school.displayPeople();
        Person found = school.findPerson("Alice");
        if(found != null){
            System.out.println("Found:");
            found.displayInfo();
        } else {
            System.out.println("Person not found.");
        }
    }
}
Main.main(null);
```

    Added: Alice
    Added: Bob
    Added: Mr. Lee
    Added: Ms. Kim
    Alice (Age: 16)
    Average Grade: 84.33333333333333
    Attendance: P P A P P | P P P P P | 
    
    Bob (Age: 17)
    Average Grade: 91.66666666666667
    Attendance: P P P P P | P A P P A | 
    
    Mr. Lee (Age: 40)
    Teaches: Physics
    
    Ms. Kim (Age: 35)
    Teaches: Chemistry
    
    Found:
    Alice (Age: 16)
    Average Grade: 84.33333333333333
    Attendance: P P A P P | P P P P P | 


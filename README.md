# Beepkart-Coding-Assesment
A small repo for the coding assignment for Beepkart Private Limited

## Guide for Question 12 Demo
Works for Ubuntu/MacOS
Create a Virtual Environment of any name
```
python3 -m venv env
```
Activate It using
```
source env/bin/activate
```
Install the modules from requirements.txt
```
pip3 install -r requirements.txt
```

Set FLASK_APP variable to upload.py
```
export FLASK_APP=upload.py
```

There is a video of the sample upload and rendering of the result being done.

## Guide for Q 13
Run
```
python3 q13.py
```

## Subjective Questions and Answers
### Answer 1
A class is basically a unit in which code and the variables that is uses that can be stored under one logical unit. An object is an instance of a class which is formed from the "blueprint" provided by a class.
A constructor is basically a block of code that is automatically called when a class's object is first declared. It follows all the syntactical rules of a normal class except that it does not have a return type and that it must share the same name as the class it is in.
For example, in Java
```
class Person {
  protected String fname = "John";
  protected String lname = "Doe";
  protected String email = "john@doe.com";
  protected int age = 24;
}

class Employee extends Person 
{
  private int joining = 2018;
  public static void main(String[] args) 
  {
    Employee myObj = new Employee();
    System.out.println("Name: " + myObj.fname + " " + myObj.lname);
    System.out.println("Email: " + myObj.email);
    System.out.println("Age: " + myObj.age);
    System.out.println("Graduation Year: " + myObj.joining);
  }
```
The protected keyword is an access modifier used for attributes, methods and constructors, making them accessible in the same package and subclasses.Protected access gives the subclass a chance to use the helper method or variable, while preventing a nonrelated class from trying to use it.
The public keyword is also an access modifier, that allows the code to be acessible by any other class.	In the case of private,the code is only accessible within the declared class.

### Answer 2
Cookies  are small text files to store the data of the client  (whether they have logged in/out, shopping cart details etc. ) stored on client(browser) side and Session info stored on server side.

The cookie is a piece of data sent from the server and stored in the client during a request and response cycle. The cookie is a small file stored in the browser and contains the session information from the server.

When accessing a website for the first time, the server sends session information and sets it in your browser cookie on your local computer. The actual session data is stored on the server side. The client side cookie is compared with the server side session data on each request to identify your current session. So when you visit a website repeatedly, your session will be recognized because of the stored cookie with its associated information.

To access data from  a Flask session, you have to provide the key value.
For example,
```
session["email"] = request.form["Email"]
```
Whereas in the case of cookies, one can use it like this,
```
res = make_response("<h1>cookie is set</h1>")  
res.set_cookie('coo','kie')  

```

## Answer 3

Overloading occurs when two or more methods in one class have the same method name but different parameters and perform different functions. Usually, this is used to perform similar but not the same task for different sets of arguments.

Overriding means having two methods with the same signature (name and parameters). It allows a child class to provide a specific implementation of a method that is already provided its parent class.

```
class Dog
{
    public void bark()
    {
        System.out.println("woof ");
    }
}
class Hound extends Dog
{
    public void sniff()
    {
        System.out.println("sniff ");
    }
 
    public void bark()
    {
        System.out.println("bowl");
    }
}
 
public class OverridingTest
{
    public static void main(String [] args)
    {
        Dog dog = new Hound();
        dog.bark();
    }
}
```

Output

>bowl

Overloading Example

```
class Dog
{
    public void bark()
    {
        System.out.println("woof ");
    }
 
    //overloading method
    public void bark(int num)
    {
    	for(int i=0; i<num; i++)
    		System.out.println("woof ");
    }
}
```

###Answer 4

GROUP BY statement groups rows that have the same values into summary rows.The GROUP BY Clause is used to collect data from multiple records and group the result by one or more column. It is generally used in a SELECT statement.
```
SELECT address, COUNT(*)  
FROM   officers   
GROUP BY address;   
```
Returns the count of rows belonging to each unique address. ie. find the number of repetitions in the address


MySQL DISTINCT clause is used to remove duplicate records from the table and fetch only the unique records. The DISTINCT clause is only used with the SELECT statement.

```
SELECT DISTINCT expressions  
FROM tables  
[WHERE conditions]; 
```


## Answer 5
A join clause is used to combine rows from two or more tables, based on a related column between them.
Inner Join Returns only what is common in the two tables.
Left Join Returns everything in left table and what is common between them.
Right join gets everything in the right table and what is common between them.o
Assuming you're joining on columns with no duplicates, which is a very common case:

An inner join of A and B gives the result of A intersect B, i.e. the inner part of a Venn diagram intersection.

An outer join of A and B gives the results of A union B, i.e. the outer parts of a Venn diagram union.

Examples

Suppose you have two tables, with a single column each, and data as follows:

A    B
-    -
1    3
2    4
3    5
4    6

Inner join

select * from a INNER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a = b.b;

a | b
--+--
3 | 3
4 | 4

Left outer joi

select * from a LEFT OUTER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a = b.b(+);

a |  b
--+-----
1 | null
2 | null
3 |    3
4 |    4
Right outer join

select * from a RIGHT OUTER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a(+) = b.b;

a    |  b
-----+----
3    |  3
4    |  4
null |  5
null |  6


##Answer 6

```
with temp as
(
 Select *
 from employee inner join salary
 on employee.id = salary.emp_id
)
with temp1 as
(
    select emp_name, salary, rn = row_number() OVER (ORDER BY salary desc)
    From temp
)
select *
from temp1 
where rn = 5
```

## Answer 8

An exception is an event, which occurs during the execution of a program that stops the normal execution of the program unless it is handled  with an exception handler.

```
try 
{
 int num1 = 10/0;
}
catch (Exception e)
{
         /* This is a generic Exception handler which means it can handle
          * all the exceptions. This will execute if the exception is not
          * handled by previous catch blocks.
          */
         System.out.println("Exception occurred");
}

```

## Answer 9 

Domain names are mainly used as names for websites.
It provides an easier to remember way to access a websites.
For example, to access google, 
you must type www.google.com, instead of its IP address, which isn't static.  
A subdomain is an additional part to your main domain name. Subdomains are created to organize and navigate to different sections of your website. You can create multiple subdomains or child domains on your main domain.

A static website is a website whose content is static and not generated dynamically. 
It has only pre-made assets and once written cannnot be changed on the fly. So, each page on the site would be represented by a .html file on the server. In this case, the "back-end" is literally just the web server. It's just responding to GETs by returning files with a media type of text/html.

A dynamic website is a website with a back-end typically with a system in place to manage content and updates (like a content management system, like WordPress.) It can be changed on the fly based on user input and due to responses from the server side.




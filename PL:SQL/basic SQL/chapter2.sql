--Brogan Avery
--Ch 2 assignment


--Q1
select *
from books;

--Q2
select title
from books;

--Q3

select title, pubdate AS "Publication Date" 
from books;

--Q4

select customer# , city , state
from customers;

--Q5
select name, contact AS "Contact Person", phone
from publisher;

--Q6

select distinct category
from books;

--Q7

select distinct customer#
from orders;

--Q8

select category, title
from books;

--Q9

select lname || ', ' || fname AS Authors
from author;

--Q10

select order#, item#, isbn,quantity,paideach, quantity*paideach AS "Item Total"
from orderitems;
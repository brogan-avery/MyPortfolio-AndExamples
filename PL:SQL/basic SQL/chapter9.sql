--Brogan Avery
--Chapter 9

--Problem 1
select BOOKS.TITLE as title , PUBLISHER.NAME as publisher, PUBLISHER.PHONE as phone
from books, publisher
where BOOKS.PUBID =PUBLISHER.PUBID;

--Problem 2
select orderitems.order# as order_ID, customers.firstname as first, customers.lastname as last 
from orderitems, orders, customers
where orderitems.order# != orders.order# and orders.customer# = customers.customer# 
order by orders.orderdate;

--Problem 3 
select c.customer#, c.firstname||''||c.lastname as name, o.order#, oi.isbn, b.category, c.state  
from customers c, orders o, books b, orderitems oi
where c.customer# = o.customer# and o.order# = oi.order# and oi.isbn = b.isbn and c.state = 'FL' and b.category= 'COMPUTER';

--select customer#,c.firstname ||''|| c.lastname as lname,order#,isbn,b.category,c.state
--from customers c join orders o using(customer#) join orderitems oi using (order#) join books b using (isbn) 
--where state = 'FL' and category = 'COMPUTER';

--Problem 4
select distinct c.firstname||' '||c.lastname as name,b.title 
from customers c, orders o, orderitems oi,books b
where (c.firstname||' '||c.lastname) = 'JAKE LUCAS' and c.customer# = o.customer# and oi.order# = o.order# and b.isbn = oi.isbn;

--Problem 5
select o.orderdate,b.title, (oi.paideach - b.cost) as profit
from customers c natural join orders o natural join orderitems oi natural join books b where c.firstname = 'JAKE' and c.lastname = 'LUCAS' 
order by profit desc, orderdate;

--Problem 6
select b.title 
from books b join bookauthor on b.isbn = bookauthor.isbn join author on bookauthor.authorid = author.authorid 
where lname = 'ADAMS';

--Problem 7
select p.gift 
from books join promotion p on retail between minretail and maxretail
where books.title ='SHORTEST POEMS';

--Problem 8
--select a.lname,a.fname,b.title
--from customers c join orders o on c.customer# = o.customer# join orderitems oi on o.order# join books b on oi.isbn = b.isbn join bookauthor ba on b.isbn = ba.isbn join author a on ba.authorid = a.authorid
--where fname = 'BECCA' and lname = 'NELSON';

select a.lname, a.fname, b.title
from books b, orders o, orderitems oi, customers c, bookauthor ba, author a
where c.customer# = o.customer# and firstname = 'BECCA' and lastname = 'NELSON' and o.order# = oi.order# and oi.isbn = b.isbn and b.isbn = ba.isbn and ba.authorid = a.authorid;

--Problem 9
select b.title, o.order#, c.state
from books b, orders o, orderitems oi, customers c
where c.customer#(+) = o.customer# and oi.isbn(+) = b.isbn and o.order#(+) = oi.order#;

--Problem 10
select e.fname||' '||e.lname as employee,e.job,e2.fname||' '||e2.lname as manager
from employees2 e, employees2 e2
where e2.empno = e.mgr;
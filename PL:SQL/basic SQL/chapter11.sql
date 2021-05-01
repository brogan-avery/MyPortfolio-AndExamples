--Brogan Avery
--Chapter 11

--problem 1
select count(*)
from books
where category = 'COOKING';

--problem 2
select count(*)
from books
where retail > 30;

--problem 3
select max(pubdate)
from books;

--problem 4
select sum(quantity*paideach) as sum
from orders join orderitems on orders.order# = orderitems.order# join books on orderitems.isbn = books.isbn
where customer# = 1017;

--problem 5
select min(retail)
from books
where category = 'COMPUTER';

--problem 6
select avg(quantity*paideach) as avg_profit
from orders join orderitems on orders.order# = orderitems.order# join books on orderitems.isbn = books.isbn;

--problem 7
select customer#,count(*)
from orders
group by customer#;

--problem 8
select name,category,avg(retail)
from books join publisher on books.pubid = publisher.pubid
where category in('COMPUTER' , 'CHILDREN')
group by name, category
having avg(retail)>50;

--problem 9
select firstname, lastname , sum(retail * quantity)
from customers join orders on customers.customer# = orders.customer# join orderitems on orders.order# = orderitems.order# join books on orderitems.isbn = books.isbn
where state in ('FL', 'GA')
group by firstname, lastname
having sum(retail*quantity) > 80;

--problem 10
select max(retail)
from books join bookauthor on books.isbn = bookauthor.isbn join author on author.authorid = bookauthor.authorid
where fname = 'LISA' and lname = 'WHITE';
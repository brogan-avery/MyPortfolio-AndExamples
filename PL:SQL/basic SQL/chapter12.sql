--Brogan Avery
--Chapter 12

--Problem 1
select title, retail
from books
where retail < (select avg(retail) from books);

--Problem 2
select b.title, c.category, b.cost 
from books b, (select category,avg(cost) averagecost from books group by category)c
where b.category = c.category and b.cost < c.averagecost;

--Problem 3
select order#
from orders
where shipstate = (select shipstate from orders where order# = 1014);

--Problem 4
 Select sum(paideach),order#
 from orderitems
 group by order#


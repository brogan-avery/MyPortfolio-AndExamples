--Brogan Avery
--March 5, 2020
--Chapter 8 assignment

--PROBLEM 1
select lastname,firstname,state
from customers
where state = 'NJ';

--PROBLEM 2
select order#, shipdate
from orders
where shipdate > '01-APR-09';

--PROBLEM 3
select title, category
from books
where category != 'FITNESS';

--PROBLEM 4
select customer#, lastname, state
from customers
where state = 'NJ' or state = 'GA'
order by lastname;

-- or can be order by 2 (for the second col)
--to decend = order by lastname desc;
--another way = where state in ('NJ','GA')

--PROBLEM 5
select order#, shipdate
from orders
where shipdate <= '01-APR-09';

select order#, shipdate
from orders
where shipdate < '02-APR-09';

--PROBLEM 6
select lname, fname
from author
where lname like '%IN%'
order by lname,fname;
--PROBLEM 7
select lastname, referred
from customers
where referred is not null;

--PROBLEM 8
select title, category
from books
where category IN('CHILDREN','COOKING');

select title, category
from books
where category = 'CHILDREN' OR category = 'COOKING';

select title, category
from books
where category like 'CHILD%' OR category like 'COOK%';
--PROBLEM 9
select isbn,title
from books
where title like '_A_N%'
order by title desc;

--PROBLEM 10
select title,pubdate
from books
where pubdate between '01-jan-05' and '31-dec-05' and category = 'COMPUTER';

select title,pubdate
from books
where pubdate >= '01-jan-05' and pubdate <= '31-dec-05' and category = 'COMPUTER');

select title,pubdate
from books
where pubdate like '%_05'  and category = 'COMPUTER';

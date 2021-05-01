--Brogan Avery
--Chapter 10

--Problem 1

select initcap(firstname) as first ,initcap(lastname) as last
from customers;

--Problem 2
select customer#,NVL2(referred, 'REFERRED','NOT REFERRED') as referred
from customers;

--Problem 3
select title, to_char(quantity*(paideach-cost), '$999.99') as profit
from books join orderitems using(isbn)
where order# = 1002;

--Problem 4
select title, round((retail-cost)/cost*100,0)||'%' as percentage
from books;

--Problem 5
select to_char(current_date,'DAY HH:MI:SS') as now
from dual;

--Problem 6
select title, LPAD(cost,12,'*') as cost
from books;

--Problem 7
select distinct length(isbn)  as length
from books;

--Problem 8
select title,pubdate,sysdate as now,trunc(months_between(sysdate,pubdate),0) as age
from books;

--Problem 9
select next_day(sysdate,'WED') 
from dual;

--Problem 10
select customer#,substr(zip,3,2),instr(customer#,3,1,1)
from customers;
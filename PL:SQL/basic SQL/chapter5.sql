--Brogan Avery
--Chapter 5

--Q1
insert into orders (order#, customer#, orderdate)
values(1021, 1009, '20-jul-09');

--Q2
update orders
set shipzip = '33222'
where order# = '1017';

--Q3
commit;

--Q4
insert into orders  (order#, customer#, orderdate)
values(1022, 2000, '06-aug-09');

--will not work because the the customer must first exist in the customer table but customer 2000 does not exist and it creates a referential integrity error.

--Q5

insert into orders  (order#, customer#)
values(1023, 1009);
-- It won't let you enter a new row and leave the order date blank/null.
commit;
--Q6
update books
set cost = &cost 
where isbn = '&isbn';

--Q7
--updated in table
--Q8
rollback;
--Q9
delete from orderitems
where order# = 1005;

delete from orders
where order# = 1005;

--Q10
rollback;


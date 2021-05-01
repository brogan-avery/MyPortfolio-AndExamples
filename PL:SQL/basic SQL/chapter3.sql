--Brogan Avery
--Ch3 assignment

--Q1
drop table category;

create table CATEGORY
(CatCode char(2), CatDesc VARCHAR2(10));

--Q2

--drop table employees;

create table EMPLOYEES
(Emp# number(5), Lastname VARCHAR2(25), Firstname VARCHAR2(25), Job_class VARCHAR2(4));

--Q3
alter table Employees
add (EmpDate date default sysdate, EndDate date);

--Q4
alter table employees
modify Job_class VARCHAR2(2);

--Q5

alter table employees
drop column EndDate;

--Q6
drop table JL_EMPS;

rename employees to JL_EMPS;

--Q7

create table BOOK_PRICING
as (select ISBN ID, Cost, Retail, Category from books);

--Q8
alter table book_pricing
set UNUSED (category);

desc book_pricing;

--Q9
truncate table book_pricing;

desc book_pricing;

--Q10
drop table book_pricing PURGE;

drop table jl_emps;

flashback table jl_emps to before drop;






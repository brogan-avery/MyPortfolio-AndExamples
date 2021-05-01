--Brogan Avery
--chapter 4

--Q1
drop table store_reps;
create table store_reps 
(rep_ID number(5) primary key, 
last varchar2(15),
first varchar2(10),
comm char(1));

alter table store_reps
modify (comm default 'Y');

--Q2
alter table store_reps
modify(first not null, last not null);

--Q3

alter table store_reps
add constraint store_reps_comm_ck check (comm = 'Y' or comm = 'N');

--Q4
alter table store_reps
add Base_salary number(7,2);

alter table store_reps
add constraint store_reps_Base_salery_ck check (Base_salary > 0);
--Q5
drop table book_stores;
create table book_stores
(Store_ID number(8) primary key,
Name varchar2(30) unique not null,
Contact varchar2(30),
Rep_ID varchar2(5));

--Q6
alter table book_stores
modify(rep_id number(5))
add constraint book_stores_Rep_ID_fk foreign key (Rep_ID)
references store_reps(rep_ID);

--Q7
alter table book_stores
drop constraint book_stores_Rep_ID_fk;

alter table book_stores
add constraint book_stores_Rep_ID_fk foreign key (rep_ID)
references store_reps(rep_ID) on delete cascade;

--Q8
create table rep_contracts
(Store_ID number(8),
Name number(5),
Quarter char(3),
Rep_ID number(5), 
constraint rep_contracts_cpk primary key (Store_id,Quarter, Rep_ID),
constraint rep_contracts_Store_ID_fk foreign key (Store_ID) 
references book_stores(Store_ID),
constraint rep_contracts_Rep_ID_fk foreign key (Rep_id) 
references store_reps (rep_id));

--Q9
select constraint_name, constraint_type, search_condition, r_constraint_name, table_name
from user_constraints
where table_name = 'store_reps';

--Q10 
alter table store_reps
disable constraint store_reps_Base_salery_ck;

alter table store_reps
enable constraint store_reps_Base_salery_ck;



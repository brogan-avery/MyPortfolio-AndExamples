/*
***************************************************
Title: Final Project - tables build
Author: Brogan Avery
Created: 2021-04-28
***************************************************
*/

desc books

--  Add Quantity on Hand column to the BOOKS table
alter table books
add quantity_on_hand number(3) default 0;

select * from books;

--  Update Quantity on Hand to 1 for all books
update books
set quantity_on_hand = 1;

commit;

--  Create Sequence for Reorder# primary key
drop sequence REORDER#_SEQ;

create sequence REORDER#_SEQ;

--select REORDER#_SEQ.nextval from dual;

--  Create REORDER table

drop table reorder;

create table reorder
    (reorder# number(3),
     reorder_date date,
     reorder_isbn varchar2(10),
     reorder_quantity number(3),
     reorder_received date,
     constraint reorder_reorder#_pk primary key(reorder#),
     constraint reorder_isbn_fk foreign key(reorder_isbn) references books(isbn));

 


/*
***************************************************
Title: Rectangle Exercise
Author: Brogan Avery
Created: 2020-02-09
***************************************************
*/
set serveroutput on 

DECLARE

    --height
    h   number(3) :=    6;

    --width
    w   number(3) :=    8;
    
    --counter 
    i   number(3);
    
    numLines    number(3) :=   h;
    
    emptySpace VARCHAR2(1) :=    ' '; 
    
BEGIN

   for i in 1 .. w loop
        dbms_output.put('*');
    end loop;
    dbms_output.put_line('');
    
    for i in 1..numLines loop
        dbms_output.put('*');
        for i in 1..w-2 loop
            dbms_output.put(' ');
        end loop;
         dbms_output.put('*');
         dbms_output.put_line('');
    end loop;
     
    for i in 1 .. w loop
        dbms_output.put('*');
    end loop;
    
    dbms_output.put_line(' ');
END;
    
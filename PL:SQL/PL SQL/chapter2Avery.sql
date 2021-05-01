/*
***************************************************
Title: chapter 2
Author: Brogan Avery
Created: 2020-02-07
***************************************************
*/

--  2-9 and 2--11

set serveroutput on 
declare

    lv_payment_due_date           date        := '01-JAN-2021';
    lv_monthly_payment_amount     number(3)   := &payment_amount;
    lv_number_of_payments         number(2)   := &number_of_payments;
    lv_remaining_balance          number(4)   :=  lv_monthly_payment_amount * lv_number_of_payments;
    itr                           number(3)   := 1;
    
begin

    dbms_output.put_line('Due Date ' || to_char(lv_payment_due_date,'mm/dd/yyyy'));
    dbms_output.put_line('Payment Amount ' || to_char(lv_monthly_payment_amount,'$999.00'));
    dbms_output.put_line('Number of Payments ' || lv_number_of_payments);
    dbms_output.put_line('Remaining Amount ' || to_char(lv_remaining_balance,'$9,999.00'));
    
    for i in 1..lv_number_of_payments loop
        dbms_output.put_line('-------------------------');
        dbms_output.put_line('Payment Number ' || i);
        dbms_output.put_line('Date Due ' || to_char(lv_payment_due_date,'mm/dd/yyyy'));
        dbms_output.put_line('Payment Amount ' || to_char(lv_monthly_payment_amount,'$999.00'));
        lv_remaining_balance := lv_remaining_balance - lv_monthly_payment_amount;
        dbms_output.put_line('Remaining Amount ' || to_char(lv_remaining_balance,'$9,999.00'));
        lv_payment_due_date := add_months(lv_payment_due_date,1);
    end loop;
    
    -- will just go negative here unless the for loop is comented out first since the are doing the same thing
    while itr <= lv_number_of_payments loop
        dbms_output.put_line('-------------------------');
        dbms_output.put_line('Payment Number ' || itr);
        dbms_output.put_line('Date Due ' || to_char(lv_payment_due_date,'mm/dd/yyyy'));
        dbms_output.put_line('Payment Amount ' || to_char(lv_monthly_payment_amount,'$999.00'));
        lv_remaining_balance := lv_remaining_balance - lv_monthly_payment_amount;
        dbms_output.put_line('Remaining Amount ' || to_char(lv_remaining_balance,'$9,999.00'));
        lv_payment_due_date := add_months(lv_payment_due_date,1);
        itr := itr + 1;
    end loop;

end;
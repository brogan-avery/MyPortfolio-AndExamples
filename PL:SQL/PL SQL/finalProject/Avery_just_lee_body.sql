/*
***************************************************
Title: Just Lee Package Body
Author: Brogan Avery
Created: 2021-04-28
***************************************************
*/

set serveroutput on

CREATE OR REPLACE PACKAGE BODY JUST_LEE AS

--PROCEDURE 1
    procedure ship_order (p_order# in orders.order#%type) AS
        v_orders_shipdate       orders.shipdate%type; -- ship date from orders table
     
        cursor qty_curs is -- cursor to get quantity ordered for each book from order items table and the number of books on hand from book table
            select order#, isbn, quantity, quantity_on_hand 
                from orderitems join books
                using(isbn)
                where order# = p_order#; 
               
        lv_order#       orderitems.order#%type;
        lv_isbn     orderitems.isbn%type;
        lv_quantity     orderitems.quantity%type;
        lv_quantity_on_hand     books.quantity_on_hand%type;
      
        count_books_not_on_hand number(3) := 0; -- stores the number of items in an order than CANNOT be filled due to low quantity
        
        --custom errors/ exceptions 
        order_has_shipped_error exception;
        order_cannot_be_placed_error exception;
  
    BEGIN
        dbms_output.put_line('Shipping order# ' || p_order#);
        
        -- gets shipdate from orders table
        select shipdate
        into v_orders_shipdate
        from orders
        where order# = p_order#;
    
        dbms_output.put_line('Ship Date: ' || v_orders_shipdate);
        
        -- loop through cursor to print all objects/ items on the order
        dbms_output.put_line('All items in order: '); 
        open qty_curs; 
            loop
                fetch qty_curs into lv_order#, lv_isbn, lv_quantity, lv_quantity_on_hand; 
                exit when qty_curs%notfound; 
                
                dbms_output.put_line('  Book ISBN: ' || lv_isbn || ' Quantity Ordered: ' || lv_quantity );
                dbms_output.put_line('     Quantity on hand ' || lv_quantity_on_hand);
                
                -- Get count of how many order items CANNOT be filled
                if lv_quantity_on_hand < lv_quantity then
                        count_books_not_on_hand := count_books_not_on_hand + 1;
                end if;
            end loop; 
        close qty_curs;
    
        -- if the ship date is null, indicating it has not been shipped,
        -- and if the count of items that cannot be filled is 0,
        -- updates shipdate and book quantity on hand
        if v_orders_shipdate is null then
            if count_books_not_on_hand = 0 then
                update books
                set quantity_on_hand = quantity_on_hand - lv_quantity
                where lv_isbn = books.isbn;
            
                update orders
                set shipdate = sysdate
                where order# = p_order#;
        
                dbms_output.put_line('Order Placed');
        
                -- raises errors if either of the two conditions are not met
            else
                raise order_cannot_be_placed_error;
            end if;
       
        else
            raise order_has_shipped_error;
       
        end if;
   
    EXCEPTION
        when order_cannot_be_placed_error then
            dbms_output.put_line('Quantity ordered not in stock.');
        when order_has_shipped_error then
            dbms_output.put_line('This order has already been processed and shipped.');
             
    END ship_order;

 --PROCEDURE 2
    procedure insert_reorder (p_isbn in books.isbn%type) AS
    BEGIN
        dbms_output.put_line('Insert reorder for ISBN ' || p_isbn);
        
        -- adds a new entry to the reorder table
        insert into reorder(reorder#, reorder_date, reorder_isbn, reorder_quantity, reorder_received)
            values (reorder#_seq.nextval, sysdate, p_isbn, 10, null); 
    END insert_reorder;

 --PROCEDURE 3
    procedure receive_reorder (p_reorder# in reorder.reorder#%type) AS
        v_reorder_isbn      reorder.reorder_isbn%type;
        v_reorder_date      reorder.reorder_date%type;
        v_reorder_quantity      reorder.reorder_quantity%type;
        v_reorder_received      reorder.reorder_received%type;
    
    BEGIN
        dbms_output.put_line('Receive reorder# ' || p_reorder#);
    
        -- query the reorder table for the reorder number the user enters
        select reorder_isbn, reorder_date, reorder_quantity, reorder_received
            into v_reorder_isbn, v_reorder_date, v_reorder_quantity, v_reorder_received
            from reorder
            where reorder# = p_reorder#;
        
            dbms_output.put_line('Reorder ISBN: ' || v_reorder_isbn);
            dbms_output.put_line('Reorder Date: ' || v_reorder_date);
            dbms_output.put_line('Reorder Quantity: ' || v_reorder_quantity);
            dbms_output.put_line('Reorder Received on: ' || v_reorder_received);
        
        -- if the order has ben received but not yet filled
        if v_reorder_received is null then
            update books
            set quantity_on_hand = quantity_on_hand + v_reorder_quantity
            where isbn = v_reorder_isbn;
        
            update reorder
            set reorder_received = sysdate
            where reorder# = p_reorder#;
        else
            -- if the order has already been filled
            dbms_output.put_line('Reorder# ' || p_reorder# || ' was received on ' || v_reorder_received);
        end if;
    
    EXCEPTION
        -- message if a reorder number entered does not exist
        when no_data_found then
        dbms_output.put_line('Reorder has not been received.'); 
    
    END receive_reorder;

END JUST_LEE;
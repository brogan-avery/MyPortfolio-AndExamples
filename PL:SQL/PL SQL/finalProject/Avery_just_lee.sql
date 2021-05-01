/*
***************************************************
Title: Just Lee Package Header / Specifications 
Author: Brogan Avery
Created: 2021-04-28
***************************************************
*/

CREATE OR REPLACE
PACKAGE JUST_LEE AS 
    
    procedure ship_order (p_order# in orders.order#%type); -- param: order number
    -- procedure used to create and fill new orders
        -- Uses Orders table
        -- 1. makes sure the order has not all ready been filled and shiped
        -- 2. makes sure that there are enough of each book that the customer orders for the quantity that they ordered
        -- 3. If both of those are true, "ship" the order by updating the table values for the date shiped and remove the quantity of books ordered from the number on hand
    
    
    procedure insert_reorder (p_isbn in books.isbn%type); -- param: ISBN code of the book the store wants to restock by ordering from the book manufacturer??
    -- procedure used to insert a new reccord into the Reorder table
        -- inserts values for:
            -- auto gen ID 
            -- current date sys date
            -- ISBN from param 
            -- quantity (10) num
            -- has the order been received yet? bool/null
            

    procedure receive_reorder (p_reorder# in reorder.reorder#%type); -- param: Reorder ID
    -- a procedure that checks if an order to the manufacturer is still in transit or if it has been received
    
END JUST_LEE;


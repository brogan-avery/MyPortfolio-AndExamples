/*
***************************************************
Title: Trigger
Author: Brogan Avery
Created: 2021-04-28
***************************************************
*/

-- trigger to order new books when they run out
create or replace trigger books_quantity_trg
    after update of quantity_on_hand on books
    for each row
    when (old.quantity_on_hand !=0 and new.quantity_on_hand = 0)
begin
    just_lee.insert_reorder(:new.isbn);
end;
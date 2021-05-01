/*
***************************************************
Title: chapter 5
Author: Brogan Avery
Created: 2021-03-05
***************************************************
*/

set serveroutput on

-- function that creates to vars for a donor id and a found/not found bool
CREATE OR REPLACE PROCEDURE DDPAY_SP (
    P_DONOR IN VARCHAR2, -- donor id
    P_RESULT OUT boolean -- has an active pledge or not
) 
AS 
    lv_idpledge dd_pledge.idpledge%type; -- each record
    lv_pledges number(3); -- pledge count
   
BEGIN
    -- adds to count if record found
    select count(*)
    into  lv_pledges
    from dd_pledge
    where idstatus = 10 and paymonths <> 0 and iddonor = p_donor; -- open status for selected donor
    
    -- if the count for records found is greater than 0:     
    if lv_pledges > 0 then
       p_result := true;
       --DBMS_OUTPUT.PUT_LINE('True');
    else
       p_result := false;
       --DBMS_OUTPUT.PUT_LINE('False');
    end if;
    return p_result;
    
END DDPAY_SP;



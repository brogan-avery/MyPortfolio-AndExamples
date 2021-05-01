/*
***************************************************
Title: chapter 7, package specification
Author: Brogan Avery
Created: 2020-03-16
***************************************************
*/

create or replace PACKAGE PLEDGE_PKG AS 
    -- declares the functions of the package
    FUNCTION dd_paydate1_pf(p_id IN dd_pledge.idpledge%TYPE)
       RETURN DATE;
  
    FUNCTION dd_payend_pf(p_id IN dd_pledge.idpledge%TYPE)
       RETURN DATE;
  
    PROCEDURE dd_pList_pp(donor_Id IN dd_donor.iddonor%TYPE);

END PLEDGE_PKG;


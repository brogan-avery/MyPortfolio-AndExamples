/*
***************************************************
Title: chapter 6-13
Author: Brogan Avery
Created: 2020-03-16
***************************************************
*/

--  Assignment 6-13

CREATE OR REPLACE FUNCTION dd_payend_sf (p_id IN dd_pledge.idpledge%TYPE)
  RETURN DATE
  IS
  lv_pay1_dat DATE;
  lv_mths_num dd_pledge.paymonths%TYPE;
BEGIN
  SELECT dd_paydate1_sf(idpledge), paymonths - 1
    INTO lv_pay1_dat, lv_mths_num
    FROM dd_pledge
    WHERE idpledge = p_id;
  IF lv_mths_num = 0 THEN
     RETURN lv_pay1_dat;
  ELSE
     RETURN ADD_MONTHS(lv_pay1_dat, lv_mths_num);
  END IF;
END;
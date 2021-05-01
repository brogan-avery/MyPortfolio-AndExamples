/*
***************************************************
Title: chapter 7, package body
Author: Brogan Avery
Created: 2020-03-16
***************************************************
*/

set serveroutput on

-- defines the functions of the package
CREATE OR REPLACE PACKAGE BODY PLEDGE_PKG AS

    FUNCTION dd_paydate1_pf (p_id IN dd_pledge.idpledge%TYPE)
        RETURN DATE AS
            lv_pl_dat DATE;
            lv_mth_txt VARCHAR2(2);
            lv_yr_txt VARCHAR2(4);
        BEGIN
        SELECT ADD_MONTHS(pledgedate,1)
            INTO lv_pl_dat
            FROM dd_pledge
            WHERE idpledge = p_id;
        lv_mth_txt := TO_CHAR(lv_pl_dat,'mm');
        lv_yr_txt := TO_CHAR(lv_pl_dat,'yyyy');
        RETURN TO_DATE((lv_mth_txt || '-01-' || lv_yr_txt),'mm-dd-yyyy');
    END dd_paydate1_pf;

    FUNCTION dd_payend_pf (p_id IN dd_pledge.idpledge%TYPE)
        RETURN DATE AS
            lv_pay1_dat DATE;
            lv_mths_num dd_pledge.paymonths%TYPE;
        BEGIN
        SELECT dd_paydate1_pf(idpledge), paymonths - 1
            INTO lv_pay1_dat, lv_mths_num
            FROM dd_pledge
            WHERE idpledge = p_id;
        IF lv_mths_num = 0 THEN
            RETURN lv_pay1_dat;
        ELSE
            RETURN ADD_MONTHS(lv_pay1_dat, lv_mths_num);
        END IF;
    END dd_payend_pf;
  
    PROCEDURE dd_pList_pp(donor_id IN dd_donor.iddonor%TYPE) is 
        cursor cursObj is
            select firstname || ' ' || lastname name, idpledge 
                from dd_donor join dd_pledge 
                using(iddonor)
                where iddonor = donor_id;
            first_Date date;
            last_Date date;
        begin
            for donor_Record in cursObj
                loop
                    first_date := pledge_pkg.dd_paydate1_pf(donor_Record.idpledge);
                    last_date := pledge_pkg.dd_payend_pf(donor_Record.idpledge);
                    dbms_output.put_line(donor_record.name || ' ' || donor_record.idpledge || ' ' || first_date || ' '|| last_date);
                end loop;
    end dd_pList_pp;
            
END PLEDGE_PKG;

--Test:
--begin 
    --pledge_pkg.dd_plist_pp(308);
--end;


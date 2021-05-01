/*
***************************************************
Title: chapter 4
Author: Brogan Avery
Created: 2020-03-01
***************************************************
*/

set serveroutput on

DECLARE
  cv_pays SYS_REFCURSOR; -- declar cursor obj
  rec_pay dd_payment%ROWTYPE;
  
  TYPE type_pay2 IS RECORD (
     pid dd_pledge.idpledge%TYPE,
     amt NUMBER(9,2));
  
  rec_pay2 type_pay2;
  
  lv_ind_txt CHAR(1) := 'D'; -- tests id input is 'D'
  lv_ind_txt_other CHAR(1) := 'S'; -- tests id input is 'S'
  lv_donor_num dd_donor.iddonor%TYPE := 308;

BEGIN
-- for input case 1 'D'
    if lv_ind_txt = 'D' then
        DBMS_OUTPUT.PUT_LINE('idpay' || '  idpledge' ||  '  payamt' || '  paydate' || '  paymethod');
        open cv_pays for 
            SELECT pa.idpay, pl.idpledge, pa.payamt, pa.paydate, pa.paymethod
            from dd_pledge pl join dd_payment pa on pl.idpledge = pa.idpledge
            where pl.iddonor = 308;
            
        loop
            fetch cv_pays into rec_pay.idpay, rec_pay.idpledge, rec_pay.payamt, rec_pay.paydate, rec_pay.paymethod;
            exit when cv_pays%notfound;
            DBMS_OUTPUT.PUT_LINE(rec_pay.idpay || '     ' || rec_pay.idpledge || '      ' || rec_pay.payamt || '     ' || rec_pay.paydate || '    ' || rec_pay.paymethod);
        end loop;
        
    elsif lv_ind_txt = 'S' then
        DBMS_OUTPUT.PUT_LINE('idpledge' || '  total payment');
        open cv_pays for 
            SELECT pl.idpledge, sum(pa.payamt)
            from dd_pledge pl join dd_payment pa on pl.idpledge = pa.idpledge
            where pl.iddonor = 308
            group by pl.idpledge;
        loop
            fetch cv_pays into rec_pay2;
            exit when cv_pays%notfound;
            DBMS_OUTPUT.PUT_LINE('    ' || rec_pay2.pid || '      ' || rec_pay2.amt);
        end loop; 
    end if;
    
    DBMS_OUTPUT.PUT_LINE(' ');
    
-- for input case 2 'S'
    if lv_ind_txt_other = 'D' then
        DBMS_OUTPUT.PUT_LINE('idpay' || '  idpledge' || ' payamt' || '  paydate' || '  paymethod');
        open cv_pays for 
            SELECT pa.idpay, pl.idpledge, pa.payamt, pa.paydate, pa.paymethod
            from dd_pledge pl join dd_payment pa on pl.idpledge = pa.idpledge
            where pl.iddonor = 308;
            
        loop
            fetch cv_pays into rec_pay.idpay, rec_pay.idpledge, rec_pay.payamt, rec_pay.paydate, rec_pay.paymethod;
            exit when cv_pays%notfound;
            DBMS_OUTPUT.PUT_LINE(rec_pay.idpay || '     ' || rec_pay.idpledge || '      ' || rec_pay.payamt || '     ' || rec_pay.paydate || '    ' || rec_pay.paymethod);
        end loop;
        
    elsif lv_ind_txt_other = 'S' then
        DBMS_OUTPUT.PUT_LINE('idpledge' || '  total payment');
        open cv_pays for 
            SELECT pl.idpledge, sum(pa.payamt)
            from dd_pledge pl join dd_payment pa on pl.idpledge = pa.idpledge
            where pl.iddonor = 308
            group by pl.idpledge;
        loop
            fetch cv_pays into rec_pay2;
            exit when cv_pays%notfound;
            DBMS_OUTPUT.PUT_LINE('    ' || rec_pay2.pid || '      ' || rec_pay2.amt);
        end loop; 
    end if;
END;

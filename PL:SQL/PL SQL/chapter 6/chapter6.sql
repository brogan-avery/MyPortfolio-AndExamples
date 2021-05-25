/*
***************************************************
Title: chapter 6
Author: Brogan Avery
Created: 2020-03-10
***************************************************
*/


-- function declaration, params, and return value/type
CREATE OR REPLACE FUNCTION DD_MTHPAY_SF (num_Monthly_Payments number, total_Amount number) 
    RETURN NUMBER AS
        monthly_Amount number;
    
    BEGIN
        monthly_amount := total_Amount / num_Monthly_Payments;
        
        return monthly_amount;
        
    end DD_MTHPAY_SF;
    
    
-- selection statments to test the function:
    
--select DD_MTHPAY_SF(12, 240) from dual;
--select DD_MTHPAY_SF(paymonths, pledgeamt) 
  --from dd_pledge
  --where paymonths != 0;


    

    


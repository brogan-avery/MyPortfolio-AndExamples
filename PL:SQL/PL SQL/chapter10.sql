/*
***************************************************
Title: chapter 10
Author: Brogan Avery
Created: 2020-03-16
***************************************************
*/

set Serveroutput on
CREATE OR REPLACE PROCEDURE dyn_addcol_sp (p_col IN VARCHAR2, p_table IN VARCHAR2, p_type IN VARCHAR2) IS
    
    lv_sql varchar2(200);
    
    BEGIN
        lv_sql := 'alter table '  || p_table || ' add ' || p_col || ' ' || p_type;   --contents of parm, construct command combination of literals and variables
        
        --dbms_output.put_line(lv_sql);
        
        EXECUTE IMMEDIATE lv_sql;
    
    END;

-- Anonymous block
begin
    dyn_addcol_sp('member1', 'dd_donor', 'varchar2(30)');
end;

--alter table dd_donor add member varchar2(30);
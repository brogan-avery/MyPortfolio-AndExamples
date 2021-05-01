/*
***************************************************
Title: In class function assignment
Author: Brogan Avery
Created: 2020-03-09
***************************************************
*/

CREATE OR REPLACE FUNCTION REVERSER_SF (
    INTEXT IN VARCHAR2 
) RETURN VARCHAR2 AS

    outText varchar2(50);
    pText varchar2(50);
    
BEGIN
    outText := regexp_replace(inText, '[^A-Za-z]', '');
    
    for x in reverse 1.. length(intext) loop
    
        if x mod 2 = 0 then
            pText := pText || lower(substr(inText, x, 1));
        else
            pText := pText || upper(substr(inText, x, 1));
        
        end if;
        
    end loop;
    
    outText := regexp_replace(pText,'[^A-Za-z]',''); 
    
  return outText;
  
END REVERSER_SF;

/*
***************************************************
Title: chapter 3
Author: Brogan Avery
Created: 2020-02-21
***************************************************
*/

set serveroutput on 

select pr.idproj,pr.PROJNAME,count(pr.idproj) "Number of Pledges",to_char(sum(pl.pledgeamt),'$99,999') "Total $ Pledged",avg(pl.pledgeamt)       "Average Pledge Amount"
from dd_project pr join dd_pledge pl on pr.idproj=pl.idproj
where pr.idproj = '&please_enter_proj_id'
group by pr.idproj, pr.projname;
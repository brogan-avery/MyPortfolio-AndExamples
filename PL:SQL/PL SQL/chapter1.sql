/*
***************************************************
Title: chapter 1
Author: Brogan Avery
Created: 2020-02-01
***************************************************
*/


-- Q1
select d.firstname || ' ' || d.lastname     "Donor Name",
       to_char(p.pledgedate,'mm/dd/yyyy')   "Pledge Date",
       to_char(p.pledgeamt,'$99,999.00')       "Pledge Amount"
  from dd_donor d join dd_pledge p on d.iddonor = p.iddonor
 where p.paymonths = 0
order by d.iddonor;

-- Q2
select d.firstname || ' ' || d.lastname    "Donor Name",
       to_char(p.pledgedate,'mm/dd/yyyy')   "Pledge Date",
       to_char(p.pledgeamt/paymonths,'$99,999.00')       "Pledge Amount"
  from dd_donor d join dd_pledge p on d.iddonor = p.iddonor
 where p.paymonths > 12
order by d.iddonor;

-- Q3
select distinct pj.idproj "Project ID", pj.projname "Project Name"
from dd_project pj join dd_pledge pl on pj.idproj = pl.idproj;

-- Q4
select iddonor "Donor ID", firstname || ' ' || lastname "Donor Name", count(*) "# Pledges made"
from dd_pledge p inner join dd_donor d using(iddonor)
group by iddonor, firstname, lastname;

-- Q5
select p.idpledge "Pledge ID", p.iddonor "Donor ID", p.pledgedate "Pledge Date", p.pledgeamt "Pledge Amount" , p.idproj "Project ID", p.idstatus "Status", p.writeoff "Write Off", p.campaign "Campaign", p.paymonths "Pay Months", p.firstpledge "First Pledge"
from dd_pledge p
where cast(p.pledgedate as date) < '08-MAR-12'

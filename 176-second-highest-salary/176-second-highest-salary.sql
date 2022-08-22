# Write your MySQL query statement below
select 
    IFNULL(
        (select salary from Employee
        group by salary
        order by salary desc limit 1 offset 1), 
    null) as SecondHighestSalary
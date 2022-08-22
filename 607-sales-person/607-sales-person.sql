# Write your MySQL query statement below
select distinct(s.name) from SalesPerson s
where s.sales_id not in (
    select distinct(sales_id) from Orders o, Company c
    where o.com_id = c.com_id and c.name = 'RED'
)
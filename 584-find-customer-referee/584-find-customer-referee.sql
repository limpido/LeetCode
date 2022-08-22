# Write your MySQL query statement below
select name from Customer
where id not in
(
    select id from Customer
    where referee_id = 2
);

-- SELECT name FROM customer WHERE referee_id != 2 OR referee_id IS NULL;
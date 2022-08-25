# Write your MySQL query statement below
select activity_date day, count(distinct user_id) active_users
from Activity
where activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY) and activity_date <= '2019-07-27'
group by activity_date;
# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person as p LEFT JOIN Address as a
on p.personId = a.personId;
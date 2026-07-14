-- Last updated: 7/14/2026, 3:20:00 PM
# Write your MySQL query statement below
SELECT email
from person
GROUP BY email
HAVING COUNT(email)>1;
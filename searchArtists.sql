/*
METHOD 1:
to count the number of matches we might use 3 layer nested loop
loop 1: iterate over lists
loop 2: iterate over keywords
loop 3: iterate over artist name and song title
Alternative:
count number of matches in 
*/

SELECT DISTINCT a.aid, a.name, a.nationality, s.title
FROM artists a, perform p, songs s
WHERE p.aid = a.aid AND p.sid = s.sid
AND (lower(a.name) LIKE '%h%'
OR lower(s.title) LIKE '%h%')

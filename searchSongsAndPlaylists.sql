/*we count the number of keyword occurances in Python
because query result is tuple and not mutable
we can make a nested list copy of tuple with 1 extra column and count number of matches*/

SELECT DISTINCT s.sid, s.title, s.duration, 'song' as category
FROM songs s
WHERE lower(s.title) LIKE '%a%';

--OR .... keyword matching part


SELECT DISTINCT p.pid, p.title, SUM(s.duration), 'playlist' as category
FROM songs s, playlists p, plinclude pl
WHERE pl.sid = s.sid AND p.pid = pl.pid
AND lower(p.title) LIKE '%music%'
-- OR ... keyword matching part
GROUP BY p.pid, p.title;


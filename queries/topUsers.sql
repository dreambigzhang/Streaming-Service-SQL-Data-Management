SELECT l.uid
FROM songs s, listen l, artists a, perform p
WHERE s.sid = l.sid AND s.sid = p.sid
AND a.aid = p.aid AND a.aid = "a10"
GROUP BY l.uid
ORDER BY SUM(s.duration * l.cnt) DESC
LIMIT 3

SELECT pl.pid
FROM plinclude pl, perform pr
WHERE pl.sid = pr.sid
AND pr.aid = "a11"
GROUP BY pl.pid
ORDER BY COUNT(pl.sid) DESC
LIMIT 3

SELECT *
FROM artists a, songs s, perform p
WHERE a.aid = p.aid AND s.sid = p.sid
AND title = "Applause" AND duration = 212
AND a.aid = "a1";


select distinct l.uid, p.aid
  from listen l, songs s, perform p
  where l.sid=s.sid and s.sid=p.sid and
        uid in (select l1.uid
                from listen l1
                group by l1.uid
                having count (distinct l1.sid)>5) and
        aid in (select p1.aid
                from listen l1, songs s1, perform p1
                where l1.uid=l.uid and l1.sid=s1.sid and s1.sid=p1.sid
                group by p1.aid
                order by sum(l1.cnt*s1.duration) desc
                limit 3);
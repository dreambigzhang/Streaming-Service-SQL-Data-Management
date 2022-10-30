SELECT DISTINCT s.sid, s.title, s.duration
FROM songs s, plinclude pl
WHERE pl.pid = :pid AND pl.sid = s.sid;
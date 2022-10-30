SELECT *
FROM plinclude pl
WHERE pl.pid = :pid AND pl.sid = :sid;

SELECT *
FROM playlists p
WHERE p.uid = :uid AND p.pid = :pid;
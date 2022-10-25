/*
More information for a song is 
the names of artists who performed it in addition to 
id, title and duration of the song as well as the 
names of playlists the song is in (if any). 
*/

SELECT DISTINCT a.name, s.sid, s.title, s.duration, p.title
FROM (((songs s LEFT OUTER JOIN perform p ON s.sid = p.sid)
LEFT OUTER JOIN artists a ON p.aid = a.aid)
LEFT OUTER JOIN plinclude pl ON s.sid = pl.sid)
LEFT OUTER JOIN playlists p ON pl.pid = p.pid
WHERE s.sid = :sid;

/*
decide whether session already exist in python
*/

--when session doesn't 

/*make new session refer to insertSession.sql
obtain the sno if already have it 
decide in python: if already exist in listen, increment cnt
otherwise insert with cnt = 1 */
/*
INSERT INTO listen
VALUES (:uid, :sno, :sid, 1);
*/

-- decide if user has already listened to this song in this session
SELECT *
FROM listen l
WHERE l.uid = 'u2' AND l.sno = 24 AND l.sid = 12;

-- update listen table when user already listend to the song
UPDATE listen
SET cnt = cnt+1
WHERE uid = 'u2' AND sno = 24 AND sid = 12;



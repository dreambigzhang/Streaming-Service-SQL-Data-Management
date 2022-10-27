
/*
--get new sno
SELECT MAX(se.sno)+1
FROM sessions se
WHERE se.uid = 'u1';
--insert session
INSERT INTO sessions
VALUES (:uid, :sno, strftime('%Y-%m-%d','now'), NULL);
*/
-- see if user already have session now
/*
SELECT se.sno
FROM sessions se
WHERE se.uid = 'u1'
AND se.end IS NULL;
*/
-- end session
UPDATE sessions
SET end = strftime('%Y-%m-%d','now')
WHERE uid = :uid AND sno = :sno;


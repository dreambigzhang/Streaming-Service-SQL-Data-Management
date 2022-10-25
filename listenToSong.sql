/*
decide whether session already exist in python
*/

--when session doesn't 

/*make new session refer to insertSession.sql
obtain the sno if already have it 
decide in python: if already exist in listen, increment cnt
otherwise insert with cnt = 1 */

INSERT INTO listen
VALUES (:uid, :sno, :sid, 1);


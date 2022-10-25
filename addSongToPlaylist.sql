/* When adding a song to a playlist, 
the song can be added to an existing playlist owned by the user (if any) 
or to a new playlist. When it is added to a new playlist, a new playlist should be created with a unique id (created by your system) and the uid set to the id of the user and a title should be obtained from input. 
*/

/* check in python if user has any playlist 
-> if yes give 2 options
-> if no give only option 2

2 options:
1. list all playlist and ask which one to insert into
 - check if song already in playlist
- insert into plinclude

2. ask for new playlist name and make new playlist and insert into playlist
- check if playlist name already exist for user
- insert into playlist
- check if song already in playlist
- insert into plinclude
*/

/* new song sorder is obtained from MAX(sorder) + 1 

--list all playlists of the user
/*
SELECT p.title
FROM playlists p
WHERE p.uid = :uid;
*/

-- make new playlist (pid generated in python)
INSERT INTO playlists VALUES (:pid, :title, :uid);

-- insert into plinclude
INSERT INTO plinclude VALUES (:pid, :sid, :sorder)

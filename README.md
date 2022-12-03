# Streaming-Service-SQL-Data-Management
Manage user data and media at scale; securely administer the distribution and consumption of music

## User guide

### Accounts and authentication
Start by entering 1 to login or 2 to sign up . 
If entered 1, first input valid user ID or valid artist ID of 4 characters less, then input valid password corresponding to that ID to login to either their user account or artist account. 
If entered 2, first input a valid unique user ID of 4 characters or less, then input password, and finally input name.
During any point in either the login page or the signup page, user can go back to main page by entering -1
If the user inputs anything else during main page, they exit the program

### User
-After a successful login, users can enter 1 to start or  2 to end a listening session, 3 to  search for songs and playlists, 4 to search for artists, 5 to logout, anything else exit the program.
-Whenever a song, playlist, or artist shows up on screen as a search result, user has the option to select them and perform the following actions on the song: 1 listen, 2 see more information about it, and 3 add it to a playlist; see all songs in a playlist; see all songs performed by the artist.

### Artist
Once the artist logs in, they are prompted to enter 1 to add a new song, 2 to find top fans and playlists, and 4 to logout. If the artist decides to add a new song, they are prompted for the title and duration. If a song with the same name and duration exists, the artist is prompted to enter a 1 to proceed with the insertion. The artist is then prompted to enter any additional aids. If the aids are invalid, an error message is printed and they are returned to the artist's main menu. 

## Design
main(): once valid input is placed into either login() or signup(), user either calls userMainMenu() or artistsMainMenu()
userMainMenu(): give user the options to call startSession(), endSession(), searchSongAndPlaylists(), or searchArtists()
songAction() is called whenever user selects a song
artistsMainMenu(): gives the artist the options to add songs and show top fans and playlists
displayUsersPlaylists(): display top users and playlists
addSong(): add new song
<img width="815" alt="Screenshot 2022-12-03 at 4 45 04 PM" src="https://user-images.githubusercontent.com/104746082/205467049-80f6a68a-c941-415e-8532-a9f8600978bb.png">


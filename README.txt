This is my TCP server, this server is a broadcast server.
Every message sent to the server is broadcasted to everyone who connects to the server.
My server has a few special functions available to the client.

Special Functions:

1. !ONLINE - when a user types this keyword the server sends him an array of online users.
2. !EXIT - when a user types this keyword the server disconnect him from the server.
3. !CHANGE - when a user types this keyword, he has the ablitiy to send messages to a specific user without the message being broadcasted to the rest of the chatroom.
4. !WHORU - when a user types this keyword the server returns a pre saved string. 

Another feature of the server is that every new connection or message that is being sent is documented in a text file located on the server.

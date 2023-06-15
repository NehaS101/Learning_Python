const express = require('express');
const app = express();
const http = require('http');
const socketIo = require('socket.io');


const server = http.createServer(app);
const io = socketIo(server);

io.on('connection',(socket)=>{
    console.log('client connected '+socket.id);

    const targetClientID = "Lee8GqDjnosdhrjhAAAD";
    io.to(targetClientID).emit('message',"hello world");
    
    socket.on('disconnect', () => {
        console.log('A client disconnected: ' + socket.id);
      });
})


server.listen(3000,()=>{
    console.log("client connected on port 3000")
})
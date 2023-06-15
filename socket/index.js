const express = require('express');
const app = express();
const http = require('http');
const socketIo = require('socket.io');


const server = http.createServer(app);
const io = socketIo(server);

io.on('connection',(socket)=>{
    console.log('client connected '+socket.id);

    socket.on('specific',data=>{
        const email = data.email;
        io.to(email).emit('message',"hello world");

    })

    
    
    socket.on('disconnect', () => {
        console.log('A client disconnected: ' + socket.id);
      });
})


server.listen(3000,()=>{
    console.log("client connected on port 3000")
})
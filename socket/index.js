const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

io.on('connection',(socket)=>{
    console.log('client connected'+socket.id);
})

server.listen(3500,()=>{
    console.log("client connected on port 3500")
})
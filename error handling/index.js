const express = require('express');
const { errorHandle } = require('./middleware');
const app = express();

app.use(express.json());
app.use(errorHandle)

app.get('/api',(req,res)=>{
    res.send("Welcome to app")
})

app.listen(3230,()=>{
    console.log('listening on port 3230');
})
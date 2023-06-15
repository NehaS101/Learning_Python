const express = require('express');
const app = express();
app.use(express.json());


app.listen(3230,()=>{
    console.log('listening on port 3230');
})
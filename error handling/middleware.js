const errorHandle=(err,req,res,next) => {
console.log(err);
if(err instanceof SyntaxError) {
res.status(404).send("Invalid request syntax")
}else if(err instanceof MongoDBError) {
res.status(500).send("mongodb error")
}else{
    res.status(500).send("Internal Server Error")
}


}
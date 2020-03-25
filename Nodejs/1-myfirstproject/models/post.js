const mongoose = require('mongoose');
//mongoose.connect('mongodb://localhost/mymessages',{useNewUrlParser: true,useUnifiedTopology: true});

const postSchema = new mongoose.Schema({
    author: { type: String, required: true },
    color: { type: String, default: '#333' },
    image: Buffer,
    text: String,
});

module.exports = new mongoose.model('Post', postSchema);




//mongoose.connect('mongodb://localhost:27017/myapp', {useNewUrlParser: true});
//var MyModel = mongoose.model('Test', new Schema({ name: String }));
// Works
//MyModel.findOne(function(error, result) { /* ... */ });



//const conn = mongoose.createConnection('mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]', options);
//const UserModel = conn.model('User', userSchema);
//https://mongoosejs.com/docs/connections.html#multiple_connections
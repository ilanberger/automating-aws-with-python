const mongoose = require('mongoose');
//mongoose.connect('mongodb://localhost/mymessages',{useNewUrlParser: true,useUnifiedTopology: true});

const postSchema = new mongoose.Schema({
    author: { type: String, required: true },
    color: { type: String, default: '#333' },
    image: Buffer,
    text: String,
});

module.exports = new mongoose.model('Stock', postSchema);


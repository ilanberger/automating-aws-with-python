const mongoose = require('mongoose');
//mongoose.connect('mongodb://localhost/mymessages',{useNewUrlParser: true,useUnifiedTopology: true});

const stockSchema = new mongoose.Schema({
    author: { type: String, required: true },
    color: { type: String, default: '#333' },
    stockname: { type: String, default: 'appl' ,required: true },
    stockvalue: { type: Number, default: 100 },
    stockvalue_get: { type: Number, default: 80 },
    date: { type: Date, default: Date.now },
    image: Buffer,
    text: String,
});

module.exports = new mongoose.model('Stock', stockSchema);


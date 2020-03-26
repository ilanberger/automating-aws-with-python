const router = require('express').Router();
const Stock = require('../models/stock');

const multer = require('multer');
const postPhotoUpload = multer({
    storage: multer.memoryStorage(),
    limits: {
        fileSize: 2 * 1024 * 1024,
    },
    fileFilter: function (req, file, cb) {
        const fname = file.originalname;
        const valid = [
            '.jpg',
            '.png',
            '.jpeg'
        ].find(ext => fname.endsWith(ext));
        cb(null, valid);
    }
}).single('postpic');


// GET /posts/new
router.get('/new', function(req, res, next) {
    const stock = new Stock();
    //res.render('stocks/new', { post: stock });
    res.render('stocks/new', { stock: stock });
});

// GET /posts
router.get('/', async function(req, res, nest) {

    const totalRecords = await Stock.estimatedDocumentCount();

    const itemsPerPage = Number(req.query.limit) || 20;
    const page = Number(req.query.page) || 1;

    const totalPages = totalRecords / itemsPerPage;
    const offset = itemsPerPage * (page - 1);

    const posts = await Stock.find({}).sort({ _id: -1 }).skip(offset).limit(itemsPerPage);
    res.render('stocks/index', {
        posts,
        pagination: {
            totalPages,
            url: (page) => `/posts?page=${page}`,
        }
    });
});

router.get('/:id/img', async function(req, res, next) {
    const stock = await Stock.findById(req.params.id);
    res.end(stock.image);
});

// POST /posts
router.post('/', postPhotoUpload, async function(req, res, next) {
    // Now I have the file processed by multer
    let params = req.body;
    if (req.file) {
        params.image = req.file.buffer;
    }
    const stock = new Stock(params);
    try {
        await stock.save();
        res.redirect('/stocks');
    } catch {
        console.log(stock.errors);
        res.render('stocks/new', { stock: stock });
    }
});

module.exports = router;
const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json({limit: '50mb'}));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
})

const port = process.env.PORT || '5000';
app.listen(port, () => console.log(`Server started on Port ${port}`));

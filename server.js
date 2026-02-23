const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Serve static files (HTML, CSS, JS, Images) from the "public" folder
app.use(express.static(path.join(__dirname, 'public')));

// API endpoint to get the list of Salats for the homepage
app.get('/api/salats', (req, res) => {
    const dataPath = path.join(__dirname, 'data', 'salat_list.json');
    fs.readFile(dataPath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({ error: "Could not read data file" });
        }
        res.json(JSON.parse(data));
    });
});

// Start the server on LAN
app.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Server is running on LAN at port ${PORT}`);
});
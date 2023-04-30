// server.js

const express = require('express');
const axios = require('axios');
//const requests = require('request');

const app = express();




app.get('/random-image', async (req, res) => {
  console.log("Handling a random image request.")
  try {
    const response = await axios.get('http://localhost:6000/images');
    const image = response.data;
    // Send response to client
    res.send("Random image: "+image);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching image');
  }
});



app.get('/random-quote', async (req, res) => {
  console.log("Handling a random quote request.")
  try {
    const response = await axios.get('http://localhost:5000/quotes');
    const quote = response.data;
    // Send response to client
    res.send(quote);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching quote');
  }
});

app.use(express.json());

app.post('/chatgpt-prompt', async (req, res) => {
  console.log("Handling a ChatGPT prompt request.")
  try {
    const inputText = req.body.input_text;
    const response = await axios.post('http://localhost:7000/prompt', { input_text: inputText });
    const result = response.data;
    // Send response to client
    res.send(result);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching data');
  }
});



app.listen(3000, () => {
  console.log('Server listening on port 3000');
});

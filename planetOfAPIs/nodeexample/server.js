const express = require('express');
const app = express();
const bodyParser = require('body-parser');

// Set up body parser middleware
app.use(bodyParser.json());

// In-memory database of pets
const pets = [
  { id: 1, name: 'Fluffy', type: 'Cat' },
  { id: 2, name: 'Buddy', type: 'Dog' },
  { id: 3, name: 'Nemo', type: 'Fish' }
];

// GET method to retrieve pet by ID
app.get('/pets/:id', (req, res) => {
  const petId = parseInt(req.params.id);
  const pet = pets.find(p => p.id === petId);

  if (!pet) {
    return res.status(404).send('Pet not found');
  }

  res.send(pet);
});

// POST method to add new pet
app.post('/pets', (req, res) => {
  const { name, type } = req.body;

  if (!name || !type) {
    return res.status(400).send('Name and type are required');
  }

  const id = pets.length + 1;
  const pet = { id, name, type };
  pets.push(pet);

  res.send(pet);
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});


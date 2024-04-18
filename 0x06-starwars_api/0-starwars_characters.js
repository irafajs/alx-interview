#!/usr/bin/node

const request = require('request');

function fetchMovieData (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error(`${response.statusCode}`));
        return;
      }
      const movieData = JSON.parse(body);
      resolve(movieData);
    });
  });
}

function fetchCharacterData (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error('Failed to fetch character data.'));
        return;
      }
      const characterData = JSON.parse(body);
      resolve(characterData);
    });
  });
}

async function printCharacters (movieId) {
  try {
    const movieData = await fetchMovieData(movieId);
    for (const characterUrl of movieData.characters) {
      const characterData = await fetchCharacterData(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('provide movie id');
} else {
  printCharacters(movieId);
}

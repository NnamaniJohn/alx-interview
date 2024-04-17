#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
const characters = [];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const charactersUrls = data.characters;
  charactersUrls.forEach((url) => {
    request(url, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(body);
      characters.push(character.name);
      if (characters.length === charactersUrls.length) {
        characters.forEach((character) => {
          console.log(character);
        });
      }
    });
  });
});

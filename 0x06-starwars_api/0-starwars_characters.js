#!/usr/bin/node
// script that prints all characters of a Star Wars movie Right order
const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];


request(`${endpoint}`, async function (error, response, body) {
  if (error) return console.log(error);

  let characters = JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});

#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const fileA = process.argv[2]; // get file paths
const fileB = process.argv[3];
const fileC = process.argv[4];
const fileAdata = fs.readFileSync(fileA, 'utf8'); // read contents
const fileBdata = fs.readFileSync(fileB, 'utf8');
const res = (fileAdata + fileBdata); // store content in res
fs.writeFileSync(fileC, res); // write content to fileC
const fileCdata = fs.readFileSync(fileC, 'utf-8'); // read fileC
console.log(fileCdata); // print fileC

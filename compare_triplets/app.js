'use strict';

const fs = require('fs');
const appDebug = require('debug')('app:debug');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
    appDebug('on data | inputString %s', inputString);
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    appDebug('on end | inputString %s', inputString);
    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the compareTriplets function below.
function compareTriplets(a, b) {
  appDebug('what happens here bro: %s | %s', JSON.stringify(a), JSON.stringify(b));
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    const b = readLine().replace(/\s+$/g, '').split(' ').map(bTemp => parseInt(bTemp, 10));

    const result = compareTriplets(a, b);

    ws.write(result.join(' ') + '\n');

    ws.end();
}


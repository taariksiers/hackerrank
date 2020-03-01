<?php

// https://www.hackerrank.com/challenges/halloween-party/problem

$method = 'halloweenParty';

function halloweenParty($k): int
{
    return floor(pow($k/2, 2));
}

$samples = [
    '5' => 6,
    '6' => 9,
    '7' => 12,
    '8' => 16

];

foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
}

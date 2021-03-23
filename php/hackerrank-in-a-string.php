<?php
// https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

$method = 'hackerrankInString';

function hackerrankInString($s): string
{
    $characters = str_split($s, 1);
    $findString = 'hackerrank';
    $find = str_split($findString, 1);
    
    foreach ($characters as $character) {
        if (current($find) == $character) {
            next($find);
        }
    }

    return next($find) === false ? 'YES' : 'NO';
}

$samples = [
    'hhaacckkekraraannk' => 'YES',
    'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt' => 'NO',
    'hereiamstackerrank' => 'YES',
    'hackerworld' => 'NO',
];


foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample set: %s' . PHP_EOL, $success, $expected, $result, json_encode($sample));
}

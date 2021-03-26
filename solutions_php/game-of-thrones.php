<?php
// https://www.hackerrank.com/challenges/game-of-thrones/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

// make palindrome from string
// 

$method = 'gameOfThrones';

function gameOfThrones($s): string
{

    $string = str_split($s, 1);
    $counts = array_count_values($string);

    $countEven = 0;
    $countOdd = 0;

    foreach ($counts as $letter => $count) {
        if ($count %2 == 0) {
            $countEven++;
        } else {
            $countOdd++;
        }
    }

// var_dump('Even', $countEven, 'Odd', $countOdd);

    if ($countEven > 0 && ($countOdd == 0 || $countOdd == 1)) {
        return 'YES';
    }

    return 'NO';
}

$samples = [
    'aabbccdd' => 'YES', // all occur twice therefore any symetric combination can be a palindrome
    'aaabbbb' => 'YES', // one even count, one odd count, therefore odd count can be centered
    'cdefghmnopqrstuvw' => 'NO', // all occur once, no chance of palindrome
];


foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample set: %s' . PHP_EOL, $success, $expected, $result, json_encode($sample));
}

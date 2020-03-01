<?php

// https://www.hackerrank.com/challenges/utopian-tree/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

$method = 'utopianTree';

function utopianTree($n): int
{
    $height = 1;
    if ($n == 0) {
        return $height;
    }

    
    for ($i=1; $i<= $n; $i++) {
        if ($i%2==0) {
            $height++;
        } else {
            $height = $height*2;
        }
    }

    return $height;
}


$samples = [
    '0' => 1,
    '1' => 2,
    '4' => 7,
];


foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
}
<?php

// https://www.hackerrank.com/challenges/find-the-median/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=30-day-campaign

$debug = $argv[1] ?? false;

$method = 'findMedian';

/**
 * Find the median 
 *
 * @param array $arr
 * @return integer
 */
function findMedian(array $arr): int
{
    global $debug;
    sort($arr);
    $median = floor(count($arr)/2);
    return $arr[$median];
}

$samples = [
    ['0 1 2 4 6 5 3', 3],
];

foreach ($samples as $subset) { 
    $sample = explode(' ', $subset[0]);
    $expected = $subset[1];
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL . PHP_EOL, $success, $expected, $result, json_encode($sample));
}

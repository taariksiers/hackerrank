<?php

// https://www.hackerrank.com/challenges/lonely-integer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

$debug = $argv[1] ?? false;

$method = 'lonelyinteger';

/**
 * Determine the array count with value == 1
 *
 * @param array $a
 * @return integer
 */
function lonelyinteger(array $a): int
{
    global $debug;

    $elementCount = array_count_values($a);

    $debug && print(json_encode($elementCount) . PHP_EOL);

    $flip = array_flip($elementCount);

    return $flip[1] ?? -1;
}

$samples = [
    [[1,2,3,4,3,2,1], 4],
    [explode(' ', '1 1 2'), 2],
    [explode(' ', '0 0 1 2 1'), 2],
];

foreach ($samples as $sample) {
    $expected = array_pop($sample);
    $result = $method(...$sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL . PHP_EOL, $success, $expected, $result, json_encode($sample));
}

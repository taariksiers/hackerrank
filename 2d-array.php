<?php

// https://www.hackerrank.com/challenges/beautiful-binary-string/problem?h_r=internal-search

$debug = $argv[1] ?? false;

$method = 'beautifulBinaryString';

/**
 * Determine
 *
 * @param array $a
 * @return integer
 */
function beautifulBinaryString($b): int
{
    global $debug;

    return substr_count($b, '010');
}

$samples = [
    ['0101010', 2],
    ['01100', 0],
];

foreach ($samples as $sample) {
    $expected = array_pop($sample);
    $result = $method(...$sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL . PHP_EOL, $success, $expected, $result, json_encode($sample));
}

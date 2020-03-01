<?php

// https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=internal-search

$debug = $argv[1] ?? false;

$method = 'insertionSort1';

/**
 *
 * @param int $n
 * @param array $arr
 * @return void
 */
function insertionSort1($n, array $arr)
{
    global $debug;
    $sorted = false;

    $unsorted = end($arr);
    $debug && printf('Count %d | Array %s' . PHP_EOL, $n, json_encode($arr));

    for ($i=$n-1; $i>=0; $i--) {

        if ($arr[$i-1] > $unsorted) {
            $arr[$i] = $arr[$i-1];
            echo implode(' ', $arr) . PHP_EOL;
            continue;
        }

        if ($unsorted > $arr[$i-1]) {
            $arr[$i] = $unsorted;
            break;
        }

    }

    echo implode(' ', $arr) . PHP_EOL;
}

$samples = [
    '1 2 4 5 3' => '1 2 3 4 5',
    '2 4 6 8 3' => '2 3 4 6 8 ',
];

foreach ($samples as $sample => $expected) {

    $arr = explode(' ', $sample);

    $result = $method(count($arr), $arr);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL . PHP_EOL, $success, $expected, $result, $sample);
}


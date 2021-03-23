<?php

// https://www.hackerrank.com/challenges/insertionsort2/problem?h_r=internal-search

$debug = $argv[1] ?? false;

$method = 'insertionSort2';

/**
 * Determine
 *
 * @param array $a
 * @return integer
 */
function insertionSort2($n, array $arr)
{
    global $debug;
    $shifts = 0;

    $debug && printf('Count %d | Array %s' . PHP_EOL, $n, json_encode($arr));

    if ($n == 1) {
        $result = implode(' ', $arr) . PHP_EOL;
        $debug && print $result;
        return $result;
    }

    for ($i=0; $i<$n; $i++) {
        $debug && printf('Elem [%d] Value [%d]' . PHP_EOL, $i, $arr[$i]);
        $current = $arr[$i];
        if ($i == $n-1) {
            $debug && printf('Reached the end of the line.' . PHP_EOL);
            continue;
        }

        $next = $arr[$i+1];
        if ($current <= $next) {
            $debug && printf('Do nothing here...' . PHP_EOL);
            $debug && print implode(' ', $arr) . PHP_EOL;
            continue;
        }

        $debug && printf('Sort some shit' . PHP_EOL);
        $arr[$i] = $next;
        $arr[$i+1] = $current;
        $shifts++;

        if ($arr[$i] > $arr[$i-1]) {
            $debug && print implode(' ', $arr) . PHP_EOL;
            continue;
        }

        for ($j=$i; $j>0; $j--) {
            $current = $arr[$j];
            $previous = $arr[$j-1];

            $debug && printf('Elem [%d] Value [%d] | Previous $j-1 [%d] | %s' . PHP_EOL, $j, $arr[$j], $arr[$j-1], $arr[$j] < $arr[$j-1] ? 'YES' : 'NO');

            if ($current < $previous) {
                $arr[$j] = $previous;
                $arr[$j-1] = $current;
                $shifts++;
            }
        }

        $debug && print implode(' ', $arr) . PHP_EOL;

    }

    return $shifts;
}

$samples = [
    '3 4 7 5 6 2 1' => 13,
    '1 4 3 5 6 2' => 5,
    '2 1 3 1 2' => 4
];

foreach ($samples as $sample => $expected) {

    $arr = explode(' ', $sample);

    $result = $method(count($arr), $arr);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL , $success, $expected, $result, $sample);
}


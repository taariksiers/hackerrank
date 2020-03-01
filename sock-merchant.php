<?php

// https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

$debug = $argv[1] ?? false;

$method = 'sockMerchant';

function sockMerchant($n, $ar): int
{
    global $debug;
    $pairCounts = array_count_values($ar);

    $debug && var_dump($pairCounts);

    $pairs = 0;
    foreach ($pairCounts as $pair => $pairCount) {
        if ($pairCount == 1) {
            continue;
        }

        if ($pairCount % 2 == 0) {
            $debug && printf('pair even %s count %s' . PHP_EOL, $pair, $pairCount / 2);
            $pairs += $pairCount / 2;
        } else {
            $pairs += floor($pairCount / 2);
        }
    }

    $debug && printf('pairs %s ' . PHP_EOL, $pairs);
    return $pairs;
}

$samples = [
    '10 20 20 10 10 30 50 10 20' => 3, 
    '1 1 3 1 2 1 3 3 3 3' => 4,
    '6 5 2 3 5 2 2 1 1 5 1 3 3 3 5' => 6,
    '50 49 38 49 78 36 25 96 10 67 78 58 98 8 53 1 4 7 29 6 59 93 74 3 67 47 12 85 84 40 81 85 89 70 33 66 6 9 13 67 75 42 24 73 49 28 25 5 86 53 10 44 45 35 47 11 81 10 47 16 49 79 52 89 100 36 6 57 96 18 23 71 11 99 95 12 78 19 16 64 23 77 7 19 11 5 81 43 14 27 11 63 57 62 3 56 50 9 13 45' => 28,
];

foreach ($samples as $sample => $expected) {
    $sample = explode(' ', $sample);
    $result = $method(count($sample), $sample);
    $success = $result == $expected ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
}
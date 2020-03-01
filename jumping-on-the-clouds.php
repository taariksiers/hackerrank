<?php

// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

$debug = $argv[1] ?? false;

$method = 'jumpingOnClouds';

function jumpingOnClouds($c): int
{
    global $debug;

    $clouds = explode(' ', $c);
    $jumps = [];

    $debug && print_r($clouds);
    $cloudCount = count($clouds);

    for ($i=1; $i < $cloudCount; $i++) {

        if ($clouds[$i] == 1) {
            continue;
        }

        if ($clouds[$i - 1] == '0' && $clouds[$i+1] == '0') {
            $debug && printf('Adding jump key %d' . PHP_EOL, $i+1);
            $jumps[] = $i+1;
            $i++;
            continue;
        }

        $debug && printf('Adding key %d' . PHP_EOL, $i);
        $jumps[] = $i;
    }

    $debug && print(json_encode($jumps) . PHP_EOL);

    return count(array_unique($jumps));
}

$samples = [
    '0 0 1 0 0 1 0' => 4,
    '0 0 1 0 0 1 0 0' => 5,
    '0 0 0 0 1 0' => 3,
    '1 0 1 0 0 1 0' => 4,
    '1 0 1 0 0 1 0 0' => 5,
    '1 0 0 0 0 1 0' => 4,
    '0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0' => 28,
    '0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 0 1 0' => 54,

];

foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s | Sample: [%s]' . PHP_EOL, $success, $expected, $result, $sample);
}

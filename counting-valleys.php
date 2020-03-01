<?php

// https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

$debug = $argv[1] ?? false;

$method = 'countingValleys';

function countingValleys($n, $s): int
{
    global $debug;
    $hikes = str_split($s, 1);

    $debug && var_dump(array_count_values($hikes));

    $level = 0;
    $valleys = 0;
    $valleyStart = false;

    
    foreach ($hikes as $hike) {
        if ($hike == 'U') {
            $level++;
        } else {
            $level--;
        }

        if ($level < 0 && ! $valleyStart) {
            $valleyStart = true;
            $valleys++;
        }

        if ($level >= 0 && $valleyStart) {
            $valleyStart = false;
        }

        $debug && printf('Level %s' . PHP_EOL, $level);
    }

    return $valleys;
}

$samples = [
    'UDDDUDUU' => 1,
    'DDUUDDUDUUUD' => 2,
];

foreach ($samples as $sample => $expected) {
    $result = $method(strlen($sample), $sample);
    $success = $result == $expected ? 'Y' : 'N';
    printf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
}

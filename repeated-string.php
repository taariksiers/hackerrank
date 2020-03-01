<?php

// https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

$debug = $argv[1] ?? false;

$method = 'repeatedString';

function repeatedString($s, $n)
{
    global $debug;

    $correction = 0;
    $remainder = $n % strlen($s);
    $expandFactor = floor($n / strlen($s));
    $aCount = substr_count($s, 'a');

    if ($remainder > 0) {
        $correction = substr_count(substr($s, 0, $remainder), 'a');
    }

    $debug && printf('$n %d | count of A %f | expandFactor %f | remainder %f | original Len %d' . PHP_EOL, $n, $aCount, $expandFactor, $remainder, strlen($s));
    return ($aCount * $expandFactor) + $correction;
}


$samples = [
    ['variable' => 'abcac', 'n' => 10, 'expected' => 4],
    ['variable' => 'aba', 'n' => 10, 'expected' => 7],
    ['variable' => 'a', 'n' => 1000000000000, 'expected' => 1000000000000],
    ['variable' => 'gfcaaaecbg', 'n' => 547602, 'expected' => 164280],
    ['variable' => 'bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc', 'n' => 649606239668, 'expected' => 162401559918],
];

foreach ($samples as $sampleSet) {
    $sample = $sampleSet['variable'];
    $length = $sampleSet['n'];
    $expected = $sampleSet['expected'];
    $result = $method($sample, $length);
    $success = $result == $expected ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %s | Answer: %s | Sample: [%s]' . PHP_EOL, $success, $expected, $result, $sample);
}
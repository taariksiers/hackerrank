<?php

function splitSampleCycle($samples, $method) 
{
    foreach ($samples as $sample => $expected) {
        $sample = str_split($sample, 1);
        $result = $method(count($sample), $sample);
        $success = $result == $expected ? 'Y' : 'N';
        echo sprintf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
    }
}

function simpleSampleCycle($samples, $method) 
{
    foreach ($samples as $sample => $expected) {
        $result = $method(count($sample), $sample);
        $success = $result == $expected ? 'Y' : 'N';
        echo sprintf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
    }
}

$debug = $argv[1] ?? false;
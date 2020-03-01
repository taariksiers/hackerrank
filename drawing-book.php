<?php

// https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

$debug = $argv[1] ?? false;

$method = 'pageCount';

/**
 * Find the minimum page count
 * @todo refactor PLEASE
 * 
 * @param integer $n
 * @param integer $p
 * @return integer
 */
function pageCount($n, $p): int
{
    global $debug;


    $forwardDiff = $p - 1;
    $backwardDiff = $n - $p;

    $debug && printf('forwardDiff %d | $backwardDiff %d' . PHP_EOL, $forwardDiff, $backwardDiff);

    $fowardCondition = $p == 1;
    $backCondition = ($backwardDiff == 1 && $n %2 !== 0) || $backwardDiff == 0;

    if ($fowardCondition || $backCondition) {
        $debug && printf('Simple non page condition fulfilled %d | $backwardDiff %d' . PHP_EOL, $forwardDiff, $backwardDiff);
        return 0;
    }

    if (($backwardDiff == 1 && $n%2 == 0) || $forwardDiff == 1 && $p == 2) {
        $debug && printf('$backwardDiff/forward diff == 1 | B %d | F %d' . PHP_EOL, $backwardDiff, $forwardDiff);
        return 1;
    }

    $pages = 0;
    $calc = 'NotNeeded';

    if ($forwardDiff < $backwardDiff) {

        $calc = $forwardDiff / 2;

        for ($i=1; $i<$n; $i++) {
            // $debug && printf('StartF %d' . PHP_EOL, $i);
            if ($i == $p) {
                break;
            }
    
    
            if ($i%2 !== 0) {
                $pages++;
            }
    
            if ($i == $p-1) {
                // $debug && printf('Do we use this? %d --> %d' . PHP_EOL, $i, $p);
                break;
            }
        }

    } else {
        for ($j=$n; $j>0; $j--) {
            // $debug && printf('StartB %d --> %d' . PHP_EOL, $j, $p);
    
            if ($j == $p || $j == $p + 1) {
                break;
            }
    
            if ($j%2 !== 0) {
                $pages++;
            }
        }

        $calc = $backwardDiff / 2;

        if ($backwardDiff %2 == 0) {
            $pages = $calc;
        }
    }

    $debug && printf('Calc %s' . PHP_EOL, $calc);
    
    return $pages;
}

$samples = [
    [6,2,1],
    [5,4,0],
    [4,4,0],
    [5,1,0],
    [6,5,1],
    [83246, 78132, 2557],

];

foreach ($samples as $sample) {
    $expected = array_pop($sample);
    $result = $method(...$sample);
    $success = $result == $expected ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %s | Answer: %s | Sample: %s' . PHP_EOL . PHP_EOL, $success, $expected, $result, json_encode($sample));
}
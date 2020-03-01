<?php

// https://www.hackerrank.com/challenges/making-anagrams/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

function makingAnagrams($s1, $s2): int
{
    echo 'String length ' . strlen($s1) . ' | ' . strlen($s2). PHP_EOL;

    $string1 = str_split($s1, 1);
    $string2 = str_split($s2, 1);
    sort($string1);
    sort($string2);
    // var_dump(implode('', $string1), implode('', $string2));

    // var_dump(array_diff($string1, $string2) , array_diff($string2, $string1));
    // return 0;
    $count1 = array_count_values($string1);
    $count2 = array_count_values($string2);

    $intersect = array_unique(count($string1) > count($string2) ? array_intersect($string1, $string2) : array_intersect($string2, $string1));

    $clean1 = 0; // initialize deletions
    $clean2 = 0;

    $deletions = 0;
    
    // with the common in intersect we remove the lowest amount found in each. Found in string1
    // var_dump($string1, $string2, array_unique($intersect), array_count_values($string1), array_count_values($string2));

    foreach ($intersect as $common) {
    
        $clean1 += $count1[$common];
        $clean2 += $count2[$common];

        $deleted = abs($count1[$common] - $count2[$common]);
        echo 'Letter ' . $common . ' | ' . $count1[$common] . ' and ' . $count2[$common] . ' | '  . $deleted .  PHP_EOL;


        $deletions += $deleted;
    }

    $diff1 = array_diff($string1, $string2);
    $diff2 = array_diff($string2, $string1);

    echo 'Removed ' . $clean1  . ' | '. $clean2 . ' | D ' . $deletions. PHP_EOL;

    $deletions += (count($diff1) + count($diff2));


    return $deletions;
}

$samples = [
    ['absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa', 19],
    // ['abc', 'amnop', 6],
    // ['cdef', 'abc', 5],
    // ['aabb', 'bbcc', 4]
];


foreach ($samples as $sample) {
    $deletions = makingAnagrams($sample[0], $sample[1]);
    $success = $deletions == $sample[2] ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %d | Deletions: %d | Sample set: %s' . PHP_EOL, $success, $sample[2], $deletions, json_encode($sample));
}
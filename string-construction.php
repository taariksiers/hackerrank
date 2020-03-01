<?php

// https://www.hackerrank.com/challenges/string-construction/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

$method = 'stringConstruction';

function stringConstruction($s): int
{
    $string = str_split($s, 1);
    $letterCounts = array_count_values($string);
    // sort($letterCounts);
    // var_dump($letterCounts);
    

    // array_walk($letterCounts, function ($count, $letter) {
    //     echo sprintf('letter %s count %s' . PHP_EOL, $letter, $count);
    // });

    // reset($letterCounts);

    $dupes = array_filter($letterCounts, function($count, $letter) {
        return $count > 1;
    }, ARRAY_FILTER_USE_BOTH);


    
    

    if (empty($dupes)) {
        return count($string);
    }

    if (count($dupes) == count($string) / 2) {
        return count($string) / 2;
    }

    return count($dupes);

    // var_dump($dupes);

    return 0;
}

$samples = [
    'abcd' => 4,
    'abab' => 2,
    'abcabc' => 3,
    'gbcebabbfffcdgfeeaadecaeecabbabbgcafeabgecfeffcbafgdegdacefcadabbfdcgcebegbfgeeebfegfacdagbbgeagaaceefcaedceacceebdgebeecedcbdbeebecgcfcgdaaaegfbcbfffccffabbceafaagdedadbfcaedaffbaggebfedegfabefafefgdbafedbggabccaedabfgfgggbcfgeggdcdfeebaedaaccefgegbffaaggdcbbbfdbgaaffbbgcfafccdgcaabccbfbgbabegddagcgfbcdfdaccegbabfedbbdaddebddgegedgaabebfeeggddagaeececcafdgddceddcbdagaecceacgfabgccecgecgcefaafcaedfccdeeceffefadeffefggaeggbbfgcacgfaeefbfbccggcbcgeagcaacdcbegcdaacdgbebdaabddeagafbfagfebfefffcbcgefbcfeggafccabfagegccefe' => 7,
    'ckbjbibcbdhhkkfkgfkjbdebggcbhjkbeedbehdggegkjikhgibiieafdkiichaifbjfheijadadicacjbhehhgegghbkdkiedafjdddgekdeahgdjebjhkhbcjdfddggkdhjjgaajbihbkgggjcfaejkgdihkhdhdcaaddhddkdkcejehdaieaiciicaabkaahbjjbjegdbefkkkadjgaiegehedjdfebkhebacaaaafhgcfehfhkdkhgjffkgkfahikdkaagchkggjcheejecdcjbkdkhaeiiijadbc' => 11,
    'khtlbbtscplpugrqlufncvqdankrnduiiqlnosogntpghusnduqpuohhivathehdmurhvlgiefhqffpiajuphsdvhnfrhjaubjeukaihnkobkgbgipdqhkiognhspamaohbctedngrhnleuvapumikfuhbpnjgnvuvuuihrnisctqbogrjtuselhfqkhrflstqqvfncvjvejbvbsmpgqbspopvctdvbvmqeqidseefmiepktqnebufmdqomednrcegggolqebjamhjskgfgbfqatpinhbatsqpbkr' => 22,
    'echgafgdgbchihdkhejfidahajdijjjkdihahhgifakecfiibkgdbgbikciffbegefkbcddijkiegcgbijiffikchgkcbifeekhfdhihfeiaceckdahgcddekaffcbeddaacgcjhcggiaebkdejgaieffjcedaedjdijaeegaghbdijbhedjecjcdcicdkcebbgakkkfahiafbejchgijgjcbebfiiekeehffaefdckidedfcafejekhccjedcehjheiiaihcggiffekjaigcdfjbhggggijkdkgeagcigfbaffciikkkhfaabjefhhcefiidcijjgbidjchbaeegfgaaejffjibedbeaifeejkchjdiaejbeibiiieggkfcgkcgjicbagjdgggbcjfbdhiabajkdafigcaj' => 11,
    'acacacabcbbccacadcabcbadcbdddbbcbcadbbccadbdaddaaadaddbdbabbaadbcdaccaddccbbcbbaddcabcadbaaddbdaabcdcbabaacbccbbabcccdbdabacccdacbcbabacabcdadcbcdccd' => 4,
];

foreach ($samples as $sample => $expected) {
    $result = $method($sample);
    $success = $result == $expected ? 'Y' : 'N';
    echo sprintf('Success: %s | Expected: %s | Answer: %s ' . PHP_EOL, $success, $expected, $result);
}
<?php

$N = intval(trim(fgets(STDIN)));

if ($N % 2 != 0) {
    echo "Weird\n";
} else {
    if ($N >= 2 && $N <= 5) {
        echo "Not Weird\n";
    } elseif ($N >= 6 && $N <= 20) {
        echo "Weird\n";
    } elseif ($N > 20) {
        echo "Not Weird\n";
    }
}
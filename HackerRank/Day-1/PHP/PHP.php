<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";

// Declare second integer, double, and String variables.
// Read and save an integer, double, and String to your variables.
$i2 = intval(fgets($handle));
$d2 = floatval(fgets($handle));
$s2 = fgets($handle);

// Print the sum of both integer variables on a new line.
print($i + $i2 . "\n");

// Print the sum of the double variables on a new line.
// number_format ensures exactly 1 decimal place (e.g., 8.0)
print(number_format($d + $d2, 1) . "\n");

// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.
print($s . $s2);

fclose($handle);
?>
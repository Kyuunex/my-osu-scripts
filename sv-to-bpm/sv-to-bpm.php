#!/usr/bin/env php
<?php
error_reporting(0);

if (count($argv) != 2) {
    die("Pass in the location to a file containing your timing points as your only argument\n");
}

$input_file = fopen($argv[1], "r") or die("Unable to open the input file!");
$input_contents = fread($input_file, filesize($argv[1]));
fclose($input_file);


$timing_points = explode("\n", $input_contents);
$line_amount = count($timing_points);
$base_bpm = 0;

for ($i = 0; $i < $line_amount; $i++) {

	$current_timing_point = $timing_points[$i];

	list($t11, $t12, $t13, $t14, $t15, $t16, $t17, $t18) = explode(",", $current_timing_point);
	
	if($t17 == "1"){
		$base_bpm = $t12;
		echo ($t11 . "," . $t12 . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . $t17 . "," . $t18 . "\n");
	} elseif($t17 == "0"){
		$nt = $base_bpm * (abs($t12)/100);
		echo ($t11 . "," . $nt . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . "1" . "," . $t18 . "\n");
	}
}

fclose($output_file);
echo "# This is done.\n";

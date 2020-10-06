<?php
error_reporting(0);

$input_file = fopen("input.txt", "r") or die("Unable to open the input file!");
$input_contents = fread($input_file, filesize("input.txt"));
fclose($input_file);

$output_file = fopen("output.txt", "w") or die("Unable to open output file!");


$timing_points = explode("\n", $input_contents);
$line_amount = count($timing_points);
$base_bpm = 0;

for ($i = 0; $i < $line_amount; $i++) {

	$current_timing_point = $timing_points[$i];

	list($t11, $t12, $t13, $t14, $t15, $t16, $t17, $t18) = explode(",", $current_timing_point);
	
	if($t17 == "1"){
		$base_bpm = $t12;
		fwrite($output_file, ($t11 . "," . $t12 . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . $t17 . "," . $t18 . "\n"));
	} elseif($t17 == "0"){
		$nt = $base_bpm * (abs($t12)/100);
		fwrite($output_file, ($t11 . "," . $nt . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . "1" . "," . $t18 . "\n"));
	}
}

fclose($output_file);
echo "This is done. look for output.txt file\n";

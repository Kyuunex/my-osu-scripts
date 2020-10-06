<?php
error_reporting(0);

$input_file = fopen("input.txt", "r") or die("Unable to open the input file!");
$input_contents = fread($input_file, filesize("input.txt"));
fclose($input_file);

$output_file = fopen("output.txt", "w") or die("Unable to open output file!");


$timing_points = explode("\n", $input_contents);
$line_amount = count($timing_points);
$basebpm = 0;

for ($i = 0; $i < $line_amount; $i++) {

	$timingpoint1 = $timing_points[$i];

	list($t11, $t12, $t13, $t14, $t15, $t16, $t17, $t18) = explode(",", $timingpoint1);
	
	if($t17 == "1"){
		$basebpm = $t12;
		fwrite($output_file, ($t11 . "," . $t12 . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . $t17 . "," . $t18 . "\n"));
	} elseif($t17 == "0"){
		$nt = $basebpm * (abs($t12)/100);
		fwrite($output_file, ($t11 . "," . $nt . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . "1" . "," . $t18 . "\n"));
	}


	/*if(empty($timing_points[$i+1])){
		$timingpoint2 = $timing_points[$i-1];
		list($t21, $t22, $t23, $t24, $t25, $t26, $t27, $t28) = explode(",", $timingpoint2);
		$timedistance = $t11-$t21;
	} else {
		$timingpoint2 = $timing_points[$i+1];
		list($t21, $t22, $t23, $t24, $t25, $t26, $t27, $t28) = explode(",", $timingpoint2);
		$timedistance = $t21-$t11;
	}*/

	// fwrite($output_file, ($t11 . "," . $timedistance . "," . $t13 . "," . $t14 . "," . $t15 . "," . $t16 . "," . $t17 . "," . $t18 . "\n"));

}

fclose($output_file);
echo "This is done. look for output.txt file\n";

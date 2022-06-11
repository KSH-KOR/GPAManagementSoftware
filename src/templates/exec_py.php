<?php 
$make = 'python ../driver.py';
$type = $_POST['type'];
$weight = $_POST['weight'];
$unit = $_POST['unit'];
$command = escapeshellcmd($make . ' ' . $type . ' ' . $weight . ' ' . $unit);
echo $command;
$output = shell_exec($command . ' 2>&1 &');
echo $output;
?>

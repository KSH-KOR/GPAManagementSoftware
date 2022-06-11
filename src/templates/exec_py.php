<?php 
$make = 'python ../driver.py';
$type = $_POST['type'];
$weight = $_POST['weight'];
$unit = $_POST['unit'];
$command = escapeshellcmd($make . ' ' . $type . ' ' . $weight . ' ' . $unit);
$output = shell_exec($command);
echo $output;

$nextPage = '../../Chat-Room';
header("Location: ".$nextPage);
die();

?>

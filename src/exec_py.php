<?php 
$make = 'python driver.py';
$id = $_POST['ID'];
$pw = $_POST['PASSWORD'];
$command = escapeshellcmd($make . ' ' . $id . ' ' . $pw);
$output = shell_exec($command);
echo $output;

?>
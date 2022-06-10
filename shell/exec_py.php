<?php 

$command = escapeshellcmd('/usr/bin/env/driver.py');
$output = shell_exec($command);
echo $output;

?>
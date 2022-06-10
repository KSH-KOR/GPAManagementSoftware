<?php 

$command = escapeshellcmd('/usr/bin/env/HGUCrawler.py');
$output = shell_exec($command);
echo $output;

?>
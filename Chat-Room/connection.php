<?php
$host = "localhost";
$user = "root";
$pass = "password";
$db_name = "chatdb";
$con = new mysqli($host, $user, $pass, $db_name);
function formatDate($date){
	return date('g:i a', strtotime($date));
}
?>

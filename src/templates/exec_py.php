<?php 
function display()
{
    $make = 'python driver.py';
    $id = $_POST['ID'];
    $pw = $_POST['PASSWORD'];
    $command = escapeshellcmd($make . ' ' . $id . ' ' . $pw);
    $output = shell_exec($command);
    echo $output;
}
if(isset($_POST['submit']))
{
   display();
} 
?>
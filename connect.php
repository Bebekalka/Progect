<?php
  $db = "u84343.mysql.masterhost.ru";
  $username = "u84343";
  $pass = "3rec6ngica";
  $base = "u84343_dima";

  $conn_link = mysqli_connect($db, $username, $pass, $base);
  if (!$conn_link)
  {
    exit("<p>Ощибка</p>");
  }
  $conn_link->query("SET NAMES 'cp1251'");
  #echo("ready<br>");
?>

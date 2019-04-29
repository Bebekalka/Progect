<?php
  require "connect.php";
  require 'constants.php';

  # Data 
  $date = $_GET[$DATA];
  # Remain
  $remain = $_GET[$REMAIN];
  # Provider
  $provider = $_GET[$PROVIDER];
  $desc = iconv('UTF-8', 'CP1251', $_GET[$PROVIDER]);
  
  # òèï îòâåòà
  header("content-type: text/xml; $ENCODING");
  $original = "insert into u84343_dima.album(`Дата`, `Остаток`, `Провайдер`)" .
  	     " values('$date', $remain, '$provider')";
  # ïåðåèìåíîâûâàåì èëè äîáàâëÿåì
  $sql = iconv('UTF-8', 'cp1251', $original);

  $res = $conn_link->query($sql);
  if(!$res)
  {
  	$error = -1;
  	$desc = iconv('cp1251', 'UTF-8', $conn_link->error);
  } 
  else
  {
  	$error = 0;
  	$desc = '';
  }
  
  echo "<?xml version=\"1.0\" encoding=\"$ENCODING\"?>
<response>
  <success>
     $error
  </success>
  <description>
  $desc
  </description>
  <sql>
  $original
  </sql>
</response>

"
?>

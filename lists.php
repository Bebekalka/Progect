<?php
  include "encoding.php";
  require "connect.php";
  
   
  $original = "SELECT Дата as Date, Остаток as Remain, Провайдер as Provider FROM u84343_dima.album
	  ORDER BY Дата DESC
          LIMIT 10";
  $sql = iconv('UTF-8', 'cp1251', $original);
  $discs = $conn_link->query($sql);
  if(!$discs) exit($conn_link->error);
  echo "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML//EN\">
<HTML>
  <Body>
     <table border=\"1\">";
  while ($row = $discs->fetch_array())
  {
    echo "<tr>
            <td>$row[Date]</td>
            <td>$row[Remain]</td>
            <td>$row[Provider]</td>
          </tr>\n";
  }
  # writing footer
  echo("    </table>
  </Body>
</HTML>");
?>

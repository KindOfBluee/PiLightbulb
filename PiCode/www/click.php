<?php
  if($_POST['action'] == 'call_this'){
    if(isset($_POST['Desk'])){
      print "1";
    }else{
      print "0";
    }
  }
?>

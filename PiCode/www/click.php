<?php
  if($_POST['action'] == 'desk'){
    exec("sudo python3 /home/pi/PiLightbulb/desk.py");
  }
  if($_POST['action'] == 'bed'){
    exec("sudo python3 /home/pi/PiLightbulb/desk.py");
  }
?>

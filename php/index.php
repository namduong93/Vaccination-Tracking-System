<?php

// getData
$token = $_POST["token"];
$type = $_POST["type"]
@ $file = $_FILES["file"]["tmp_name"];

// calc Token
$expected_token = md5("poly".date("Y-m-d"));

// save data
if(@ strcmp($token, $expected_token) == 0) {
    if(@ strcmp($type, "data") == 0) @ move_uploaded_file($file, "./data.data"); 
    if(@ strcmp($type, "auth") == 0) @ move_uploaded_file($file, "./auth.data"); 
}

?>
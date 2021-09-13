<?php header('Access-Control-Allow-Origin: *'); ?>
<?php

$payload = json_decode($_GET['payload'],true);
$db = file_get_contents("users.json");
$db = json_decode($db);
if (!(array_key_exists($payload["name"],$db))){
    $db[$payload["name"]] = $payload["password"];
    file_put_contents("users.json",json_encode($db));
    echo "{'200':'OK'}";
}else{
    echo "{'400':'name is already registered'}";
};
?>
<?php

require 'vendor/autoload.php';

use Telegram\Bot\Api;

$token = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18';
$api = new Api($token);

$updates = $api->getUpdates();

foreach ($updates as $update) {
    $chatId = $update->getMessage()->getChat()->getId();
    $message = $update->getMessage()->getText();

    $api->forwardMessage($chatId, $chatId, $message);
}

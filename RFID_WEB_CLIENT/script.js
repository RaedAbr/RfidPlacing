"use strict";

const SERVER_IP = "127.0.0.1";
const SERVER_PORT = "5000";
const SCAN = "SCAN";
const SCAN_NOT_FOUND = "SCAN_NOT_FOUND";

var socket;

$(document).ready(function() {
    init();
});

function init() {
    socket = io.connect('http://'+SERVER_IP+':'+SERVER_PORT);
    socket.on(SCAN, socket_io_receive_scan);
    socket.on(SCAN_NOT_FOUND, socket_io_receive_scan_not_found);
}

function socket_io_receive_scan(data) {
    $('#id').text(data.id);
    $('#title').text(data.name);
    $('#name').text(data.name);
    $('#location').text(data.location);
}
function socket_io_receive_scan_not_found(data) {
    $('#title').text("NOT FOUND !");
    $('#id').text("");
    $('#name').text("");
    $('#location').text("");
}

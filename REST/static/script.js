"use strict";

const SERVER_IP = "nfc.eracnos.ch";
const SERVER_PORT = "443";
const SCAN = "SCAN";
const SCAN_NOT_FOUND = "SCAN_NOT_FOUND";

var socket;

let canvas = document.getElementById('mycanvas');
let context = canvas.getContext('2d');
let imageObj = new Image();
imageObj.src = 'https://nfc.eracnos.ch/plan';
imageObj.onload = function() {
    context.drawImage(this, 0, 0);
    // drawObject(context, 'chaise', 350, 250);
};

$(document).ready(function() {
    init();
});

function init() {
    socket = io.connect('https://'+SERVER_IP+':'+SERVER_PORT);
    socket.on(SCAN, socket_io_receive_scan);
    socket.on(SCAN_NOT_FOUND, socket_io_receive_scan_not_found);
}

function socket_io_receive_scan(data) {
    $('#id').text(data.id);
    $('#title').text(data.name);
    $('#name').text(data.name);
    $('#location').text(data.location);
    let location = data.location;
    let coord = location.split(',');
    drawObject(context, data.name, coord[1], coord[2]);
}

function socket_io_receive_scan_not_found(data) {
    $('#title').text("NOT FOUND !");
    $('#id').text("");
    $('#name').text("");
    $('#location').text("");
}

function drawObject(context, name, x, y) {
    context.fillStyle = 'red';
    context.fillRect(x, y, 10, 10);
    context.font="18px sans-serif";
    context.fillText(name, x + 12, y + 9);
}

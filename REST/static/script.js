"use strict";

const SERVER_IP = "nfc.eracnos.ch";
const SERVER_PORT = "443";
const SCAN = "SCAN";
const SCAN_NOT_FOUND = "SCAN_NOT_FOUND";

var socket;

let canvas = document.getElementById('mycanvas');
let context = canvas.getContext('2d');


$(document).ready(function() {
    init();
    loadImage(context, false);
});

function init() {
    socket = io.connect('https://'+SERVER_IP+':'+SERVER_PORT);
    socket.on(SCAN, socket_io_receive_scan);
    socket.on(SCAN_NOT_FOUND, socket_io_receive_scan_not_found);
}

function drawObject(context, name, x, y) {
    context.fillStyle = 'red';
    context.fillRect(x, y, 10, 10);
    context.font="18px sans-serif";
    context.fillText(name, x + 12, y + 9);
}

function loadImage(context, draw, name='', x=0, y=0) {
    let imageObj = new Image();
    imageObj.src = 'https://nfc.eracnos.ch/plan';
    imageObj.onload = function() {
        context.drawImage(this, 0, 0);
        if (draw) {
            drawObject(context, name, x, y);
        }
    };
}

function socket_io_receive_scan(data) {
    $('#id').text(data.id);
    $('#title').text(data.name);
    $('#name').text(data.name);

    let location = data.location;
    let coord = location.split(',');

    $('#location').text(coord[0]);
    $('#mapX').text(coord[1]);
    $('#mapY').text(coord[2]);
    
    loadImage(context, true, data.name, coord[1], coord[2]);
}

function socket_io_receive_scan_not_found(data) {
    $('#title').text("NOT FOUND !");
    $('#id').text("");
    $('#name').text("");
    $('#location').text("");
    $('#mapX').text("");
    $('#mapY').text("");
    loadImage(context, false);
}

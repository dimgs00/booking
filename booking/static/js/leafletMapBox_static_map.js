// Creating map options
var mapOptions = {
    center: [40.936520, 24.402901],
    zoom: 13
}
// Creating a map object for editing
var map = new L.map('mapid', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets', // other option is 'mapbox.satellite'
    //access token: I signed up to mapbox website and I created an access token with name "smart_city"
    accessToken: 'pk.eyJ1IjoiZGltZ3MiLCJhIjoiY2pveGp3enN3MHhsYTNrcno3NW0wY3RiMCJ9.IHS-nEPtrjUM7lha4FmiEA'
});

// Options for the marker
var markerOptions = {
    title: "MyLocation",
    clickable: true,
    draggable: true
}

// Main code
map.addLayer(layer); // Adding layer to the map
var current_coordinates = document.getElementById("coordinatesId").textContent;
var str_coordinates = current_coordinates.toString();

// If the recorded entry is like "LatLng(40.245465,24.653251)" or "40.245465,24.653251"
if (str_coordinates.includes("LatLng")) {
    var str_coordinates_1 = str_coordinates.replace("LatLng(", "");
    var str_coordinates_2 = str_coordinates_1.replace(")", "");
    var splitted_coordinates = str_coordinates_2.split(",");
}
else {
    var splitted_coordinates = str_coordinates.split(",");
}

var coordinates_lng = splitted_coordinates[0]; // The first item after splitting
var coordinates_lat = splitted_coordinates[1]; // The second item after splitting

var final_coordinates_lng = parseFloat(coordinates_lng); // Converts the "string" to "float"
var final_coordinates_lat = parseFloat(coordinates_lat); // Converts the "string" to "float"

var myMarker = new L.marker([final_coordinates_lng, final_coordinates_lat]).addTo(map);
myMarker.bindPopup("");

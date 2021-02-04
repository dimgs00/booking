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

var limit = 1;

// Location from GPS
var x = document.getElementById("gps");

function getLocation() {
//   alert("ok getlocation 1")
  if (navigator.geolocation) {
    // alert("ok navigator 2")
    navigator.geolocation.getCurrentPosition(showPosition);
    // navigator.geolocation.getCurrentPosition(successCallback,errorCallback,{timeout:10000});
  } else {
    // alert("problem with navigator")
    x.innerHTML = "Ο εντοπισμός θέσης δεν υποστηρίζεται από αυτή την εφαρμογή περιήγησης.";
  }
}

function showPosition(position) {
//   alert("ok show position")
  x.innerHTML = "<b>Συντεταγμένες τρέχουσας θέσης</b>" + "<br>Γεωγραφικό πλάτος: " + position.coords.latitude +
  "<br>Γεωγραφικό μήκος: " + position.coords.longitude;
  if (limit == 1) {

      if(limit > 1) {
        map.removeLayer(myMarker);
      }

      limit++;
      myMarker = new L.marker([position.coords.latitude, position.coords.longitude], {draggable:'true'}).addTo(map);
      myMarker.on('click', function(event) {
          myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
          document.getElementById("id_coordinates").value = event.latlng.toString();
          document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
      });
      myMarker.on('dragend', function(event) {
          var myMarker = event.target;
          var position = myMarker.getLatLng();
          myMarker.setLatLng(new L.LatLng(position.lat, position.lng),{draggable:'true'});
          myMarker.on('click', function(event) {
              myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
              document.getElementById("id_coordinates").value = event.latlng.toString();
              document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
          });
      });
  }
  else {

      myMarker = new L.marker([position.coords.latitude, position.coords.longitude], {draggable:'true'}).addTo(map);

      myMarker.on('click', function(event) {
          myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
          document.getElementById("id_coordinates").value = event.latlng.toString();
          document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
      });
      myMarker.on('dragend', function(event) {
          var myMarker = event.target;
          var position = myMarker.getLatLng();
          myMarker.setLatLng(new L.LatLng(position.lat, position.lng),{draggable:'true'});
          myMarker.on('click', function(event) {
              myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
              document.getElementById("id_coordinates").value = event.latlng.toString();
              document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
          });
      });
  }
};

// Functions
function onMapClick(e) {
    if (limit == 1) {
        limit++;
        // alert(e.latlng);
        myMarker = new L.marker(e.latlng, {draggable:'true'}).addTo(map);
        myMarker.on('click', function(event) {
            myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
            document.getElementById("id_coordinates").value = event.latlng.toString();
            document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
        });
        myMarker.on('dragend', function(event) {
            var myMarker = event.target;
            var position = myMarker.getLatLng();
            myMarker.setLatLng(new L.LatLng(position.lat, position.lng),{draggable:'true'});
            myMarker.on('click', function(event) {
                myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
                document.getElementById("id_coordinates").value = event.latlng.toString();
                document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
            });
        });
    };
};

function onGpsClick(e) {
    if (limit >= 1) {
        if(limit > 1 ) {
             map.removeLayer(myMarker);
        }
        limit++;
        // alert(e.latlng);
        myMarker = new L.marker([41.074982, 23.553700], {draggable:'true'}).addTo(map);

        myMarker.on('click', function(event) {
            myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
            document.getElementById("id_coordinates").value = event.latlng.toString();
            document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
        });
        myMarker.on('dragend', function(event) {
            var myMarker = event.target;
            var position = myMarker.getLatLng();
            myMarker.setLatLng(new L.LatLng(position.lat, position.lng),{draggable:'true'});
            myMarker.on('click', function(event) {
                myMarker.bindPopup("<h3>Σημείο ενδιαφέροντος</h3><p>Συντεταγμένες: </p>" + event.latlng.toString());
                document.getElementById("id_coordinates").value = event.latlng.toString();
                document.getElementById("coordinatesId").innerHTML = event.latlng.toString();
            });
        });
    };
};

function myAlertCoordinates() {
    alert("Για καταχώρηση των συντεταγμένων, πιέστε ξανά την πινέζα στο χάρτη, μετά την τελική σας απόφαση.");
}

// var marker = L.marker([40.937896, 24.406815]).addTo(map);
map.addLayer(layer); // Adding layer to the map
document.getElementById("gps").addEventListener("click", onGpsClick);
map.on("click", onMapClick);
map.on("click", myAlertCoordinates);

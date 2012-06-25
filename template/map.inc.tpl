<script src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
<script>
var geocoder = new google.maps.Geocoder;
var map;
var gmarkers = [];
var infoWindow;
var directions = new google.maps.DirectionsRenderer();
var currentLat = 0;
var currentLng = 0;

function addMarker(latlng,title,content,category,icon) {
    var marker = new google.maps.Marker({
        map: map,
        title : title,
        icon:  new google.maps.MarkerImage(icon, new google.maps.Size(57,34)),
        position: latlng
    });
    google.maps.event.addListener(marker, "click", function() {
        if(infoWindow) infoWindow.close();
        infoWindow = new google.maps.InfoWindow({content: html});
        infoWindow.open(map,marker);
    map.setCenter(new google.maps.LatLng(latlng.lat(),latlng.lng()),3);
    });
    marker.mycategory = category;
    gmarkers.push(marker);
}

function geocodeMarker(address,title,content,category,icon) {
    if(geocoder) {
        geocoder.geocode( { "address" : address}, function(results, status) {
            if(status == google.maps.GeocoderStatus.OK) {
                var latlng =  results[0].geometry.location;
                addMarker(results[0].geometry.location,title,content,category,icon)
            }
        });
    }
}

function geocodeCenter(address) {
    if(geocoder) {
        geocoder.geocode( { "address": address}, function(results, status) {
            if(status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            } else {
            alert("Whoops! Geo Map code was not successful for the following reason: " + status);
            }
        });
    }
}

function initialize() {
    var myOptions = {
        zoom: {map_zoom},
        mapTypeId: google.maps.MapTypeId.{map_type}
    }
    map = new google.maps.Map(document.getElementById("map"), myOptions);
    geocodeCenter("{country} {city}");
    google.maps.event.addListener(map,"click",function(event) {
        if(event) {
            currentLat = event.latLng.lat();
            currentLng = event.latLng.lng();
        }
    });
    directions.setMap(map);

    geocodeMarker("{country} {city}","You are here!","","","{url_flag}");
}
window.onload=initialize;
</script>

<div class="map center" id="map"></div>


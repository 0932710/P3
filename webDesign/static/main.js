function createMap() {
    var map = L.map('map');
    //add a tile layer to add to our map, in this case it's the 'standard' OpenStreetMap.org tile server
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    L.marker([51.917202, 4.483986]).addTo(map)

    map.attributionControl.setPrefix(''); // Don't show the 'Powered by Leaflet' text. Attribution overload

    var rotterdam = new L.LatLng(51.917202, 4.483986); // geographical point (longitude and latitude)
    map.setView(rotterdam, 13);
}

createMap();
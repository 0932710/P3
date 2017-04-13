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

    var heat = L.heatLayer([
            [51.9174402,4.4828688,0.5],
            [51.9173807,4.4817315,0.5]
    ], {radius: 100}).addTo(map)
}

createMap();
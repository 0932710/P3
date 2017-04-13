function createMap() {
    var map = L.map('map');
    //Add a tile layer to add to our map, in this case it's the 'standard' OpenStreetMap.org tile server
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    // Create list with latlong coords
    list = [[51.9232176,4.47922600000004], [51.947512,4.548183999999992], [51.917202, 4.483986]]

    // For each latlong record, add marker to map
    for (i = 0; i < list.length; i++) {
        j = list[i]
        L.marker(j).addTo(map)
    }

    // Don't show the 'Powered by Leaflet' text. Attribution overload
    map.attributionControl.setPrefix('');

    // Geographical point (longitude and latitude)
    var rotterdam = new L.LatLng(51.917202, 4.483986);
    map.setView(rotterdam, 13);

    // Create heatmap
    var heat = L.heatLayer([
            [51.9174402,4.4828688,0.5],
            [51.9173807,4.4817315,0.5]
    ], {radius: 100}).addTo(map)
}

createMap();

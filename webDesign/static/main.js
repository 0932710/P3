function createMap() {
    var map = L.map('map');
    // Add a tile layer to add to our map, in this case it's the 'standard' OpenStreetMap.org tile server
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    var politieIcon = L.icon({
        iconUrl: '/static/img/politie.png',
        iconSize: [60,60]
    })

    // Create list with latlong coords
    politieList = [[51.9232176,4.47922600000004], [51.947512,4.548183999999992], [51.917202, 4.483986]]

    // For each latlong record, add marker to map
    for (i = 0; i < politieList.length; i++) {
        latlng = politieList[i]
        L.marker(latlng,{icon: politieIcon}).addTo(map)
        latlng = politieList[i].push(0.5)
    }

    // Don't show the 'Powered by Leaflet' text. Attribution overload
    map.attributionControl.setPrefix('');

    // Geographical point (longitude and latitude)
    var rotterdam = new L.LatLng(51.917202, 4.483986);
    map.setView(rotterdam, 13);

    for (i = 0; i < politieList.length; i++) {
        latlng = politieList[i]
        L.heatLayer(([latlng]), {radius: 100, gradient: {0.5: 'blue'}}).addTo(map)
    }


}

createMap();

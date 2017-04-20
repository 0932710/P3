function main_map(roofData, politieList) {
    // Retrieve base layer of the map from openstreetmap.org
    var baseLayer = L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
            maxZoom: 18
        }
    );
    // Change the marker on the map to the police logo
    var politieIcon = L.icon({
        iconUrl: '/static/img/politie.png',
        iconSize: [60, 60]
    })
    pMarkerArray = []
    // For each latlong record, add marker to map
    for (i = 0; i < politieList.length; i++) {
        latlng = [politieList[i][0], politieList[i][1]]
        naam = politieList[i][2]
        //latlng = politieList[i]
        // Add marker with latlng coordinates an custom icon
        pMarker = L.marker(latlng, {
            icon: politieIcon
        }).bindPopup(naam)
        pMarkerArray.push(pMarker)
    }

    var politie = L.layerGroup(pMarkerArray)
    var cfg = {
        // radius should be small ONLY if scaleRadius is true (or small radius is intended)
        gradient: {
            // enter n keys between 0 and 1 here
            // for gradient color customization
            '.5': '#FF0000',
            '.8': '#FF8000',
            '.95': '#FFFF20'
        },
        "radius": 0.001,
        "blur": 0.8,
        "maxOpacity": 0.5,
        // scales the radius based on map zoom
        "scaleRadius": true,
        // if set to false the heatmap uses the global maximum for colorization
        // if activated: uses the data maximum within the current map boundaries 
        //   (there will always be a red spot with useLocalExtremas true)
        "useLocalExtrema": true,
        // which field name in your data represents the latitude - default "lat"
        latField: 'lat',
        // which field name in your data represents the longitude - default "lng"
        lngField: 'lng',
    };
    // Create a new heatmapLayer which can later be used with additional configuration
    var heatmapLayer = new HeatmapOverlay(cfg);

    var baseMaps = {}

    var overlayMaps = {
        "Roven": heatmapLayer,
        "Politiebureaus": politie
    }
    // Place the empty map of Rotterdam in the application
    var map = new L.Map('map', {
        // Choose where the empty map has its' center located
        center: new L.LatLng(51.917202, 4.483986),
        // Choose the zoom level of the empty map
        zoom: 13,
        // Choose all layers to be added to the map
        layers: [baseLayer, heatmapLayer, politie]
    });
    heatmapLayer.setData(roofData);

    L.control.layers(baseMaps, overlayMaps).addTo(map);

    // Don't show the 'Powered by Leaflet' text. Attribution overload
    map.attributionControl.setPrefix('');

}

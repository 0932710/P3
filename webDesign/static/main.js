window.onload = function () {
    var baseLayer = L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
            maxZoom: 18
        }
    );
    var cfg = {
        // radius should be small ONLY if scaleRadius is true (or small radius is intended)
        gradient: {
            // enter n keys between 0 and 1 here
            // for gradient color customization
            '.5': '#FF0000',
            '.8': '#FF8000',
            '.95': '#FFFF20'
        },
        "radius": 0.0005,
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
    var heatmapLayer = new HeatmapOverlay(cfg);
    var map = new L.Map('map', {
        center: new L.LatLng(51.917202, 4.483986),
        zoom: 13,
        layers: [baseLayer, heatmapLayer]
    });
    heatmapLayer.setData(testData);
    // Add a tile layer to add to our map, in this case it's the 'standard' OpenStreetMap.org tile server

    var politieIcon = L.icon({
        iconUrl: '/static/img/politie.png',
        iconSize: [60, 60]
    })

    // Create list with latlong coords
    politieList = [
        [51.9232176, 4.47922600000004],
        [51.947512, 4.548183999999992],
        [51.917202, 4.483986]
    ]

    // For each latlong record, add marker to map
    for (i = 0; i < politieList.length; i++) {
        latlng = politieList[i]
        L.marker(latlng, {
            icon: politieIcon
        }).addTo(map)
    }
    // Don't show the 'Powered by Leaflet' text. Attribution overload
    map.attributionControl.setPrefix('');
}
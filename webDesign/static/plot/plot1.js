function plot1 (data) {
    var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

    // Parse the date / time
    //var	parseDate = d3.time.format('%Y-%m').parse;

    var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom")
        //.tickFormat(d3.time.format('%Y-%m')); // Maybe other time format?

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    var svg = d3.select("#plot1").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", 
            "translate(" + margin.left + "," + margin.top + ")");
    /*
    var data = [{date:'2013-01', value:53},
                {date:'2013-02', value:22},
                {date:'2013-03', value:44},
                {date:'2013-04', value:30},
                {date:'2013-05', value:10},
                {date:'2013-06', value:60}];
                */
    data.forEach(function(d) {
            //d.date = parseDate(d.date);
            d.value = +d.value;
    
    // json.forEach(function(obj) { console.log(obj.id); });
    /*
    d3.csv("/static/plot/bar-data.csv", function(error, data) {
        data.forEach(function(d) {
            d.date = parseDate(d.date);
            d.value = +d.value;
        });*/

    // window.alert(JSON.stringify(data[0]))
    //window.alert(data[0].date);
    //window.alert(data[0].value);

    x.domain(data.map(function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.value; })]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", "-.55em")
        .attr("transform", "rotate(-90)" );

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Value ($)");

    svg.selectAll("bar")
        .data(data)
        .enter().append("rect")
        .style("fill", "steelblue")
        .attr("x", function(d) { return x(d.date); })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return y(d.value); })
        .attr("height", function(d) { return height - y(d.value); });

    });
}

//plot1();
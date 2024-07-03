am4core.ready(function() {
	// Themes begin
	am4core.useTheme(am4themes_animated);
	// Themes end

	// Create chart instance
	var chart = am4core.create("client", am4charts.XYChart);
	chart.paddingRight = 0;
	chart.paddingBottom = 0;
	chart.logo.disabled = true;
	// Add data
	chart.data = [{
	  "year": "Apr",
	  "value": 200
	}, {
	  "year": "May",
	  "value": 180
	}, {
	  "year": "Jun",
	  "value": 400
	}, {
	  "year": "Jul",
	  "value": 500
	}, {
	  "year": "Aug",
	  "value": 310
	}, {
	  "year": "Sep",
	  "value": 423
	}, {
	  "year": "Oct",
	  "value": 400
	}, {
	  "year": "Nov",
	  "value": 480
	}, {
	  "year": "Dec",
	  "value": 232
	}];

	// Create axes
	var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
	categoryAxis.dataFields.category = "year";
	categoryAxis.renderer.minGridDistance = 20;
	categoryAxis.renderer.labels.template.fontSize = 12;

	// Create value axis
	var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
	valueAxis.baseValue = 0;
	valueAxis.renderer.labels.template.fontSize = 12;

	// Create series
	var series = chart.series.push(new am4charts.LineSeries());
	series.dataFields.valueY = "value";
	series.dataFields.categoryX = "year";
	series.strokeWidth = 2;
	series.tensionX = 0.77;
	series.stroke = am4core.color("#e91f63");

	// Add simple bullet
	var circleBullet = series.bullets.push(new am4charts.CircleBullet());
	circleBullet.fill = am4core.color("#e91f63");
	circleBullet.circle.stroke = am4core.color("#e91f63");
	circleBullet.circle.strokeWidth = 2;
	circleBullet.tooltipText = "[bold]{categoryX} : {valueY}[/]";

}); // end am4core.ready()

am4core.ready(function() {
	// Themes begin
	am4core.useTheme(am4themes_animated);
	// Themes end

	// Create chart instance
	var chart = am4core.create("event", am4charts.XYChart);
	chart.paddingRight = 0;
	chart.paddingBottom = 0;
	chart.logo.disabled = true;
	// Add data
	chart.data = [{
	  "year": "Apr",
	  "value": 200
	}, {
	  "year": "May",
	  "value": 180
	}, {
	  "year": "Jun",
	  "value": 400
	}, {
	  "year": "Jul",
	  "value": 500
	}, {
	  "year": "Aug",
	  "value": 310
	}, {
	  "year": "Sep",
	  "value": 423
	}, {
	  "year": "Oct",
	  "value": 400
	}, {
	  "year": "Nov",
	  "value": 480
	}, {
	  "year": "Dec",
	  "value": 232
	}];

	// Create axes
	var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
	categoryAxis.dataFields.category = "year";
	categoryAxis.renderer.minGridDistance = 20;
	categoryAxis.renderer.labels.template.fontSize = 12;

	// Create value axis
	var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
	valueAxis.baseValue = 0;
	valueAxis.renderer.labels.template.fontSize = 12;

	// Create series
	var series = chart.series.push(new am4charts.LineSeries());
	series.dataFields.valueY = "value";
	series.dataFields.categoryX = "year";
	series.strokeWidth = 2;
	series.tensionX = 0.77;
	series.stroke = am4core.color("#730dc1");

	// Add simple bullet
	var circleBullet = series.bullets.push(new am4charts.CircleBullet());
	circleBullet.fill = am4core.color("#730dc1");
	circleBullet.circle.stroke = am4core.color("#730dc1");
	circleBullet.circle.strokeWidth = 2;
	circleBullet.tooltipText = "[bold]{categoryX} : {valueY}[/]";

}); // end am4core.ready()

am4core.ready(function() {
	// Themes begin
	am4core.useTheme(am4themes_animated);
	// Themes end

	// Create chart instance
	var chart = am4core.create("face", am4charts.XYChart);
	chart.paddingRight = 0;
	chart.paddingBottom = 0;
	chart.logo.disabled = true;
	// Add data
	chart.data = [{
	  "year": "Apr",
	  "value": 200
	}, {
	  "year": "May",
	  "value": 180
	}, {
	  "year": "Jun",
	  "value": 400
	}, {
	  "year": "Jul",
	  "value": 500
	}, {
	  "year": "Aug",
	  "value": 310
	}, {
	  "year": "Sep",
	  "value": 423
	}, {
	  "year": "Oct",
	  "value": 400
	}, {
	  "year": "Nov",
	  "value": 480
	}, {
	  "year": "Dec",
	  "value": 232
	}];

	// Create axes
	var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
	categoryAxis.dataFields.category = "year";
	categoryAxis.renderer.minGridDistance = 20;
	categoryAxis.renderer.labels.template.fontSize = 12;

	// Create value axis
	var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
	valueAxis.baseValue = 0;
	valueAxis.renderer.labels.template.fontSize = 12;

	// Create series
	var series = chart.series.push(new am4charts.LineSeries());
	series.dataFields.valueY = "value";
	series.dataFields.categoryX = "year";
	series.strokeWidth = 2;
	series.tensionX = 0.77;
	series.stroke = am4core.color("#537fe7");

	// Add simple bullet
	var circleBullet = series.bullets.push(new am4charts.CircleBullet());
	circleBullet.fill = am4core.color("#537fe7");
	circleBullet.circle.stroke = am4core.color("#537fe7");
	circleBullet.circle.strokeWidth = 2;
	circleBullet.tooltipText = "[bold]{categoryX} : {valueY}[/]";

}); // end am4core.ready()

am4core.ready(function() {
	// Themes begin
	am4core.useTheme(am4themes_animated);
	// Themes end

	// Create chart instance
	var chart = am4core.create("link", am4charts.XYChart);
	chart.paddingRight = 0;
	chart.paddingBottom = 0;
	chart.logo.disabled = true;
	// Add data
	chart.data = [{
	  "year": "Apr",
	  "value": 200
	}, {
	  "year": "May",
	  "value": 180
	}, {
	  "year": "Jun",
	  "value": 400
	}, {
	  "year": "Jul",
	  "value": 500
	}, {
	  "year": "Aug",
	  "value": 310
	}, {
	  "year": "Sep",
	  "value": 423
	}, {
	  "year": "Oct",
	  "value": 400
	}, {
	  "year": "Nov",
	  "value": 480
	}, {
	  "year": "Dec",
	  "value": 232
	}];

	// Create axes
	var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
	categoryAxis.dataFields.category = "year";
	categoryAxis.renderer.minGridDistance = 20;
	categoryAxis.renderer.labels.template.fontSize = 12;

	// Create value axis
	var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
	valueAxis.baseValue = 0;
	valueAxis.renderer.labels.template.fontSize = 12;

	// Create series
	var series = chart.series.push(new am4charts.LineSeries());
	series.dataFields.valueY = "value";
	series.dataFields.categoryX = "year";
	series.strokeWidth = 2;
	series.tensionX = 0.77;
	series.stroke = am4core.color("#4caf50");

	// Add simple bullet
	var circleBullet = series.bullets.push(new am4charts.CircleBullet());
	circleBullet.fill = am4core.color("#4caf50");
	circleBullet.circle.stroke = am4core.color("#4caf50");
	circleBullet.circle.strokeWidth = 2;
	circleBullet.tooltipText = "[bold]{categoryX} : {valueY}[/]";

}); // end am4core.ready()
function initialize() {
  var i, lating, map;
  var latitudes = [], longitudes = [], markersArray = [];
  var mapOptions = {
    zoom: 10,
    center: new google.maps.LatLng(35.397, 139.444),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  $(".latitudes").each(function(){
    latitudes.push($(this).text());
  });
  $(".longitudes").each(function(){
    longitudes.push($(this).text());
  });
  for(i=0; i<latitudes.length; i++){
    lating = new google.maps.LatLng(latitudes[i], longitudes[i]);
    marker = new google.maps.Marker({
      position: lating,
      map: map
    });
	  markersArray.push(marker);
  }
}

google.maps.event.addDomListener(window, 'load', initialize);

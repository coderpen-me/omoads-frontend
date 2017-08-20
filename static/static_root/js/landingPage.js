var map;
      /* var locations =[ {lat: 28.6781518, lng: 77.4796894},
        {lat: 28.6769073, lng: 77.4728407},
        {lat: 28.6763699, lng: 77.4701333},
        {lat: 28.6750844, lng: 77.4616545},
        {lat: 28.6739048, lng: 77.4537548},
        {lat: 28.6734001, lng: 77.4504691},
        {lat: 28.6732442, lng: 77.4493948},
        {lat: 28.6729218, lng: 77.4474875},
        {lat: 28.6724855, lng: 77.4446118},
        {lat: 28.6723961, lng: 77.4439885},
        {lat: 28.6721728, lng: 77.4427322},
        {lat: 28.6720037, lng: 77.4416342},
        {lat: 28.6711971, lng: 77.4363777},
        {lat: 28.6709432, lng: 77.4354001},
        {lat: 28.6707214, lng: 77.4334270},
        {lat: 28.6695674, lng: 77.4265163},
        {lat: 28.6696689, lng: 77.4265052},
        {lat: 28.6733651, lng: 77.4430692},
        {lat: 28.6737519, lng: 77.4429944},
        {lat: 28.6740493, lng: 77.4429626},
        {lat: 28.6754751, lng: 77.4425713},
        {lat: 28.6676614, lng: 77.4290214},
        {lat: 28.6675485, lng: 77.4273665},
        {lat: 28.669957, lng: 77.431754},
        {lat: 28.668975, lng: 77.432054},
        {lat: 28.66819, lng: 77.432332},
        {lat: 28.666023, lng: 77.433521},
        {lat: 28.665319, lng: 77.433852},
        {lat: 28.664172, lng: 77.434386},
        {lat: 28.663109, lng: 77.434857},
        {lat: 28.662789, lng: 77.435217},
        {lat: 28.661489, lng: 77.435542},
        {lat: 28.659875, lng: 77.435756},
        {lat: 28.657659, lng: 77.434879},
        {lat: 28.6650903, lng: 77.455809},
        {lat: 28.6625591, lng: 77.4621732},
        {lat: 28.6624664, lng: 77.4621041},
        {lat: 28.662228, lng: 77.462863},
        {lat: 28.660013, lng: 77.465962},
        {lat: 28.6589961, lng: 77.4672889},
        {lat: 28.658889, lng: 77.4671946},
        {lat: 28.647186, lng: 77.44578},
        {lat: 28.647782, lng: 77.444806},
        {lat: 28.647887, lng: 77.444905},
        {lat: 28.649038, lng: 77.443181},
        {lat: 28.651482, lng: 77.43973},
        {lat: 28.653684, lng: 77.436644},
        {lat: 28.654753, lng: 77.435084},
        {lat: 28.655983, lng: 77.433325},
        {lat: 28.6568593, lng: 77.4321415},
        {lat: 28.6577404, lng: 77.430892},
        {lat: 28.6597278, lng: 77.4280974},
        {lat: 28.6706658, lng: 77.4149831},
        {lat: 28.6727632, lng: 77.4069683},
        {lat: 28.67312, lng: 77.4062585},
        {lat: 28.676807, lng: 77.3918759},
        {lat: 28.6784319, lng: 77.3865805},
        {lat: 28.6779715, lng: 77.3884973},
        {lat: 28.67755, lng: 77.3899839},
        {lat: 28.6743781, lng: 77.401846},
        {lat: 28.6738745, lng: 77.4037004},
        {lat: 28.67284, lng: 77.4074226},
        {lat: 28.672345, lng: 77.409681},
        {lat: 28.6721493, lng: 77.410478},
        {lat: 28.6718569, lng: 77.4114681},
        {lat: 28.675918, lng: 77.418503},
        {lat: 28.6770641, lng: 77.420316},
        {lat: 28.678621, lng: 77.422418},
        {lat: 28.6797252, lng: 77.4239189},
        {lat: 28.6808859, lng: 77.4252781},
        {lat: 28.683349, lng: 77.428079}
        ];
      */
        var locations = [];
		var locID = [];
		//the above var location is javascript var and the below one comes from djago code.bad names. confusing. gotta change
        {% for location in locations %}
        locations.push({
          lat: {{ location.lat }},
          lng: {{ location.lng }},
		  //id: {{ location.id }}
        });
		locID.push({{ location.id }});
		
        {% endfor %}
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 28.683349, lng: 77.428079 },
          zoom: 12
        });
        var markerGroup = locations.map(function(location, i) {
          return new google.maps.Marker({
            position: location,
            map: map,
            title: "OMOADS Site",
            icon: "{% static 'resources/images/marker3.png' %}"
			
          });
        });
        // var marker = new google.maps.Marker({
        //   position: locations[0],
        //   map: map,                     // required
        //   //label: "Big Poster"
        //   });
        //var markerCluster = new MarkerClusterer(map, markerGroup,
          //  {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
        for (var i = 0; i < locations.length; i++) {
			markerGroup[i].id_try = locID[i];
			markerGroup[i].addListener('click', function() {
            // infowindow.setContent(this.content);
            // infowindow.open(map, this);
            // console.log("hey popups!");
			console.log(this.id_try);
			$.ajax({
				  type: "POST",
				  url: "{% url 'ham_honge_kamiyab' %}",
				  data: {
					"csrfmiddlewaretoken": "{{ csrf_token }}",
					"id_point":String(this.id_try)
					
				  },
				  success: function(data){
				  //set values according to id here
				  
				  //#################################################################################################################
				  //heere chaasifhsklgsalgjsalgjaslkgjsalkg
				  
				  $('#panelID').text(data["id"])
				  $('#price').text(data["cost"])
				  $('#MapLoc').text(data["lat"] + " / " + data["long"])
				  $('#dimensions').text(data["dim"])
          $('#landmark').text(data["landmark"])
				  },
				  error: function(){
					alert("Error! Something wrong. Please try again later")
				  },
				});

			
			
            $('#myModal').modal('show');
          });
        }
        // Create the search box and link it to the UI element.
        var input = document.getElementById('pac-input');
        var searchBox = new google.maps.places.SearchBox(input);
        //map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
        // Bias the SearchBox results towards current map's viewport.
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });
        var markers = [];
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();
          if (places.length == 0) {
            return;
          }
          // Clear out the old markers.
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];
          // For each place, get the icon, name and location.
          var bounds = new google.maps.LatLngBounds();
          places.forEach(function(place) {
            if (!place.geometry) {
              console.log("Returned place contains no geometry");
              return;
            }
            var icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25)
            };
            // Create a marker for each place.
            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));
            if (place.geometry.viewport) {
              // Only geocodes have viewport.
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        });
		
		var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: 'clusterImage/'});
		
        }
		<script src="markerclusterer.js">
		</script>
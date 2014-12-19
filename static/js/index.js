

movementsVisable = false;
	$(document).ready(function(){
		init();
		resizeColumns();
	});


//Make ajax requests and return data to respective display container
function addArtwork(url, data, container){	
	$.get(url,data).done(function(rsp){	
		console.log(rsp)


		

		if(container == "artworkContainer"){	
			displayArtwork(rsp, container);

		}else{
		  displayData(rsp, container);
		}
	}); 
}



//Parse ajax response and create correct display  
function displayData(data, container){

	if (container == null){
		return;
	}
	var id,name,thumbnailURL,obj,img = null
	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];

		if (obj.id === "" || obj.name === "" || obj.thumbnailURL === ""){
			console.log("look here")
			continue; 
		}
		
		if (obj.hasOwnProperty("id")){
			id = obj.id;
		}

		if (obj.hasOwnProperty("name")){
			name = obj.name;
		}

		if (obj.hasOwnProperty("thumbnailURL")){
			thumbnailURL = obj.thumbnailURL;
		}

		if (obj.hasOwnProperty("numArtwork")){
			numArtwork = obj.numArtwork;

		}
		if (obj.hasOwnProperty("numArtist")){
			numArtist = obj.numArtist;

		}

//Display ind Artist representative image and stats. 
		if(obj.hasOwnProperty("numImgs") && obj.hasOwnProperty("dates")){
				if(obj.numImgs == 0){
					continue;
				}	
			numImgs = obj.numImgs;
			dates = obj.dates;

			var imgContainer = document.createElement('div');
			$(imgContainer).addClass('imgContainer');
		
			var img = $(new Image()).attr({
				"src" : thumbnailURL,
				"data-id" : id,
				"data-name" : name,
				"numImgs" : numImgs,
				"dates" : dates,
				"class" : "artist_img",
			});

			var overlay = document.createElement('div');
			$(overlay).addClass('stats_overlay');

				if(numImgs == 1){
					$(overlay).append("<p>" 
						+ img.attr("data-name")
						+ "</p>"+"<div>" 
						+ img.attr("dates") 
						+ "<br>" 
						+ img.attr("numImgs") +
					    " " + "image" + "</div>");
				}else{
					$(overlay).append("<p>"
						+img.attr("data-name")
						+"</p>"+"<div>" 
						+ img.attr("dates") 
						+ "<br>" 
						+ img.attr("numImgs") 
						+ " " + "images" + "</div>");
				}

			$(imgContainer).append(img).append(overlay);
			
			
		}else{

//Display movement and people in movement
			var imgContainer = document.createElement('figure');

			$(imgContainer).addClass('imgContainer');

			var img = $(new Image()).attr({
				"src" : thumbnailURL,
				"data-id" : id,
				"data-name" : name,
				"class" : "movement_img",
				"numArtwork" : numArtwork,
				"numArtist" : numArtist
			});
			console.log(img)

			var overlay = document.createElement('div');
			$(overlay).addClass('stats_overlay');

				if(numArtist == 1){
					$(overlay).append("<p>"+img.attr("data-name") +"</p>" 
									+ "<div>" + img.attr("numArtist") + " " + "artist" + "</div>");
				}else{
					$(overlay).append("<p>"+img.attr("data-name")+"</p>" 
									+ "<div>" + img.attr("numArtist") + " " + "artists" + "</div>");
				}

			$(imgContainer).append(img).append(overlay);
		}
		$('#'+container).append(imgContainer);
		setequalHeight();
	}
	
}


//Parse ajax response specific to individual artworks
function displayArtwork(data, container){
	if (container == null){
		return;
	}
	var obj,id,thumbnailURL,artist,title,year,medium,dimensions,img = null;

	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];

		if (thumbnailURL == ""){
			continue; 
		}

		if(obj.hasOwnProperty("id")){
			id = obj.id;
		}

		if(obj.hasOwnProperty("thumbnailURL")){
			thumbnailURL = obj.thumbnailURL;
		}

		if(obj.hasOwnProperty("artist")){
			artist = obj.artist;
		}

		if(obj.hasOwnProperty("title")){
			title = obj.title;
		}

		if(obj.hasOwnProperty("year")){
			year = obj.year;
		}
		if(obj.hasOwnProperty("medium")){
			medium = obj.medium;
		}
		if(obj.hasOwnProperty("dimensions")){
			dimensions = obj.dimensions;
		}

		var imgContainer = document.createElement('figure');
		$(imgContainer).addClass('large_imgContainer');


		var img = $(new Image()).attr({
			"src" : thumbnailURL,
			"data-id" : id,
			"artist" : artist,
			"title" : title,
			"year" : year,
			"medium" : medium,
			"class" : "artwork_img",
			"dimensions" : dimensions
		});

		var caption = document.createElement("figcaption");
		caption.innerHTML = img.attr("artist") 
							+ "<br>" 
							+ img.attr("title") 
							+ "<br>"+ img.attr("year") 
							+ "<br>" + img.attr("medium") 
							+ "<br>" + img.attr("dimensions")


		$(imgContainer).append(img).append(caption);
		$('#'+container).append(imgContainer);
		setequalHeight();
	}
}

//Resize columns on browser re-size
function resizeColumns(){

	$( window ).resize(function(){
		setequalHeight();

 	});
}



//Resize columns on image load
function setequalHeight(){

	$('.fan').each(function(){
		$(this).height(window.innerHeight-25);
	})
    
}


//Set up inital event handlers for display collumns
function init(){

		$('.overlay').click(function(evt){

				$("#columnWrapper>li").css({
					"position":"absolute",
					"width":"100%"
				});

				$("#logo").css({
					"width": "300px",
					"padding-left": "5%",
					"padding-top":"10px",
				});

				$("#intro").remove();

				$('#era').css({
					"display": "block"
				});

				$('#columnWrapper>li#eraColumn').css({
					"padding":"0",
					"height": "auto"
				});

				$('#columnWrapper>li#eraColumn>div').addClass('fan');

				$("#columnWrapper,#columnWrapper>li>ul,#columnWrapper>li>div>ul").css({
					"height": "auto"
				});

			setequalHeight();

			var era = $(this).prev().attr("data-era");
			transitionToMovements(era);
			addArtwork("/api/movements", {"data":era}, "movementContainer");

			var display_era = $(this).prev().attr("data-name");
			$('#breadcrumbs').empty()
			$('#breadcrumbs').append("<span>"+ display_era+ "</span>"); 
		
		});

		$('#closeMovements,#closeArtists,#closeArtwork').click(function(evt){
			closePane($(this).parent());
		});
	
 		$("#movementColumn").on("click", ".fan .stats_overlay", function(){
 		
 			var movement = $(this).prev().attr("data-id")
 			transitionToArtists(movement);
 			addArtwork("/api/artists",{"data":movement}, "artistContainer");

 			var display_movement = $(this).prev().attr("data-name");

 			if ( $('#breadcrumbs').children().length > 1 ){
 				$('#breadcrumbs span:last-child')[0].remove();
    			}

 			$('#breadcrumbs').append("<span>"+ display_movement +"</span>");
 		});


 		$("#artistColumn").on("click", ".fan .stats_overlay", function(){ 
 			var artist = $(this).prev().attr("data-id");
 			console.log(artist);
 		 	transitionToArtwork(artist);
 		 	addArtwork("/api/artwork",{data:$(this).prev().attr("data-id")}, "artworkContainer");

 		 	var display_artist = $(this).prev().attr("data-name");

 		 	if ( $('#breadcrumbs').children().length > 2 ){
 				$('#breadcrumbs span:last-child')[0].remove();
    			}

 			$('#breadcrumbs').append("<span>"+ display_artist+"</span>") ;
 		});
 
 	}


//Close current display windows, empty content
function closePane(pane){

		var paneToExpand = pane.prev();
		var paneToExpand2 = pane;

		$('#breadcrumbs span:last-child')[0].remove();

		pane.find(".fan").empty();
		switch (paneToExpand.attr("id"))
		{
			case ("eraColumn"):
				transitionToEras(pane);
				break;
			default:
				transitionToPrev(paneToExpand2);
				transitionToPrev(paneToExpand);
		}
}


//Close current display windows move to inital display 
function transitionToEras(pane){

		$("#eraColumn").animate({
			"width": "100%"
		},250,function(){
			$('#breadcrumbs span').remove();
			movementsVisable = false;
		});
		pane.children("div").animate({
			"marginLeft": "20%"
		});
		pane.animate({
			"width": "100%"
		},250,function(){

		});
}


//Expand previous display window reset CSS attributes 
function transitionToPrev(paneToExpand){

		paneToExpand.prev().animate({
			"width": "20%"
		},250,function()
		{
			
		});
		paneToExpand.prev().find(".imgContainer>img").css({
			"width": "70%"
		});
		paneToExpand.children("div").animate({
			"marginLeft": "20%"
		});
		paneToExpand.animate({
			"width": "100%"
		},250,function()
		{
			
		});
		paneToExpand.find(".imgContainer").css({
			"margin-left":"5%",
		    "margin-right":"17%",
		    "margin-top":"5%",
		});
		paneToExpand.find(".imgContainer>img").css({
			"width": "150%"
		});
		paneToExpand.find(".stats_overlay").css({
			"width": "156%",
			"left": "0%"
		});
		paneToExpand.find(".stats_overlay>p").css({
			"font-size":"2.5em",
		});
		paneToExpand.find(".stats_overlay>div").css({
			"font-size":"1.5em",
		});
}



//Minimize era display set attributes for movement display
function transitionToMovements(era){

		$("#eraColumn").animate({
			"width": "20%"
		},250,function()
		{
			movementsVisable = true;
		});
		$("#columnWrapper>li#movementColumn").css({
			"display" : "block"
		});
		$("#columnWrapper>li#artistColumn").css({
			"display" : "block"
		});
		$("#columnWrapper>li#artworkColumn").css({
			"display" : "block"
		});
		$(".fan").css({
			"overflow" : "scroll"
		});
		$("#closeArtwork>img ").css({
			"display" : "block"
		})
}


//Minimize movement display set attributes for artists display
function transitionToArtists(movement){

		$("#eraColumn").animate({
			"width": "0%"
		},250,function()
		{
			
		});
		$("#movementColumn>div").animate({
			"marginLeft": "0%"
		});
		$("#movementColumn").animate({
			"width": "20%"
		},250,function()
		{
		});
		$("#movementColumn .imgContainer").css({
			"margin-top": "5%",
			
		});
		$("#movementColumn .imgContainer>img").css({
			"width": "70%",
			
		});
		$("#movementColumn .stats_overlay").css({
			"width": "80%",
			"left":"10%",
		});
		$("#movementColumn .stats_overlay>*").css({
			"font-size":"18px"
		});
}


//Minimize artist display set attributes for artwork display
function transitionToArtwork(artist){

		$("#movementColumn").animate({
			"width" : "0%"
		},250,function()
		{
			
		});
		$("#artistColumn>div").animate({
			"marginLeft" : "0%"
	
		});
		$("#artistColumn").animate({
			"width" : "20%"
		},250,function()
		{
		});
		$("#artistColumn .imgContainer").css({
			"margin-top": "5%",
			
		});
		$("#artistColumn .imgContainer>img").css({
			"width": "70%",
			
		});
		$("#artistColumn .stats_overlay").css({
			"width": "80%",
			"left":"10%"
		});
		$("#artistColumn .stats_overlay>*").css({
			"font-size":"18px"
		});
			
}
		








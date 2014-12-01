
movementsVisable = false;
	$(document).ready(function()
	{
		init();
	});

/**
 * Make ajax requests and return data to respective display container
 *
 * @param url String API URL
 * @param data Object Data ID object to pass to API
 * @param container String Where to place API response
 *
 * @return null
 */
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

function displayData(data, container){

	if (container == null){
		return;
	}
	var id,name,thumbnailURL,obj,img = null;

	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];
		
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

		if (id == "" || name == "" || thumbnailURL == ""){
			//possible optimiztion move this to the top
			continue; 
		}
		


//ARTISTS 
		if(obj.hasOwnProperty("numImgs") && obj.hasOwnProperty("dates")){
			numImgs = obj.numImgs;
			dates = obj.dates;

			var imgContainer = document.createElement('div');
			$(imgContainer).addClass('imgContainer');
			// possibly dont need to set all as attributes
			var img = $(new Image()).attr({
				"src" : thumbnailURL,
				"data-id" : id,
				"data-name" : name,
				"numImgs" : numImgs,
				"dates" : dates,
				"class" : "artist_img",
			});

			var overlay = document.createElement('div');
			$(overlay).addClass('overlay');

				if(numImgs == 1){
					$(overlay).append("<p>" 
						+ img.attr("data-name")
						+ "</p>"+"<div>" + img.attr("dates") + "<br>" + img.attr("numImgs") + " " + "image" + "</div>");
				}else{
					$(overlay).append("<p>"+img.attr("data-name")+"</p>"+"<div>" + img.attr("dates") + "<br>" + img.attr("numImgs") + " " + "images" + "</div>");
				}

			$(imgContainer).append(img).append(overlay);
			
			
		} else {
//MOVEMENTS 
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

			var overlay = document.createElement('div');
			$(overlay).addClass('overlay');

			// var icon = $(new Image()).attr({
			// 	"src" : "../static/img/expand_icon.png"
			// });
				if(numArtist == 1){
					$(overlay).append("<p>"+img.attr("data-name")+"</p>" + "<div>" + img.attr("numArtist") + " " + "artist" + "</div>");
				}else{
					$(overlay).append("<p>"+img.attr("data-name")+"</p>" + "<div>" + img.attr("numArtist") + " " + "artists" + "</div>");
				}

			$(imgContainer).append(img).append(overlay);
		}
		$('#'+container).append(imgContainer);
		setequalHeight();
	}
	
}

function displayArtwork(data, container){
	if (container == null){
		return;
	}
	var obj,id,thumbnailURL,artist,title,year,medium,dimensions,img = null;

	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];

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

// possibly dont need to set all as attributes
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
		caption.innerHTML = img.attr("artist") + "<br>" + img.attr("title") + "<br>"+ img.attr("year") + "<br>" + img.attr("medium") + "<br>" + img.attr("dimensions")

// .append("<h4>"+img.attr("data-name")+" "+img.attr("data-id")+"<h4>");


		$(imgContainer).append(img).append(caption);
		$('#'+container).append(imgContainer);
		setequalHeight();
	}
}


// function resizeColumns(){
// 	$( window ).resize(function() {
// 		$('.fan').each(function(){
// 		$(this).height(window.innerHeight-25);
// 	    })
//  	});
// }


function setequalHeight(){
	$('.fan').each(function(){
		$(this).height(window.innerHeight-25);
	})
    // getting the height of browser window, 
    // styling scroll bar
    // $(this).height(window.innerHeight-25);
}


function init()
	{
		$('li#eraColumn>div>ul>li>img').click(function(evt)
		{	
				$("#columnWrapper>li").css({
					"position":"absolute",
					"width":"100%"
				});
				$("#logo").css({
					"width": "200px",
					"padding-left": "5px",
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
				$("#columnWrapper,#columnWrapper>li>ul,#columnWrapper>li>div>ul").css({
					"height": "auto"
				});
			setequalHeight();
			var era = $(this).attr("data-era");
			transitionToMovements(era);
			
			addArtwork("/api/movements", {"data":era}, "movementContainer");
		
		});
		$('#closeMovements,#closeArtists,#closeArtwork').click(function(evt)
		{
			closePane($(this).parent());
		});
 		$("#movementColumn").on("click", ".fan .overlay", function()
 		{
 			var movement = $(this).prev().attr("data-id")
 			transitionToArtists(movement);
 			addArtwork("/api/artists",{"data":movement}, "artistContainer");
 		});
 		$("#artistColumn").on("click", ".fan .overlay", function()	 			
 		{ 
 			var artist = $(this).prev().attr("data-id");
 			console.log(artist);
 		 	transitionToArtwork(artist);
 		 	addArtwork("/api/artwork",{data:$(this).prev().attr("data-id")}, "artworkContainer");
 		});
 
 	}

function closePane(pane){

		var paneToExpand = pane.prev();
		var paneToExpand2 = pane;
		// console.log(paneToExpand.attr("id"));
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

// function updateNav(container, data){


// }


function transitionToEras(pane){

		$("#eraColumn").animate({
			"width": "100%"
		},250,function()
		{
			movementsVisable = false;
		});
		pane.children("div").animate({
			"marginLeft": "20%"
		});
		pane.animate({
			"width": "100%"
		},250,function()
		{
			
		});
}

function transitionToPrev(paneToExpand){

		console.log(paneToExpand.attr("id"));
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
		paneToExpand.find(".overlay").css({
			"width": "156%",
			"left": "0%"
		});
		paneToExpand.find(".overlay>p").css({
			"font-size":"2.5em",
		});
		paneToExpand.find(".overlay>div").css({
			"font-size":"1.5em",
		});
}

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
		$("#movementColumn .overlay").css({
			"width": "80%",
			"left":"10%",
		});
		$("#movementColumn .overlay>*").css({
			"font-size":"18px"
		});
}
	
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
		$("#artistColumn .overlay").css({
			"width": "80%",
			"left":"10%"
		});
		$("#artistColumn .overlay>*").css({
			"font-size":"18px"
		});
			
}
		








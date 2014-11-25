
movementsVisable = false;
	$(document).ready(function()
	{
		init();
	});

function addArtwork(url, data, container){	
	$.get(url,data).done(function(rsp){	
		console.log(rsp)
		displayData(rsp, container);
	}); 
}

function displayData(data, container){
	// console.log("debug1")
	if (container == null){
		return;
	}
	var id,name,thumbnailURL,obj,img = null;

	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];
		// console.log("debug1")
		// console.log(obj);
		if(obj.hasOwnProperty("id")){
			id = obj.id;
		}

		if(obj.hasOwnProperty("name")){
			name = obj.name;
		}

		if(obj.hasOwnProperty("thumbnailURL")){
			thumbnailURL = obj.thumbnailURL;
		}

		if (id == "" || name == "" || thumbnailURL == ""){
			//move on to next obj if this one is empty
			continue; 
		}

		if(obj.hasOwnProperty("numImgs") && obj.hasOwnProperty("dates")) {
			numImgs = obj.numImgs;
			dates = obj.dates;
			var img = $(new Image()).attr({
			"src" : thumbnailURL,
			"data-id" : id,
			"data-name" : name,
			"numImgs" : numImgs,
			"dates" : dates,
			"id" : "artistImg",
			});
			img.append("<div id='overlay'></div>");
			var imgHeight = img.height()
			var imgWidth = img.width()
			$("overlay").height(imgHeight)
			$("overlay").width(imgHeight)
			$("#overlay").on("mouseover", function(){
	 			console.log( "I hovered")
	 		});

		} else {
			var img = $(new Image()).attr({
				"src" : thumbnailURL,
				"data-id" : id,
				"data-name" : name,
			});
		}
		$('#'+container).append(img);
		setequalHeight();
	}
	// call masonry for image layout 

}				

// //new images are made on the page with the correct attributes
// 		var img = $(new Image()).attr({
// 			"src" : thumbnailURL,
// 			"data-id" : id,
// 			"data-name" : name,
// 			// "numImgs" : numImgs,
// 			// "dates" : dates,
// 		});
// 		$('#'+container).append(img);
// // 		setequalHeight();		
// 	}
// 	// call masonry for image layout 

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
				setequalHeight();
				var era = $(this).attr("data-era");
				transitionToMovements(era);
				
				addArtwork("/api/movements", {"data":era}, "movementContainer")
			
			});

			$('#closeMovements,#closeArtists').click(function(evt)
			{
				closePane($(this).parent());
			});
			
// SET UP EVENT HANDLERS

	 		$("#movementColumn").on("click", ".fan img", function()
	 		{
	 			var movement = $(this).attr("data-id");
	 			console.log(movement)
	 			transitionToArtists(movement);

	 			addArtwork("/api/artists",{"data":movement}, "artistContainer");
	 									   // {data:$(this).attr("data-id")}
	 									   // {"data":movement}
	 		});






	 		// $("#artistImg").on("mouseover", function(){

	 		// 	console.log( "I hovered")
	 		// 	var imgHeight = $(this).height();
	 		// 	var imgWidth = $(this).width();

	 		// 	$(this).append("<div id='overlay'></div>");

	 		// 	$("#overlay")
	 		// 		.height(imgHeight)
	 		// 		.width(imgWidth)
	 		// 		.css({
	 		// 			"opacity" : 0.4,
	 		// 			"position" : "absolute",
	 		// 			"top":0,
	 		// 			"left":0,
	 		// 			"color" : "black", 
	 		// 			"z-index": 85
	 		// 		}); 
	 		// });


	 		// {data:$(this).attr("data-id")}

	 		// $("#artistColumn").on("click", ".fan img", function()
	 		// {
 			//  	transitionToArtwork();
 			//  	addArtwork("/api/artwork",{data:$(this).attr("data-id")}, "artworkContainer");
	 		// }
 	
	 		$("#artworkColumn").on("click", ".fan img", function()
	 		{
	 			console.log("artwork clicked");
	 		});
 	
 	
	 	}

	
	function closePane(pane)
		{
			var paneToExpand = pane.prev();
			// console.log(paneToExpand.attr("id"));

			pane.find(".fan").empty();

			switch (paneToExpand.attr("id"))
			{
				case ("eraColumn"):
					transitionToEras(pane);
					break;
				default:
					transitionToPrev(paneToExpand);
			}
		}

	function transitionToEras(pane)
		{
			// console.log(pane.attr("id"));
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

	function transitionToPrev(paneToExpand)
		{
			console.log(paneToExpand.attr("id"));
			paneToExpand.prev().animate({
				"width": "20%"
			},250,function()
			{
				
			});

			paneToExpand.children("div").animate({
				"marginLeft": "20%"
			});

			paneToExpand.animate({
				"width": "100%"
			},250,function()
			{
				
			});
		}

	function transitionToMovements(era)
		{
			$("#eraColumn").animate({
				"width": "20%"
			},250,function()
			{
				movementsVisable = true;
			});
		}

	function transitionToArtists(movement)
		{
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
		}
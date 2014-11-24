
movementsVisable = false;
	$(document).ready(function()
	{
		init();
	});

function addArtwork(url, data, container){	
	$.get(url,data).done(function(rsp){	
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

		if (id == null || name == null | thumbnailURL == null){
			//move on to next obj if this one is empty
			continue; 
		}
//new images are made on the page with the correct attributes
		var img = $(new Image()).attr({
			"src" : thumbnailURL,
			"data-id" : id,
			"data-name" : name,
		});
		$('#'+container).append(img);		
	}
	// call masonry for image layout 

}


// function setequalHeight(){
// 	// var eraColumn = $('#eraColumn').height();
// 	// console.log(eraColumn);
// 	// var movementColumn = $('#movementColumn').height();
// 	// console.log(movementColumn);
// 	// var artworkColumn = $('#artworkColumn').height();
// 	// console.log(artworkColumn);
// 	var highestBox = 0;

// 	$('.fan').each(function(){
// 		// console.log($(this).height());
// 			if($(this).height() > highestBox){
// 				highestBox = $(this).height();
// 				// console.log(highestBox);
// 			}
// 	});
// 	$('.fan').each(function(){
// 		$(this).height(highestBox);

// 	})

// }

	function init()
		{
			$('li#eraColumn>div>ul>li>img').click(function(evt)
			{
				// setequalHeight();
				var era = $(this).attr("data-era");
				transitionToMovements(era);
				
				addArtwork("/api/movements", {"data":era}, "movementContainer")
			
			});

			$('#closeMovements,#closeArtwork').click(function(evt)
			{
				closePane($(this).parent());
			});
			
// SET UP EVENT HANDLERS

	 		$("#movementColumn").on("click", ".fan img", function()
	 		{
	 			transitionToArtwork();
	 			addArtwork("/api/artwork",{data:$(this).attr("data-id")}, "artworkContainer");
	 		});

	 		// $("#artistColumn").on("click", ".fan img", function()
	 		// {
 			//  	transitionToArtwork();
 			//  	addArtwork("/api/artist",{data:$(this).attr("data-id")}, "artworkContainer");
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

	function transitionToArtwork(movement)
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
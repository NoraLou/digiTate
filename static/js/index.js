
movementsVisable = false;
	$(document).ready(function()
	{
		init();
	});

function addArtwork(url, data, container){
	console.log(url,data,container);
	$.get(url,data).done(function(rsp){
		console.log("************************")
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
//the click function only gets set on last item in group : addArtwork gets called with same id over and over
		
		img.click(function(evt)
		{
			// setequalHeight();
			var nextContainer = null;
			switch(container){
				case("movementContainer"):
					nextContainer = "artworkContainer";
					nextUrl = "/api/artwork";
					transitionToArtwork()
					break;
			}
			console.log("debug2 ********************************************")
			console.log(img)
			console.log(obj) 

//the obj being passed as the id is always the last  one in the group... ???? 
			addArtwork(nextUrl,{data:$(this).attr("data-id")},nextContainer);
		});

		$('#'+container).append(img);		
	}
	$('img').load(function(){
		setequalHeight();
	});

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
				// console.log(era);
    //     		console.log(evt);
    //     		console.log(evt.target);
				addArtwork("/api/movements", {"data":era}, "movementContainer")
			
			});

			// $('#movementContainer>img').click(function(evt){
			// 	alert(evt.currentTarget.dataset.id);
			// 	var movement = $(this).attr("data-movement");
			// 	transitionToArtists(movement);
			// });

			$('#closeMovements,#closeArtwork').click(function(evt)
			{
				closePane($(this));
			});
		}

	function closePane(pane)
		{
			var paneToExpand = pane.parent().prev();
			// console.log(paneToExpand.attr("id"));

			switch (paneToExpand.attr("id"))
			{
				case ("eraColumn"):
					transitionToEras(pane.parent());
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
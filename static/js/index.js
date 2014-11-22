
movementsVisable = false;
	$(document).ready(function()
	{
		init();
	});

function addArtwork(url, data, container){
	console.log(url,data,container);
	$.get(url,data).done(function(rsp){
		console.log(rsp)
	//makea ajax call to url getting json back
		displayData(rsp, container);
	}); 
}

function displayData(data, container){
	console.log("debug1")
	if (container == null){
		return;
	}
	var id, name,thumbnailURL,obj,img = null;
	$('#'+container).empty();

	for(var i = 0; i<data.length; i++){
		obj = data[i];
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
//make a new img out of item
		var img = $(new Image()).attr({
			"src" : thumbnailURL,
			"data-id" : id,
			"data-name" : name,
		});
		img.click(function(evt)
		{
			var nextContainer = null;
			switch(container){
				case("movementContainer"):
					nextContainer = "artworkContainer";
					nextUrl = "/api/artwork";
					transitionToArtists()
					break;
			}
		
			addArtwork(nextUrl, {data:id}, nextContainer);
		});
		//once loaded add them to the container
		// console.log(img);
		$('#'+container).append(img);
	}
}	   
	function init()
		{
			$('li#eraColumn>ul>li>img').click(function(evt)
			{
				var era = $(this).attr("data-era");
				transitionToMovements(era);
				console.log(era);
        		console.log(evt);
        		console.log(evt.target);
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
			console.log(paneToExpand.attr("id"));

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
			console.log(pane.attr("id"));
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
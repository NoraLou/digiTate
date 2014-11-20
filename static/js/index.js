
		movementsVisable = false;
		$(document).ready(function()
		{
			init();
      // addArtwork("things");
		});


function addArtwork(evt){
    alert(evt.currentTarget.dataset.era);

    $.get("/test",{ 
        data : evt.currentTarget.dataset.era, 
      })
      	.done(function(data){
	        console.log(data);
	        displayData(data);

      })
      	.fail(function(){
        alert("error")
      });

}

function displayData(data){
	//for array in data
	for(var a = 0; a<data.length; a++){
		var item = data[a]
		
		if(item.hasOwnProperty('thumbnailURL'))
			console.log(item['thumbnailURL']);
			var image_url = item['thumbnailURL'];
			$(new Image()).attr('src', '' + image_url).appendTo($('li#movementColumn>div>ul>li')).fadeIn();
		   
	}
}

// funtion handledoubleClick(evt)
// if user clicks twice on an image durint the session ;images will not load twice!



	function init()
		{
			$('li#eraColumn>ul>li>img').click(function(evt)
			{
				var era = $(this).attr("data-era");
				transitionToMovements(era);
        		console.log(evt);
        		addArtwork(evt);

			});

			$('li#movementColumn>div>ul>li>img').click(function(evt)
			{
				var movement = $(this).attr("data-movement");
				transitionToArtists(movement);
			});

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
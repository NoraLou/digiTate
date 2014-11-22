function addArtwork(url,data,container)
{
	$.get(url, data).done(function(rsp)
	{
		displayData(rsp, container);
	});
}

function displayData(data, container)
{
	if (container == null)
	{
		return;
	}
	
	var id,name,thumbnailURL,obj,img = null;

	for (var i = 0; i < data.length; i++)
	{
		id,name,thumbnailURL,img = null;
		obj = data[i];

		if (obj.hasownProperty("id"))
		{
			id = obj.id;
		}

		if (obj.hasownProperty("name"))
		{
			name = obj.name;
		}

		if (obj.hasownProperty("thumbnailURL"))
		{
			thumbnailURL = obj.thumbnailURL;
		}

		if (id == null || name == null | thumbnailURL == null)
		{
			continue;
		}

		img = $("<img />").attr({
			"src": thumbnailURL
		}).click(function(evt)
		{
			var nextContainer = null;
			switch (container)
			{
				case ("eraContainer"):
					nextContainer = "movementContainer";
					break;
				case ("movementContainer"):
					nextContainer = "artistContainer";
					break;
			}

			addArtwork(nextUrl, {dataName: id}, nextContainer);
		});

		img.appendTo(container);
	}
}
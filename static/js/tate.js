$(document).ready(function () {	

	$("#movement_img").click(movementImages);
});



function movementImages(evt) {
    evt.preventDefault();

}
    // console.log("clicked on reset button");
    // $.post(
    //     "/api/wall/reset",
    //     {},
    //      function(data){
    //         console.log('handleClearButton got: ');
    //         console.log(data);
    //         if (data.result == 'OK') {
    //             //alert("GOT THIS FAR!");
    //             $("#message-container").empty();
    //             loadmessages();
    //         }
    //      }
    //     );


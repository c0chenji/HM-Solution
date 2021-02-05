$(document).ready(function() {

    $('#cameraID').change(function(eventObject) {
      if ($(this).val() == "1") {
        $('.IPcamera').show();

      } else {
      	$('.IPcamera').hide();
      	window.location = $(this).val(); 
      }
    }).change();

  });








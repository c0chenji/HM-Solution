$(document).ready(function() {

    $('#USBID').change(function(eventObject) {
      if ($(this).val() == "2") {
        $('.USBcamera').show(); 

      } else {
         $('.USBcamera').hide();
         window.location = $(this).val(); 
      }
    }).change();

  });








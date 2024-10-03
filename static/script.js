

$(document).ready(function () {
    

// default view of filter card - hide
   $("#filter-slide").hide();

// Toggle on filter option
   $("#filterBtn").click(function(){
      $("#filter-slide").slideToggle("slow");
   });

   //Turn on active on active pages when click
   document.querySelectorAll(".nav-link").forEach((link) => {
      if (link.href === window.location.href) {
          link.classList.add("active");
          link.setAttribute("aria-current", "page");
      }
  });

//  Spinner script
  $('#spinner').hide();


  $('#submitbtnget').click(function(){
      $('#spinner').show();
  }) 


  $('#submitbtnadd').click(function(){
   $('#spinner').show();
   }) 

  
// Validation on get item input requiring valid data

  $('#id_form-0-quantity').on('input', function() {

      if ( 
            !$('#id_form-0-member').val() ||
            !$('#id_form-0-site').val() ||
            !$('#id_form-0-floor').val() ||
            !$('#id_form-0-purpose').val() > 0 ) {

         alert('Please input your NAME, CLIENT, and DEPARTMENT before submitting this form.')
      
         $('#submitbtnget').prop('disabled', true);

      }
      else{

         $('#submitbtnget').prop('disabled', false);

      }

   });

   // Validation on get item input requiring valid data

   $('#id_form-0-member, #id_form-0-site, #id_form-0-floor, #id_form-0-purpose').on('input', function() {

      if ( 
            !$('#id_form-0-member').val() ||
            !$('#id_form-0-client_name').val() > 0 ) {
      
         $('#submitbtnget').prop('disabled', true);

      }
      else{

         $('#submitbtnget').prop('disabled', false);

      }

   });


});



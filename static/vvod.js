

$(document).ready(function(){
    PPopUpShow();
});
function PopUpShow(){
    $("#popup1").show();
}
function PopUpHide(){
    $("#popup1").hide();
}



function check_vvod(value){
			if (value.replace(/\s/g, '').length === 0 || isNaN(value)) {

			  for(var i=0; i <= 10; i++){
				  var a = document.getElementById('f'+i);
				  if(a.value == value){
					  a.style.borderColor = 'red';
				  }
			  }
			}
			else{
				for(var i=0; i <= 10; i++){
				  var a = document.getElementById('f'+i);
				  if(a.value == value){
					  a.style.borderColor = 'gray';
				  }
			  }
			}
		}
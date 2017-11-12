function updateStrength(event){
	if($(event.target).val().length < 8){
		$(".progress-bar").addClass("weak");
		$(".progress-bar").addClass("bg-danger");
	}
	else{
		$(".progress-bar").removeClass("weak").addClass("intermediate");
		$(".progress-bar").removeClass("bg-danger").addClass("bg-warning");
	}
}

function addHandlers(){
	$("#password").keypress(updateStrength);
}

$(document).ready(function(){
	addHandlers();		
});

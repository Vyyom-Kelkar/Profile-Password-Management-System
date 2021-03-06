/*
	This file creates the password strength bar for the signup page
	Dakota Duncan
*/

function hasLowercase(str){
	var lowercase = /[a-z]/;
	return lowercase.test(str);
}

function hasUppercase(str){
	var uppercase = /[A-Z]/;
	return uppercase.test(str);
}

function hasUppercaseAsFirstLetter(str){
	var firstLetter = str.substring(0,1);
	var restOfStr = str.substring(1);
	if (hasUppercase(firstLetter) && !hasUppercase(restOfStr)){
		return true;
	}
	return false;
}

/*function hasUppercaseAsFirstLetter(str){
	var firstLetter = str.substring(0,1);
	if (hasUppercase(firstLetter)){
		return true;
	}
	return false;
}
*/
function hasSpecial(str){
	var special = /[!@#$%?'&*]/;
	return special.test(str);
}

function hasSpecialAsLastLetter(str){
	var lastLetter = str.substring(str.length-1);
	var restOfStr = str.substring(0,str.length-1);
	if (hasSpecial(lastLetter) && !hasSpecial(restOfStr)){
		return true;
	}
	return false;
}
/*
function hasSpecialAsLastLetter(str){
	var lastLetter = str.substring(str.length-1);
	if (hasSpecial(lastLetter)){
		return true;
	}
	return false;
}
*/
function hasNumeric(str){
	var numeric = /[0-9]/;
	return numeric.test(str);
}

function updateStrength(event){

	input = $(event.target).val();
	var count = 0;
	if (hasNumeric(input)){
		count = count + 1;
	}
	if (hasUppercase(input) && !hasUppercaseAsFirstLetter(input)){
		count = count + 1;
	}

/*	if (hasUppercaseAsFirstLetter(input)){
		var restOfInput = input.substring(1);
		if(hasUppercase(restOfInput)){

			count = count + 1;
		}
	}else if (hasUppercase(input)){
		count = count + 1;
	}
*/
	if (hasLowercase(input)){
		count = count + 1;
	}
	if(hasSpecial(input) && !hasSpecialAsLastLetter(input)){
		count = count + 1;
	}
	
/*	if(hasSpecialAsLastLetter(input)){
		var charBeforeLast = input.sustring(input.length-2, input.length-1);
		if(hasSpecial(charBeforeLast)){

			count = count + 1;
		}
	}else if (hasSpecial(input)){
		count = count + 1;
	}
*/
	if(input.length == 0){
		$(".progress-bar").removeClass("great");
		$(".progress-bar").removeClass("good");
		$(".progress-bar").removeClass("intermediate");
		$(".progress-bar").removeClass("weak");
		$(".progress-bar").removeClass("bg-info");
		$(".progress-bar").removeClass("bg-danger");
		$(".progress-bar").removeClass("bg-success");
		$(".progress-bar").removeClass("bg-warning");
	}
	else if(input.length < 8){
		$(".progress-bar").removeClass("great");
		$(".progress-bar").removeClass("good");
		$(".progress-bar").removeClass("intermediate");
		$(".progress-bar").addClass("weak");
		$(".progress-bar").removeClass("bg-info");
		$(".progress-bar").removeClass("bg-success");
		$(".progress-bar").removeClass("bg-warning");
		$(".progress-bar").addClass("bg-danger");
	}
	else if(count == 4){
		$(".progress-bar").removeClass("weak");
		$(".progress-bar").removeClass("good");
		$(".progress-bar").removeClass("intermediate");
		$(".progress-bar").addClass("great");
		$(".progress-bar").removeClass("bg-info");
		$(".progress-bar").removeClass("bg-danger");
		$(".progress-bar").removeClass("bg-warning");
		$(".progress-bar").addClass("bg-success");
	}
	else if(count == 3){
		$(".progress-bar").removeClass("weak");
		$(".progress-bar").removeClass("great");
		$(".progress-bar").removeClass("intermediate");
		$(".progress-bar").addClass("good");
		$(".progress-bar").removeClass("bg-success");
		$(".progress-bar").removeClass("bg-danger");
		$(".progress-bar").removeClass("bg-warning");
		$(".progress-bar").addClass("bg-info");
	}
	else if(count == 2){
		$(".progress-bar").removeClass("weak");
		$(".progress-bar").removeClass("good");
		$(".progress-bar").removeClass("great");
		$(".progress-bar").addClass("intermediate");
		$(".progress-bar").removeClass("bg-success");
		$(".progress-bar").removeClass("bg-danger");
		$(".progress-bar").removeClass("bg-info");
		$(".progress-bar").addClass("bg-warning");
	}
	else{
		$(".progress-bar").removeClass("great");
		$(".progress-bar").removeClass("good");
		$(".progress-bar").removeClass("intermediate");
		$(".progress-bar").addClass("weak");
		$(".progress-bar").removeClass("bg-success");
		$(".progress-bar").removeClass("bg-warning");
		$(".progress-bar").removeClass("bg-info");
		$(".progress-bar").addClass("bg-danger");
	}
}

function addHandlers(){
	$("#password").keyup(updateStrength);
}

$(document).ready(function(){
	addHandlers();		
});

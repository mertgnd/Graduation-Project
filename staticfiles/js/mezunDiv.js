function ogrenci() {
var mezunDiv = document.all("mezun");
mezunDiv.style.display = "none";
}

function mezun() {
var mezunDiv = document.all("mezun");
mezunDiv.style.display = "block";
}

function changeFunc(){
	var selectBox = document.getElementById("selectBox");
	var selectedValue = selectBox.options[selectBox.selectedIndex].value;
	if (selectedValue == "Çalışmıyorum"){
		var calisiyorumDiv = document.getElementById("calisiyorum");
		calisiyorumDiv.style.display = "none";
	}
	else if (selectedValue == "Çalışıyorum"){
		var calisiyorumDiv = document.getElementById("calisiyorum");
		calisiyorumDiv.style.display = "block";
	}

}

function sehirFunction(){
	var selectBox2 = document.getElementById("selectBox2");
	var selectedValue2 = selectBox2.options[selectBox2.selectedIndex].value;
	if (selectedValue2 == "turkiye"){
		var türkiyeDiv = document.getElementById("turkiye");
		var diğerDiv = document.getElementById("diger");
		türkiyeDiv.style.display = "block";
		diğerDiv.style.display = "none";
	}
	else if (selectedValue2 == "diger"){
		var türkiyeDiv = document.getElementById("turkiye");
		var diğerDiv = document.getElementById("diger");
		türkiyeDiv.style.display = "none";
		diğerDiv.style.display = "block";
	}

}
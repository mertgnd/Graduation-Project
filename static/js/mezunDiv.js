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

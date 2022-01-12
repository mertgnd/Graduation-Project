function ogrenciFormuSecici() {
    var ogrenciFormu = document.getElementById("ogrenciForm");
    var mezunFormu = document.getElementById("mezunForm");
    if (ogrenciFormu.style.display == 'none')
        mezunFormu.style.display = 'none';
        ogrenciFormu.style.display = 'block';
        document.getElementById("ogrencibuton").style.backgroundColor = "lightblue";
        document.getElementById("mezunbuton").style.backgroundColor = "white";
}

function mezunFormuSecici() {
    var ogrenciFormu = document.getElementById("ogrenciForm");
    var mezunFormu = document.getElementById("mezunForm");
    if (mezunFormu.style.display == 'none')
        ogrenciFormu.style.display = 'none';
        mezunFormu.style.display = 'block';
        document.getElementById("mezunbuton").style.backgroundColor = "lightblue";
        document.getElementById("ogrencibuton").style.backgroundColor = "white";
}
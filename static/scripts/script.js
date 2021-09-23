var chbox;
chbox = document.getElementById('cb1');


function kkk(){
	if (chbox.checked) {
		document.getElementById('body').style.background = '#282828';
		document.getElementById("thems").innerHTML = "Dark";
		document.getElementById("thems").style.color = '#f0f0f0';
		document.getElementById("bb1").style.color = '#f0f0f0';
		document.getElementById("bb2").style.color = '#f0f0f0';
		// document.getElementsByClassName("thems").innerHTML = "Dark";
	}
	else {
		document.getElementById('body').style.background = '#f0f0f0';
		document.getElementById("thems").innerHTML = "Light";
		document.getElementById("thems").style.color = '#282828';
		document.getElementById("bb1").style.color = '#282828';
		document.getElementById("bb2").style.color = '#282828';
		// document.getElementsByClassName("thems").innerHTML = "Light";
	}
}
var chbox;
chbox = document.getElementById('cb1');
var colors = {
    "Волки" : "#30324b",
    "Львы" : "orange",
	"Вороны" : "purple",
	"угроза" : "#31814b"
}

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
function draw(h){
	document.getElementById("all_map").innerHTML = '<defs><pattern id="smallGrid" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M 14 0 L 0 0 0 14" fill="none" stroke="gray" stroke-width="0.5"></path></pattern><pattern x="14" id="grid" width="70" height="70" patternUnits="userSpaceOnUse"><rect width="70" height="70" fill="url(#smallGrid)"></rect><path d="M 70 0 L 0 0 0 70" fill="none" stroke="gray" stroke-width="1"></path></pattern></defs>';
	document.getElementById("all_map").innerHTML += '<rect x="14"width="351px" height="351px" fill="url(#grid)" /> ';
	for(let i = 25; i > 0; i--){
		if(i >= 10){
			document.getElementById("all_map").innerHTML += `<text fill="gray" font-size="11" font-family="Verdana" x="-1" y="${14 * (26 - i)}">${i}</text>`;
		}else{
			document.getElementById("all_map").innerHTML += `<text fill="gray" font-size="13" font-family="Verdana" x="0" y="${14 * (26 - i)}">${i}</text>`;
		}	
	}
	for(let i = 1; i <= 25; i++){
		if(i >= 10){
			document.getElementById("all_map").innerHTML += `<text fill="gray" font-size="10" font-family="Verdana" x="${14 * i}" y="${14 * 26}">${i}</text>`;
		}else{
			document.getElementById("all_map").innerHTML += `<text fill="gray" font-size="12" font-family="Verdana" x="${(14 * i) + 3}" y="${14 * 26}">${i}</text>`;
		}	
	}
	for(let hy=0; hy < h.length; hy++){
		for(let hx=0; hx < h[hy].length; hx++){
			var i = h[hy];
			var j = h[hx];
			var y = hy;
			var x = hx + 1;
			if(j != "*" && typeof j === 'string'){
				document.getElementById("all_map").innerHTML += `<rect height="4%" width="4%" y="${14 * y}" x="${14 * x}" stroke-width="1.5" stroke="${colors[j]}" fill="${colors[j]}"/>`;
			}
			if(typeof j  !== 'string' ){
				document.getElementById("all_map").innerHTML += `<rect height="4%" width="2%" y="${14 * y}" x="${14 * x}" stroke-width="1.5" stroke="${colors[j[0]]}" fill="${colors[j[0]]}" />`;
				document.getElementById("all_map").innerHTML +=	`<rect height="4%" width="2%" y="${14 * y}" x="${14 * x + 7}" stroke-width="1.5" stroke="${colors[j[1]]}" fill="${colors[j[1]]}"/>`;
			}
		}
	}
	console.log("update")
}
// function uptd()
// {
// 	$.ajax({
//     type: "get",
//     url: "https://lis.maxar2005.repl.co/update",
//     data: NaN,
//     success: draw
// });
// }
// $(document).ready(function(){  
//     uptd();  
//     setInterval('uptd()',10000);  
// }); 

// show about-inner

var button_h4 = document.querySelectorAll(".questions h4"),
	p = document.querySelectorAll(".questions p");

p[0].style.display = "block";

button_h4[0].onclick = function () {
	if (p[0].style.display === "none") {
		p[0].style.display = "block";
		p[1].style.display = "none";
		p[2].style.display = "none";
		p[3].style.display = "none";
		p[4].style.display = "none";
	} else {
		p[0].style.display = "none";
	}
};

p[1].style.display = "none";
button_h4[1].onclick = function () {
	if (p[1].style.display === "none") {
		p[1].style.display = "block";
		p[0].style.display = "none";
		p[2].style.display = "none";
		p[3].style.display = "none";
		p[4].style.display = "none";
	} else {
		p[1].style.display = "none";
	}
};

p[2].style.display = "none";
button_h4[2].onclick = function () {
	if (p[2].style.display === "none") {
		p[2].style.display = "block";
		p[1].style.display = "none";
		p[0].style.display = "none";
		p[3].style.display = "none";
		p[4].style.display = "none";
	} else {
		p[2].style.display = "none";
	}
};

p[3].style.display = "none";
button_h4[3].onclick = function () {
	if (p[3].style.display === "none") {
		p[3].style.display = "block";
		p[1].style.display = "none";
		p[2].style.display = "none";
		p[0].style.display = "none";
		p[4].style.display = "none";
	} else {
		p[3].style.display = "none";
	}
};

p[4].style.display = "none";
button_h4[4].onclick = function () {
	if (p[4].style.display === "none") {
		p[4].style.display = "block";
		p[1].style.display = "none";
		p[2].style.display = "none";
		p[3].style.display = "none";
		p[0].style.display = "none";
	} else {
		p[4].style.display = "none";
	}
};


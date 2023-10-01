/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
	theme: {
		colors: {
			maincolor: "#e63946",
			secondarycolor: "#1d3557",
			thirdcolor: "#a8dadc",
			fourthcolor: "#f1faee"
		},
		container: {
			center: true,
			padding: "2rem"
		},
		extend: {}
	},
	plugins: [require("flowbite/plugin")]
};

$(document).ready(function() {

	// SPIN UP button pressed
	$("#btn-spinup").click(function() {
		console.log("SPIN UP");
		var start = Date.now();
		$.get("/spinup", function(data) {
			console.log(parseInt(data) - start);
		});
	});

	// RAISE button pressed
	$("#btn-raise").click(function() {
		console.log("RAISE");
	});

	// LOWER button pressed
	$("#btn-lower").click(function() {
		console.log("LOWER");
	});

	// FIRE button pressed
	$("#btn-fire").click(function() {
		console.log("FIRE");
	});

	// HALT button pressed
	$("#btn-halt").click(function() {
		console.log("HALT");
	});
});


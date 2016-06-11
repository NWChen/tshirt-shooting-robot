function motion(event) {
	gyro.startTracking(function(o) {
		document.getElementById("x").innerHTML = o.alpha;
		document.getElementById("y").innerHTML = o.beta;
		document.getElementById("z").innerHTML = o.gamma;		
	});
	/*
		console.log(event.accelerationIncludingGravity.x + ", " +
			event.accelerationIncludingGravity.y + ", " + 
			event.accelerationIncludingGravity.z);
		document.getElementById("x").innerHTML = 
			Math.round(event.accelerationIncludingGravity.x*10);
		document.getElementById("y").innerHTML = 
			Math.round(event.accelerationIncludingGravity.y*10);
		document.getElementById("z").innerHTML = 
			Math.round(event.accelerationIncludingGravity.z*10);
			*/
}

if(window.DeviceMotionEvent) {
	window.addEventListener("devicemotion", motion, false);
} else {
	console.log("Unsupported event");
}
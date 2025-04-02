

difference() {
	color(alpha = 1.0000000000, c = [0.2820000000, 0.2820000000, 1]) {
		cube(size = [50, 80, 1]);
	}
	translate(v = [30, 40, 0]) {
		rotate(a = [180, 0, 90]) {
			color(alpha = 1.0000000000, c = [0, 1, 0.2120000000]) {
				text(font = "Arial", halign = "center", size = 10, text = "A.R et M.J", valign = "center");
			}
		}
	}
	translate(v = [10, 40, 0]) {
		rotate(a = [180, 0, 90]) {
			color(alpha = 1.0000000000, c = [0, 1, 0.2120000000]) {
				text(font = "Arial", halign = "center", size = 10, text = "IFT 2125", valign = "center");
			}
		}
	}
}
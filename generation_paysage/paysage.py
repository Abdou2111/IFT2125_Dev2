from solid import *
from solid.utils import color


plaque = color((0.282, 0.282, 1))(cube([50, 80, 1]))
initials = translate((30, 40, 0))(
    rotate((180, 0, 90))(
        color((0, 1, 0.212))(
            text("A.R et M.J", size=10, font="Arial", valign="center", halign="center")
        )
    )
)
sigle = translate((10, 40, 0))(
    rotate((180, 0, 90))(
        color((0, 1, 0.212))(
            text("IFT 2125", size=10, font="Arial", valign="center", halign="center")
        )
    )
)
output = difference()(
    plaque,
    initials,
    sigle
)

scad_code = scad_render(initials)
scad_code2 = scad_render(plaque)
output = scad_render(output)

with open("paysage.scad", "w") as file:
    #file.write(scad_code)
    #file.write(scad_code2)
    file.write(output)


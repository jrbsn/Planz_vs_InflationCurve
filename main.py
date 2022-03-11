from PIL import Image

# basic inputs: all imperial units
diameter = 4
vls = 131
aird = 0.002 # 40,000 ft: .000585189
weight = 11
cd = 2.2
cfc = 8  # canopy fill constant
avt = 2  # area vs time relationship
# preliminary calculations
mass = weight / 32.174
tf = (diameter * cfc) / (vls**0.85)
cds = (((diameter/2)**2) * 3.1415926) * cd

# Inflation Curve Method
delta_t = 0.01 
fx_curve = 0 # will replace this throughout sim to represent maximum sustained drag (opening force)

time = 0
drag = weight
acceleration = 0
velocity = -vls

while time <= tf:
    if (0.5 * aird * (velocity**2) * cds * (time/tf)**avt) < weight:
        drag = weight
    else:
        drag = 0.5 * aird * (velocity**2) * cds * (time/tf)**avt
    acceleration = (drag - weight) / mass
    velocity += acceleration * delta_t
    time += delta_t

    if drag > fx_curve:
        fx_curve = drag

# Knacke Method
ballastic_parameter = (2 * mass) / (cds * aird * vls * tf)
print("Match up the X1 Factor (y-axis) with the Ballastic Parameter (x-axis)")
print("Ballistic Parameter: %.3f" % ballastic_parameter)
x1_picture = Image.open('x1.jpg')
x1_picture.show()
x1 = float(input("Enter X1 Factor: "))
fx_knacke = x1 * cds * (.5 * aird * vls**2)
# Comparison
print("Inflation Curve Method: %i" % fx_curve)
print("Phlanz Method: %i" % fx_knacke)
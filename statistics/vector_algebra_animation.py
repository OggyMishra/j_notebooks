# for linera algebra tranasformation:

# this is to create two dimensional space and project the PI icon on it.

plane = NumberPlane()
pi_creature = PiCreature(color = PINK)
plane.prepare_for_nonlinear_transformation()
plane.add(pi_creature)
def homotopy(x, y, z, t):
	norm = np.linalg.norm([x, y])
	tau = interpolate(5, -5, t) + norm / SPACE_WIDTH
	alpha = sigmoid(tau)
	return [x, y+0.5*np.sin(2*np.pi*alpha), z]

play(HomotopyAnimation(homotopy, plane, run_time =3))
dither(2)
play(MatrixTransformation([[2, 1], [1, 2]]), plane)

# basis in vectors:
# The basis of a vector space is a set of linearly independent vectors that span the full space.
# highly confusing.

# SLICING IS HARD!!!

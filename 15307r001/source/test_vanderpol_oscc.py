from vanderpol_oscc import function as f
import numpy as np
from scipy.integrate import odeint
import unittest


class TestProject1(unittest.TestCase):

    """
    test_function tests whether function is correctly written
    test_soln tests whether solution of the ODE is coming out to be correct
    """
    def test_function(self):
        sol = f([0, 0], 100)
        self.assertAlmostEqual(sol[0], 0.0)
        self.assertAlmostEqual(sol[1], 0.0)

    def test_soln(self):
        t = np.linspace(0, 1, 100)
        sol = odeint(f, [0, 0], t)
        for i in range(100):
            self.assertAlmostEqual(sol[i, 0], 0.0)
            self.assertAlmostEqual(sol[i, 1], 0.0)

if __name__ == '__main__':
    unittest.main()

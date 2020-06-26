"""
from __init__ import App
#m=App()
xyz=2
class abc:
    def abc(self):
        App.sim(self)

A=abc()
A.l=[1]
A.abc()

Below:

 > Required in order to run the documentation checker on this code.

 > The comment
     pragma: no cover
   means that this block of code will not be checked for unit test
   coverage by the `coverage` module.

"""
import unittest
from src.unittest.python import model_tests
suite = unittest.TestLoader().loadTestsFromModule(model_tests)
unittest.TextTestRunner().run(suite)

from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(6)) == 5*6

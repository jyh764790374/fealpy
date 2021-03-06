#!/usr/bin/env python3
# 
import sys
import sympy as sp
from fealpy.symcom import MonomialSpace2d


class MonomialSpace2dTest():

    def __init__(self):
        pass

    def basis(self, p=3):
        domain = sp.Matrix([-1, 1, -1, 1])
        space0 = MonomialSpace2d(p, domain=domain)
        print(space0.phi)

        domain = sp.Matrix([1, 3, -1, 1])
        space1 = MonomialSpace2d(p, domain=domain)
        print(space1.phi)

    def mass_matrix(self, p=3):
        domain = sp.Matrix([-1, 1, -1, 1])
        space0 = MonomialSpace2d(p, domain=domain)
        H0 = space0.mass_matrix()
        print('H0:', H0)


        domain = sp.Matrix([1, 3, -1, 1])
        space1 = MonomialSpace2d(p, domain=domain)
        H1 = space1.mass_matrix()
        print('H1:', H1)

    def basis_jacobian(self, p=3):
        domain = sp.Matrix([-1, 1, -1, 1])
        space0 = MonomialSpace2d(p, domain=domain)
        J0 = space0.basis_jacobian() 
        print('J0:', J0)
        print(space0.vector_basis())
        print(space0.curl_vector_basis())


        domain = sp.Matrix([1, 3, -1, 1])
        space1 = MonomialSpace2d(p, domain=domain)
        J1 = space1.basis_jacobian() 
        print('J1:', J1)
        print(space1.vector_basis())
        print(space1.curl_vector_basis())
        
test = MonomialSpace2dTest()

if sys.argv[1] == 'basis':
    p = int(sys.argv[2])
    test.basis(p=p)
elif sys.argv[1] == 'mass_matrix':
    p = int(sys.argv[2])
    test.mass_matrix(p=p)
elif sys.argv[1] == 'basis_jacobian':
    p = int(sys.argv[2])
    test.basis_jacobian(p=p)



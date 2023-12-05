# import lines
from sparc.sparc_core import SPARC
from ase.build import molecule

# make the atoms
atoms = molecule('H2')
atoms.cell = [[6,0,0],[0,6,0],[0,0,6]]
atoms.center()

# set up the calculator
calc = SPARC(
             KPOINT_GRID=[1,1,1],
             h = 0.12,
             EXCHANGE_CORRELATION = 'GGA_PBE',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)

# set the calculator on the atoms and run
atoms.set_calculator(calc)
print(atoms.get_potential_energy())


-17.158835505
fijwew-Gisry0-pyfwut



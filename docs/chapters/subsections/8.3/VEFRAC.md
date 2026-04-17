### VEFRAC -- Vertical Equilibrium Relative Permeability Fraction (Grid)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the Vertical Equilibrium ("VE") relative permeability weighting factor (α) used to calculate the VE relative permeability curves to be used in the simulation, for when the VE option has been activated by the VE keyword in the RUNSPEC section. If α = 1.0, then the VE model calculated relative permeability curves will be used, and if α = 0.0, then the curves entered via the SWOF, SGOF, SLGOF series of keywords or the SWFN, SGFN, SGWFN, SOF2, SOF3, SOF32D series of keywords, will be used. A value of α between zero and one will result in weighted average relative permeability curves being employed, that is:

Note that VEFRAC sets α for the whole grid; whereas, the VEFRACV keyword in the PROPS section assigns α on a cell by cell basis, See also the VEFRACP and VEFRACPV keywords that apply the weighting factors to the capillary pressure data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

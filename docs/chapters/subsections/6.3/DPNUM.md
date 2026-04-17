### DPNUM -- Define Dual and Single Porosity Grid Block Array

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

In dual porosity runs only, that is not dual permeability runs, the DPNUM keyword defines which wells should be treated as single porosity cells and which cells should be treated as dual porosity cells, for when the Dual Porosity model has been activated by the DUALPORO keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

### NODPPM -- Deactivate Fracture Porosity-Permeability Calculation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NODPPM keyword deactivates the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability in dual porosity and dual permeability runs. Either the DUALPORO or DUALPERM keywords in the RUNSPEC section must be declared in the input file in order to use this keyword. If the default calculation is switched off by this keyword, then the effective fracture permeability is taken to be those entered for the fracture using the PERMX, PERMY and PERMZ keywords in the GRID section. If the keyword is absent from the input deck, then the entered PERMX, PERMY and PERMZ arrays for the fractures are multiplied by fracture PORO array values in order to obtain the effective fracture permeability.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE FRACTURE POROSITY-PERMEABILITY CALCULATION

\--

NODPPM

The above example switches off the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability.

### STONE -- Activate Stone's Second Three Phase Oil Relative Permeability Model (Alias for STONE2)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword is an alias for STONE2 keyword that activates Stone's[^1] second three phase oil relative permeability model as modified by Aziz and Settari[^2]. If the STONE, STONE1 and STONE2 keywords are not present in the input deck then the default three phase oil relative permeability model is employed. The STONE keyword should only be used in three phase runs containing the oil, gas and water phases.

There is no data required for this keyword.

#### Example

\--

\-- ACTIVATE STONE'S SECOND THREE PHASE RELATIVE PERMEABILITY MODEL

\--

STONE

The above example switches on the Modified Stone three phase relative permeability model.

[^1]: Stone, H. L. "Estimation of Three-Phase Relative Permeability and Residual Oil Data," Journal of Canadian Petroleum Technology (1973) 12, No. 4, 53-61.

[^2]: Aziz, K. and Settari, A. Petroleum Reservoir Simulation, London, UK, Applied Science Publishers (1979), page 398.

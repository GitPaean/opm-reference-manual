### STONE1 -- Activate Stone's First Three Phase Oil Relative Permeability Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates Stone's[^1] first three phase oil relative permeability model as modified by Aziz and Settari[^2]. If the STONE1 and STONE2 keywords are not present in the input deck then the default three phase oil relative permeability model is employed. The STONE1 keyword should only be used in three phase runs containing the oil, gas and water phases.

There is no data required for this keyword.

#### Example

\--

\-- ACTIVATE STONE'S FIRST THREE PHASE RELATIVE PERMEABILITY MODEL

\--

STONE1

The above example switches on the Modified Stone three phase relative permeability model.

[^1]: Stone, H. L. "Probability Model for Estimating Three-Phase Relative Permeability," paper SPE 2116, Journal of Canadian Petroleum Technology (1973) 22, No. 2, 214-218.

[^2]: Aziz, K. and Settari, A. Petroleum Reservoir Simulation, London, UK, Applied Science Publishers (1979), page 398.

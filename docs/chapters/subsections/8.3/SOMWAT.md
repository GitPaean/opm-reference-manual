### SOMWAT -- STONE1 Model Minimum Oil Saturation versus Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the minimum oil saturation as a function of water saturation for Stone's[^1] first three phase oil relative permeability model as modified by Aziz and Settari[^2]. If the STONE1 and STONE2 keywords are not present in the input deck then the default three phase oil relative permeability model is employed. The SOMWAT and STONE1 keywords should only be used in three phase runs containing the oil, gas and water phases. The keyword is optional.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Stone, H. L. "Probability Model for Estimating Three-Phase Relative Permeability," paper SPE 2116, Journal of Canadian Petroleum Technology (1973) 22, No. 2, 214-218.

[^2]: Aziz, K. and Settari, A. Petroleum Reservoir Simulation, London, UK, Applied Science Publishers (1979), page 398.

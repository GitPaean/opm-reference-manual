### STONE1EX -- Define Stone's First Three Phase Oil Relative Permeability Parameter

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the exponent used in Stone's[^1] first three phase oil relative permeability model as modified by Aziz and Settari[^2]. The STONE1EX keyword should only be used in three phase runs containing the oil, gas and water phases and when the STONE1 keyword in the PROPS section has been used to activate Stone's first three phase oil relative permeability model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | STONEPAR1 | A real positive value that defines the exponent to be used in the Modified Stone first three phase oil relative permeability model. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN records as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain only one value and is terminated by a "/"<br>3)  There is no "/" terminator for the keyword. |  |  |  |

Table 8.180: STONE1EX Keyword Description

If the STONE, STONE1 and STONE2 keywords are not present in the input deck then the default three phase oil relative permeability model is employed.

#### Example

Given NTSFUN equals five on the TABDIMS keyword in the RUNSPEC section, then:

\--

\-- DEFINE STONE\'S FIRST THREE PHASE RELATIVE PERMEABILITY MODEL PARAMETER

\--

STONE1EX

1.000 / SATURATION TABLE NO. 01

1.000 / SATURATION TABLE NO. 02

2.000 / SATURATION TABLE NO. 03

1.000 / SATURATION TABLE NO. 04

3.000 / SATURATION TABLE NO. 05

Defines the exponents to be used in the Modified Stone first three phase oil relative permeability model, for each of the five saturation tables.

[^1]: Stone, H. L. "Probability Model for Estimating Three-Phase Relative Permeability," paper SPE 2116, Journal of Canadian Petroleum Technology (1973) 22, No. 2, 214-218.

[^2]: Aziz, K. and Settari, A. Petroleum Reservoir Simulation, London, UK, Applied Science Publishers (1979), page 398.

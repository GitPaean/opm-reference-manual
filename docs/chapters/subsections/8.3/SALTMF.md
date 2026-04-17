### SALTMF -- Define the Salt Liquid-Phase Mole Fraction for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALTMF keyword defines a uniform salt liquid-phase mole fraction for all cells in the model. The keyword should only be used with OPM Flow's CO~2~-Brine model which is activated via the CO2STORE keyword in the RUNSPEC section.

This is an OPM Flow specific keyword.

| No. | Name | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Field | Metric | Laboratory | 0 |
| 1 | SALTMF | A real positive value that defines the salt liquid-phase mole fraction for all grid blocks in the model for when the CO~2~-Brine model has been activated. |  |  |  |
| mole fraction | mole fraction | mole fraction |  |  |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |  |  |

Table 8.3.277.1: SALTMF Keyword Description

See also the CO2STORE keyword in the RUNSPEC section.

#### Example

The example sets the salt liquid-phase mole fraction for all cells in the model to 0.018.

\--

\-- SET SALT LIQUID-PHASE MOLE FRACTION FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALTMF

0.018 /

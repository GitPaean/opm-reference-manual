### GRIDOPTS -- Grid Processing Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

GRIDOPTS activates the negative directional dependent transmissibility multipliers option, defines the maximum number of MULTNUM regions and the number of PINCHNUM regions for the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TRANMULT | A character string that activates the negative directional dependent transmissibility multipliers option by setting TRANMULT to YES. Setting the value to NO switches off this option.<br>OPM Flow uses a positive directional dependent transmissibility formulation to describe the flow between two cells, that is for cell (I, J, K) OPM Flow calculates the x face transmissibility between (I, J, K) and (I +1, J, K) cell face. Modification to the transmissibilities in this case is accomplished by the MULTX, MULTY and MULTZ keywords.<br>Setting TRANMULT to YES invokes the option to use a negative directional dependent multiplier scheme using the MULTX-, MULTY- and MULTZ- keywords. In this case OPM Flow applies the x face transmissibility between (I - 1, J, K) and (I, J, K) cell face when using the MULTX-, MULTY- and MULTZ- keywords.<br>Note that if TRANMULT is defaulted, and there are negative directional dependent multiplier keywords in the input deck, then OPM Flow will continue to process the MULTX-, MULTY- and MULTZ keywords correctly. Whereas, the commercial simulator will terminate with an error. | NO |
| 2 | NRMULT | A positive integer value that defines the maximum number of MULTNUM regions for the MULTNUM array.<br>The MULTNUM array is used in the GRID section to define various inter-region transmissibility regions in the model and NRMULT sets the maximum number of regions which is the maximum value of an element in the MULTNUM array.<br>Inter-region MULTNUM transmissibility multipliers can be defined using the MULTREGT and regional pore volumes multipliers can be set using the MULTREGP keyword. | 0 |
| 3 | NRPINC | A positive integer value that defines the maximum number of PINCHNUM regions for the PINCHNUM array.<br>The PINCHNUM array is used in the GRID section to define various regions in the model and NRPINC sets the maximum of regions which is the maximum value of an element in the PINCHNUM array.<br>Each regions criteria for setting the pinch out criteria is set by the PINCHREG keyword. | 0 |
| Notes:<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 5.18: GRIDOPTS Keyword Description

See also the MULTNUM, MULTREGP, MULTREGT, PINCHNUM, and PINCHREG keywords.

#### Example

---

\-- NEG MAX MAX

\-- MULTS MULTNUM PINCHNUM

GRIDOPTS

NO 9 1\* /

The above example switches off the negative directional dependent transmissibility multipliers option and defines the maximum of MULTNUM regions to be nine,. The NRPINC parameter is defaulted which means there the maximum number of PINCHREG regions is zero.

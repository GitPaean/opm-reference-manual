### MULTREGP -- Multiply Pore Volumes Based On Region Number

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MULTREGP keyword multiplies the pore volume of a cell by a constant for all cells with a specific region number. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTREGP keyword is read by the simulator. The constant should be a real number.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION | REGION is a positive integer representing the region for which the CONSTANT in (2) should be applied. | None |
| 2 | CONSTANT | A real value to multiply the pore volume by for a given REGION. | 1 |
| 3 | REGION<br>ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION in (1). ARRAY can have the following values:<br>1)  F for the FLUXNUM array.<br>2)  M for the MULTNUM array.<br>3)  O for the OPERNUM array. | M |
| Notes:<br>1)  Where the REGION should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FIPNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section.<br>2)  If the GRIDOPTS keyword is not present in the RUNSPEC section or if the GRIDOPTS keyword is present but the maximum number of MULTNUM regions (NRMULT) equals zero then REGION ARRAY will default to F for the FLUXNUM array.<br>3)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.78: MULTREGP Keyword Description

#### Example

\--

\-- RESET PORE VOLUME FOR DIFFERENT REGIONS

\--

\-- REGION PORV REGION ARRAY

\-- NUMBER MULT M / F / O

MULTREGP

1 1.0456573 M / Fault Block 1

2 0 M / Fault Block 2

3 0.9756715 M / Fault Block 3

4 0 M / Inactive Blocks

/

The above example re-scales the pore volumes for MULTNUM regions one and three and makes regions two and four inactive by setting their pore volumes to zero.

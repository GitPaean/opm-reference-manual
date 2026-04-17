### MULTREGT -- Multiply Transmissibilities Between Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MULTREGT keyword multiplies the transmissibility between two regions by a constant. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTREGT keyword is read by the simulator. The constant should be a real number.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION1 | A positive integer value that defines the from REGION number for which the CONSTANT in (3) should be applied. | None |
| 2 | REGION2 | A positive integer value that defines the to REGION number for which the CONSTANT in (3) should be applied. | None |
| 3 | CONSTANT | A real positive value to multiply the transmissibility between REGION1 and REGION2. | 1 |
| 4 | DIR | A character string that defines the direction to apply the transmissibility multiplier between the two regions, should be set to one of the following X, Y, Z, XY, XZ, YZ, or XYZ. | XYZ |
| 5 | TYPE | A character string that defines the type of connections the transmissibility multiplier should be applied to, should be one of the following:<br>1)  NNC -- Only apply the transmissibility multiplier between REGION1 and REGION2 to non-neighbor connections.<br>2)  NONNC -- Do not apply the transmissibility multiplier between REGION1 and REGION2 to non-neighbor connections.<br>3)  ALL -- Apply the transmissibility multiplier between REGION1 and REGION2 to all connections. | ALL |
| 6 | REGION<br>ARRAY | A single character that defines the REGION ARRAY that is used to specify the regions identified by REGION1 and REGION2. REGION ARRAY can have the following values:<br>1)  F for the FLUXNUM array<br>2)  M for the MULTNUM array<br>3)  O for the OPERNUM array | M |
| Notes:<br>1)  Where REGION1 and REGION2 should be less than or equal to the maximum number of regions as defined on the REGDIMS keyword for the FLUXNUM and OPERNUM arrays or the GRIDOPTS keyword for the MULTNUM array in the RUNSPEC section.<br>2)  If REGION1 is defaulted then the transmissibilities between REGION2 and all other regions will be multiplied. Similarly, if REGION2 is defaulted then the transmissibilities between REGION1 and all other regions will be multiplied. If both REGION1 and REGION2 are defaulted then the transmissibilities between all pairs of regions will be multiplied.<br>3)  If REGION1 and REGION2 are equal and positive then all the transmissibilities within that region as well as the transmissibilities between that region and all other regions will be multiplied.<br>4)  If the same combination of REGION1 and REGION2 is repeated then only the latest multiplier is used regardless of whether the REGION ARRAY specified is the the same or not.<br>5)  If the GRIDOPTS keyword is not present in the RUNSPEC section or if the GRIDOPTS keyword is present but the maximum number of MULTNUM regions (NRMULT) equals zero then REGION ARRAY will default to F for the FLUXNUM array.<br>6)  Each record must be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 6.79: MULTREGT Keyword Description

#### Example

\--

\-- SET TRANSMISSIBILITES ACROSS DIFFERENT RESERVOIRS TO ZERO

\--

\-- REGION REGION TRANS DIREC NNC REGION ARRAY

\-- FROM TO MULT OPT OPTS M / F / O

MULTREGT

1\* 1\* 0.0 1\* \'ALL\' M / ALL REGIONS SEALED

/

The above example isolates all regions from one another by setting the transmissibility for the MULTNUM regions to zero in all directions and for all connections types.

### COORDSYS -- Define Coordinate Grid Options

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword sets various options for when multiple grid systems are being used, as declared by the NUMRES keyword in the RUNSPEC section. OPM Flow does not support multiple grid systems. The keyword is also used to stipulate for radial grids if the completion of the circle in the THETA direction should be implemented using non-neighbor connections.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | K1 | A positive integer that defines the lower bound of the array in the K-direction for the given grid system. | None |
| 2 | K2 | A positive integer that defines the upper bound of the array in the K-direction for the given grid system. | None |
| 3 | COMPLETE | COMPLETE is a defined character string that determines for radial grids if the circle should be completed in THETA direction, and should be set to COMP to complete the circle, or INCOMP for not completing the circle. | INCOMP |
| 4 | CONNECT | A defined character string that declares how the reservoir below should be connected to the given reservoir, and should be set to JOIN to connect the two reservoirs by calculating the inter-reservoir transmissibilities, or SEPARATE to isolate the reservoirs. | SEPARATE |
| 5 | R1 | R1 is a positive integer defining the lower reservoir unit that is is connected to the given reservoir unit. | Current<br>Reservoir<br>Record |
| 6 | R2 | R2 is a positive integer defining the upper reservoir unit that is is connected to the given reservoir unit. |  |
| Notes:<br>1)  The DIMENS keyword defines the dimensions of the model (NX, NY and NZ) and the NUMRES keyword the number of multiple grid systems (reservoirs), both keywords are in the RUNSPEC section.<br>2)  Each record must be terminated by a "/" and there must be exactly NUMRES records entered for the keyword.<br>3)  There is no "/" terminator for this keyword. |  |  |  |

Table 6.15: COORDSYS Keyword Description

#### Example

\--

\-- DEFINE COORDINATE GRID OPTIONS

\--

\-- K1 K2 COMP CONNECT LOWER UPPER

\-- Layer Layer CIRCLE RES RES RES

COORDSYS

1 1 COMP /

/

The above example connects the circle in the THETA direction for the RADIAL model, for when the number of grids have been set to one via the NUMRES keyword in the SCHEDULE section.

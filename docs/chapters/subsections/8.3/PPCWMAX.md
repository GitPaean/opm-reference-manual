### PPCWMAX -- Define SWATINIT Calculated Capillary Pressure Constraints

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PPCWMAX keyword defines the maximum capillary pressure allowed when scaling the capillary pressure tables to match the inputted SWATINIT array. This is primary used for when the SWATINIT array has values of water saturation above the connate water saturation significantly outside than capillary pressure transition zone, that is high on the structure. In this case OPM Flow may generate large values for the capillary pressure which may result in numerical converge problems. This keyword sets the maximum allowable calculated capillary pressure and how the water saturation should be treated when the limit is exceeded.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PCWO | A columnar vector of real values that defines the maximum allowable capillary pressure for each SATNUM region.<br>The default value of infinity means there is no limit applied. | Infinity |
| psia | barsa | atma |  |
| 2 | OPTN | A columnar vector of character strings that should be set to:<br>1)  NO: To ignore the SWATINIT value for the offending cell for when PCWO is exceeded. In this cases the capillary pressure for the block is set to the maximum (PCWO) and the water saturation is re-calculated based on PCWO.<br>2)  YES: To set the SWATINIT value to the connate water saturation for the offending cell for when PCWO is exceeded. In this case the capillary pressure is set to the maximum value of the appropriate SATNUM table and the initial water saturation is calculated to be consistent with the tables maximum capillary pressure. This results in the capillary pressures not being re-scale for the offending cell. | No |
| Notes:<br>1)  The keyword is followed by NTSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each row show contain two values representing PCWO and OPTN values.<br>3)  Each row is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.111: PPCWMAX Keyword Description

#### Example

\--

\-- SET MAXIMUM PC FOR SWATINIT INITIALIZATION

\-- MAX MATCH

\-- PC SWATINIT

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

PPCWMAX

100.0 YES / TABLE NO 01

125.0 YES / TABLE NO 02

135.0 YES / TABLE NO 03

The above example sets the maximum capillary pressure for three saturation regions to 100, 125 and 135 with SWATINIT reset to the connate water saturation for when the capillary pressure limit is exceeded.

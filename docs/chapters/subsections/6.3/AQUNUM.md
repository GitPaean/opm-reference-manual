### AQUNUM -- Define Numerical Aquifer Properties

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The AQUNUM keyword defines the properties of numerical aquifers, including which grid blocks in the model should be utilized as part of the numerical aquifer. Each row entry in the AQUNUM keyword defines one numerical aquifer. Note that a numerical aquifer may consists of more than one grid cell, in order to better describe the water influx from the aquifer to the grid.

| 1 | AQUID | AQUID is a positive integer greater than or equal to one and less than or equal to the maximum number of numerical aquifers as defined by the MXNAQN variable on the AQUDIMS keyword in the RUNSPEC section, that defines the aquifer to be connected to the grid. | None |
| --- | --- | --- | --- |
| 2 | I | A positive integer that defines the cell in the I-direction that represents the AQUID aquifer, and which must be greater than or equal to one and less than or equal to NX. | None |
| 3 | J | A positive integer that defines the cell in the J-direction that represents the AQUID aquifer, and which must be greater than or equal to one and less than or equal to NY. | None |
| 4 | K | A positive integer that defines the cell in the K-direction that represents the AQUID aquifer, and which must be greater than or equal to one and less than or equal to NZ. | None |
| 5 | AREA | AREA is a real positive value that defines the cross-sectional area of the aquifer used in calculating the aquifer connection transmissibility.<br>The actual transmissibility between the numerical aquifer and the connected grid cell is the harmonic average of the aquifer connection transmissibility and the calculated connected cell transmissibility.<br>The value entered for AREA does not effect the visualization of the cell in OPM ResInsight, as it is only used in calculating the transmissibility.<br>Note that the AQUOPT1 variable on the AQUCON keyword in the GRID section allows one to use the value entered for AREA or to use the grid cell cross-sectional area instead for the transmissibility calculation. | None |
| ft^2^ | m^2^ | cm^2^ |  |
| 6 | LENGTH | LENGTH is a real positive value that defines the length of the numerical aquifer. Similar to the AREA variable, LENGTH is not constrained by the original host cell size and the value entered does not effect the visualization of the cell in OPM ResInsight. | None |
| feet | m | cm |  |
| 7 | PORO | PORO is a real positive number greater than zero and less than or equal to one that assigns the porosity to the numerical aquifer. | None |
| dimensionless | dimensionless | dimensionless |  |
| 8 | PERM | PERM is a real positive number that assigns the permeability to the numerical aquifer. | None |
| mD | mD | mD |  |
| 9 | DATUM | DATUM is a real positive number that sets the reference datum depth of the numerical aquifer. Similar to the AREA variable, DATUM is not constrained by the original host cell depth and the value entered does not effect the visualization of the cell in OPM ResInsight.<br>If defaulted then the depth of cell (I, J, K) will be used | Cell<br>Depth |
| feet | m | cm |  |
| 10 | PRESS | PRESS is a single positive value that defines the numerical aquifer pressure at DATUM.<br>If PRESS is defaulted then the simulator will set the aquifer's initial reservoir pressure to be in equilibrium with the cells the aquifer is contacted to. This is the preferred manner to initialize the numerical aquifer. | 1\* |
| psia | barsa | atma |  |
| 11 | PVTNUM | PVTNUM is positive integer greater than zero and less than the NTPVT variable on the TABDIMS keyword in the RUNSPEC section, that defines the PVTW table allocated to the numerical aquifer.<br>If defaulted then the PVT tables allocated to cell (I, J, K) will be used. | Cell<br>PVTNUM |
| 12 | SATNUM | SATNUM is positive integer greater than zero and less than the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section, that defines the saturation tables allocated to the numerical aquifer.<br>If defaulted then the saturation tables allocated to cell (I, J, K) will be used. | Cell<br>SATNUM |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  The keyword is followed by up to MXNAQN records as defined on the AQUDIMS keyword in the RUNSPEC section<br>3)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 6.10: AQUNUM Keyword Description

Numerical aquifers are modeled as one-dimensional, with aquifer flow assumed to be in the direction defined by LENGTH, and flux out of the aquifer is through the cross sectional area defined by AREA. Note that, all the aquifer cells must be isolated from the reservoir cells, with only the AQUCON connections connecting to the actual reservoir cells.

The values entered on the AQUNUM keyword are used to calculate the aquifer\'s pore volume and the transmissibility between the aquifer and the connected cell faces defined on the AQUCON keyword. Thus:

3)  1)  1)  The aquifer's pore volume is always calculated from the data entered on the AQUNUM keyword usingand any modifications to the host cell values performed in either the GRID or EDIT sections are always ignored for cells declared as numerical aquifers cells.

        2)  For the transmissibility calculation either the cross-sectional area (AREA) defined on the AQUNUM keyword may be used or the connecting cell cross-sectional area by setting the AQUOPT1 variable on the AQUCON keyword.

In order to fully define a numerical aquifer one has to define the aquifer properties via the AQUNUM keyword, and how the aquifer is connected to the reservoir using the AQUCON keyword in the GRID or SOLUTION sections.

Using one aquifer cell should generally be sufficient, provided the aquifer properties are constant. However, employing multiple cells may be appropriate if the aquifer properties vary with distance or depth, which is not uncommon. Secondly, having multiple cells may help to minimize throughput-related convergence problems by increasing the pore volumes exponentially away from the reservoir cells. Typically, three to five aquifer cells are employed under theses circumstances.

The aquifer pore volume can be used to define the amount of pressure support; whereas, the aquifer transmissibility will influence the responsiveness of the aquifer.

See also the AQUDIMS keyword in the RUNSPEC section that defines the numerical aquifer dimensions.

#### Example

Given the following grid and aquifer dimensions in the RUNSPEC section:

\--

\-- MAX MAX MAX

\-- NDIVIX NDIVIY NDIVIZ

DIMENS

96 58 28 /

\-- AQF AQF AQF AQF AQF AQF AQF AQF

\-- MXAQN MXNAQC NIFTBL NRIFTB NANAQU NCAMAX MXNALI MXAAQL

AQUDIMS

3 3 1\* 1\* 1\* 1\* 1\* 1\* /

The following numerical aquifer definition:

\--

\-- NUMERICAL AQUIFER DESCRIPTION

\--

\-- AQUID - LOCATION - AQF AQF AQF AQF AQF AQF PVT SATNUM

\-- NUMBER I J K AREA LENGTH PORO PERM DATUM PRES TAB TAB

\--

AQUNUM

1 1 3 28 5.20E03 2.0E3 0.05 0.3 1\* 1\* 1\* 1\* /

1 1 2 28 5.20E06 2.0E6 0.05 0.3 1\* 1\* 1\* 1\* /

1 1 1 28 5.20E09 2.0E9 0.05 0.3 1\* 1\* 1\* 1\* /

/

defines one numerical aquifer consisting of three cells. The connection to the grid cells would take the form of:

\--

\-- NUMERICAL AQUIFER CONNECTIONS

\--

\-- ID \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- CONNECT TRANS TRANS ADJOIN

\-- NUMBER I1 I2 J1 J2 K1 K2 FACE MULT OPTN CELLS

AQUCON

1 1 1 4 58 28 28 \'K+\' 1.3 1\* 1\* /

1 2 96 1 58 28 28 \'K+\' 1.3 1\* 1\* /

/

that creates a basal aquifer[^1].

[^1]: Basal Aquifer: An aquifer located at the bottom of a geologic unit.

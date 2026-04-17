### AQUFET -- Define Fetkovich Analytical Aquifer and Connections

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The AQUFET keyword defines Fetkovich[^1] analytical aquifers, the aquifer properties, together with the cell connections to the aquifer. Each row entry in the AQUFETP keyword defines one Fetkovich analytical aquifer and one cell face to be connected to the aquifer.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped; however, see the AQUFETP keyword in the SOLUTION section and AQUANCON keyword in the GRID section, on how to define and connect Fetkovich analytical aquifers.

| 1 | DATUM | DATUM is a single positive value that defines the Fetkovich reference datum depth for PRESS. | None |
| --- | --- | --- | --- |
| feet | m | cm |  |
| 2 | PRESS | PRESS is a single positive value that defines the aquifer pressure at DATUM.<br>If PRESS is defaulted then the simulator will set the aquifer's initial reservoir pressure to be in equilibrium with the cells the aquifer is contacted to. Defaulting this parameter will avoid inconsistent equilibration pressures between the reservoir cells and the aquifer. | 1\* |
| psia | barsa | atma |  |
| 3 | PORV | 1)  A real positive value that defines the initial water volume of the aquifer. | None |
| stb | sm^3^ | scc |  |
| 4 | COMP | COMP is a real number defining the total compressibility (Ct) of the aquifer, that is the rock compressibility (Cf) plus the water compressibility (Cw) at the aquifer datum pressure (DATUM) and is defined as: | None |
| 1/psia | 1/barsa | 1/atma |  |
| 5 | PI | A real positive number that defines the aquifer productivity index based on the aquifer influx rate per unit pressure drop. | None |
| stb/d/psia | sm^3^/barsa | scc/hr/atma |  |
| 6 | PVTW | A positive integer that defines the aquifer's PVTW water property table. | 1 |
| 7 | I1 | A positive integer that defines the lower bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 8 | I2 | A positive integer that defines the upper bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to I1 and less than or equal to NX | NX |
| 9 | J1 | A positive integer that defines the lower bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 10 | J2 | A positive integer that defines the upper bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to JI and less than or equal to NY. | NY |
| 11 | K1 | A positive integer that defines the lower bound of the cells in the K-direction to be to be connected to the aquifer and must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 12 | K2 | A positive integer that defines the upper bound of the cells in the K-direction to be connected to the aquifer and must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 13 | AQUFACE | AQUFACE is a character string that sets the connection "face" of the cells declared by this record and should be set to one of the following:<br>3)  X+, Y+, or Z+ for the positive direction, or X-, Y- or Z- for the negative direction transmissibilities.<br>4)  I+, J+, or K+ for the positive direction, or I-, J- or K- for the negative direction transmissibilities. | None |
| 14 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer.<br>This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the DIMENS keyword in the RUNSPEC section.<br>2)  The keyword is followed by up to NANAQU records as defined on the AQUDIMS keyword in the RUNSPEC section<br>3)  The keyword should be terminated by a "/". |  |  |  |

Table 10.7: AQUFET Keyword Description

Note this keyword should only be used in equilibration and enumerated initialize runs, that is it should be omitted from RESTART runs.

#### Example

Given the following grid and aquifer dimensions in the RUNSPEC section:

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC \--

\-- MAX MAX MAX

\-- NDIVIX NDIVIY NDIVIZ

DIMENS

20 1 5 /

\-- AQF AQF AQF AQF AQF AQF AQF AQF

\-- MXAQN MXNAQC NIFTBL NRIFTB NANAQU NCAMAX MXNALI MXAAQL

AQUDIMS

1\* 1\* 5 100 1 1\* 1\* 1\* /

The Fetkovich Analytical aquifer is defined in the SOLUTION sections as:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION \--

\-- FETKOVICH AQUIFER DESCRIPTION AND CONNECTIONS

\--

\-- DATUM AQF AQF AQF AQF AQF \-\-\-\-\-\-\-- BOX \-\-\-\-\-\-- CONNECT SALT

\-- DEPTH PRESS VOLM COMP PI PVT I1 I2 J1 J2 K1 K2 FACE CONC

\--

AQUFET

1130. 1\* 1.0E+12 3.0E-5 500E3 1 1 1 1 1 1 1 \'J-\' /

Here one Fetkovich Analytical aquifer is connected to a single cell (1, 1, 1) at the J- face (or X- face) of the grid.

[^1]: Fetkovich, M. J. "A Simplified Approach to Water Influx Calculations - Finite Aquifer Systems," Journal of Petroleum Technology, (1971) 23, No. 7, 814-828.

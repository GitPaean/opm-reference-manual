### SMULTY -- Multiply Cell Transmissibility in the +Y Direction (Auto-Refinement)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SMULTY multiples the transmissibility between two cell faces in the +Y direction between cells in a host base grid and the connecting auto-refined grid cells, via an array, that is the keyword sets the transmissibility multiplier of block (Ihost, Jhost, Khost) in the host base grid, multiplies the transmissibility all the cells (Iauto, Jauto, Kauto) and (Iauto, J+1auto, Kauto) in the auto-refinement grid. The Auto Refinement option must be enabled to use this keyword via the AUTOREF keyword in the RUNSPEC section.

An alternative to defining the complete array is to use the BOX keyword to define an area of the grid and then use the SMULTY keyword to set the multipliers just for the area defined by the BOX keyword (see the example).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SMULTY+ | SMULTY+ is an array of real positive numbers assigning the transmissibility multipliers in the +X direction to each cell face in the model.<br>Repeat counts may be used, for example 20\*100.0. | 1.0 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.119: SMULTY Keyword Description

See also the MULTX, MULTY and MULTZ keywords for scaling transmissible between grid cells.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 3 / DEFINE BOX AREA

\--

\-- SET SMULTY+ TRANSMISSIBILITY MULTIPLIERS

\--

SMULTY

18\*0.300 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding BOX statement. The ENDBOX keyword resets the input box to the full grid.

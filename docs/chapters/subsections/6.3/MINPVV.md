### MINPVV -- Set a Minimum Grid Block Pore Volume Threshold for Individual Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

MINPVV is an array that defines the minimum threshold pore volume for each cell, that makes grid blocks whose pore volume is below this value inactive in the model (inactive cells are not used in OPM Flow calculations).

Note this keyword is different to the MINPV and MINPORV keywords in the GRID section, that set a constant minimum threshold pore volume for all cells in the model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | MINPVV | MINPVV is an array of real positive numbers that defines the minimum pore volumes for each cell in the model in order for the cells to be active. | Defined |
| rb<br>1.0e-6 | rm^3^<br>1.0e-6 | rcc<br>1.0e-6 |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.64: MINPVV Keyword Description

The MINPVV, MINPV, and MINPORV keywords only apply their minimum threshold pore volume values to active cells. Thus, cells that have been made inactive via setting their ACTNUM values to zero, remain inactive, even if their pore volume exceeds the values set by the MINPVV, MINPV, and MINPORV keywords.

Secondly, although the MINPVV keyword allows one to set a minimum threshold pore volume below the default value, this is not recommended, as cells with small pore volumes can cause significant numerical convergence errors. Thus, in practice, values greater than the default values are normally applied to eliminate cells that have relatively small pore volumes. In addition, the simulator reports the total pore volume and the number of cells made inactive, as well as the pore volume reduction, when the keyword is invoked; allowing one to run some sensitivities to the minimum pore volume value.

See also the PINCH keyword for the treatment of inactive grid cells and pinch-outs.

#### Example

The example below shows how to define 500 rb (or m3) as the minimum pore volume for all cells in layer 19 to be active in the model, and 750 rb (or m3) as the minimum pore volume for all cells in layer 20, by using the BOX keyword to set the portion of the grid of interest.

\--

\-- DEFINE A BOX GRID FOR THE BOTTOM TWO LAYERS OF A 100 X 100 X 20 MODEL

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 19 20 / SELECT THE BOTTOM LAYERS

\--

\-- MINIMUM PORE VOLUME FOR INDIVIDUAL CELLS TO BE ACTIVE

\--

MINPVV

10000\*500.0 10000\*750.0 /

\--

\-- RESET THE INPUT BOX TO BE THE FULL MODEL

\--

ENDBOX

Although this will work in the commercial simulators, it does not currently work in OPM Flow, that is one cannot use the MINPVV keyword in conjunction with the BOX keyword, as shown in the aforementioned example.

Instead one can use:

\--

\-- MINIMUM PORE VOLUME FOR INDIVIDUAL CELLS TO BE ACTIVE

\--

MINPVV

10000\* 10000\* 10000\* 10000\* 10000\*

10000\* 10000\* 10000\* 10000\* 10000\*

10000\* 10000\* 10000\* 10000\* 10000\*

10000\* 10000\* 10000\*

10000\*500.0 10000\*750.0 /

To accomplish the same thing, where the 10000\* instructs the simulator to use the default value of 1.0 x 10^-6^ for 10,000 cells, which in this case is one layer.

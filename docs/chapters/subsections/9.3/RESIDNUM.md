### RESIDNUM -- Define Vertical Equilibrium Residual Flow Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RESIDNUM keyword defines the Vertical Equilibrium ("VE") residual flow calculation saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block. The keyword should only be used if the Vertical Equilibrium option has been invoked via the VE keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | RESIDNUM | RESIDNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of RESIDNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a RESIDNUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.18: RESIDNUM Keyword Description

Note that any capillary pressure data on the relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) will be ignored by the VE option.

#### Example

The example below sets three RESIDNUM regions for the model, by first setting all values to one, then setting layers 2 to 10 to two, and finally setting layers 30 to 50 to three.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SATNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SATNUM 2 1 2 1 2 2 10 / SET REGION 2

SATNUM 3 1 2 1 2 30 50 / SET REGION 3

/

### WH3NUM -- Define WAG Hysteresis Saturation Table Region Numbers (Three Phase)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WH3NUM keyword defines the three phase Water-Alternating-Gas ("WAG") hysteresis tables (relative permeability and capillary pressure tables) region numbers for each grid block, for when the hysteresis option has been activated by the WAGHYSTR variable on the SATOPTS keyword in the RUNSPEC section. The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block. Note that this keyword if the three phase water relative permeabilities WAG option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | WH3NUM | WH3NUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of WH3NUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | Taken from cell allocated SATNUM |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a WH3NUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table : WH3NUM Keyword Description

#### Example

The example below sets three WH3NUM regions for a model.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

WH3NUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

WH3NUM 2 1 2 1 2 1 1 / SET REGION 2

WH3NUM 3 1 2 1 2 2 2 / SET REGION 3

/

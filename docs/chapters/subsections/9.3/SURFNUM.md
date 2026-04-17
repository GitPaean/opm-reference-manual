### SURFNUM -- Define the Surfactant Miscible Saturation Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SURFNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of oil-water relative permeability tables (SWFN, SOF2, SOF3, and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block. In this case the SURFNUM allocated tables assume that oil and water are miscible, whereas the SATNUM allocated tables are used to allocate the immiscible saturation tables. To use this keyword the Surfactant option must have been activated by the SURFACT keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SURFNUM | SURFNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of SURFNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a SURFNUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.22: SURFNUM Keyword Description

#### Example

The example below sets three SURFNUM for the model.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SURFNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

SURFNUM 2 1\* 1\* 1\* 1\* 1 1 / SET REGION 2

SURFNUM 3 1\* 1\* 1\* 1\* 2 2 / SET REGION 3

/

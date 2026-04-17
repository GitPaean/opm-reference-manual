### LWSLTNUM -- Define the Low Salt Oil Wet Saturation Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LWSLTNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables (SWFN, SOF3 and related keywords) are used to calculate the relative permeability and capillary pressure in a grid block. The keyword should only be used if the Low Salinity option for the Brine model has been activated by the LOWSALT kwyword in the RUNSPEC section.

The oil wet curves are calculated as a weighted average of the low salinity saturation tables (allocated by this keyword) and the high salinity oil wet saturation tables (allocated by the SATNUM keyword in the REGIONS section), using the weights provided by the LSALTFNC keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | LWSLTNUM | LWSLTNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of LSLTWNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a LWSLTNUM region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.13: LWSLTNUM Keyword Description

#### Example

The example below sets three LWSLTNUM regions for the model.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

LWSLTNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

LWSLTNUM 2 1 2 1 2 1 1 / SET REGION 2

LWSLTNUM 3 1 2 1 2 2 2 / SET REGION 3

/

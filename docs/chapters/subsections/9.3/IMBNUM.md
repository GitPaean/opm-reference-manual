### IMBNUM -- Define the Imbibition Saturation Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The IMBNUM keyword defines the imbibition saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | IMBNUM | IMBNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of IMBNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  If a cell is not assigned an IMBNUM region then the default value of one will be used. |  |  |  |

Table 9.9: IMBNUM Keyword Description

In addition, saturation table assignment may be directional dependent in which case the directional dependent versions of the aforementioned array should be used, that is IMBNUMX, IMBNUMY and IMBNUMZ instead of IMBNUM. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected, the non-reversible versions of the aforementioned arrays should be used, that is IMBNUMX, IMBNUMX-, IMBNUMY, IMBNUMY-, IMBNUMZ and IMBNUMZ-, instead of the IMBNUM keyword. For reference, see [Table 5.40](#anchor-2), that lists the various keywords that may be used with directional dependent relative permeability tables.

Note, currently IMBNUMX-, IMBNUMY-, and IMBNUMZ- are not supported by OPM Flow.

#### Example

The example below sets three IMBNUM regions for a 4 x 5 x 2 model using the EQUALS keyword.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

IMBNUM 1 1\* 1\* 1\* 1\* 1\* 1\* / SET REGION 1

IMBNUM 2 1 2 1 2 1 1 / SET REGION 2

IMBNUM 3 1 2 1 2 2 2 / SET REGION 3

/

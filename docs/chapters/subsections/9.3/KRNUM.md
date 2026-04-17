### KRNUM -- Define the Directional Saturation Table Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The KRNUM keyword defines the direction dependent saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block face, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables (SGFN, SWFN, SOF2, SOF3, SOF32D, SGOF, SLGOF and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block. The keyword should only be used if Directional Dependent Saturation Function option has been activated by the DIRECT parameter on the SATOPTS keyword in the RUNSPEC section. Otherwise the standard none directional relative permeability curves should be assigned by the SATNUM keyword in the REGIONS section.

This keyword is not in the standard keyword format due to the cell face (X, X-, Y, Y-, Z, and Z- for Cartesian grids and R, R-, T, T-, Z, and Z- for radial grids) being concatenated to the end of the keyword KRNUM to fully define the keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | KRNUM | KRNUM defines an array of positive integers assigning a grid cell to a particular saturation table region.<br>The maximum number of KRNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a KRNUM region then the default value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.10: KRNUM Keyword Description

If the Directional Dependent Saturation Function option has been activated by the DIRECT parameter on the SATOPTS keyword in the RUNSPEC section, then the KRNUMX, KRNUMY and KRNUMZ versions of the keyword should be used for cartesian grids. Secondly, if the Non-Reversible End-Point Scaling option has also been activated by the IRREVERS parameter on the SATOPTS keyword in the RUNSPEC section, then the non-reversible versions of the KRNUM should be used, that is KRNUMX, KRNUMX-, KRNUMY, KRNUMY-, KRNUMZ and KRNUMZ-. For reference, see [Table 5.40](#anchor-2), that lists the various keywords that may be used with directional dependent relative permeability tables.

The keywords KRNUMX-, KRNUMY-, and KRNUMZ- are not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

The example below sets the directional saturation tables in all three directions using the EQUALS keyword.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

KRNUMX 1 1\* 1\* 1\* 1\* 1\* 1\* / SET X-DIR TABLES

KRNUMY 2 1\* 1\* 1\* 1\* 1\* 1\* / SET Y-DIR TABLES

KRNUMZ 3 1\* 1\* 1\* 1\* 1\* 1\* / SET Z-DIR TABLES

/

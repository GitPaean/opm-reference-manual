### MISCNUM -- Define the Miscibility Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The MISCNUM keyword defines the miscibility region number mixing tables as defined by the TLMIXPAR keyword in the PROPS section, for when the miscibility option has been activated by the MISCIBLE keyword in the RUNSPEC section. MISCNUM also allocates miscible residual oil saturation versus water saturation tables (SORWMIS keyword in the PROPS section) used to calculate the relative permeability and PVT properties for a grid cell.

Note that although this keyword can only be used when the miscibility option is active, it is not necessary to use this keyword even if the MISCIBLE keyword in the RUNSPEC has been activated as the default value of one will be applied to all grid blocks. Secondly, a value of zero for a grid cell results in immiscible fluids in that grid cell.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MISCNUM | MISCNUM defines an array of positive integers greater than or equal to zero, that assign a grid cell to a particular table of mixing parameters as defined by the TLMIXPAR and SORWMIS keywords.<br>A value of zero sets the fluids within a grid cell to be immiscible.<br>The maximum number of MISCNUM regions is set by the NTMIS variable on the MISCIBLE keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a MISCNUM region then the default value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.15: MISCNUM Keyword Description

See also the TLMIXPAR and SORWMIS keyword in the PROPS section.

#### Example

The example below sets three MISCNUM regions in the model on a layer by layer basis, using the EQUALS keyword.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MISCNUM 1 1\* 1\* 1\* 1\* 1 12 / SET REGION 1

MISCNUM 2 1\* 1\* 1\* 1\* 13 55 / SET REGION 2

MISCNUM 3 1\* 1\* 1\* 1\* 56 120 / SET REGION 3

/

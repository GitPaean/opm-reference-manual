### IKRO -- End-Point Scaling of Grid Cell Kro(Swl) (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

IKRO defines the scaling parameter for the imbibition oil relative permeability value at the connate water saturation (ISWL), for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the SATOPTS keyword in the RUNSPEC section has to be activated to invoke the Hysteresis option. The SCALCERS keyword in the PROPS section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | IKRO | IKRO is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned imbibition scaling IKRO values for each cell in the model.<br>Repeat counts may be used, for example 50\*0.500. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this the directional independent version of the keyword used with the end-point scaling option. If directional end-point scaling has been activated then the IKROX±, IKROY± and IKROZ± series of the keywords should be used. |  |  |  |

Table 8.51: IKRO Keyword Description

For the two point scaling option and for the IKRORW or IKRORG oil imbibition relative permeability arrays NOT being present in the input deck the kro value for a grid block is scaled by:

Where:

= the resulting kro value for a grid cell.

= the scaling oil relative permeability value from the IKRO array for a given

cell.

= the oil relative permeability from a grid block's oil relative permeability

table at the grid blocks oil saturation.

= the maximum oil relative permeability from a grid block's oil relative table,

that is at the critical water saturation (Swcr).

If the IKRORW or IKRORG keywords are present in the input deck then the scaling matches the relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the SCALECRS keyword in the PROPS section the critical displacing phase is defined as:

| 1 | KRORW | S ~critical~ = 1.0 -- SWCR - SGL |
| --- | --- | --- |
| 2 | KRORG | S ~critical~ = 1.0 -- SGCR - SWL |

Table 8.52: Critical Displacement Relationships

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of ISWU, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-, instead of the ISWU keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the IKRG, IKRGR, IKRO, IKRORG, IKRORW, IKRW and IKRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is IKRGX, IKRGY and IKRGZ instead of IKRG, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is IKRGX, IKRGX-, IKRGY, IKRGY-,I KRGZ and IKRGZ-, instead of the IKRG keyword.

#### Example

The example below defines an input box for the whole grid and for layers one to three, for layer one IKRO is set equal to 0.850, for layer two IKRO equals 0.875, and for layer three IKRO equals 0.900.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

IKRO 0.8500 1\* 1\* 1\* 1\* 1 1 / IKRO FOR LAYER 1

IKRO 0.8750 1\* 1\* 1\* 1\* 2 2 / IKRO FOR LAYER 2

IKRO 0.9000 1\* 1\* 1\* 1\* 3 3 / IKRO FOR LAYER 3

/

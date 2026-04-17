### KRW -- End-Point Scaling of Grid Cell Krw(Sw =1.0) (Drainage)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

KRW defines the scaling parameter at the maximum drainage water relative permeability value (SWU), that is for Sw = 1.0, for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. The SCALCERS keyword in the PROPS section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | KRW | KRW is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling KRW values for each cell in the model.<br>Repeat counts may be used, for example 50\*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this the directional independent version of the keyword used with the end-point scaling option. If directional end-point scaling has been activated then the KRWX±, KRWY± and KRWZ± series of the keywords should be used. |  |  |  |

Table 8.83: KRW Keyword Description

For the two point scaling option and for the KRWR water relative permeability array NOT present in the input deck the krw value for a grid block is scaled by:

Where:

= the resulting KRW value for a grid cell.

= the scaling water relative permeability value from the KRW array for a

given cell.

= the water relative permeability from a grid block's oil relative permeability

table at the grid blocks water saturation.

= the maximum water relative permeability from a grid block's water

relative table, that is at the maximum water saturation.

If the KRWR keyword is present in the input deck then the scaling matches the relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the SCALECRS keyword in the PROPS section the critical displacing phase is defined as:

| 1 | Gas-Oil | S ~critical~ = 1.0 -- SOWCR - SGL |
| --- | --- | --- |
| 2 | Gas-Oil-Water | S ~critical~ = 1.0 -- SOWCR - SGL |
| 3 | Gas-Water | S ~critical~ = 1.0 -- SGCR |

Table 8.84: Critical Displacement Relationships

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWUX, SWUY and SWUZ instead of SWU, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWUX, SWUX-, SWUY, SWUY-, SWUZ and SWUZ-, instead of the SWU keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the KRG, KRGR, KRW, KRORG, KRORW, KRW and KRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is KRWX, KRWY and KRWZ instead of KRW, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is KRWX, KRWX-, KRWY, KRWY-, KRWZ and KRWZ-, instead of the KRW keyword.

If the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section, then the equivalent imbibition arrays suffixed with the letter I, for example IKRW, can be used to define the KRW for the relative permeability imbibition tables.

#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one KRW is set equal to 0.855, for layer two KRW equals 0.875, and for layer three KRW equals 0.900.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 1 3 / DEFINE BOX AREA

\--

\-- SET KRW VALUES FOR THREE LAYERS IN THE MODEL

\--

KRW

10000\*0.855 10000\*0.875 10000\*0.900 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The next example does exactly the same thing using the EQUALS keyword instead.

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

KRW 0.8550 1\* 1\* 1\* 1\* 1 1 / KRW FOR LAYER 1

KRW 0.8750 1\* 1\* 1\* 1\* 2 2 / KRW FOR LAYER 2

KRW 0.9000 1\* 1\* 1\* 1\* 3 3 / KRW FOR LAYER 3

/

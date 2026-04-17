### KRG -- End-Point Scaling of Grid Cell Krg(Sgu) (Drainage)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

KRG defines the scaling parameter at the maximum drainage gas relative permeability value (SGU), normally SGU is equal to 1.0 - Swc, for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. The SCALCERS keyword in the PROPS section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | KRG | KRG is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling KRG values for each cell in the model.<br>Repeat counts may be used, for example 50\*0.400. dimensionless | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this the directional independent version of the keyword used with the end-point scaling option. If directional end-point scaling has been activated then the KRGX±, KRGY± and KRGZ± series of the keywords should be used. |  |  |  |

Table 8.73: KRG Keyword Description

For the two point scaling option and for the KRGR gas relative permeability array NOT present in the input deck the krg value for a grid block is scaled by:

Where:

= the resulting krg value for a grid cell.

= the scaling gas relative permeability value from the KRG array for a given

cell.

= the gas relative permeability from a grid block's gas-oil table at the grid

blocks gas saturation.

= the maximum gas relative permeability from a grid block's gas-oil table, that

is at the connate water saturation (Swc).

If the KRGR keyword is present in the input deck then the scaling matches the relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the SCALECRS keyword in the PROPS section the critical displacing phase is defined as:

| 1 | Gas-Oil | S ~critical~ = 1.0 -- SOGCR - SWL |
| --- | --- | --- |
| 2 | Gas-Oil-Water | S ~critical~ = 1.0 -- SOGCR - SWL |
| 3 | Gas-Water | S ~critical~ = 1.0 -- SWCR |

Table 8.74: Critical Displacement Relationships

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWUX, SWUY and SWUZ instead of SWU, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWUX, SWUX-, SWUY, SWUY-, SWUZ and SWUZ-, instead of the SWU keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the KRG, KRGR, KRO, KRORG, KRORW, KRW and KRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is KRGX, KRGY and KRGZ instead of KRG, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is KRGX, KRGX-, KRGY, KRGY-, KRGZ and KRGZ-, instead of the KRG keyword.

If the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section, then the equivalent imbibition arrays prefixed with the letter I, for example IKRG, can be used to scale KRG for the relative permeability imbibition tables.

#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one KRG is set equal to 0.555, for layer two KRG equals 0.575, and for layer three KRG equals 0.600.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 1 3 / DEFINE BOX AREA

\--

\-- SET KRG VALUES FOR THREE LAYERS IN THE MODEL

\--

KRG

10000\*0.555 10000\*0.575 10000\*0.600 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The next example does exactly the same thing using the EQUALS keyword instead.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

KRG 0.5550 1\* 1\* 1\* 1\* 1 1 / KRG FOR LAYER 1

KRG 0.5750 1\* 1\* 1\* 1\* 2 2 / KRG FOR LAYER 2

KRG 0.6000 1\* 1\* 1\* 1\* 3 3 / KRG FOR LAYER 3

/

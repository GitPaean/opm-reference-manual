### KRO -- End-Point Scaling of Grid Cell Kro(Swl) (Drainage)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[KRO](#__RefHeading___Toc97395_621662414) defines the scaling parameter for the drainage oil relative permeability value at the connate water saturation ([SWL](#__RefHeading___Toc22881_7842323221)), for all the cells in the model via an array. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. The SCALCERS keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [KRO](#__RefHeading___Toc97395_621662414) | [KRO](#__RefHeading___Toc97395_621662414) is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling [KRO](#__RefHeading___Toc97395_621662414) values for each cell in the model.<br>Repeat counts may be used, for example 50\*0.500. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this the directional independent version of the keyword used with the end-point scaling option. If directional end-point scaling has been activated then the [KROX](#__RefHeading___Toc97395_621662414)±, [KROY](#__RefHeading___Toc97395_621662414)± and [KROZ](#__RefHeading___Toc97395_621662414)± series of the keywords should be used. |  |  |  |

Table 8.77: KRO Keyword Description

For the two point scaling option and for the [KRORW](#__RefHeading___Toc70191_335817223) or [KRORG](#__RefHeading___Toc70189_335817223) oil relative permeability arrays NOT being present in the input deck the kro value for a grid block is scaled by:

Where:

= the resulting kro value for a grid cell.

= the scaling oil relative permeability value from the [KRO](#__RefHeading___Toc97395_621662414) array for a given

cell.

= the oil relative permeability from a grid block's oil relative permeability

table at the grid blocks oil saturation.

= the maximum oil relative permeability from a grid block's oil relative table,

that is at the critical water saturation (Swcr).

If the [KRORW](#__RefHeading___Toc70191_335817223) or [KRORG](#__RefHeading___Toc70189_335817223) keywords are present in the input deck then the scaling matches the relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the [SCALECRS](#__RefHeading___Toc2086108_3315222525) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section the critical displacing phase is defined as:

| 1 | [KRORW](#__RefHeading___Toc70191_335817223) | S ~critical~ = 1.0 -- [SWCR](#__RefHeading___Toc27248_784232322) - [SGL](#__RefHeading___Toc22881_784232322) |
| --- | --- | --- |
| 2 | [KRORG](#__RefHeading___Toc70189_335817223) | S ~critical~ = 1.0 -- [SGCR](#__RefHeading___Toc20428_784232322) - [SWL](#__RefHeading___Toc22881_7842323221) |

Table 8.78: Critical Displacement Relationships

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#__RefHeading___Toc22881_7842323221), [SWCR](#__RefHeading___Toc27248_784232322), [SWU](#__RefHeading___Toc22883_7842323221), [SGL](#__RefHeading___Toc22881_784232322), [SGCR](#__RefHeading___Toc20428_784232322), [SGU](#__RefHeading___Toc22883_784232322), [SOWCR](#__RefHeading___Toc30436_784232322), and [SOGCR](#__RefHeading___Toc30434_784232322) saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [SWUX](#__RefHeading___Toc22883_7842323221), [SWUY](#__RefHeading___Toc22883_7842323221) and [SWUZ](#__RefHeading___Toc22883_7842323221) instead of [SWU](#__RefHeading___Toc22883_7842323221), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [SWUX](#__RefHeading___Toc22883_7842323221), [SWUX-](#__RefHeading___Toc22883_7842323221), [SWUY](#__RefHeading___Toc22883_7842323221), [SWUY-](#__RefHeading___Toc22883_7842323221), [SWUZ](#__RefHeading___Toc22883_7842323221) and [SWUZ-](#__RefHeading___Toc22883_7842323221), instead of the [SWU](#__RefHeading___Toc22883_7842323221) keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the [KRG](#__RefHeading___Toc97393_621662414), [KRGR](#__RefHeading___Toc70187_335817223), [KRO](#__RefHeading___Toc97395_621662414), [KRORG](#__RefHeading___Toc70189_335817223), [KRORW](#__RefHeading___Toc70191_335817223), [KRW](#__RefHeading___Toc97397_621662414) and [KRWR](#__RefHeading___Toc70193_335817223) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [KROX](#__RefHeading___Toc97395_621662414), [KROY](#__RefHeading___Toc97395_621662414) and [KROZ](#__RefHeading___Toc97395_621662414) instead of [KRO](#__RefHeading___Toc97395_621662414), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [KROX](#__RefHeading___Toc97395_621662414), [KROX-](#__RefHeading___Toc97395_621662414), [KROY](#__RefHeading___Toc97395_621662414), [KROY-](#__RefHeading___Toc97395_621662414), [KROZ](#__RefHeading___Toc97395_621662414) and [KROZ-](#__RefHeading___Toc97395_621662414), instead of the [KRO](#__RefHeading___Toc97395_621662414) keyword.

If the hysteresis model option has been activated on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the equivalent imbibition arrays suffixed with the letter I, for example [IKRO](#__RefHeading___Toc97395_6216624141), can be used to define the [KRO](#__RefHeading___Toc97395_621662414) for the relative permeability imbibition tables.

#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one [KRO](#__RefHeading___Toc97395_621662414) is set equal to 0.855, for layer two [KRO](#__RefHeading___Toc97395_621662414) equals 0.875, and for layer three [KRO](#__RefHeading___Toc97395_621662414) equals 0.900.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 1 3 / DEFINE BOX AREA

\--

\-- SET KRO VALUES FOR THREE LAYERS IN THE MODEL

\--

KRO

10000\*0.855 10000\*0.875 10000\*0.900 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The next example does exactly the same thing using the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword instead.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

KRO 0.8550 1\* 1\* 1\* 1\* 1 1 / KRO FOR LAYER 1

KOG 0.8750 1\* 1\* 1\* 1\* 2 2 / KRO FOR LAYER 2

KRO 0.9000 1\* 1\* 1\* 1\* 3 3 / KRO FOR LAYER 3

/

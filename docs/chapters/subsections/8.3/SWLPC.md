### SWLPC -- End-Point Scaling Grid Cell Capillary Pressure Connate Water Saturations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SWLPC](#__RefHeading___Toc179514_1371377330) defines the connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table. The keyword only applies the scaling to the drainage capillary pressures tables, unlike the [SWL](#__RefHeading___Toc22881_7842323221) keyword that applies the scaling to both the capillary pressure and relative permeability tables. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWLPC](#__RefHeading___Toc179514_1371377330) | [SWLPC](#__RefHeading___Toc179514_1371377330) is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword.<br>If [SWLPC](#__RefHeading___Toc179514_1371377330) is omitted from the input deck the values will be defaulted to those on the [SWL](#__RefHeading___Toc22881_7842323221) series of keywords. If the [SWL](#__RefHeading___Toc22881_7842323221) series of keywords are missing from the input deck then the values are taken from the cell allocated capillary pressure table.<br>Repeat counts may be used, for example 30\*0.03 | Taken from [SGL](#__RefHeading___Toc22881_784232322) or from the cell allocated capillary pressure table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Note this the directional independent version of the connate gas saturation array used with the end-point scaling option. If directional end-point scaling has been activated then the [SWLX](#__RefHeading___Toc22881_7842323221)± , [SWLY](#__RefHeading___Toc22881_7842323221)± and SWZ± series of keyword should be used.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.188: SWLPC Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#__RefHeading___Toc22881_7842323221), [SWCR](#__RefHeading___Toc27248_784232322), [SWU](#__RefHeading___Toc22883_7842323221), [SGL](#__RefHeading___Toc22881_784232322), [SGCR](#__RefHeading___Toc20428_784232322), [SGU](#__RefHeading___Toc22883_784232322), [SOWCR](#__RefHeading___Toc30436_784232322), and [SOGCR](#__RefHeading___Toc30434_784232322) saturation grid arrays for the saturation end-points, and the [KRG](#__RefHeading___Toc97393_621662414), KROG, KROW and [KRW](#__RefHeading___Toc97397_621662414) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [SWLX](#__RefHeading___Toc22881_7842323221), [SWLY](#__RefHeading___Toc22881_7842323221) and [SWLZ](#__RefHeading___Toc22881_7842323221) instead of [SWL](#__RefHeading___Toc22881_7842323221) or [SWLPC](#__RefHeading___Toc179514_1371377330). There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [SWLX](#__RefHeading___Toc22881_7842323221), [SWLX-](#__RefHeading___Toc22881_7842323221), [SWLY](#__RefHeading___Toc22881_7842323221), [SWLY-](#__RefHeading___Toc22881_7842323221), [SWLZ](#__RefHeading___Toc22881_7842323221) and [SWLZ-](#__RefHeading___Toc22881_7842323221), instead of the [SWL](#__RefHeading___Toc22881_7842323221) or [SWLPC](#__RefHeading___Toc179514_1371377330) keywords.

M*issing *Some F*unctionality - *Use with Caution.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SWLPC DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SWLPC

300\*0.150 /

The above example defines a constant connate water saturation of 0.15 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

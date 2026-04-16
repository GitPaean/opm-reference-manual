### SGCR -- End-Point Scaling Grid Cell Critical Gas Saturations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SGCR](#__RefHeading___Toc20428_784232322) defines the critical gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The critical gas saturation is defined as the maximum gas saturation for which the gas relative permeability is zero in a two-phase relative permeability table.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SGCR](#__RefHeading___Toc20428_784232322) | [SGCR](#__RefHeading___Toc20428_784232322) is an array of real numbers assigning the critical gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword.<br>Repeat counts may be used, for example 30\*0.03 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Note this the directional independent version of the critical gas saturation used with the end-point scaling option. If directional end-point scaling has been activated then the [SGCRX](#__RefHeading___Toc20428_784232322)± , [SGCRX](#__RefHeading___Toc20428_784232322)± and [SGCRX](#__RefHeading___Toc20428_784232322)± series of keyword should be used.<br>2)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.146: SGCR Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#__RefHeading___Toc22881_7842323221), [SWCR](#__RefHeading___Toc27248_784232322), [SWU](#__RefHeading___Toc22883_7842323221), [SGL](#__RefHeading___Toc22881_784232322), [SGCR](#__RefHeading___Toc20428_784232322), [SGU](#__RefHeading___Toc22883_784232322), [SOWCR](#__RefHeading___Toc30436_784232322), and [SOGCR](#__RefHeading___Toc30434_784232322) saturation grid arrays for the saturation end-points, and the [KRG](#__RefHeading___Toc97393_621662414), [KRGR](#__RefHeading___Toc70187_335817223), [KRO](#__RefHeading___Toc97395_621662414), [KRORG](#__RefHeading___Toc70189_335817223), [KRORW](#__RefHeading___Toc70191_335817223), [KRW](#__RefHeading___Toc97397_621662414) and [KRWR](#__RefHeading___Toc70193_335817223) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [SGCRX](#__RefHeading___Toc20428_784232322), [SGCRY](#__RefHeading___Toc20428_784232322) and [SGCRZ](#__RefHeading___Toc20428_784232322) instead of [SGCR](#__RefHeading___Toc20428_784232322). There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [SGCRX](#__RefHeading___Toc20428_784232322), [SGCRX-](#__RefHeading___Toc20428_784232322), [SGCRY](#__RefHeading___Toc20428_784232322), [SGCRY-](#__RefHeading___Toc20428_784232322), [SGCRZ](#__RefHeading___Toc20428_784232322) and [SGCRZ-](#__RefHeading___Toc20428_784232322), instead of the [SGCR](#__RefHeading___Toc20428_784232322) keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SGCR DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SGCR

300\*0.050 /

The above example defines a constant critical gas saturation of 0.05 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

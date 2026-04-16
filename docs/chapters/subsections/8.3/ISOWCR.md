### ISOWCR -- End-Point Scaling of Grid Cell Critical Oil Saturation to Water (Imbib.)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[ISOWCR](#__RefHeading___Toc30436_7842323221) defines the imbibition critical oil saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#__RefHeading___Toc68146_2267116897) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the hysteresis model option has been activated on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The critical oil saturation with respect to water is defined as the maximum oil saturation for which the oil relative permeability is zero in a two-phase oil-water relative permeability table. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [ISOWCR](#__RefHeading___Toc30436_7842323221) | [ISOWCR](#__RefHeading___Toc30436_7842323221) is an array of real numbers assigning the critical oil saturation with respect to water values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword.<br>Repeat counts may be used, for example 30\*0.30 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the critical gas saturation used with the end-point scaling option. |  |  |  |

Table 8.68: ISOWCR Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#__RefHeading___Toc22881_78423232211), [ISWCR](#__RefHeading___Toc27248_7842323221), [ISWU](#__RefHeading___Toc22883_78423232211), [ISGL](#__RefHeading___Toc22881_7842323222), [ISGCR](#__RefHeading___Toc64693_2379415017), [ISGU](#__RefHeading___Toc22883_7842323222), [ISOWCR](#__RefHeading___Toc30436_7842323221), and [ISOGCR](#__RefHeading___Toc30434_7842323221) saturation grid arrays for the saturation end-points, and the [IKRG](#__RefHeading___Toc506847_2135714711), [IKRORG](#__RefHeading___Toc70189_3358172231), [IKRORW](#__RefHeading___Toc70191_3358172231) and [IKRW](#__RefHeading___Toc97397_6216624141) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [ISOWCRX](#__RefHeading___Toc30436_7842323221), [ISOWCRY](#__RefHeading___Toc30436_7842323221) and [ISOWCRZ](#__RefHeading___Toc30436_7842323221) instead of [ISOWCR](#__RefHeading___Toc30436_7842323221). There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [ISOWCRX](#__RefHeading___Toc30436_7842323221), [ISOWCRX-](#__RefHeading___Toc30436_7842323221), [ISOWCRY](#__RefHeading___Toc30436_7842323221), [ISOWCRY-](#__RefHeading___Toc30436_7842323221), [ISOWCRZ](#__RefHeading___Toc30436_7842323221) and [ISOWCRZ-](#__RefHeading___Toc30436_7842323221), instead of the [ISOWCR](#__RefHeading___Toc30436_7842323221) keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISOWCR DATA FOR ALL CELLS

\-- (NX x NY x NZ = 300)

\--

ISOWCR

300\*0.200 /

The above example defines a constant critical gas saturation of 0.20 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section

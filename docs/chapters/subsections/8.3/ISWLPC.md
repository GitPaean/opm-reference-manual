### ISWLPC -- End-Point Scaling Grid Cell Capillary Pressure Connate Water Saturations (Imbibition)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[ISWLPC](#__RefHeading___Toc176392_1371377330) defines the imbibition connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#__RefHeading___Toc68146_2267116897) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the hysteresis model option has been activated on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table. The keyword only applies the scaling to the imbibition capillary pressures tables, unlike the [ISWL](#__RefHeading___Toc22881_78423232211) keyword that applies the scaling to both the capillary pressure and relative permeability tables. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [ISWLPC](#__RefHeading___Toc176392_1371377330) | [ISWLPC](#__RefHeading___Toc176392_1371377330) is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword.<br>If [ISWLPC](#__RefHeading___Toc176392_1371377330) is omitted from the input deck the values will be defaulted to those on the [ISGL](#__RefHeading___Toc22881_7842323222) series of keywords. If the [ISWL](#__RefHeading___Toc22881_78423232211) series of keywords are missing from the input deck then the values are taken from the cell allocated capillary pressure table.<br>Repeat counts may be used, for example 30\*0.15 | Taken from [SWL](#__RefHeading___Toc22881_7842323221) or from the cell allocated capillary pressure table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the connate gas saturation array used with the end-point scaling option. |  |  |  |

Table 8.71: ISWLPC Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#__RefHeading___Toc22881_78423232211), [ISWCR](#__RefHeading___Toc27248_7842323221), [ISWU](#__RefHeading___Toc22883_78423232211), [ISGL](#__RefHeading___Toc22881_7842323222), [ISGCR](#__RefHeading___Toc64693_2379415017), [ISGU](#__RefHeading___Toc22883_7842323222), [ISOWCR](#__RefHeading___Toc30436_7842323221), and [ISOGCR](#__RefHeading___Toc30434_7842323221) saturation grid arrays for the saturation end-points, and the [IKRG](#__RefHeading___Toc506847_2135714711), [IKRORG](#__RefHeading___Toc70189_3358172231), [IKRORW](#__RefHeading___Toc70191_3358172231) and [IKRW](#__RefHeading___Toc97397_6216624141) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is [ISWLX](#__RefHeading___Toc22881_78423232211), [ISWLY](#__RefHeading___Toc22881_78423232211) and [ISWLZ](#__RefHeading___Toc22881_78423232211) instead of [ISWL](#__RefHeading___Toc22881_78423232211) or [ISWLPC](#__RefHeading___Toc176392_1371377330). There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is [ISWLX](#__RefHeading___Toc22881_78423232211), [ISWLX-](#__RefHeading___Toc22881_78423232211), [ISWLY](#__RefHeading___Toc22881_78423232211), [ISWLY-](#__RefHeading___Toc22881_78423232211), [ISWLZ](#__RefHeading___Toc22881_78423232211) and [ISWLZ-](#__RefHeading___Toc22881_78423232211), instead of the [ISWL](#__RefHeading___Toc22881_78423232211) or [ISWLPC](#__RefHeading___Toc176392_1371377330) keywords.

M*issing *Some F*unctionality - *Use with Caution.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISWLPC DATA FOR ALL CELLS (

\-- NX x NY x NZ = 300)

\--

ISWLPC

300\*0.150 /

The above example defines a constant connate water saturation of 0.15 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

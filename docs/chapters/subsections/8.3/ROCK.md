### ROCK -- Define the Rock Compressibility for Various Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[ROCK](#__RefHeading___Toc45809_719036256) defines the rock compressibility for various regions in the model. The number of [ROCK](#__RefHeading___Toc45809_719036256) vector data sets is defined by the NTPVT parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the allocation of the [ROCK](#__RefHeading___Toc45809_719036256) tables to different grid blocks in the model is done via the [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section. One data set consists of one record or line which is terminated by a "/".

This keyword must be defined in the OPM Flow input deck.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | PRESS is a real number defining the rock reference pressure for the other parameters for this data set. | Default |
| psia<br>14.7 | barsa<br>1.0132 | atma<br>1.0 |  |
| 2 | RCOMP | RCOMP is a real number defining the rock compressibility (cf) at the rock reference pressure and is defined as: | Defined |
| 1/psia<br>0.0 | 1/barsa<br>0.0 | 1/atma<br>0.0 |  |
| Notes:<br>1)  The keyword is followed by NTPVT vectors as declared by the NTPVT parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>Note, however, that if [ROCKOPTS](#__RefHeading___Toc111814_2939291539)(ROCKOPT3) parameter has been used to set the allocation of the [ROCK](#__RefHeading___Toc45809_719036256) data via the [ROCKNUM](#__RefHeading___Toc118210_2939291539) array, then the number of [ROCK](#__RefHeading___Toc45809_719036256) vectors should correspond to the value entered on [TABDIMS](#__RefHeading___Toc89327_327352552)(NTROCC) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Similarly, if the [ROCKOPTS](#__RefHeading___Toc111814_2939291539)(ROCKOPT3) has been used to set the assignment of the [ROCK](#__RefHeading___Toc45809_719036256) data via the [SATNUM](#__RefHeading___Toc71136_2752266063) array, then the number of vectors should correspond to the value entered via the [TABDIMS](#__RefHeading___Toc89327_327352552)(NTSFUN) parameter, since the tables will be allocated via the [SATNUM](#__RefHeading___Toc71136_2752266063) array.<br>1)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.125: ROCK Keyword Description

The simulator adjusts the pore volume based on the reference pressure (PRESS), that is:

where:

= rock compressibility (RCOMP) at the reference pressure (PRESS),

= initial grid cell pressure,

= reference pressure (PRESS),

= pore volume at initial conditions, and

= pore volume at at the reference pressure.

See also the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) and [ROCKTAB](#__RefHeading___Toc107256_3812137098) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Examples

The following shows the [ROCK](#__RefHeading___Toc45809_719036256) keyword for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set to one.

\--

\-- ROCK COMPRESSIBILITY

\--

\-- REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE

\-- AS THE PORV IS ALREADY AT RESERVOIR CONDITIONS (OPM FLOW USES THE

\-- REFERENCE PRESSURE) TO CONVERT THE GIVEN PORV TO RESERVOIR CONDITIONS

\-- USING THE DATA ON THE ROCK KEYWORD)

\--

\-- REF PRES CF

\-- PSIA 1/PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

ROCK

3966.9 5.0E-06 / ROCK COMPRESSIBILITY

The next example shows the [ROCK](#__RefHeading___Toc45809_719036256) keyword for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set to three.

\--

\-- ROCK COMPRESSIBILITY

\--

\-- REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE

\-- AS THE PORV IS ALREADY AT RESERVOIR CONDITIONS (OPM FLOW USES THE

\-- REFERENCE PRESSURE) TO CONVERT THE GIVEN PORV TO RESERVOIR CONDITIONS

\-- USING THE DATA ON THE ROCK KEYWORD)

\--

\-- REF PRES CF

\-- PSIA 1/PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

ROCK

3566.9 5.0E-06 / ROCK COMPRESSIBILITY REGION 1

3966.9 5.5E-06 / ROCK COMPRESSIBILITY REGION 2

4566.9 6.0E-06 / ROCK COMPRESSIBILITY REGION 3

The above example defines three [ROCK](#__RefHeading___Toc45809_719036256) tables and assumes that NTPVT equals three on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no terminating "/" for this keyword, and thus the number entries must match the value entered via the [TABDIMS](#__RefHeading___Toc89327_327352552)(NTPVT), [TABDIMS](#__RefHeading___Toc89327_327352552)(NTROCC), or [TABDIMS](#__RefHeading___Toc89327_327352552)(NTSFUN) parameters, depending on the option selected via the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword.

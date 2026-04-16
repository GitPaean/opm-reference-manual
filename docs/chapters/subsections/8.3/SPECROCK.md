### SPECROCK -- Define the Specific Heat of the Reservoir Rock

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SPECROCK](#__RefHeading___Toc121481_83452205) defines the specific heat of the reservoir rock for various PVT regions in the model for when the [THERMAL](#__RefHeading___Toc137276_650382403) option has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The number of [SPECROCK](#__RefHeading___Toc121481_83452205) vector data sets is defined by the NTSFUN parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the allocation of the [SPECROCK](#__RefHeading___Toc121481_83452205) data sets to different grid blocks in the model is done via the [SATNUM](#__RefHeading___Toc71136_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section.

This keyword can only be used if OPM's Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#__RefHeading___Toc146397_3544483072) | A columnar vector of real monotonically increasing down the column values that define the temperature for the corresponding rock specific heat values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | ROCKHEAT | ROCKHEAT is a columnar vector of positive real numbers defining the specific heat of the rock at the corresponding temperature, [TEMP](#__RefHeading___Toc146397_3544483072). | None |
| Btu/ft3/oR | kJ/m3/K | J/cc/K |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.171: SPECROCK Keyword Description

See also the [SPECHEAT](#__RefHeading___Toc121479_83452205) keyword to define the specific heat relationships for the oil, water and gas phases.

#### Example

The example below defines three rock specific heat versus temperature tables assuming NTSFUN equals three and NSSFUN is greater than or equal to two on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- SPECIFIC HEAT OF ROCK

\--

SPECROCK

\-- TEMP SPECHEAT

\-- ROCK

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 20.000

250.000 20.000 / TABLE NO. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 21.000

260.000 21.000 / TABLE NO. 02

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 23.000

270.000 23.000 / TABLE NO. 03

There is no terminating "/" for this keyword.

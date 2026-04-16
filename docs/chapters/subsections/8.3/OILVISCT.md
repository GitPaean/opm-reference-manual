### OILVISCT -- Define Oil Viscosity versus Temperature Functions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[OILVISCT](#__RefHeading___Toc107282_57619843) defines the oil viscosity as a function of temperature for when OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The reference pressure and solution gas-oil ratio of the oil for this table is given by the [VISCREF](#__RefHeading___Toc121487_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. Note this is an OPM Flow keyword used with OPM Flow's black-oil thermal model that is not available in the commercial simulator's black-oil thermal formulation.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#__RefHeading___Toc146397_3544483072) | A columnar vector of real monotonically increasing down the column values that defines the temperature values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | VIS | A columnar vector of real increasing down the column values that defines the oil viscosity for the corresponding temperature values ([TEMP](#__RefHeading___Toc146397_3544483072)).<br>VIS should be given at the reference pressure and solution gas-oil ratio as defined by PRESS and [RS](#__RefHeading___Toc137361_1317547213) variables on the [VISCREF](#__RefHeading___Toc121487_83452205) keyword. | None |
| cP | cP | cP |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.93: OILVISCT Keyword Description

There is no terminating "/" for this keyword.

#### Example

The following example shows the [OILVISCT](#__RefHeading___Toc107282_57619843) keyword for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set equal to one.

\--

\-- OIL VISCOSITY VERSUS TEMPERATURE TABLES (OPM FLOW EXTENSION KEYWORD)

\--

\-- OIL OIL

\-- TEMP VISC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

OILVISCT

100.0 0.600

110.0 0.650

120.0 0.680

150.0 0.720

165.0 0.725 / TABLE NO. 01

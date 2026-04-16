### SPECHEAT -- Define the Specific Heat of Oil, Water and Gas

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SPECHEAT](#__RefHeading___Toc121479_83452205) defines the specific heat of the oil, water and gas phases for various PVT regions in the model for when the [THERMAL](#__RefHeading___Toc137276_650382403) option has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The number of [SPECHEAT](#__RefHeading___Toc121479_83452205) vector data sets is defined by the NTPVT parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the allocation of the [SPECHEAT](#__RefHeading___Toc121479_83452205) data sets to different grid blocks in the model is done via the [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#__RefHeading___Toc146397_3544483072) | A columnar vector of real monotonically increasing down the column values that define the temperature for the corresponding oil, water and gas specific heat values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | OILSHEAT | OILSHEAT is a columnar vector of positive real numbers defining the specific heat of oil at the corresponding temperature, [TEMP](#__RefHeading___Toc146397_3544483072). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 3 | WATSHEAT | WATSHEAT is a columnar vector of positive real numbers defining the specific heat of water at the corresponding temperature, [TEMP](#__RefHeading___Toc146397_3544483072). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 4 | GASSHEAT | GASHEAT is a columnar vector of positive real numbers defining the specific heat of gas at the corresponding temperature, [TEMP](#__RefHeading___Toc146397_3544483072). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.170: SPECHEAT Keyword Description

See also the [SPECROCK](#__RefHeading___Toc121481_83452205) keyword to define the reservoir rock specific heat.

#### Example

The example below defines three fluid phases specific heat versus temperature tables assuming NTPVT equals three and NPPVT is greater than or equal to two on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- SPECIFIC HEAT OF OIL, WATER AND GAS TABLE

\--

SPECHEAT

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5000 1.5000 0.5000

250.000 0.5000 1.5000 0.5000 / TABLE NO. 01

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5500 1.5000 0.5000

260.000 0.5500 1.5000 0.5000 / TABLE NO. 02

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5500 1.5500 0.5000

270.000 0.6000 1.5500 0.5000 / TABLE NO. 03

There is no terminating "/" for this keyword.

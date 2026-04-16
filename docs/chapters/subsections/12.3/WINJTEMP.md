### WINJTEMP -- Define Injection Fluid Thermal Properties

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WINJTEMP](#__RefHeading___Toc152097_2509125675) defines the injection fluid thermal properties for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Only water and gas injection is supported.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection fluid thermal properties are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| 2 | STEAMQAL | STEAMQAL is a real positive value greater than or equal to zero and less than or equal to one that defines the steam quality of the injected fluid for the defined well.<br>This parameter should be defaulted using 1\* as STEAMQAL is not used by OPM FLOW, as only water and gas injection is supported.<br>This data is used by the commercial simulator's [THERMAL](#__RefHeading___Toc137276_650382403) option and is not supported by OPM Flow's [THERMAL](#__RefHeading___Toc137276_650382403) option. | 1\* |
| dimensionless | dimensionless | dimensionless |  |
| 3 | [TEMP](#__RefHeading___Toc146397_3544483072) | [TEMP](#__RefHeading___Toc146397_3544483072) is a real positive value that defines the temperature of the injected fluid for the defined well. | None |
| ^o^F | ^o^C | ^o^C |  |
| 4 | PRES | PRES is a real positive value that defines the pressure of the injected fluid for the defined well. | None |
| psia | barsa | atma |  |
| 5 | ENTHALPY | ENTHALPY is a real positive value that defines the specific enthalpy of the injected fluid for the defined well.<br>This is data is used by the commercial simulator's [THERMAL](#__RefHeading___Toc137276_650382403) option and is not supported by OPM Flow's [THERMAL](#__RefHeading___Toc137276_650382403) option. | None |
| Btu/lbs-M | kJ/kg-M | J/gm-M |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.102: WINJTEMP Keyword Description

#### Example

The following example shows the [WINJTEMP](#__RefHeading___Toc152097_2509125675) keyword for when OPM Flow's temperature option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- INJECTION FLUID THERMAL PROPERTIES

\--

\-- WELL STEAM INJ INJ SPEC

\-- NAME QUAL TEMP PRES ENTH

WINJTEMP

WI01 1\* 68.0 220.0 1\* /

WI02 1\* 70.0 230.0 1\* /

/

Here the water injection fluid's temperature and pressure, in field units, for two water injections well are defined. Notice that both the steam quality and the specific enthalpy of the injected fluid for the defined wells are defaulted (or skipped), as OPM Flow's [THERMAL](#__RefHeading___Toc137276_650382403) option does not support this data.

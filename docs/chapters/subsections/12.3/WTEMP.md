### WTEMP -- Define An Injection Well's Fluid Temperature

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WTEMP](#__RefHeading___Toc192631_213178337) keyword defines the temperature of the injection fluid being injected by an injection well.

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for an injection well for which the injection well fluid's temperature data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | [TEMP](#__RefHeading___Toc146397_3544483072) | A real positive value greater than zero that defines the temperature of the injected fluid. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  Injection wells that are not declared via this keyword have their injection fluid temperatures set to zero degrees in the run's units.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.126: WTEMP Keyword Description

See also the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword to define a group's injection targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the injected fluid temperatures for three water injection wells for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- DEFINE INJECTION WELL FLUID TEMPERATURE

\--

\-- WELL FLUID

\-- NAME TEMP.

\-- \-\-\-\-\-\-\--

WTEMP

WI01 39.00 /

WI02 37.00 /

WI03 39.00 /

/

Here wells WI01 and WI03 inject water with a water temperature of 39 oF and well WI02's injection water temperature is 37 oF.

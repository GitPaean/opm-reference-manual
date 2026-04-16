### WPOLYMER -- Define Water Injection Well Polymer and Salt Concentrations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPOLYMER](#__RefHeading___Toc121643_2412586160) keyword defines a water injection well's polymer and salt injection stream concentrations that are to be used for when the polymer and salt options have been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) and [BRINE](#__RefHeading___Toc162083_289573908) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Note that if the Brine option has not be activated by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the salt concentrations in the third column are ignored. Secondly, if the brine phase is declared but the polymer phase has not been made active, then the [WSALT](#__RefHeading___Toc950256_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section can be used to set the salt concentration.

Currently the Brine option is not implemented in OPM Flow and therefore both the SALTCON and GRPSALT variables on this keyword are ignored.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | POLCON | A real positive value that defines the polymer concentration of the well's injection stream.<br>This value may be specified using a User Defined Argument (UDA). | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 3 | SALTCON | A real positive value that defines the salt concentration of the well's injection stream.<br>This value may be specified using a User Defined Argument (UDA).<br>This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 4 | GRPPOL | A character string of up to eight characters in length that defines the group name for which the group's produced polymer concentration should be used instead of the well's POLCON value stated on this keyword. | None |
| 5 | GRPSALT | A character string of up to eight characters in length that defines the group name for which the group's produced salt concentration should be used instead of the well's SALTCON value stated on this keyword.<br>This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored. | None |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.114: WPOLYMER Keyword Description

Water injection wells that are not declared via this keyword have their concentrations defaulted to zero.

See also the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the polymer and salt injection stream concentrations for three water injection wells for when the polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- DEFINE WATER INJECTION WELL POLYMER AND SALT CONCENTRATIONS

\--

\-- WELL POLYMER SALT POLYMER SALT

\-- NAME POLCON SALTCON GROUP GROUP

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

WPOLYMER

WI01 0.2500 /

WI02 1\* 1\* GRPINJ1 /

WI03 0.2500 1\* GRPINJ1 /

/

The polymer concentration for well WI01 is set to 0.25 and the stated polymer concentration for well WI02 will be ignored, as both WI02 and WI03 will re-inject the produced polymer from the GRPINJ1 group.

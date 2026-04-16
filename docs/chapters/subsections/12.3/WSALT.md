### WSALT -- Define Water Injection Well Salt Concentrations

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSALT](#__RefHeading___Toc950256_4263943340) keyword defines a water injection well's salt injection stream concentration that is to be used for when the salt option has been activated by the [BRINE](#__RefHeading___Toc162083_289573908) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note that if the Polymer option has also been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the [WPOLYMER](#__RefHeading___Toc121643_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section should be used to enter both the polymer and salt concentrations.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the injection salt concentrations are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | SALTCON | A real positive vector of values that defines the salt concentration of the well's injection stream and consists of:<br>1)  If the Standard Brine model has been invoked by the [BRINE](#__RefHeading___Toc162083_289573908) keyword, then SALTCON consist of one value representing the injection salt concentration;<br>2)  If OPM Flow's Water Vaporization and Salt Precipitation models have been activated by the [VAPWAT](#__RefHeading___Toc317543_3149455253) and [PRECSALT](#__RefHeading___Toc332782_3149455253) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then SALTCON consist of one value representing the injection salt concentration; or,<br>3)  If the Multi-Component Brine option has been activated by the [BRINE](#__RefHeading___Toc162083_289573908) and [ECLMC](#__RefHeading___Toc206960_803326780) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then SALTCON consists of a vector of values representing the salt concentration of each brine within the injected brine mixture.<br>Only options (1) and (2) are currently supported.<br>This value may be specified using a User Defined Argument (UDA).<br>Note if SALTCON is defaulted (1\*) then the well's salt concentration will be equal to the well's group salt concentration. | 1\* |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.117: WSALT Keyword Description

Water injection wells that are not declared via this keyword have their concentrations defaulted to zero.

See also the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Examples

The following example defines the salt injection stream concentration for three water injection wells for when the brine phase has been activated by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- DEFINE WATER INJECTION WELL SALT CONCENTRATIONS (STANDARD)

\--

\-- WELL SALT-1 SALT-2 SALT-3 SALT-4

\-- NAME SALTCON SALTCON SALTCON SALTCON

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

WSALT

WI01 0.2500 /

WI02 1\* /

WI03 0.2500 /

/

The salt concentration for both well WI01 and WI03 is set to 0.25, and for well WI02 the salt concentration will be taken from the well's group salt concentration.

The next example is based on using the Multi-Component Brine option, that is the [BRINE](#__RefHeading___Toc162083_289573908) and [ECLMC](#__RefHeading___Toc206960_803326780) keywords have been used in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and assuming three salts.

\--

\-- DEFINE WATER INJECTION WELL SALT CONCENTRATIONS (MULTIPLE)

\--

\-- WELL SALT-1 SALT-2 SALT-3 SALT-4

\-- NAME SALTCON SALTCON SALTCON SALTCON

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

WSALT

WI01 0.1500 0.0500 0.0500 /

WI02 0.1500 0.0500 0.0500 /

WI03 0.2000 0.0500 0.0600 /

/

Here the salt concentrations for both well WI01 and WI02 are set to 0.1500, 0.0500, 0.0500 for the three salts and for well WI03 the salt concentrations are 0.2000, 0.0500 and 0.0600.

Note that OPM Flow does not currently support the Multi-Component brine model.

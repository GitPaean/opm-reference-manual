### WINJFCNC -- Define Injection Well Filtrate Concentration

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WINJFCNC](#REF_HEADING_KEYWORD_WINJFCNC) keyword defines the injected filtrate concentration for wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the filter cake properties are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | FCONCPPM | A real positive value that defines the volumetric concentration of filtrate in the injected water.<br>This value may be specified using a User Defined Argument (UDA). | 0 |
| ppm | ppm | ppm |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".<br>3)  New records overwrite previously specified data. |  |  |  |

Table 12.3.296.1: WINJFCNC Keyword Description

See also the [WINJDAM](#REF_HEADING_KEYWORD_WINJDAM) keyword to define the filter cake properties and the [WINJCLN](#REF_HEADING_KEYWORD_WINJCLN) keyword to signal that a filter cake should be completely or partially cleaned. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the filtrate injection concentration for a water injection well using [WINJFCNC](#REF_HEADING_KEYWORD_WINJFCNC):

\--

\-- WELL FILTRATE INJECTION CONCENTRATION

\--

\-- WELL FILTRATE

\-- NAME CONC

WINJFCNC

INJ-A1 10 /

INJ-B\* 30 /

/

Well INJ-A1 has a filtrate concentration of 10 ppm in the injection water, and wells matching INJ-B\* have a concentration of 30 ppm.

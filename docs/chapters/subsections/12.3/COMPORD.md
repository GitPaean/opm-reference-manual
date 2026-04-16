### COMPORD -- Define Well Connection Ordering

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [COMPORD](#__RefHeading___Toc97657_3261743917) keyword defines how the well connection data entered on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section are to be ordered for a well.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | [COMPORD](#__RefHeading___Toc97657_3261743917) | A character string that defines the method for ordering the well connections given on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword, and should be set to [DEPTH](#__RefHeading___Toc58139_3701168388), INPUT, or TRACK.<br>1)  [DEPTH](#__RefHeading___Toc58139_3701168388): The connections are ordered by a connection's true vertical depth from the shallowest to the deepest. If multiple connections are at the same depth then these connections are sub ordered by the sequence they were entered on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword.<br>2)  INPUT: This option results in the connections being ordered in the same sequence as entered via the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword. In this case the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well.<br>3)  TRACK: This option enables OPM Flow to trace the well connections through the grid to obtain the correct order for the connections. If the supplied [COMPDAT](#__RefHeading___Toc97651_3261743917) indicates the well is vertical (via the DIRECT variable being equal to Z on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword) then the [DEPTH](#__RefHeading___Toc58139_3701168388) option will be applied instead.<br>All options are now *supported by OPM Flow*. | TRACK |
| Notes:<br>1)  The keyword is followed by any number of records.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.15: COMPORD Keyword Description

See also the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the connections for two vertical oil wells using the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword and the [COMPORD](#__RefHeading___Toc97657_3261743917) to defined the connection ordering for the wells.

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

OP01 1\* 1\* 20 56 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 1\* 1\* 75 100 SHUT 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP02 35 96 75 100 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

\--

\-- DEFINE WELL CONNECTION ORDERING

\--

\-- WELL COMPL

\-- NAME ORDER

COMPORD

OP01 DEPTH /

OP02 DEPTH /

/

The [DEPTH](#__RefHeading___Toc58139_3701168388) option has been chosen because both wells are vertical. Also one could use the following format instead for the [COMPORD](#__RefHeading___Toc97657_3261743917):

\--

\-- DEFINE WELL CONNECTION ORDERING

\--

\-- WELL COMPL

\-- NAME ORDER

COMPORD

\* DEPTH /

/

as both wells should utilize the [DEPTH](#__RefHeading___Toc58139_3701168388) option. This version would set all wells in the model to [DEPTH](#__RefHeading___Toc58139_3701168388) connection ordering.

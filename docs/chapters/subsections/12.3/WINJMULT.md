### WINJMULT -- Define Well Pressure Dependent Injectivity Multipliers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WINJMULT](#__RefHeading___Toc121402_332691817) keyword defines pressure dependent injectivity multipliers for injection wells and can be used to approximate the increase or decrease in a well's injectivity due to hydraulic fracturing in water injection wells. Only injection wells are processed by this keyword, even if production wells have been entered by the keyword.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | FRACPRES | FRACPRES is the fracture opening pressure (Pfractue) used in equation . | None |
| psia | barsa | atma |  |
| 3 | ALPHA | ALPHA is the multiplier gradient, *α*, in equation . | Defined |
| 1/psia<br>0.0 | 1/barsa<br>0.0 | 1/atma<br>0.0 |  |
| 4 | OPTION | A defined character string that determines how the data on this keyword is applied, and should be set to one of the following character strings:<br>1)  CIRR: The injectivity multiplier as applied to the selected connections (I, J, K) is *irreversibl*e, and the pressure at the *connection's sand face* (Pwbhp) is used in equation , instead of the well's flowing bottom-hole pressure.<br>This option means that even if the pressures in the wellbore, and therefore the sand face pressures, later declines, injectivity remains unchanged for all the connections.<br>1)  CREV: The injectivity multiplier as applied to the selected connections (I, J, K) is *reversible*, and the pressure at the *connection's sand face* is used in equation ,<br>The reversibility of this option means that if the pressures in the wellbore, and therefore the sand face pressures, later declines, injectivity will also decline for *al*l the connections.<br>1)  WREV: The injectivity multiplier as applied to all connections in the well is reversible, and the wells' *flowing bottom-hole pressure* (*P*~*wbhp*~) is used in equation , instead of the pressure at the connection's sand face. The connections stipulated by (I, J, K) are ignored.<br>The reversibility of this option means that if the pressures in the wellbore, later declines, injectivity will also decline for all the connections. | WREV |
| 5 | I | An integer value less than or equal to NX that defines the connection location in the I-direction.<br>If set to zero, a negative value, or defaulted with 1\* then all connections in the I-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1\* |
| 6 | J | An integer value less than or equal to NY that defines the connection location in the J-direction.<br>If set to zero, a negative value, or defaulted with 1\* then all connections in the J-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1\* |
| 7 | K | An integer value less than or equal to NZ that defines the connection location in the K-direction.<br>If set to zero, a negative value, or defaulted with 1\* then all connections in the K-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1\* |
| Notes:<br>1)  The keyword is followed by any number of records.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

*Table 12.3.296.1: WINJMULT Keyword Description*
The methodology for applying the well pressure dependent injectivity multipliers is outlined in equation .

where:

*Multiplier* = the resulting multiplier to be applied to the selected connections.

*α* = the ALPHA multiplier gradient in .

*P*~*WBHP*~ = either the well's current flowing bottom-hole pressure, or the selected

individual connection's sand face pressure.

*P*~*fracture*~ = the effective fracture opening pressure, FRACPRES in .

The equation is applied every time there is a calculation to determine a well's flow rate, this results in the calculated mobility rates being scaled up by the Multiplier value in equation . Note also that since the scaling is performed on the connection fluid mobility values, then the reported connection transmissibilities in the print file etc. remain unchanged.

#### Example

The example below show the [WINJMULT](#__RefHeading___Toc121402_332691817) keyword for three water injection wells.

\--

\-- DEFINE WELL CONNECTION MULTIPLIERS

\--

\-- WELL FRAC MULT FRAC \--LOCATION\--

\-- NAME PRES VALUE OPTN I J K

WINJMULT

WI01 4200 0.0250 1\* 1\* 1\* 1\* /

WI02 4250 0.0025 CIRR 1\* 1\* 145 /

WI02 4250 0.0025 CIRR 1\* 1\* 146 /

WI02 4250 0.0025 CIRR 1\* 1\* 147 /

WI03 4400 0.0055 CREV 1\* 1\* 160 /

WI03 4400 0.0055 CREV 1\* 1\* 165 /

/

The first well, WI01, uses the default value for OPTION, that is WREV, which means that the injectivity multiplier will be applied to all the connections in the well and the well's bottom-hole pressure is used in the calculation. In this case the process is reversible. The second well, WI02, applies the injectivity multiplier to all connections in layers 145 to 147 using the sand face pressures in the calculation, and the process is irreversible. Finally for well WI03, the multiplier is applied to all connections in layers 160 and 165 using the sand face pressures in the calculation, and in this case the process is reversible.

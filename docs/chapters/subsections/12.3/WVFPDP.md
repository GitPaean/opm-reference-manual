### WVFPDP -- Modify Well BHP Obtained from VFP Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WVFPDP](#__RefHeading___Toc1443515_4263943340) keyword modifies a well's Bottom-Hole Pressure ("BHP") estimated by the simulator by interpolation of the Vertical Flow Performance ("VFP") tables. The production VFP tables are entered via the [VFPPROD](#__RefHeading___Toc121919_2556401936) keyword and the injection tables by the [VFPINJ](#__RefHeading___Toc121917_2556401936) keyword; both keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Note that simulator automatically adjusts the interpolated BHP to account for hydrostatic head using the density of the wellbore fluid and the difference between a well's BHP reference depth, as per the BHPREF parameter on the [WELSPECS](#__RefHeading___Toc268463_1366622701) or [WELSPECL](#__RefHeading___Toc147691_6053652) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, and the VFPREF parameter reference depth on the [VFPPROD](#__RefHeading___Toc121919_2556401936) and [VFPINJ](#__RefHeading___Toc121917_2556401936) keywords. Thus, [WVFPDP](#__RefHeading___Toc1443515_4263943340) applies an additional adjustment in order to match a well's flow rate to a given tubing head pressure, by adjusting the BHP.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which VFP interpolated BHP adjustment is to be applied.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONPROD](#__RefHeading___Toc146754_4203985108) (or [WCONINJE](#__RefHeading___Toc146750_4203985108)) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | DELTAP | A real positive or negative value that is added to the VFP interpolated BHP value (BHPVFP).<br>A positive value of DELTAP increases the BHP and therefore makes a production well less productive; whereas, a negative value is subtracted from the BHP and therefore increases the productivity of a production well.<br>Consequently, the opposite effect occurs for injection wells, that is, a positive value of BHPVFP increases the BHP and therefore increases an injection well's injectivity; whereas, a negative value is subtracted from the BHP and therefore decreases the injectivity of an injection well. | 0.0 |
| psia | barsa | atma |  |
| 3 | MULTP | MULTP is a real positive or negative value that scales the tubing pressure loss by the following equation;<br>Thus, a MULTP value greater then 1.0 increases the BHP and therefore makes a production well less productive; whereas, a value less than 1.0 increases the productivity of a production well. Consequently, the opposite effect occurs for injection wells | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.130: WVFPDP Keyword Description

#### Example

The following example below shows three oils operating under THP control.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- WELL PRODUCTION WELL CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS LIQ RES BHP THP VFP VFP

\-- NAME SHUT MODE RATE RATE RATE RATE RATE PRES PRES TABLE ALFQ

WCONPROD

OP01 OPEN THP 1\* 1\* 1\* 5000 1\* 750.0 500. 9 1\* /

OP02 OPEN THP 1\* 1\* 1\* 5000 1\* 750.0 500. 9 1\* /

OP03 OPEN THP 1\* 1\* 1\* 5000 1\* 750.0 500. 9 1\* /

/

\--

\-- WELL VFP BHP-THP CORRECTION DATA

\--

\-- WELL BHP BHP

\-- NAME DELTAP MULTP

WVFPDP

OP01 20.O 1\* /

OP01 -5.O 1\* /

OP01 0.O 1.10 /

/

Well OP01 has a delta pressure correction of 20 psia applied to it's BHP resulting in a reduction in the well's productivity for the given 500.0 psia THP operating target. For well OP02, the well's productivity is increased by subtracting 5.0 psia from the BHP. And finally for well OP03, the MULTP value of 1.10 decreases the well's productivity by increasing the pressure loss between the THP and BHP by 10%.

### WELTARG -- Modify Well Target and Constraint Values

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WELTARG](#__RefHeading___Toc134888_2055188184) keyword modifies the target and constraints values of both rates and pressures for previously defined wells without having to define all the variables on the well control keywords: [WCONPROD](#__RefHeading___Toc146754_4203985108), [WCONHIST](#__RefHeading___Toc134880_2055188184), [WCONINJE](#__RefHeading___Toc146750_4203985108), or [WCONINJH](#__RefHeading___Toc146752_4203985108). Variables not changed by the [WELTARG](#__RefHeading___Toc134888_2055188184) keyword remain the same as those previously entered via the well control keywords or previously entered [WELTARG](#__RefHeading___Toc134888_2055188184) keywords. Note that the well must still be initially fully defined using the [WCONPROD](#__RefHeading___Toc146754_4203985108) or [WCONINJE](#__RefHeading___Toc146750_4203985108) keywords. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production rates and pressures data are being redefined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONPROD](#__RefHeading___Toc146754_4203985108) (or [WCONINJE](#__RefHeading___Toc146750_4203985108)) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | TARGET | A defined character string that sets the item to be changed for the well the value of the item is set by item (3).<br>1)  ORAT: reset the surface oil production rate value as defined by item (3).<br>2)  WRAT: reset the surface water production rate value as defined by item (3).<br>3)  GRAT: reset the surface gas production rate value as defined by item (3).<br>4)  LRAT: reset the surface liquid (oil plus water) production rate value as defined by (3).<br>5)  CRAT: reset the linearly combined calculated rate value as defined by (3). *This option is not supported*.<br>6)  RESV: reset the in situ reservoir volume rate value as defined by (3).<br>7)  BHP: reset the bottom-hole pressure value as defined by item (3).<br>8)  THP: reset the tubing head pressure value for the well as defined by item (3).<br>9)  VFP: reset the vertical lift performance table number as defined by (3).<br>10) LIFT: reset the artificial lift quantity for use with vertical lift performance tables.<br>11) GUID: reset the guide rate value for wells operating under group control.<br>The commercial compositional simulator options: WGRA, NGL, CVAL, REIN, STRA, SATP and SATT are not applicable. Note that TARGET only defines the variable to be changed, it does not change how a well is controlled. For example, if a well is operating on ORAT control, as defined by the previously entered [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword, entering TARGET equal to LRAT with a value, changes the liquid constraint but the well still remains on ORAT control. Use the [WELCNTL](#__RefHeading___Toc134886_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to change the control mode of a well. | None |
| 3 | VALUE<br>Liquid<br>Gas<br>Res Vol<br>Pressure<br>VFP<br>LIFT | A real positive value that defines the value of the variable declared by TARGET<br>This value may be specified using a User Defined Argument (UDA). | None |
| stb/d<br>Mscf/d<br>rb/d<br>psia<br>dimensionless<br>same as<br>[VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) | sm^3^/day<br>sm3/day<br>rm^3^/day<br>barsa<br>dimensionless<br>same as<br>[VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) | scc/hour<br>scc/hour<br>rcc/hour<br>atma<br>dimensionless<br>same as<br>[VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.93: WELTARG Keyword Description

If a well is currently a history matching well, then [WELTARG](#__RefHeading___Toc134888_2055188184) should only be used to change a well\'s bottom-hole pressure limit, vertical flow performance table number or the artificial lift quantity.

See also the [WELCNTL](#__RefHeading___Toc134886_2055188184) keyword, in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that can be used to reset the control mode, as well as a well's target and constraints of both rates and pressures.

#### Example

The following example below shows the oil rates for the OP01 oil producer at the start of the schedule section (January 1, 2000).

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- WELL PRODUCTION WELL CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS LIQ RES BHP THP VFP VFP

\-- NAME SHUT MODE RATE RATE RATE RATE RATE PRES PRES TABLE ALFQ

WCONPROD

OP01 OPEN ORAT 3000 1\* 1\* 1\* 1\* 750.0 500. 9 1\* /

/ DATES

01 FEB 2000 /

/

\--

\-- WELL PRODUCTION AND INJECTION TARGETS

\--

\-- WELL WELL TARGET

\-- NAME TARG VALUE

WELTARG

OP01 ORAT 2000 /

/

From January 1, 2000 to February 1, 2000 well OP01 is open and is on oil rate control and has a target oil rate of 3,000 stb/d, and uses [VFPPROD](#__RefHeading___Toc121919_2556401936) vertical lift table number 9 with a minimum tubing head pressure constraint of 500 psia. After February 1, 2000 the well's oil rate is reduced to 2,000 stb/d and all the other parameters remain unchanged.

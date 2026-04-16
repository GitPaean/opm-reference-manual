### WTMULT -- Multiply a Well Target or Constraint by a Constant

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [WTMULT](#__RefHeading___Toc1141674_4263943340), multiplies a defined well's target or constraint by a constant, for the target and constraints previously stipulated on the [WCONPROD](#__RefHeading___Toc146754_4203985108), [WCONINJE](#__RefHeading___Toc146750_4203985108), or [WELTARG](#__RefHeading___Toc134888_2055188184) keywords, but not for the history matching wells using the [WCONHIST](#__RefHeading___Toc134880_2055188184) or [WCONINJH](#__RefHeading___Toc146752_4203985108) keywords. All the aforementioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The constant should be positive value.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well target or constraint (CONTROL) is being adjusted by the multipler (FACTOR).<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | CONTROL | A defined character string that declares the well target or constraint that will be adjusted by multiplying its current value by the FACTOR defined in (3). CONTROL should be set to one of the following character strings:<br>1)  ORAT: the well's surface oil production rate will be adjusted.<br>2)  WRAT: the well's surface water production rate will be adjusted.<br>3)  GRAT: the well's surface gas production rate will be adjusted.<br>4)  LRAT: the well's surface liquid (oil plus water) production rate will be adjusted.<br>5)  CRAT: the well's linearly combined maximum surface rate, as per the [LINCOM](#__RefHeading___Toc287176_2843394514) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, will be adjusted.<br>6)  RESV: the well's in situ reservoir volume rate will be adjusted.<br>7)  BHP: the well's bottom-hole pressure will be adjusted.<br>8)  THP: the well's tubing head pressure will be adjusted. In this case a vertical performance table must have been previously assigned to the well via the [WCONPROD](#__RefHeading___Toc146754_4203985108) or [WCONINJE](#__RefHeading___Toc146750_4203985108) keywords. The tables are entered via the [VFPINJ](#__RefHeading___Toc121917_2556401936) or the [VFPPROD](#__RefHeading___Toc121919_2556401936) keywords. All the keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>9)  LIFT: the well's artificial lift quantity will be adjusted. Again, as for the THP, a vertical performance table must have been assigned to the well.<br>10) GUID: the well's guide rate will be adjusted. Only wells under group control and have a guide rate stipulated by the [WGRUPCON](#__RefHeading___Toc121641_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, may use this option.<br>11) CVAL: the well's calorific rate will be adjusted.<br>12) NGL: the well's natural gas liquid rate will be adjusted.<br>Note that the CRAT, CVAL and the NGL options are not available in OPM Flow and should not be used. | None |
| 3 | FACTOR | A postive real value that defines the FACTOR that is used to multiply the CONTROL specified in (2).<br>This value may be specified using a User Defined Argument (UDA). | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | NTIME | A positive integer greater than or equal to one that defines the number of report time steps for which the well target or constraint (CONTROL) is multiplied by the FACTOR. This is only applied when the FACTOR is specified by a User Defined Argument (UDA).<br>The default value of one means that the multiplication is applied only at the current time step for the UDA variable.<br>This option is not supported by OPM Flow. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.128: WTMULT Keyword Description

See also the [WELTARG](#__RefHeading___Toc134888_2055188184) and [WELCNTL](#__RefHeading___Toc134886_2055188184) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that can be used to reset the well's target and constraints of both rates and pressures, as well as the well's control mode.

#### Example

The example shows three oil wells having the flow streams adjusted.

\--

\-- WELL TARGET/LIMIT MULTIPLIER

\--

\-- WELL WELL MULT REPORT

\-- NAME CNTL FACTOR TIMES

WTMULT

OP01 ORAT 0.90 /

OP02 BHP 0.95 /

OP03 LIFT 1.25 /

/

Well OP01 has its current oil rate target multiplied by 0.90, well OP02 has its bottom-hole pressure constraint multiplied by 0.95, and well OP03 has its artificial lift quantity increased by 1.25 times.

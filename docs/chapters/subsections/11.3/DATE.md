### DATE -- Activate the DATE Option for the SUMMARY File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates the writing out of the date of each time step to the [SUMMARY](#__RefHeading___Toc43949_784232322) file. Normally only the time in days and decimal years are written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) file, activating the [DATE](#__RefHeading___Toc210146_2884651453) option also results in the [DATE](#__RefHeading___Toc210146_2884651453) being written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) file as well. This option is normally used when the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section has been activated to produce a RSM file.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

The following example shows an example RSM file output when the [DATE](#__RefHeading___Toc210146_2884651453) option has not been activated.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SUMMARY OF RUN NO-DATE-KEYWORD

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TIME YEARS FPR FOEW FOPR FOPT

DAYS YEARS PSIA STB/DAY STB

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0 0 4467.125 0 0 0

1.000000 0.002738 4466.943 0.000239 3235.662 3235.662

31.00000 0.084873 4464.476 0.007407 3230.117 100256.4

60.00000 0.164271 4462.717 0.014291 3193.902 193421.5

91.00000 0.249144 4460.813 0.021523 3127.557 291306.3

121.0000 0.331280 4458.909 0.028362 3055.878 383879.7

152.0000 0.416153 4456.914 0.035262 2982.212 477271.4

.......................................................

And activating the [SUMMARY](#__RefHeading___Toc43949_784232322) file [DATE](#__RefHeading___Toc210146_2884651453) option with:

\--

\-- ACTIVATE DATE SUMMARY FILE OPTION

\--

DATE

Results in the following example RSM file output.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SUMMARY OF RUN WITH-DATE-KEYWORD

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

DATE YEARS DAY MONTH YEAR FPR FOEW FOPR

YEARS PSIA STB/DAY

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1-JAN-98 0 19 10 1992 4467.125 0 0

2-JAN-98 0.002738 20 10 1992 4466.943 0.000239 3235.662

31-JAN-98 0.084873 21 10 1992 4464.476 0.007407 3230.117

28-FEB-98 0.164271 24 10 1992 4462.717 0.014291 3193.902

31-MAR-98 0.249144 28 10 1992 4460.813 0.021523 3127.557

30-APR-98 0.331280 3 11 1992 4458.909 0.028362 3055.878

31-MAY-98 0.416153 14 11 1992 4456.914 0.035262 2982.212

.......................................................

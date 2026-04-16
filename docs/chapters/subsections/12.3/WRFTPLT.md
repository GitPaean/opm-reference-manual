### WRFTPLT -- Activate Well RFT and PLT Reporting to the RFT File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates reporting of a well's depth pressure and fluid rates profile to the RFT file for the requested wells at the time the keyword is activated. Data written out by the simulator is used to match the field measured data collected from both the Repeat Formation Tester ("RFT") tool and various Production Logging Tools ("PLT").

See the [WRFT](#__RefHeading___Toc268467_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section for a brief description of the RFT data set. This keyword also actives the writing out of each well connection's fluid rates, connection factors and KH data, etc., as the PLT data. The PLT data is used to compare with measured data from wire line production logging tools.

+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                       | > WELNAME  | > A columnar vector of character strings of up to eight characters in length for each item, that defines the well name for which the RFT data should be written to the RFT file.                                                                                                                           | > None |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | > Note that the WELNAME must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur.                                                                                 |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | > If the WELNAME is left blank then the data is written out for all wells at the time they are first opened to flow.                                                                                                                                                                                       |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | > If the WELNAME is given, then the RFT data for the well at the time step the keyword is invoked is written out.                                                                                                                                                                                          |        |
+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                       | > RFT      | > A defined character string that sets the RFT data set output options and should be set to one of the following character strings.                                                                                                                                                                        | > NO   |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 1)  NO: do not write RFT data for the well.                                                                                                                                                                                                                                                                |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 2)  YES: write out the RFT data at the current reporting time step.                                                                                                                                                                                                                                        |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 3)  REPT: write out the RFT data at the current reporting time step and all subsequent reporting time steps.                                                                                                                                                                                               |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 4)  TIMESTEP: write out the RFT data at the current reporting time step and all subsequent time steps.                                                                                                                                                                                                     |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 5)  FOPN: write out the RFT data at the current reporting time step for the well if it is opened, otherwise write the RFT data out the first time the named well is opened.                                                                                                                                |        |
+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                                                       | > PLT      | > A defined character string that sets the PLT data set output options and should be set to one of the following character strings.                                                                                                                                                                        | > NO   |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 1)  NO: do not write PLT data for the well.                                                                                                                                                                                                                                                                |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 2)  YES: write out the PLT data at the current reporting time step.                                                                                                                                                                                                                                        |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 3)  REPT: write out the PLT data at the current reporting time step and all subsequent reporting time steps.                                                                                                                                                                                               |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 4)  TIMESTEP: write out the PLT data at the current reporting time step and all subsequent time steps.                                                                                                                                                                                                     |        |
+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 4                                                                                                                       | > MULTISEG | > A defined character string that sets the output options for multi-segment wells, that is the flow rates and pressures through each well segment, and should be set to one of the following character strings.                                                                                            | > NO   |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 1)  NO: do not write multi-segment well data for the well.                                                                                                                                                                                                                                                 |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 2)  YES: write out the multi-segment well data at the current reporting time step.                                                                                                                                                                                                                         |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 3)  REPT: write out the multi-segment well data at the current reporting time step and all subsequent reporting time steps.                                                                                                                                                                                |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | 4)  TIMESTEP: write out the multi-segment well data at the current reporting time step and all subsequent time steps.                                                                                                                                                                                      |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            | > Note the commercial simulator also uses MULTISEG to control the output of "rivers" for when the RIVERS Model has been enabled via the [RIVRDIMS](#__RefHeading___Toc681201_501926209) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. OPM Flow does not support the RIVERS Model. |        |
+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                  |            |                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                           |            |                                                                                                                                                                                                                                                                                                            |        |
| 1)  The keyword is followed by any number of records terminated by a "/" and the keyword should be terminated by a "/".   |            |                                                                                                                                                                                                                                                                                                            |        |
+---------------------------------------------------------------------------------------------------------------------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.116: WRFTPLT Keyword Description

See also the [WRFT](#__RefHeading___Toc268467_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that has less flexible reporting options.

#### Examples

The first example activates RFT output at the current reporting time step for all the wells that are opened to flow, otherwise the RFT data is written out the first time a well is opened.

\--

\-- WELL RFT, PLT AND SEGMENT DATA

\--

\-- WELL RFT PLT SEGMENT

\-- NAME DATA DATA DATA

WRFTPLT

\'\*\' FOPN /

/

The next example writes out the RFT and PLT data for two wells at the current reporting time step.

\--

\-- WELL RFT, PLT AND SEGMENT DATA

\--

\-- WELL RFT PLT SEGMENT

\-- NAME DATA DATA DATA

WRFTPLT

OP01 YES YES /

OP02 YES YES /

/

The final example is shown below:

\--

\-- WELL RFT, PLT AND SEGMENT DATA

\--

\-- WELL RFT PLT SEGMENT

\-- NAME DATA DATA DATA

WRFTPLT

OP01 REPT NO /

OP02 NO YES /

/

In this case the RFT data for well OP01 is written out at the current reporting time step and all subsequent reporting time steps. For well OP02, no RFT is written out but the PLT data is written out for the current report time step only.

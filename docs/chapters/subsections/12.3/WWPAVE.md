### WWPAVE -- Well Block Average Pressure Calculation Parameters for Individual Wells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WWPAVE](#__RefHeading___Toc1464916_4263943340) keyword defines the method and parameters for calculating a well's block average pressures for individual wells that can be written to the [SUMMARY](#__RefHeading___Toc43949_784232322) and RSM files via the WBP, WBP4, WBP5 and WBP9 vectors in the [SUMMARY](#__RefHeading___Toc43949_784232322) section. The resulting average pressure can be written out to the summary file in order to compared with field observed data. The keyword is similar to the [WPAVE](#__RefHeading___Toc121923_2556401936) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that has similar functionality, but is applied to all wells in the model.

Note that [WWPAVE](#__RefHeading___Toc1464916_4263943340) will overwrite any parameters on the [WPAVE](#__RefHeading___Toc121923_2556401936) keyword for a given well, and that [WWPAVE](#__RefHeading___Toc1464916_4263943340) can also be overwritten by any subsequent [WPAVE](#__RefHeading___Toc121923_2556401936) keyword.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well average pressure calculation parameters are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | WPAVE1 | A real dimensionless value that defines the weighting factor between the inner block and the surrounding blocks used in the calculation of the connection factor weighted average pressure.<br>If WPAVE1 is greater than or equal to zero and less than or equal to one, then the average pressure for each well connection is calculated based on this weighting factor. A value of zero indicates only the surrounding blocks should be used in the calculation; and a value of one indicates only the inner blocks should be used.<br>If WPAVE1 is less than zero, then the average pressure for each well connection is weighted based on the pore volumes of the inner and surrounding blocks. | 0.5 |
| 3 | WPAVE2 | A real dimensionless value greater than or equal to zero and less than or equal to one, that defines the weighting factor between the connection weighted average pressures and the pore volume weighted average pressures.<br>If WPAVE2 is equal to one, then the average pressures are calculate based only using the connection factor calculated pressures.<br>If WPAVE2 is equal to zero, then average pressures are calculate based on only using the pore volumes calculated pressures. | 1.0 |
| 4 | WPAVE3 | A defined character string that determines how the hydrostatic head calculation is performed in correcting the pressures to the BHP reference depth on the [WELSPECS](#__RefHeading___Toc268463_1366622701) or [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. WPAVE3 should be set to one of the following character strings:<br>1)  WELL: the hydrostatic head is calculated using the density of the fluid in the wellbore at the well connections.<br>2)  RES: he hydrostatic head is calculated using the density of the fluid in the reservoir with well connections and averaged over the connections.<br>3)  NONE: no hydrostatic correction is applied to the pressures. | WELL |
| 5 | WPAVE4 | A defined character string that determines which connections should be used in the calculations, WPAVE4 should be set to one of the following character strings:<br>1)  OPEN: only open connections and associated grid blocks should be used in the calculations. This option may result in pressure discontinuities if connections are opened and closed during the run.<br>2)  [ALL](#__RefHeading___Toc4420_421927891): all currently defined open and closed connections and associated grid blocks are used in the calculations. The pressure discontinuities issue mentioned above can be avoided with this option and defining all the well connections for a well at the beginning of the run.<br>Only the OPEN option is currently supported by the simulator. | OPEN |
| Notes:<br>1)  The keyword should be terminated by a "/". |  |  |  |

Table 12.3.356.1: WWPAVE Keyword Description

The keyword is not applicable and should not be used with radial and spider grid geometries.

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword that defines a well and a well's bottom-hole pressure reference depth, the [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keyword that also defines a well's bottom-hole pressure reference depth, and the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define a well's connections. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Examples

The following example defines the default well block average pressure calculation parameters for three oil wells: OP01, OP02 and OP03.

\--

\-- DEFINE WELL BLOCK AVERAGE PRESSURE CALCULATION PARAMETERS

\--

\-- WELL INNER PORV WELL OPEN

\-- NAME OUTER CONN RES ALL

WWPAVE

OP01 0.5 1.0 WELL ALL /

OP02 0.5 1.0 WELL ALL /

OP03 0.5 1.0 1\* 1\* /

And the next example shows the parameters used in the Norne model.

\--

\-- DEFINE WELL BLOCK AVERAGE PRESSURE CALCULATION PARAMETERS

\--

\-- WELL INNER PORV WELL OPEN

\-- NAME OUTER CONN RES ALL

WPAVE

OP01 1\* 0.0 WELL ALL /

OP02 1\* 0.0 WELL ALL /

OP03 1\* 0.0 WELL ALL /

Here only pore volume weighting is used instead of connection weighting.

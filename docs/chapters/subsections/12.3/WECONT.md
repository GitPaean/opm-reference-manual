### WECONT -- Well Economic Tracer Criteria for Production Wells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WECONT](#__RefHeading___Toc956535_487874538) keyword defines the tracer economic criteria for production wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONPROD](#__RefHeading___Toc146754_4203985108) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, for tracers define by the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

Note that wells can be allocated to a group when they are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword and groups can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the [GECONT](#__RefHeading___Toc299954_156692946) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and the controls specified by this keyword. Note that [GECONT](#__RefHeading___Toc299954_156692946) is not supported by OPM Flow in the current release

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1-1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well target and constraints are being defined. | None |
| --- | --- | --- | --- |
| 1-2 | [ACTION](#__RefHeading___Toc148342_63720426) | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. [ACTION](#__RefHeading___Toc148342_63720426) should be set to one of the following character strings:<br>1)  NONE: no action is taken.<br>2)  CON: close the worst offending connection in the worst offending. If connections have been welled as completions then the worst offending completion will be closed.<br>3)  +CON: close the worst offending connection and all below it in the worst offending well. If connections have been welled as completions then the worst offending completion and all below it in the worst offending well will be closed.<br>4)  WELL: shut or stop the well as per the AUTO variable on the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword.<br>5)  PLUG: plug back the worst offending well based on the plug back length and options defined on the [WPLUG](#__RefHeading___Toc628135_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322).<br>The corrective action takes places at the end of the time step in which the constraint is violated. | None |
| 1-3 | [END](#__RefHeading___Toc46631_2479612490) | A defined character string that defines if the simulation should terminate if the well is shut or stopped. [END](#__RefHeading___Toc46631_2479612490) should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step. | NO |
| 1-4 | WELL | A character string of up to eight characters in length that defines the well name of a fully defined well that will be "opened" when the well WELNAME is shut-in or stopped. | None |
| 1-5 | / | Record one terminated by a "/" | Not Applicable |
| 2-1 | NAME | A three letter character string defining the tracer's name.<br>Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 2-2 | MXTOTAL | A real positive value that defines the maximum total (free plus solution) tracer rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-3 | MXFREET | A real positive value that defines the maximum total (free plus solution) tracer concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-4 | MXFREEQ | A real positive value that defines the maximum free tracer rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-5 | MXCONC | A real positive value that defines the maximum free tracer concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-6 | MXSOLNQ | A real positive value that defines the maximum solution rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-7 | MXSOLNC | A real positive value that defines the maximum solution concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. |  |
| 2-8 | / | Record two terminated by a "/" | Not Applicable |
| 3-1 | / | Well terminated by a "/" | Not Applicable |
| Notes:<br>1)  [WECONT](#__RefHeading___Toc956535_487874538) keyword consists of two records, with entries 1-1 to 1-5 representing record one items and 2-1 to 2-8 representing record number two items, in the "No." column in this table. A maximum of three type two records can be entered following a type one record.<br>2)  Each type one and type two records are terminate by a "/" as indicated in the table, and a well data set is terminated by a further "/", after which additional well data sets can be entered stating with a record of type one followed by type two.<br>3)  The keyword the keyword should be terminated by an additional "/" after the well data set termination "/" character. |  |  |  |

Table 12.83: WECONT Keyword Description

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define a wells shut-in or stop options, and [WECON](#__RefHeading___Toc134884_2055188184) for setting a well's economic criteria. Both the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the tracer economic criteria for the field and two wells, OP01 and OP02.

\--

\-- WELL TRACER ECONOMIC CRITERIA FOR PRODUCTION WELLS

\--

\-- WELL WORK END MAX

\-- NAME OVER RUN WELLS

WECONT

OP01 +CON \'YES\' 1\* / START OF WELL

\--

\-- TRACER TRACER TRACER TRACER TRACER TRACER TRACER

\-- NAME TOTAL TOTAL FREE FREE SOLN SOLN

\-- RATE CONCEN RATE CONCEN RATE CONCEN

PLY 800.0 /

BRI 800.0 /

/

OP02 +CON \'YES\' 1\* / START OF WELL

\--

\-- TRACER TRACER TRACER TRACER TRACER TRACER TRACER

\-- NAME TOTAL TOTAL FREE FREE SOLN SOLN

\-- RATE CONCEN RATE CONCEN RATE CONCEN

PLY 800.0 /

BRI 800.0 / END OF WELL

/ END OF KEYWORD

If the economic limits are violated then the worst offending connection and all below it in the worst offending well will be closed, If connections have been grouped as completions then the worst offending completion and all below it in the worst offending well will be closed

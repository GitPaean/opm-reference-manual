### WHISTCTL -- Define Well Historical Target Phase

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WHISTCTL](#__RefHeading___Toc268465_1366622701) keyword changes the target control for wells declared as history match wells via the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. The target phase is set on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword and [WHISTCTL](#__RefHeading___Toc268465_1366622701) overrides this value for all subsequent entries on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.

| 1 | TARGET | A defined character string that sets the observed target production phase for the well, all the other phases are calculated unconstrained and used for reporting only. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (6) and (10) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>TARGET should be set to one of the following character strings:<br>1)  ORAT: the target is set to the surface oil production rate as defined by item (4) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>2)  WRAT: the target is set to the surface water production rate as defined by item (5) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>3)  GRAT: the target is set to the surface gas production rate as defined by item (6) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>4)  LRAT: the target is set to the surface liquid (oil plus water) production rate and is calculated by the simulator using (4) and (5) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>5)  RESV: the target is set to the in situ reservoir volume rate and is calculated by the simulator using items (4), (5) and (6) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>6)  BHP: the target rate is set to the bottom-hole pressure as defined by item (10) on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>7)  NONE: revert back to the TARGET control mode on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword.<br>```{=html} <!-- --> ``` 1)  The TARGET control mode defined on this keyword resets the TARGET control mode on the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, from the time the [WHISTCTL](#__RefHeading___Toc268465_1366622701) is invoked, thus avoiding changing the control model on all subsequent [WCONHIST](#__RefHeading___Toc134880_2055188184) keywords. | None |
| --- | --- | --- | --- |
| 2 | [END](#__RefHeading___Toc46631_2479612490) | A defined character string that defines if the simulation should terminate if the well has switch to BHP control by the simulator, and should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step.<br>Wells set to BHP control via the [WCONHIST](#__RefHeading___Toc134880_2055188184) or WHISCTL keywords are ignored. Only [END](#__RefHeading___Toc46631_2479612490) equal to NO is currently supported in OPM Flow. | NO |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.98: WHISTCTL Keyword Description

History matching wells are handled differently then ordinary wells that use the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword for controlling their production targets and constraints. However, the wells still need to be defined like ordinary production wells using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. History matching wells are converted to ordinary wells by restating a well's control mode using either the [WCONPROD](#__RefHeading___Toc146754_4203985108) or [WELTARG](#__RefHeading___Toc134888_2055188184) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

See also the [WCONHIST](#__RefHeading___Toc134880_2055188184) and [WCONINJH](#__RefHeading___Toc146752_4203985108) keywords that are used to define the historical production and injection data, All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The example below shows the observed gas rates for the OP01 oil producer for the first quarter of 2000.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\--

\-- DEFINE WELL HISTORICAL TARGET PHASE

\--

\-- CNTL BHP

\-- MODE STOP

WHISTCTL

RESV NO /

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.5E3 100.0 1550 10 1\* 900.0 1\* /

/ DATES

01 FEB 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.2E3 150.0 1520 1\* 1\* 875.0 3250.0 /

/ DATES

01 MAR 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.0E3 200.0 1500 1\* 1\* 850.0 1\* /

/

From January 1, 2000 the [WCONHIST](#__RefHeading___Toc134880_2055188184) keyword defines well OP01, which is open and is on oil rate control, to produce 15,500 stb/d oil, with the observed rates of 100 stb/d of water and 15.5 MMscf/d of gas. However the WHISCTL keyword resets the target control to reservoir voidage from January 1, 2000 and onward. This is useful in initial history matching runs to get a "reasonable" pressure match, by ensuring that the total reservoir withdrawals are correct, although the individual phase withdrawals will not match. Once a reasonable pressure match is achieved for the reservoir then one can reset TARGET to the sales phase, [OIL](#__RefHeading___Toc97439_1778172979) or [GAS](#__RefHeading___Toc38607_2267116897), and continue with the matching of all the phases.

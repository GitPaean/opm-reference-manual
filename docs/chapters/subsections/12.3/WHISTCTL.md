### WHISTCTL -- Define Well Historical Target Phase

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WHISTCTL keyword changes the target control for wells declared as history match wells via the WCONHIST keyword in the SCHEDULE section. The target phase is set on the WCONHIST keyword and WHISTCTL overrides this value for all subsequent entries on the WCONHIST keyword.

| 1 | TARGET | A defined character string that sets the observed target production phase for the well, all the other phases are calculated unconstrained and used for reporting only. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (6) and (10) on the WCONHIST keyword.<br>TARGET should be set to one of the following character strings:<br>1)  ORAT: the target is set to the surface oil production rate as defined by item (4) on the WCONHIST keyword.<br>2)  WRAT: the target is set to the surface water production rate as defined by item (5) on the WCONHIST keyword.<br>3)  GRAT: the target is set to the surface gas production rate as defined by item (6) on the WCONHIST keyword.<br>4)  LRAT: the target is set to the surface liquid (oil plus water) production rate and is calculated by the simulator using (4) and (5) on the WCONHIST keyword.<br>5)  RESV: the target is set to the in situ reservoir volume rate and is calculated by the simulator using items (4), (5) and (6) on the WCONHIST keyword.<br>6)  BHP: the target rate is set to the bottom-hole pressure as defined by item (10) on the WCONHIST keyword.<br>7)  NONE: revert back to the TARGET control mode on the WCONHIST keyword.<br>```{=html} <!-- --> ``` 1)  The TARGET control mode defined on this keyword resets the TARGET control mode on the WCONHIST keyword in the SCHEDULE section, from the time the WHISTCTL is invoked, thus avoiding changing the control model on all subsequent WCONHIST keywords. | None |
| --- | --- | --- | --- |
| 2 | END | A defined character string that defines if the simulation should terminate if the well has switch to BHP control by the simulator, and should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step.<br>Wells set to BHP control via the WCONHIST or WHISCTL keywords are ignored. Only END equal to NO is currently supported in OPM Flow. | NO |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.98: WHISTCTL Keyword Description

History matching wells are handled differently then ordinary wells that use the WCONPROD keyword for controlling their production targets and constraints. However, the wells still need to be defined like ordinary production wells using the WELSPECS keyword in the SCHEDULE section. History matching wells are converted to ordinary wells by restating a well's control mode using either the WCONPROD or WELTARG keywords in the SCHEDULE section.

See also the WCONHIST and WCONINJH keywords that are used to define the historical production and injection data, All the aforementioned keywords are described in the SCHEDULE section.

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

From January 1, 2000 the WCONHIST keyword defines well OP01, which is open and is on oil rate control, to produce 15,500 stb/d oil, with the observed rates of 100 stb/d of water and 15.5 MMscf/d of gas. However the WHISCTL keyword resets the target control to reservoir voidage from January 1, 2000 and onward. This is useful in initial history matching runs to get a "reasonable" pressure match, by ensuring that the total reservoir withdrawals are correct, although the individual phase withdrawals will not match. Once a reasonable pressure match is achieved for the reservoir then one can reset TARGET to the sales phase, OIL or GAS, and continue with the matching of all the phases.

### TRACER -- Define Passive Tracer Variables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [TRACER](#__RefHeading___Toc121485_83452205) keyword defines a series of passive tracers that are associated with a phase (oil, water, or gas) in the model. The maximum number of tracers for each phase are declared on the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| 1 | NAME | A three letter character string defining the tracer's name.<br>NAME is used by the [TNUM](#__RefHeading___Toc95487_3812137098) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section, and unlike other keywords, the [TNUM](#__RefHeading___Toc95487_3812137098) keyword itself must be concatenated with the phase and the name of the tracer defined by NAME.<br>Similarly for the [TVDP](#__RefHeading___Toc210170_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, where the [TVDP](#__RefHeading___Toc210170_2884651453) keyword itself must be concatenated with the either letter F (for free) or S (for solution), followed by the name of the tracer defined by NAME.<br>Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| --- | --- | --- | --- |
| 2 | PHASE | A three letter character string that defines the tracer given by NAME to a particular fluid phase. The character should be set to [OIL](#__RefHeading___Toc97439_1778172979), WAT or [GAS](#__RefHeading___Toc38607_2267116897). | None |
| 3 | UNITS | The units for the tracer. This can be any unit but should be consistent with values entered via the [TBLK](#__RefHeading___Toc198434_3325167686) and [TVDP](#__RefHeading___Toc210170_2884651453) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. The default values are the same as the PHASE in the model. | Same as the phases in the model |
| Liquid: stb<br>Gas: Mscf | Liquid: sm^3^<br>Gas: sm^3^ | Liquid: scc<br>Gas: scc |  |
| 4 | SOLPHASE | A three or four letter character string defining the partitioned tracer's solution phase. The character string should be set to [OIL](#__RefHeading___Toc97439_1778172979), WAT, [GAS](#__RefHeading___Toc38607_2267116897) or MULT.<br>Note that SOLPHASE only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#__RefHeading___Toc264979_2928331029) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 5 | KPNUM | The table number to be used with the partitioned tracers defined by the [PARTTRAC](#__RefHeading___Toc264979_2928331029), [TRACERKP](#__RefHeading___Toc1279807_4250154414) and [TRACERKM](#__RefHeading___Toc1279805_4250154414) keywords.<br>Note that KPNUM only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#__RefHeading___Toc264979_2928331029) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| 6 | ADSPHASE | A three letter character string defining the phase used for the adsorption calculation for when the MULT option has been for SOLPHASE. The character string should be set to [OIL](#__RefHeading___Toc97439_1778172979), WAT, [GAS](#__RefHeading___Toc38607_2267116897) or [ALL](#__RefHeading___Toc4420_421927891).<br>Note that ADSPHASE only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#__RefHeading___Toc264979_2928331029) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | None |
| Notes:<br>1)  Each record (or row) should be terminated by a "/" and the keyword is terminated by a "/". |  |  |  |

Table 8.194: TRACER Keyword Description

See also the [TNUM](#__RefHeading___Toc95487_3812137098) keyword in the REGION section that defines tracer regions, and the [TVDP](#__RefHeading___Toc210170_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section that sets the initial tracer saturation for all the cells as a function of depth.

#### Example

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER

\-- NAME PHASE

\-- \-\-\-\-\-- \-\-\-\-\--

TRACER

\'IGS\' \'GAS\' / GAS INJECTOR

\'DGS\' \'GAS\' / DISOLVED GAS

\'IW1\' \'WAT\' / WAT INJECTOR 1

\'Iw2\' \'WAT\' / WAT INJECTOR 2

/

The above example defines four passive tracers one for a gas injection well, one for tracking the dissolved gas, and two to track the injected water from two water injection wells.

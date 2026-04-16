### TNUM -- Define Passive Tracer Concentration Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [TNUM](#__RefHeading___Toc95487_3812137098) keyword defines the regions associated with the series of tracers associated with a phase (oil, water, or gas) in the model. The maximum number of tracers for each phase are declared on the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Unlike other keywords, the [TNUM](#__RefHeading___Toc95487_3812137098) keyword must be concatenated with the phase and the name of the tracer declared by [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. outlines the format of the [TNUM](#__RefHeading___Toc95487_3812137098) keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [TNUM](#__RefHeading___Toc95487_3812137098) | A four letter character equal to [TNUM](#__RefHeading___Toc95487_3812137098) that is the root keyword name for this data set array. | None |
| 2 | PHASE | A one letter character string that must be equal to F or S, that is concatenated to [TNUM](#__RefHeading___Toc95487_3812137098).<br>The letter F states that the tracer is for the "free" phase, for example oil or water, as well as gas cap gas (free gas).<br>The letter S signifies that the tracer is a "solution" phase tracer, for example gas dissolved in oil (as activated by the [DISGAS](#__RefHeading___Toc39767_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section), or condensate (vaporized oil) in the gas (as per the [VAPOIL](#__RefHeading___Toc56610_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section).<br>Note tracers that are defined by the letter S to be in the "solution" phase, must also be initialized by the "free" phase as well. | None |
| 3 | NAME | A three letter character string defining the tracer's name, which is concatenate to [TNUM](#__RefHeading___Toc95487_3812137098) and PHASE to given the full name of the keyword<br>Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |

Table 9.24: [TNUM](#__RefHeading___Toc95487_3812137098) Keyword Name Format

Following the declaration of the full keyword name, TNUMPHASENAME, the keyword is followed by the data as outlined below.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TNUMREG | TUNREG defines an array of positive integers assigning a grid cell to a particular tracer table region.<br>The maximum number of TNUMREG regions is set by the NTTRVD variable on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a TNUMREG region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.25: [TNUM](#__RefHeading___Toc95487_3812137098) Keyword Data Description

See also the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section and the [TBLK](#__RefHeading___Toc198434_3325167686) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

#### Example

First define four passive tracers one for a free gas, one for dissolved gas, one for oil and one to track the water.

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER

\-- NAME PHASE

\-- \-\-\-\-\-- \-\-\-\-\--

TRACER

\'GCG\' \'GAS\' / GAS CAP GAS

\'DGS\' \'GAS\' / DISOLVED GAS

\'OIL\' \'OIL\' / OIL

\'WAT\' \'WAT\' / WAT

/

Given a 100 x 100 x 5 grid with [DISGAS](#__RefHeading___Toc39767_2267116897) activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the following [TNUM](#__RefHeading___Toc95487_3812137098) keywords define the various tracer regions given that NTTRVD equals four on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- DEFINE PASSIVE TRACER CONCENTRATION REGIONS

\--

TNUMFGCG

1000\*1

1000\*2

1000\*2

1000\*2

1000\*2

/

TNUMSDGS

1000\*1

1000\*1

1000\*1

1000\*1

1000\*1

/

TNUMFOIL

1000\*3

1000\*3

1000\*3

1000\*3

1000\*3

/

TNUMFWAT

1000\*4

1000\*4

1000\*4

1000\*4

1000\*4

/

The keyword name is derived from the [TNUM](#__RefHeading___Toc95487_3812137098) keyword, plus either F or S, plus the tracer name declared in the [TRACER](#__RefHeading___Toc121485_83452205) keyword. For example for the gas cap (free gas) this would be [TNUM](#__RefHeading___Toc95487_3812137098)+F+[GAS](#__RefHeading___Toc38607_2267116897) to give the TNUMFGAS keyword. And for the dissolved (solution) gas this would be [TNUM](#__RefHeading___Toc95487_3812137098)+S+DGS resulting in the TNUMSDGS keyword.

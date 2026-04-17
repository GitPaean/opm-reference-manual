### TNUM -- Define Passive Tracer Concentration Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TNUM keyword defines the regions associated with the series of tracers associated with a phase (oil, water, or gas) in the model. The maximum number of tracers for each phase are declared on the TRACER keyword in the RUNSPEC section. Unlike other keywords, the TNUM keyword must be concatenated with the phase and the name of the tracer declared by TRACER keyword in the PROPS section. outlines the format of the TNUM keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TNUM | A four letter character equal to TNUM that is the root keyword name for this data set array. | None |
| 2 | PHASE | A one letter character string that must be equal to F or S, that is concatenated to TNUM.<br>The letter F states that the tracer is for the "free" phase, for example oil or water, as well as gas cap gas (free gas).<br>The letter S signifies that the tracer is a "solution" phase tracer, for example gas dissolved in oil (as activated by the DISGAS keyword in the RUNSPEC section), or condensate (vaporized oil) in the gas (as per the VAPOIL keyword in the RUNSPEC section).<br>Note tracers that are defined by the letter S to be in the "solution" phase, must also be initialized by the "free" phase as well. | None |
| 3 | NAME | A three letter character string defining the tracer's name, which is concatenate to TNUM and PHASE to given the full name of the keyword<br>Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |

Table 9.24: TNUM Keyword Name Format

Following the declaration of the full keyword name, TNUMPHASENAME, the keyword is followed by the data as outlined below.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TNUMREG | TUNREG defines an array of positive integers assigning a grid cell to a particular tracer table region.<br>The maximum number of TNUMREG regions is set by the NTTRVD variable on the EQLDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a TNUMREG region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.25: TNUM Keyword Data Description

See also the TRACER keyword in the PROPS section and the TBLK keyword in the SOLUTION section.

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

Given a 100 x 100 x 5 grid with DISGAS activated in the RUNSPEC section, then the following TNUM keywords define the various tracer regions given that NTTRVD equals four on the EQLDIMS keyword in the RUNSPEC section.

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

The keyword name is derived from the TNUM keyword, plus either F or S, plus the tracer name declared in the TRACER keyword. For example for the gas cap (free gas) this would be TNUM+F+GAS to give the TNUMFGAS keyword. And for the dissolved (solution) gas this would be TNUM+S+DGS resulting in the TNUMSDGS keyword.

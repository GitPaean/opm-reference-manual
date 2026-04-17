### TRKPF -- Define Partitioned Tracer Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TRKPF keyword defines the regions associated with the series of partition tracers and the partitioning tables allocated to grid blocks in the model, for when the Partitioned Tracer option has been enabled by the PARTTRAC keyword in the RUNSPEC section. The maximum number of tracers for each phase are declared on the TRACERS keyword in the RUNSPEC section. Unlike other keywords, the TRKPF keyword must be concatenated with the name of the tracer declared by TRACER keyword in the PROPS section. outlines the format of the TRKPF keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TRKPF | A five letter character string equal to TRKPF that is the root keyword name for this data set array. | None |
| 2 | NAME | A three letter character string defining the tracer's name, as declared by the TRACER keyword, which is concatenate to TRKPF to given the full name of the keyword<br>Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |

Table 9.26: TRKPF Keyword Name Format

Following the declaration of the full keyword name, TRKPFNAME, the keyword is followed by the data as outlined below.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TRKPFREG | TRKPFREG defines an array of positive integers assigning a grid cell to a particular tracer table region.<br>The maximum number of TRKPFREG regions is set by the NTTRVD variable on the EQLDIMS keyword in the RUNSPEC section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a TRKPFREG region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.27: TRKPF Keyword Data Description

See also the TRACER and TRACERKP keywords in the PROPS section and the TBLK keyword in the SOLUTION section.

#### Example

First define one mult-partitioned tracer for the water phase.

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER TRACER PARTITION NUM ADSOR

\-- NAME PHASE VOLUME PHASE K(P) PHASE

\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-- \-\-\-\--

TRACER

\'WAT\' \'WAT\' 1\* MULT 2 ALL / WAT

/

Then for a given a 100 x 100 x 5 grid assign the partitioned tracer regions and K(P) tables, based on two regions.

\--

\-- DEFINE PARTITIONED TRACER REGIONS

\--

TRKPFWAT

1000\*1

1000\*1

1000\*2

1000\*2

1000\*2

/

The keyword name is derived from the TRKPF keyword, plus the tracer name declared in the TRACER keyword, in this case the keyword name is TRKPFWAT.

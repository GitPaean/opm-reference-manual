### TRKPF -- Define Partitioned Tracer Regions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [TRKPF](#__RefHeading___Toc1607157_4250154414) keyword defines the regions associated with the series of partition tracers and the partitioning tables allocated to grid blocks in the model, for when the Partitioned Tracer option has been enabled by the [PARTTRAC](#__RefHeading___Toc264979_2928331029) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The maximum number of tracers for each phase are declared on the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Unlike other keywords, the [TRKPF](#__RefHeading___Toc1607157_4250154414) keyword must be concatenated with the name of the tracer declared by [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. outlines the format of the [TRKPF](#__RefHeading___Toc1607157_4250154414) keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [TRKPF](#__RefHeading___Toc1607157_4250154414) | A five letter character string equal to [TRKPF](#__RefHeading___Toc1607157_4250154414) that is the root keyword name for this data set array. | None |
| 2 | NAME | A three letter character string defining the tracer's name, as declared by the [TRACER](#__RefHeading___Toc121485_83452205) keyword, which is concatenate to [TRKPF](#__RefHeading___Toc1607157_4250154414) to given the full name of the keyword<br>Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |

Table 9.26: [TRKPF](#__RefHeading___Toc1607157_4250154414) Keyword Name Format

Following the declaration of the full keyword name, TRKPFNAME, the keyword is followed by the data as outlined below.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TRKPFREG | TRKPFREG defines an array of positive integers assigning a grid cell to a particular tracer table region.<br>The maximum number of TRKPFREG regions is set by the NTTRVD variable on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a TRKPFREG region then the default value will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.27: [TRKPF](#__RefHeading___Toc1607157_4250154414) Keyword Data Description

See also the [TRACER](#__RefHeading___Toc121485_83452205) and [TRACERKP](#__RefHeading___Toc1279807_4250154414) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section and the [TBLK](#__RefHeading___Toc198434_3325167686) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

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

The keyword name is derived from the [TRKPF](#__RefHeading___Toc1607157_4250154414) keyword, plus the tracer name declared in the [TRACER](#__RefHeading___Toc121485_83452205) keyword, in this case the keyword name is TRKPFWAT.

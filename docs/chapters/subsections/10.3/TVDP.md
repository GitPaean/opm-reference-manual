### TVDP -- Define the Initial Equilibration Tracer Saturation versus Depth Functions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the initial equilibration tracer concentration versus depth functions for each grid cell in the model, for when the Tracer option has been enabled by the TRACERS keyword in the RUNSPEC section. The maximum number of tracers for each phase are declared on the TRACERS keyword in the RUNSPEC section. Unlike other keywords, the TVDP keyword must be concatenated with the name of the tracer declared by the TRACER keyword in the PROPS section as outlined in .

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TVDP | A four letter character string equal to TVDP that is the root keyword name for this data set function. | None |
| 2 | STATE | A one letter character string defining the tracer's state, which is concatenated to TVDP to give the partial name of the keyword. STATE should be set to F ("free") or S ("solution"), with the latter related to a tracer that is dissolved in an associated phase. If the tracer defined by NAME is associated with the OIL, GAS or WATER phases then STATE should be set to F. If the tracer is associated with the DISGAS or VAPOIL phases then STATE should be set to S. | None |
| 3 | NAME | A three letter character string defining the tracer's name as defined by the TRACER keyword, which is concatenated to TVDP and STATE to given the full name of the keyword. For example, if the TRACER keyword has been used to define a tracer named SEA in the WAT phase, then the full keyword name would be TVDPFSEA. Whereas, if a tracer was defined as IGS for the GAS phase then it could be TVDPFIGS and/or TVDPSIGS depending if one was wishing to track the "free" or "solution" gas phase, or both. Note it is best to avoid names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |

Table 10.61: TVDP Keyword Name Format

Following the declaration of the full keyword name, TVDPSTATENAME, the keyword is followed by the data as outlined below.

| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding initial tracer saturations, TVDP | None |
| --- | --- | --- | --- |
| feet | m | cm |  |
| 2 | TVDPVAL | A columnar vector of real values, greater than or equal to zero, that defines the initial tracer concentration values at the corresponding DEPTH.<br>If tracer units have been defined by the UNITS parameter on the TRACER keyword in the PROPS section, then the units of TVDPVAL are the ratio of UNITS divided by the TVDPVAL units given below. For example, if UNITS was defined as kg, then for metric units TVDPVAL units would be kg/sm^3^. | None |
| Liquid: stb<br>Gas: Mscf | Liquid: sm^3^<br>Gas: sm^3^ | Liquid: scc<br>Gas: scc |  |
| Notes:<br>1)  The keyword is followed by NTTRVD records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSTRVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.62: TVDP Keyword Description

See also the TBLK keyword in the SOLUTION section that also sets the initial tracer concentration for each grid block.

#### Example

This example is taken from Norne model, in which there are seven tracers related to the water phase.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- MAX MAX RSVD TVDP TVDP

\-- EQLNUM DEPTH NODES TABLE NODES

EQLDIMS

9 1\* 20 7 1\* /

\-- ==============================================================================

\--

\-- PROPS SECTION

\--

\-- ==============================================================================

PROPS

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER

\-- NAME PHASE

\-- \-\-\-\-\-- \-\-\-\-\--

TRACER

SEA WAT /

HTO WAT /

S36 WAT /

2FB WAT /

4FB WAT /

DFB WAT /

TFB WAT /

/

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- INITIAL EQUILIBRATION TRACER SATURATION VERSUS DEPTH

\--

\-- DEPTH TRACER

\-- CONCENT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

TVDPFSEA

1000.0 0.0

5000.0 0.0 / TRACER FSEA CONCENTRATION VS DEPTH

TVDPFHTO

1000.0 0.0

5000.0 0.0 / TRACER FHTO CONCENTRATION VS DEPTH

TVDPFS36

1000.0 0.0

5000.0 0.0 / TRACER FS36 CONCENTRATION VS DEPTH

TVDPF2FB

1000.0 0.0

5000.0 0.0 / TRACER F2FB CONCENTRATION VS DEPTH

TVDPF4FB

1000.0 0.0

5000.0 0.0 / TRACER F4FB CONCENTRATION VS DEPTH

TVDPFDFB

1000.0 0.0

5000.0 0.0 / TRACER FDFB CONCENTRATION VS DEPTH

TVDPFTFB

1000.0 0.0

5000.0 0.0 / TRACER FTFB CONCENTRATION VS DEPTH

Here we first define the number of tracers in the model via the EQLDIMS keyword in the RUNSPEC section, then the actual tracers themselves in the PROPS section using the TRACER keyword, and finally the initial tracer concentrations are all set to zero via the TVDP keyword in the PROPS section.

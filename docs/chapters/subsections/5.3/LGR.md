### LGR -- Define Local Grid Refinement Dimensions and Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LGR keyword defines the maximum dimensions and parameters for the Local Grid Refinement ("LGR") option.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator, but is documented here for completeness.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MAXLGR | A positive integer value that defines the maximum number of LGRs in the model. | 0 |
| 2 | MAXCLS | A positive integer value that defines the maximum number of grid blocks in all the LGRs. | 0 |
| 3 | MCOARS | A positive integer value that defines the maximum number of amalgamated coarse grid blocks in the model. | 0 |
| 4 | MAMALG | A positive integer value that defines the maximum number of LGR amalgamations in the model. | 0 |
| 5 | MXLALG | A positive integer value that defines the maximum number of LGRs in any amalgamation in the model. | 0 |
| 6 | LSTACK | A positive integer that defines the maximum number of previous search directions stored by the linear solver for the LGR. See the NSTACK keyword in the RUNSPEC section for a full description. | 10 |
| 7 | INTOPT | A character string set to either INTERP to activate the Quandalle[^1] pressure correction, or NOINTERP to deactivate this option. The option applies bi-linear interpolation to the global cells surrounding an LGR in order to improve the accuracy of the flow calculations between the LGR and the host cells. | NOINTERP |
| 8 | NCHCOR | A positive integer value that defines the maximum number of grid blocks within a coarsened grid that overlap parallel domain boundaries for when the Parallel option has been invoked by the PARALLEL keyword in the RUNSPEC section.<br>OPM Flow uses a different numerical scheme which makes this parameter redundant, see section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to run OPM Flow in parallel mode. |            | | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.19: LGR Keyword Description

#### Example

\--

\-- LOCAL GRID REFINEMENT DIMENSIONS AND PARAMETERS

\--

\-- LGR LGR LGR LGR LGR LGR LGR LGR

\-- MAXLGR MAXCLS MCOARS MAMALG MXLALG LSTACK INTOPT NCHCOR

LGR

10 1000 1\* 1\* 1\* 1\* INTERP 1\* /

The above example sets the maximum number of LGRs to 10 and the maximum number of grid blocks a LGR may contain to 1,000, and that the Quandalle pressure correction should be used to improve the flow calculation.

[^1]: Quandalle, Philippe & Besset, P. (1985). Reduction of Grid Effects Due to Local Sub-Gridding in Simulations Using a Composite Grid. 10.2118/13527-MS.

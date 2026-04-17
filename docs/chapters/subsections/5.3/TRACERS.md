### TRACERS -- Activate Tracer Options and Set Tracer Array Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TRACERS keyword defines the number of tracers in the model and the various passive tracer tracking options.

| 1 | MXOILTR | A positive integer defining the maximum number of passive oil tracers defined using the TRACER keyword. | 0 |
| --- | --- | --- | --- |
| 2 | MXWATTR | A positive integer defining the maximum number of passive water tracers defined using the TRACER keyword. | 0 |
| 3 | MXGASTR | A positive integer defining the maximum number of passive gas tracers defined using the TRACER keyword. | 0 |
| 4 | MXENVTR | A positive integer defining the maximum number of passive environmental tracers defined using the TRACER keyword. Environmental tracers are used with the Environment Tracer model that takes into account tracer adsorption and decay.<br>Only the default value of zero is currently supported. | 0 |
| 5 | DIFFOPT | A character string defining the numerical diffusion option for tracer tracking runs that should be set to:<br>1)  DIFF activates the numerical diffusion control options.<br>2)  NODIFF deactivates the numerical diffusion control options.<br>Only the default value of NODIFF is supported | NODIFF |
| 6 | MXITRTR | A positive integer defining the maximum number of non-linear iterations to be used when the tracer option is activated. | 12 |
| 7 | MNITRTR | A positive integer defining the minimum number of non-linear iterations to be used when the tracer option is activated. | 1 |
| 8 | NONLIN | A character string stating if passive tracers as should be linear (NO) or non-linear (YES).<br>Only the default value of NO is supported. | No |
| 9 | LNCONFAC | A real value defining the initial linear convergence factor. The default value of 1\* means the parameter will not be utilized. | 1\* |
| 10 | NLCONFAC | A real value defining the initial non-linear convergence factor. The default value of 1\* means the parameter will not be utilized. | 1\* |
| 11 | CONFAC | A real value defining the LNCONFAC and NLCONFAC convergence factors to be used after the initial convergence factor has been applied. | 1.0 |
| 12 | NUMCONF | A positive integer defining the maximum number of times CONFAC can be used. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.48: TRACERS Keyword Description

See also the TRACER keyword in the PROPS section that defines the individual tracers.

#### Example

\--

\-- NO OIL NO WAT NO GAS NO ENV DIFF MAX MIN TRACER

\-- TRACERS TRACERS TRACERS TRACERS CONTL NONLIN NONLIN NONLIN

TRACERS

0 7 1 0 \'NODIFF\' 1\* 1\* 1\* /

The above example defines seven tracers in the water phase and one tracer in the gas phase.

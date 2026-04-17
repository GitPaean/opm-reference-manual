### EOS -- Specify Equation of State

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EOS keyword specifies the Equation Of State (EOS) to be used for each EOS region. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EQUATION | A defined character string that specifies the Equation of State to be used, and should be set to one of the following:<br>1)  PR: Peng-Robinson,<br>2)  RK: Redlich-Kwong, or<br>3)  SRK: Soave-Redlich-Kwong, or<br>4)  ZJ: Zudkevitch-Joffe-Redlich-Kwong. | PR |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.51.1: EOS Keyword Description

#### Example

The following example defines Peng-Robinson as the Equation of State for a model with a single EOS region.

\--

\-- SPECIFY EQUATION OF STATE

\--

EOS

PR /

The following example defines Peng-Robinson as the Equation of State for EOS region one, and Soave-Redlich-Kwong as the Equation of State for EOS region two in a model with two EOS regions.

\--

\-- SPECIFY EQUATION OF STATE

\--

EOS

PR /

RK /

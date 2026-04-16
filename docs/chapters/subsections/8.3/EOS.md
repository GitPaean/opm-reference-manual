### EOS -- Specify Equation of State

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EOS](#REF_HEADING_KEYWORD_EOS_5_3) keyword specifies the Equation Of State ([EOS](#REF_HEADING_KEYWORD_EOS_5_3)) to be used for each [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region. The keyword should only be used if the compositional mode has been requested using the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EQUATION | A defined character string that specifies the Equation of State to be used, and should be set to one of the following:<br>1)  PR: Peng-Robinson,<br>2)  RK: Redlich-Kwong, or<br>3)  SRK: Soave-Redlich-Kwong, or<br>4)  ZJ: Zudkevitch-Joffe-Redlich-Kwong. | PR |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.51.1: [EOS](#REF_HEADING_KEYWORD_EOS_5_3) Keyword Description

#### Example

The following example defines Peng-Robinson as the Equation of State for a model with a single [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region.

\--

\-- SPECIFY EQUATION OF STATE

\--

EOS

PR /

The following example defines Peng-Robinson as the Equation of State for [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region one, and Soave-Redlich-Kwong as the Equation of State for [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region two in a model with two [EOS](#REF_HEADING_KEYWORD_EOS_5_3) regions.

\--

\-- SPECIFY EQUATION OF STATE

\--

EOS

PR /

RK /

### BIC -- Binary Interaction Coefficients

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [BIC](#REF_HEADING_KEYWORD_BIC) keyword defines the binary interaction coefficients for each pair of compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [BIC](#REF_HEADING_KEYWORD_BIC) | A series of real numbers that define the binary interaction coefficients for each pair (*i*, *j*) of compositional components active in the model. The matrix is symmetrical with zeroes on the diagonal so only the portion of the matrix below the diagonal is required (i.e., *i* = {2, \... [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1)} and *j* \< *i*), where [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) is specified by the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The values are ordered with *j* cycling fastest (i.e. , , , , , , \...). | 0 |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record must contain [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) × ([COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) - 1) / 2 values as specified by the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.17.1: [BIC](#REF_HEADING_KEYWORD_BIC) Keyword Description

#### Examples

The following example defines the binary interaction coefficients for each pair of compositional components in a single three-component equation of state model.

\--

\-- Binary Interaction Coefficients

\--

BIC

0.1209

0.1310 0.0339 /

The following example defines the binary interaction coefficients for each component in two three-component equation of state models.

\--

\-- Binary Interaction Coefficients

\--

BIC

0.1209

0.1310 0.0339 /

0.1209

0.1310 0.0339 /

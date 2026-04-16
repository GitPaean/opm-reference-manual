### ACF -- Define Acentric Factors

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ACF](#REF_HEADING_KEYWORD_ACF) keyword defines the acentric factors for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [ACF](#REF_HEADING_KEYWORD_ACF) | A series of real numbers that define the acentric factors for each of the compositional components active in the model. | None |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record must contain [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) values as specified by the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.1.1: ACF Keyword Description

#### Examples

The following example defines the acentric factors for each component in a single three-component equation of state model.

\--

\-- Acentric Factors

\--

ACF

0.0108 0.2273 0.3434 /

The following example defines the acentric factors for each component in two three-component equation of state models.

\--

\-- Acentric Factors

\--

ACF

0.0108 0.2273 0.3434 /

0.0110 0.2281 0.3428 /

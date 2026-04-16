### VISCAQA -- Specify Ezrokhi Coefficients for Aqueous Viscosity

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [VISCAQA](#REF_HEADING_KEYWORD_VISCAQA_8_3) keyword specifies the three Ezrokhi coefficients for each compositional component and for each equation of state that are used to calculate the aqueous phase viscosity. The keyword should only be used if the compositional mode has been requested using the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is only supported by OPM Flow when the two phase gas-water CO~2~ storage model has been activated using the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword and either the [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) or the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The component names \"H2O\", \"CO2\" and \"NACL\" (water, CO~2~ and salt respectively) must be specified using the [CNAMES](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1) keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | COEFFS | A series of real numbers that define the three Ezrokhi coeffients for each of the compositional components active in the model. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each record must contain three values for each compositional component, where the number of components is specified by the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.376.1: VISCAQA Keyword Description

#### Examples

The following example defines the Ezrokhi coefficients for each component in a single three-component equation of state model.

\--

\-- Ezrokhi Coefficients for Aqueous Viscosity Calculation

\--

VISCAQA

\--COEFF0 COEFF1 COEFF2

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9 /

The following example defines the Ezrokhi coefficients for each component in two three-component equation of state models.

\--

\-- Ezrokhi Coefficients for Aqueous Viscosity Calculation

\--

VISCAQA

\--COEFF0 COEFF1 COEFF2

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9 /

\--

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9

2.0E-7 0.0 1.0E-9 /

### DENAQA -- Specify Ezrokhi Coefficients for Aqueous Density

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DENAQA keyword specifies the three Ezrokhi coefficients for each compositional component and for each equation of state that are used to calculate the aqueous phase density. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is only supported by OPM Flow when the two phase gas-water CO~2~ storage model has been activated using the CO2STORE keyword and either the GASWAT or the GAS and WATER keywords in the RUNSPEC section. The component names \"H2O\", \"CO2\" and \"NACL\" (water, CO~2~ and salt respectively) must be specified using the CNAMES keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | COEFFS | A series of real numbers that define the three Ezrokhi coeffients for each of the compositional components active in the model. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NMEOSR records as specified by the TABDIMS keyword in the RUNSPEC section.<br>2)  Each record must contain three values for each compositional component, where the number of components is specified by the COMPS keyword in the RUNSPEC section.<br>3)  Each record is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.28.1: DENAQA Keyword Description

#### Examples

The following example defines the Ezrokhi coefficients for each component in a single three-component equation of state model.

\--

\-- Ezrokhi Coefficients for Aqueous Density Calculation

\--

DENAQA

\--COEFF0 COEFF1 COEFF2

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9 /

The following example defines the Ezrokhi coefficients for each component in two three-component equation of state models.

\--

\-- Ezrokhi Coefficients for Aqueous Density Calculation

\--

DENAQA

\--COEFF0 COEFF1 COEFF2

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9 /

\--

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9

2.0E-6 -5.0E-7 2.0E-9 /

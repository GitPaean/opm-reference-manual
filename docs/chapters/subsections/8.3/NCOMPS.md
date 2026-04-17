### NCOMPS -- Confirm Number of Compositional Components

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword confirms the maximum number of compositional components in the model, as such it should have the same number of components as that declared via the COMPS keyword in the RUNSPEC section. The keyword should only be used if the CO2STORE keyword and either the GASWAT or the GAS and WATER keywords in the RUNSPEC section, have also be activated for the gas-water two component model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NCOMPS | A positive integer defining the maximum number of compositional components in the model. Secondly the number of components must be the same as that enter via the COMPS keyword in the RUNSPEC section.<br>Only the default value of two is currently supported by OPM Flow. | 2 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.90: NCOMPS Keyword Description

#### Example

The following example defines how to confirm a two component formulation to be used with the CO2STORE and GASWAT options.

\--

\-- CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)

\--

NCOMPS

2 /

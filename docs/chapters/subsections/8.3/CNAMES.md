### CNAMES -- Define Compositional Component Names

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The CNAMES keyword defines the names for each of the compositional components active in the model. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | CNAMES | A series of character strings of up to eight characters in length that define the names for each of the compositional components active in the model. | None |
| Notes:<br>1)  The keyword must contain COMPS values as specified by the COMPS keyword in the RUNSPEC section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.25: CNAMES Keyword Description

#### Example

The following example defines how to confirm a three component formulation, together with defining the names of the compositional components, to be used with the CO2STORE and GASWAT options.

\--

\-- CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)

\--

NCOMPS

3 /

\--

\-- DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)

\--

CNAMES

\'H2O\'

\'CO2\'

\'NACL\' /

### ZMFVD -- Define Compositional Components versus Depth

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ZMFVD keyword defines the compositional component mole fractions, for each component, as a function of depth, as such the keyword should have the same number of component columnar vectors as that declared via the COMPS keyword in the RUNSPEC section, and the NCOMPS keyword in the PROPS section. The keyword should only be used if the CO2STORE and GASWAT keywords in the RUNSPEC section have also be activated for the gas-water two component model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding compositional component mole fractions.<br>The default number of DEPTH values is 20, as defined by the NDRXVD parameter on the EQLDIMS keyword in the RUNSPEC section, and which may be used to reset the number of DEPTH values. | None |
| feet | m | cm |  |
| 2 | ZCOMP | A series of columnar vectors, with each columnar vector representing a compositional component mole fraction as a function of DEPTH. In addition, the sum of the compositional component mole fractions must sum to one for a given DEPTH value, otherwise an error will occur. Secondly, if the composition is independent of depth, then only one single row may be entered.<br>Note that the number of columnar vectors, should be the same as that entered via the NCOMPS keyword in the PROPS section, and the COMPS keyword in the RUNSPEC section.<br>Finally, only the default value of two components are currently supported by OPM Flow. | None |
| mole fraction | mole fraction | mole fraction |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.201: ZMFVD Keyword Description

#### Example

The following example defines how to confirm a two component formulation, together with defining the names of the composition components, as well as the compositional gradient, to be used with the CO2STORE and GASWAT options.

\--

\-- CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)

\--

NCOMPS

2 /

\--

\-- DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)

\--

CNAMES

\'CO2\'

\'H2O\' /

\--

\-- COMPOSITIONAL COMPONENT MOLE FRACTIONS VS DEPTH (OPM FLOW KEYWORD)

\--

\-- DEPTH CO2 H2O

ZMFVD

2000 0.0 1.0

2100 0.0 1.0

/

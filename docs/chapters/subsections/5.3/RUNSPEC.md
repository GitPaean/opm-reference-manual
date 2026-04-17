### RUNSPEC -- Define the Start of the RUNSPEC Section of Keywords

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RUNSPEC activation keyword marks the start of the RUNSPEC section that defines the key parameters for the simulator including the dimensions of the model, phases present in the model (oil, gas and water for example), number of tables for a given property and the maximum number of rows for each table, the maximum number of groups, wells and well completions, as well as various options to be invoked by OPM Flow.

Apart from COMMENTS entered by "\--" in columns one and two, this keyword should be the first keyword in the input deck.

There is no data required for this keyword and there is no keyword terminating "/"

#### Example

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

The above example marks the start of the RUNSPEC section in the OPM Flow data input file.

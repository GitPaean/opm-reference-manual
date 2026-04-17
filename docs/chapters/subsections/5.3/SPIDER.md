### SPIDER -- Spider Grid Activation Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SPIDER activates the OPM Flow spider grid geometry option for the model, if this keyword and the RADIAL keyword are omitted then Cartesian geometry is assumed by OPM Flow. Note that is an OPM Flow specific keyword and option.

Spider Grids basically take the standard radial geometry keywords in the grid section and transform the grid specification to an Irregular Corner-Point Grid which can then be viewed in OPM ResInsight in a more intuitive form. The only difference is that in the RUNSPEC section the SPIDER keyword is used instead of the RADIAL keyword.

See also the RADIAL keyword in the RUNSPEC section ([RADIAL -- Radial Grid Activation Option](#anchor-2)). Both Spider and Radial grids created by OPM Flow will be displayed the same in OPM ResInsight, as they are both output as Irregular Corner-Point Grid files. The difference is that the radial model's pore volumes are adjusted to match the radial geometry pore volumes, whereas, the Spider grid volumes are not adjusted. See the examples in the section on Radial Grids ([Radial Grids](#anchor-3)) and Spider Grids ([Spider Grids](#anchor-4)) for further information

#### Example

\--

\-- DEFINE SPIDER GRID GEOMETRY (OPM FLOW RADIAL GRID KEYWORD)

\--

SPIDER

The above example actives OPM Flow's spider grid geometry option.

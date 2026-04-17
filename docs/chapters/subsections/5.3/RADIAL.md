### RADIAL -- Radial Grid Activation Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

RADIAL activates the radial grid geometry option for the model, if this keyword and the SPIDER keyword are omitted then Cartesian geometry is assumed by OPM Flow.

See also the SPIDER keyword in the RUNSPEC section ([SPIDER -- Spider Grid Activation Option](#anchor-2)). This is an OPM Flow specific keyword for the simulator's Spider Grid option, that emulates a Radial Grid via corner-point geometry. Both Spider and Radial grids will be displayed the same in OPM ResInsight, as they both use Irregular Corner-Point Grid geometry. The difference is that the radial model's pore volumes are adjusted to match the radial geometry pore volumes, whereas, the Spider grid volumes are not adjusted. See the examples in the section on Radial Grids ([Radial Grids](#anchor-3)) and Spider Grids ([Spider Grids](#anchor-4)) for further information.

#### Example

\--

\-- DEFINE RADIAL GRID GEOMETRY

\--

RADIAL

The example activates the radial grid geometry option.

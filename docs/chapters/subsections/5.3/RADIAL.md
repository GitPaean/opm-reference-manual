### RADIAL -- Radial Grid Activation Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[RADIAL](#__RefHeading___Toc51752_2905512151) activates the radial grid geometry option for the model, if this keyword and the [SPIDER](#__RefHeading___Toc439805_750232207) keyword are omitted then Cartesian geometry is assumed by OPM Flow.

See also the [SPIDER](#__RefHeading___Toc439805_750232207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section ([[SPIDER -- Spider Grid Activation Option](#anchor-2)](#5.2.111.SPIDER – Spider Grid Activation Option|outline)). This is an OPM Flow specific keyword for the simulator's Spider Grid option, that emulates a Radial Grid via corner-point geometry. Both Spider and Radial grids will be displayed the same in OPM ResInsight, as they both use Irregular Corner-Point Grid geometry. The difference is that the radial model's pore volumes are adjusted to match the radial geometry pore volumes, whereas, the Spider grid volumes are not adjusted. See the examples in the section on Radial Grids ([[Radial Grids](#anchor-3)](#6.2.3.Radial Grids|outline)) and Spider Grids ([[Spider Grids](#anchor-4)](#6.2.4.Spider Grids|outline)) for further information.

#### Example

\--

\-- DEFINE RADIAL GRID GEOMETRY

\--

RADIAL

The example activates the radial grid geometry option.

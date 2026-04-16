### SPIDER -- Spider Grid Activation Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SPIDER](#__RefHeading___Toc439805_750232207) activates the OPM Flow spider grid geometry option for the model, if this keyword and the [RADIAL](#__RefHeading___Toc51752_2905512151) keyword are omitted then Cartesian geometry is assumed by OPM Flow. Note that is an OPM Flow specific keyword and option.

Spider Grids basically take the standard radial geometry keywords in the grid section and transform the grid specification to an Irregular Corner-Point Grid which can then be viewed in OPM ResInsight in a more intuitive form. The only difference is that in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section the [SPIDER](#__RefHeading___Toc439805_750232207) keyword is used instead of the [RADIAL](#__RefHeading___Toc51752_2905512151) keyword.

See also the [RADIAL](#__RefHeading___Toc51752_2905512151) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section ([[RADIAL -- Radial Grid Activation Option](#anchor-2)](#4.2.24.RADIAL – Radial Grid Activation Option|outline)). Both Spider and Radial grids created by OPM Flow will be displayed the same in OPM ResInsight, as they are both output as Irregular Corner-Point Grid files. The difference is that the radial model's pore volumes are adjusted to match the radial geometry pore volumes, whereas, the Spider grid volumes are not adjusted. See the examples in the section on Radial Grids ([[Radial Grids](#anchor-3)](#6.2.3.Radial Grids|outline)) and Spider Grids ([[Spider Grids](#anchor-4)](#6.2.4.Spider Grids|outline)) for further information

#### Example

\--

\-- DEFINE SPIDER GRID GEOMETRY (OPM FLOW RADIAL GRID KEYWORD)

\--

SPIDER

The above example actives OPM Flow's spider grid geometry option.

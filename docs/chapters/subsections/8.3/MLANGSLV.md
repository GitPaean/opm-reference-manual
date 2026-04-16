### MLANGSLV -- Define Langmuir Maximum Solvent Concentration for All Grid Cells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [MLANGSLV](#__RefHeading___Toc580808_3181922006), defines the coal bed methane Langmuir Adsorption[^1] maximum solvent concentration for each grid cell used to scale the Langmuir isotherm solvent table allocated to the cell, for when the Coal Bed Methane option has been activated via the [COAL](#__RefHeading___Toc234580_3519154785) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition, the Solvent phase must have been declared by the [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. See the [COALNUM](#__RefHeading___Toc82393_1778172979) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section for allocating the Langmuir solvent tables to the grid blocks, and also the [LANGMUIR](#__RefHeading___Toc214338_2843394514) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section for defining the Langmuir Adsorption Isotherm tables. Keywords [COALADS](#__RefHeading___Toc248981_3519154785) and [COALPP](#__RefHeading___Toc253787_3519154785), also in the [PROPS](#__RefHeading___Toc39329_784232322) section, are used to specify the relative adsorption data in runs containing the solvent phase.

Note that if he Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or the [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then [MLANGSLV](#__RefHeading___Toc580808_3181922006) applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004

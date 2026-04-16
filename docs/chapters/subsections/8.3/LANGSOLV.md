### LANGSOLV -- Langmuir Adsorption Isotherm Solvent Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [LANGMUIR](#__RefHeading___Toc214338_2843394514) keyword defines the coal bed methane Langmuir Adsorption Isotherms[^1] Solvent tables, for when the Coal Bed Methane option has been activated via the [COAL](#__RefHeading___Toc234580_3519154785) keyword and the Solvent phase has been declared by the [SOLVENT](#__RefHeading___Toc62787_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. See the [COALNUM](#__RefHeading___Toc82393_1778172979) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section for allocating the Langmuir solvent tables to the grid blocks, and also the [LANGMUIR](#__RefHeading___Toc214338_2843394514) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section for defining the Langmuir Adsorption Isotherm tables. Keywords [COALADS](#__RefHeading___Toc248981_3519154785) and [COALPP](#__RefHeading___Toc253787_3519154785), also in the [PROPS](#__RefHeading___Toc39329_784232322) section, are used to specify the relative adsorption data in runs containing the solvent phase.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004

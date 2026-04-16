### LANGMPL -- Define Langmuir Pressure Grid Cell Multiplier

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [LANGMPL](#__RefHeading___Toc208762_2843394514), defines the coal bed methane Langmuir Adsorption[^1] pressure multiplier for each grid block, for when the Coal Bed Methane option has been activated via the [COAL](#__RefHeading___Toc234580_3519154785) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword applies the multiplier to the pressure values in a cell's allocated Langmuir table when calculating a cell's adsorption capacity. See the [LANGMUIR](#__RefHeading___Toc214338_2843394514) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section for specifying the Langmuir tables for the model.

Note that if he Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or the [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then [LANGMPL](#__RefHeading___Toc208762_2843394514) applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]:  Langmuir, Irving (June 1918). \"The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum\". The Research Laboratory of the General Electric Company. 40 (9): 1361--1402. doi:10.1021/ja02242a004

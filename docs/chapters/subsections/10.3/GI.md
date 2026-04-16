### GI -- Define the Initial Equilibration Gi Values for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GI](#__RefHeading___Toc372466_1414963541) keyword defines the initial equilibration [GI](#__RefHeading___Toc372466_1414963541) values for all grid cells in the model and should be used in conjunction with the other enumeration equilibration keywords; [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the [GI](#__RefHeading___Toc372466_1414963541) Pseudo Compositional option has been activated in the model via the [GIMODEL](#__RefHeading___Toc383678_1414963541) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also the [GIALL](#__RefHeading___Toc378111_1414963541) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that sets the [GI](#__RefHeading___Toc372466_1414963541) values as a function of pressure, as well as setting the corresponding [RVGI](#__RefHeading___Toc335902_516898843), [RSGI](#__RefHeading___Toc316970_516898843), [BGGI](#__RefHeading___Toc223319_1539708736) and [BOGI](#__RefHeading___Toc223321_1539708736) values at the same time.

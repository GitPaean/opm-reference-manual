### SIGMAGD -- Dual Porosity Matrix to Fracture Sigma for Gravity Drainage (All Cells)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SIGMAGD](#__RefHeading___Toc1228903_516898843) keyword defines the dual porosity matrix to fracture transmissibility multiplier, sigma, that is applied to all cells, for when the Dual Porosity model has been activated by either the [DUALPORO](#__RefHeading___Toc241173_1772380413) or the [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition, the [GRAVDR](#__RefHeading___Toc455285_1414963541) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be used to enable the Gravity Drainage model for the run. Sigma (σ) takes into account the matrix-fracture interface area per unit volume and was defined by Kazemi et al[^1] to be:

Where lx, ly and lz are not the grid block dimensions in the model in the respective directions, but the dimensions of the blocks of the matrix material. In practice, σ is used as a tuning parameter in dual porosity runs to match reservoir and well performance.

Note that [SIGMAGD](#__RefHeading___Toc1228903_516898843) keyword data is used for areas being swept by gas and the [SIGMA](#__RefHeading___Toc695245_516898843) keyword data is used when the area is being invaded by water. See also the [SIGMAGDV](#__RefHeading___Toc1228905_516898843) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that supplies the sigma values on an individual cells basis

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Kazemi, H., Merrill JR., L. S., Porterfield, K. L., and Zeman, P. R. "Numerical Simulation of Water-Oil Flow in Naturally Fractured Reservoirs," paper SPE 5719, Society of Petroleum Engineers Journal (1976) 16, No. 6, 317-326.

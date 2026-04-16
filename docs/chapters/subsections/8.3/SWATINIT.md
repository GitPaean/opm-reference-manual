### SWATINIT -- Define the Initial Water Saturation Array for Capillary Pressure Scaling

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[SWATINIT](#__RefHeading___Toc323952_1728001293) defines the initial water saturation for all the cells in the model via an array. The keyword can be used with all grid types. [SWATINIT](#__RefHeading___Toc323952_1728001293) is used to initialize the model by setting each grid block's initial water saturation ("Sw"). If the array is present in the input deck, then OPM Flow will re-scale the water-oil capillary pressure curves entered via the [SWFN](#__RefHeading___Toc106882_335817223) saturation functions in the [PROPS](#__RefHeading___Toc39329_784232322) section, so that the resulting initialized Sw matches the values in the [SWATINIT](#__RefHeading___Toc323952_1728001293) array.

Normally the [SWATINIT](#__RefHeading___Toc323952_1728001293) array is generated in the static earth model when calculating the hydrocarbons in-place. volumes using Saturation Height Functions ("SHF") derived from capillary pressure functions. Static earth models do not directly use capillary pressure in these type of calculations as individual cell pressures are not required. There is therefore some potential for inconsistencies to arise between the two sets of formulations. This is normally manifested by extreme scaling in the scaled capillary pressure values calculated by the simulator. If this is the case then the [PPCWMAX](#__RefHeading___Toc150617_332691817) keyword can be used to set a maximum scaled capillary pressure value. Note that as large values of scaled capillary pressures can result in numerical issues, a more technically sound approach would be to resolve these inconsistencies before continuing with the model build.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWATINIT](#__RefHeading___Toc323952_1728001293) | [SWATINIT](#__RefHeading___Toc323952_1728001293) is an array of real positive numbers that are greater than or equal to zero and less than or equal to one, that define the initial water saturation values to each cell in the model.<br>Repeat counts may be used, for example 3000\*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.184: SWATINIT Keyword Description

See also the [PPCWMAX](#__RefHeading___Toc150617_332691817) to control the re-scaling of the capillary pressure entries on the [SWFN](#__RefHeading___Toc106882_335817223) saturation function keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

\--

\-- DEFINE GRID BLOCK INITIAL SW DATA FOR ALL CELLS

\-- (BASED ON NX x NY x NZ = 300)

\--

SWATINIT

300\*0.300 /

The above example defines a constant initial water saturation of 0.300 to all 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

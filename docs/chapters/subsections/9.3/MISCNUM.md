### MISCNUM -- Define the Miscibility Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MISCNUM](#__RefHeading___Toc129667_83452205) keyword defines the miscibility region number mixing tables as defined by the [TLMIXPAR](#__RefHeading___Toc121483_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, for when the miscibility option has been activated by the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [MISCNUM](#__RefHeading___Toc129667_83452205) also allocates miscible residual oil saturation versus water saturation tables ([SORWMIS](#__RefHeading___Toc121477_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section) used to calculate the relative permeability and PVT properties for a grid cell.

Note that although this keyword can only be used when the miscibility option is active, it is not necessary to use this keyword even if the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) has been activated as the default value of one will be applied to all grid blocks. Secondly, a value of zero for a grid cell results in immiscible fluids in that grid cell.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [MISCNUM](#__RefHeading___Toc129667_83452205) | [MISCNUM](#__RefHeading___Toc129667_83452205) defines an array of positive integers greater than or equal to zero, that assign a grid cell to a particular table of mixing parameters as defined by the [TLMIXPAR](#__RefHeading___Toc121483_83452205) and [SORWMIS](#__RefHeading___Toc121477_83452205) keywords.<br>A value of zero sets the fluids within a grid cell to be immiscible.<br>The maximum number of [MISCNUM](#__RefHeading___Toc129667_83452205) regions is set by the NTMIS variable on the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  If a cell is not assigned a [MISCNUM](#__RefHeading___Toc129667_83452205) region then the default value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.15: MISCNUM Keyword Description

See also the [TLMIXPAR](#__RefHeading___Toc121483_83452205) and [SORWMIS](#__RefHeading___Toc121477_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The example below sets three [MISCNUM](#__RefHeading___Toc129667_83452205) regions in the model on a layer by layer basis, using the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

MISCNUM 1 1\* 1\* 1\* 1\* 1 12 / SET REGION 1

MISCNUM 2 1\* 1\* 1\* 1\* 13 55 / SET REGION 2

MISCNUM 3 1\* 1\* 1\* 1\* 56 120 / SET REGION 3

/

### DIMENS -- Define the Dimensions of the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

DIMENS defines the dimensions of the model entered as integer vector. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NX | A positive integer value that defines the number of grid blocks in the x direction for Cartesian grids or the number of grid blocks in the r direction for radial grids | None |
| 2 | NY | A positive integer value that defines the number of grid blocks in the y direction for Cartesian grids or the number of grid blocks in the theta direction for radial grids. | None |
| 3 | NZ | A positive integer value that defines the number of grid blocks in the z direction for both Cartesian and radial grids. | None |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.9: DIMENS Keyword Description

Note that NX, NY and NZ are not maximum values but the actual size of the grid. OPM Flow applies these parameters when reading in particular data sets. For example if NX, NY, and NZ are set to 10, 10 and 10 respectively, then for the grid property data like PORO. OPM Flow expects to read in 10 x 10 x 10 or 1,000 porosity values for the PORO array. If the number of porosity values is not equal to 1,000 then OPM Flow will produce an error.

#### Example

\--

\-- MAX MAX MAX

\-- NDIVIX NDIVIY NDIVIZ

DIMENS

46 112 22 /

The above example defines the dimensions for the Norne model of 46 cells in the x direction, 112 cells in the y direction and 22 cells in the z direction.

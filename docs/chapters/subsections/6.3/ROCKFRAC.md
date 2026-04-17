### ROCKFRAC -- Define the Rock Volume to Bulk Volume Fraction for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ROCKFRAC defines the rock volume to bulk volume fraction for all the cells, The keyword can be used with all grid types. Rock volume of a grid block is calculated by multiply a cell's bulk volume by it's ROCKFRAC volume. A cell's rock volume is used in the Coal option to calculate the adsorbed gas in the rock (coal), as well as the Thermal and Temp options to calculate the energy is stored in the rock.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ROCKFRAC | ROCKFRAC is an array of real numbers greater than or equal to zero and less than or equal to one, that are assigned the rock volume to bulk volume fraction values for each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 200\*0.850. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Setting a cells ROCKFRAC value to zero will make the cell inactive, similar to setting the cells ACTNUM property to zero.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.115: NTG Keyword Description

See also the PORO, PERMX, PERMY, PERMZ and NTG keywords to fully define a grid's properties.

#### Example

\--

\-- DEFINE GRID ROCKFRAC DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

ROCKFRAC

100\*1.000 100\*0.850 100\*0.500 /

The above example defines a constant ROCKFRAC of 1.00 for the first 100 cells, then 0.85 for the second 100 hundred cells, and finally 0.500 for the last 100 cell, for the 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.

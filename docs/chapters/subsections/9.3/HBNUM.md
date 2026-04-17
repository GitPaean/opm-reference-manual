### HBNUM -- Define Herschel-Bulkley Region Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HBNUM keyword defines the Herschel-Bulkley rheological property table region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which table of Herschel-Bulkley rheological property data is assigned to a grid block, for when the Polymer option has been invoked via the POLYMER keyword in the RUNSPEC section and the Non-Newtonian Fluid phase has been declared active by the NNEWTF keyword, also in the RUNSPEC section. The FHERCHBL keyword in the PROPS section is used to specify the Herschel-Bulkley rheological property table data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

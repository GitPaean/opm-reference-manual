### OILAPI -- Define the Initial Equilibration Oil API for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The OILAPI keyword defines the initial equilibration oil API gravity pressures for all grid cells in the model, for when the Oil API Tracking option as been invoked by the API keyword in the RUNSPEC section. The keyword should be used in conjunction with the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model.

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the EQUIL keyword in the SOLUTION section. This is the non-standard formulation to initialize the model and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | OILAPI | OILAPI is an array of real positive numbers assigning the initial equilibration oil API gravity to each cell in the model.<br>The American Petroleum Institute ("API") classifies oils based on an API gravity (γ~API~), or degrees API (^o^API), the relationship between relative density (γ~o~) of oil and API gravity (γ~API~) is given by:<br>Repeat counts may be used, for example 20\*38.5 | None |
| ^o^API | ^o^API | ^o^API |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.18: OILAPI Keyword Description

See also the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION OIL API FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

OILAPI

1000\*40.2 1000\*39.5 1000\*38.2 /

The above example defines the initial equilibration oil API gravity to be 40.2 for all the cells in the first layer, 39.5 for all the cells in the second layer, and finally 38.2 for all the cells in the third layer.

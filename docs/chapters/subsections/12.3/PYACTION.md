### PYACTION -- Define Python Based Action Conditions and Command Processing

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PYACTION keyword is part of OPM Flow's Python scripting facility that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time. The "included" Python script file is executed by the standard Python interpreter. Thus, OPM Flow's Python scripting facility offers greater flexibility compared to the commercial simulator's ACTION series of keywords (ACTION, ACTIONG, ACTIONR, ACTIONS, ACTIONW and ACTIONX) that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. Note that OPM Flow has also implemented the commercial simulator's ACTIONX keyword, but not the ACTION, ACTIONG, ACTIONR, ACTIONS and ACTIONW keywords, as the ACTIONX keyword implements their functionality with greater flexibility. For a python class documentation and for further documentation and examples, also refer to the [OPM Online Python Documentation](https://opm.github.io/opm-python-documentation/index.html).

This keyword starts the definition of a PYACTION section that specifies the name of the action and a string indicating the number of times the action should be run; this is then followed by the name of the file containing the Python script. Note that unlike an ACTIONX block that is terminated by the ENDACTIO keyword the PYACTION section has no terminating keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the PYACTION facility allows the user to implement complex functionality and the implementation was new for the 2020-04 release. Users should therefore use caution when using this facility.

| PYACTION | PYACTION declares the start of a PYACTION Definition Section. This is then followed by one record that defines the name of the action and a string indicating the number of times the action should be run; this is then followed by a second record indicating the file containing the Python script. | Not Applicable |  |
| --- | --- | --- | --- |
| 1-1 | ACTNAME | ACTNAME is a character sting of any length enclose in quotes that defines the name of this action definition. | None |
| 1-2 | ACTNSTEP | ACTNSTEP is a defined character string that indicates the number of times the action should be performed, and should be set to one of the following:<br>1)  SINGLE: Here the action script is run only once.<br>2)  UNLIMITED: If this option is selected then the action is run at the end of every time step.<br>3)  FIRST_TRUE: This option forces the action to be run at the end of every time step until the script returns a value of True.<br>Note that the FIRST_TRUE option is only supported for back compatibility when using the deprecated run() function style Python scripts. | SINGLE |
| 1-4 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | FILENAME | A character string enclosed in quotes that defines the Python module/script file to read in and to be processed by OPM Flow. | None |
| 2-2 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  There is no terminating "/" for this keyword. |  |  |  |

Table 12.60: PYACTION Keyword Description

The PYACTION keyword is a result of combining two programming languages, the interactive Python interpreter and OPM Flow's source code language C++. When combing two languages one extends and embeds one into the other. When extending Python with C++ the functionality implemented in C++ is made available to Python applications, when embedding Python in C++ one can call Python functions from within C++. The PYACTION keyword is based on embedding a Python interpreter in the C++ OPM Flow simulator, such that Python code is run from within the simulator.

Note that to use the PYACTION keyword OPM Flow must be built with embedded python enabled in opm-common/CMakeLists.txt.

option(OPM_ENABLE_EMBEDDED_PYTHON \"Enable embedded python?\" ON)

In order to fully benefit from the power of the PYACTION keyword one should familiarize oneself with the Python wrapper classes for the various OPM Flow C++ classes. These classes are essential to share the simulator state with the PYACTION script. That is, the function provides the interface between the two programming languages.

To learn more about these classes you can use the pydoc utility, for example, to learn more about the SummaryState class, in a Linux terminal one would issue the following bash command:

bash% pydoc opm.io.sim.SummaryState

The Python script file (FILENAME in the PYACTION keyword) should be a standard Python module[^1] that defines the PYACTION script and should consist of 100% pure Python. The PYACTION Python module (FILENAME) is imported during processing of the input deck and as such this implies:

3)  1)  1)  Basic Python syntax checking is performed when the Python module (FILENAME) is read in.

        2)  It is verified that the module has the correct format.

The syntax of the Python module (FILENAME) is given in together with a description of the Python module opm_embedded.

| 1 | ecl_state | The ecl_state variable is an instance of the opm.io.ecl_state.EclipseState class which is initialized with all the static information in the simulation, for example the 3D grid properties and the PVT and saturation tables.<br>This object can be read by the Python script but the available data should not be modified as any updates will not be passed back to the simulator. |
| --- | --- | --- |
| 2 | schedule | The schedule variable is an instance of the opm.io.sched.Schedule class which has all the SCHEDULE information internalized (Schedule object). For a complete documentation of the available call points of opm.io.schedule.Schedule, we refer to <https://opm.github.io/opm-python-documentation/master/common.html#opm.io.schedule.Schedule>. The most notable ones are:<br>schedule.open_well(well_name, report_step)<br>schedule.shut_well(well_name, report_step)<br>schedule.stop_well(well_name, report_step)<br>Which can be used to open, shut or stop a well at a particular report step (or at the current report step if the report_step argument is not specified), and:<br>schedule.insert_keywords(kw)<br>Which can be used to insert various keywords where kw is a string defining the keyword and associated records. For the 2024.10 release this has been tested with the following keywords:<br>BOX,<br>COMPSEGS,<br>ENDBOX, EXIT,<br>FIELD,<br>INCLUDE,<br>GCONINJE, GCONPROD, GCONSUMP, GEFAC, GRUPTREE,<br>METRIC, MULTX, MULTX-, MULTY, MULTY-, MULTZ, MULTZ-,<br>NEXT, NEXTSTEP,<br>WCONINJE, WCONPROD, WECON, WEFAC, WELOPEN, WELPI, WELTARG, WGRUPCON, WELSEGS, WELSPECS, WSEGVALV, WLIST, WPIMULT, WTEST, WTMULT<br>This list is subject to change for future releases.<br>The parsing strictness for the ACTIONX and PYACTION keywords can be set using the \--action-parsing-strictness command line option. If the default option \--action-parsing-strictness=\"normal\" has been set then OPM Flow will only apply keywords that have been tested, whereas if the option \--action-parsing-strictness=\"low\" has been set then OPM Flow will attempt to apply all keywords (however the simulation results may be incorrect).<br>Adding additional call points to the opm.io.schedule.Schedule instance in order to update the Schedule object in more ways is an obvious candidate for improving the PYACTION functionality. |
| 3 | report_step | The current report step. |
| 4 | summary_state | The summary_state variable is an instance of the opm.io.sim.SummaryState class, the purpose of this class is to serve as a container for SUMMARY variables that contain the simulation results; for example, the Field Oil Rate (FOPR) or a Well's Water CuT (WWCT). See the [SUMMARY SECTION](#anchor-2) for a detailed description of the variables available.<br>The summary_state variable will typically be the variable one will use to access the state of the simulation. For example, to check if the water cut in well OP01 exceeds 0.5 one would use the following statement:<br>if summary_state.well_var(\"OP01\", \"WWCT\") \> 0.50:<br>\...<br>The summary_state variable can also be use to update variables including UDQ variables, i.e:<br>summary_state.update_well_var(\"OP01\", \"WUXX\", 0.25)<br>The above assigns a value of 0.25 to the well UDQ variable WUXX for well OP01. |

Table 12.61: PYACTION Module Script Definition

See also the PYINPUT and PYEND keywords in the GRID[^2] section which are also part of OPM Flow's Python scripting facility, that process standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck. The main purpose of the facility is to script the construction of the various keywords.

#### Examples

The first example checks if well OP01 has a water cut greater than 0.8 and if so then the well is shut in. In the input deck we would have:

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'MAXWCUT\' \'UNLIMITED\' /

\'pthon/script/MAXWCUT.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/MAXWCUT.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

executed = False

setup_done = True

if (not executed and summary_state.well_var(\"OP1\", \"WWCT\") \> 0.80):

message = \"Well OP01 has been shut-in due to WWCT \> 0.80\\n\"

opm_embedded.OpmLog.info(message)

schedule.shut_well(\"OP1\")

executed = True

Note how the \'executed\' variable is used to ensure that the action is only executed once the first time the water cut is greater than 0.8.

The next example is based on the first example from the ACTIONX keyword ([ACTIONX -- Define Action Conditions and Command Processing](#anchor-4)). The Python script first checks if the field's water production is greater than 30,000 stb/d, and if not returns control back to the simulator. If the field water production is greater than 30,000 stb/d then the script uses a Python variable count to keep track of the number of times the script has been executed, and then sorts the wells from high water cut to low, via the wct_list variable, and then shuts in the worst offending well. If a well is shut-in the count variable is increased by one and control is passed back to the simulator. The script is executed as maximum of ten times.

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'WSHUTIN\' \'UNLIMITED\' /

\'pthon/script/WSHUTIN.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/WSHUTIN.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

execution_counter = 0

setup_done = True

if (execution_counter \< 10 and summary_state\[\"FWPR\"\] \>= 30000):

\#

\# Get Sorted Well List

\#

wct_list = sorted( \[ (well, summary_state.well_var(well, \"WWCT\"))

for well in summary_state.wells\], reverse=True )

\#

\# Shut-in Well with Highest Water Cut

\#

well, wwct = wct_list\[0\]

if wwct \> 0:

schedule.shut_well(well)

execution_counter += 1

Note that by using PYACTION it makes sense to combine the UDQ variable into the PYACTION statement, like shown in the example above, although this is not necessary, as one could in principle use a normal UDQ statement and then access the variables in the PYACTION script using the summary_state variable.

The final example checks to see if the field's gas rate is below 600 MMscf/d and if the simulation time is greater that January 1, 2030. If it is, then compression is installed by re-setting all the gas producing well's THP and BHP pressures to 450 psia and 300 psia respectively. In addition all gas wells currently shut-in are tested to see if they can be opened up under the new THP and BHP constraints.

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'WSHUTIN\' \'UNLIMITED\' /

\'pthon/script/PHASE3.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/PHASE3.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import datetime

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

executed = False

setup_done = True

if not executed:

sim_time = schedule.start +

datetime.timedelta( seconds = summary_state.elapsed() )

if (summary_state\[\"FGPR\"\] \< 600000 and

sim_time \> datetime.datetime(2030, 1, 1)):

\#

\# Do WELTARG and WTEST action

\#

\...

executed = True

Note how the current simulation time (sim_time) is evaluated from the simulation start time (schedule.start) and elapsed time (summary_state.elapsed); and how it is compared with 00:00 on 1 January 2030 using the Python datetime module.

[^1]: A Python module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module's name (as a string) is available as the value of the global variable \_\_name\_\_.

[^2]: Note the PYINPUT and PYEND keywords can be used in the GRID, EDIT, PROPS, SOLUTION, SUMMARY and SCHEDULE sections, but are described in the GRID section.

A.

B.  # RUNNING PREVIOUS RELEASES OF OPM FLOW

A.  1.  ## Running OPM Flow 2025-04

The command line syntax for running OPM Flow is:

flow \[OPTIONS\] CASENAME

and typing the following command from your terminal:

flow CASENAME

will start the simulator and run the case specified by CASENAME.DATA.

OPM Flow accepts command line options to control various aspects of the simulator's run time behavior, as described in the table below. To give a command line option use "key=value" syntax, with no spaces around the equals sign. It is also possible to put multiple options together in a parameter file. To do so, put one option on each line of the file with ".param" as the extension and pass that filename as a command line parameter to OPM Flow using:

flow \--parameter-file=CASENAME.param

to instruct OPM Flow to read the parameter file.

| 1 | -h or \--help | A character string that causes OPM Flow to print a help message that gives a brief description of the available command line parameters.<br>This now only prints the active user facing command line options. | N/A |
| --- | --- | --- | --- |
| 2 | \--help-all | Prints all the command line options included in the release, including obsolete, hidden and deprecated options. | N/A |
| 3 | \--accelerator-mode | A defined character string that selects the linear solver, usage: \'\--accelerator-mode=\[none\|cusparse\|opencl\|amgcl\|rocalution\|rocsparse\]\'. | \"none\" |
| 4 | \--action-parsing-strictness | A defined character string. Set strictness of parsing process for ActionX and PyAction. Available options are normal (do not apply keywords that have not been tested for ActionX or PyAction) and low (try to apply all keywords, beware: the simulation outcome might be incorrect). | \"normal\" |
| 5 | \--add-corners | A boolean value. Add corners to partition. | false |
| 6 | \--allow-distributed-wells | Allow the perforations of a well to be distributed to interior of multiple processes. | false |
| 7 | \--allow-splitting-inactive-wells | A boolean value. Allow inactive (never non-shut) wells to be split across multiple domains. | true |
| 8 | \--alternative-well-rate-init | Use alternative well rate initialization procedure. | true |
| 9 | \--bda-device-id | Renamed as \--gpu-device-id. | 0 |
| 10 | \--check-group-constraints-inner-well-iterations | A boolean value. Allow checking of group constraints during inner well iterations. | true |
| 11 | \--check-satfunc-consistency | A boolean value. Whether or not to check saturation function consistency requirements. | false |
| 12 | \--continue-on-convergence-error | Continue with a non-converged solution instead of giving up if we encounter a time step size smaller than the minimum time step size. | false |
| 13 | \--convergence-monitoring | A boolean value. Enable convergence monitoring. | false |
| 14 | \--convergence-monitoring-cut-off | An integer value. Cut off limit for convergence monitoring. | 6 |
| 15 | \--convergence-monitoring-decay-factor | A real value. Decay factor for convergence monitoring. | 0.75 |
| 16 | \--cpr-reuse-interval | A positive integer that sets the reuse preconditioner interval. Used when<br>*\--cpr-reuse-setup*<br>is set to 4, then the preconditioner will be fully recreated instead of reused every N linear solve, where N is this parameter. | 30 |
| 17 | \--cpr-reuse-setup | A positive integer that defines if the CPR solver should re-use the AMG setup. Valid options are:<br>0.  Recreate the preconditioner for every linear solve.<br>1.  Recreate once every time step.<br>2.  Recreate if last linear solve took more than 10 iterations.<br>3.  Never recreate.<br>4.  Recreate every N linear solves, where N is the parameter \--cpr-reuse-interval.<br>Changed the default value from three to four. | 4 |
| 18 | \--dbph-max-rel | A real positive value that sets the maximum relative change of the bottom-hole pressure in a single iteration. | 1.0 |
| 19 | \--debug-emit-cell-partition | A boolean value that determines whether (true) or not (false) to emit cell partitions as a debugging aid. | false |
| 20 | \--dp-max-rel | A real positive double precision value that sets the maximum allowed relative change of pressure per iteration. | 0.3 |
| 21 | \--ds-max | A real positive double precision value that sets the maximum allowed change in saturation per iteration. | 0.2 |
| 22 | \--dwell-fraction-max | A real positive value that sets the maximum allowed change in well's volume fraction per iteration. | 0.2 |
| 23 | \--ecl-deck-file-name | A character string that defines the name of the OPM Flow input file which contains the simulator's ECLIPSE formatted input deck to be simulated.<br>Note that there must be no spaces in the filename. If there are spaces, which can typically occur on Windows based systems, then the filename should be enclosed in quotes; thus instead of FILE NAME use "FILE NAME". | "" |
| 24 | \--ecl-output-double-precision | A boolean value that switches on (true) or off (false) double precision in restart files.<br>Useful for \'perfect\' restarts. | false |
| 25 | \--ecl-output-interval | An integer value defining the number of report steps that ought to be skipped between two writes of restart files results. | -1 |
| 26 | \--edge-weights-method | A defined positive integer value that defines the edge-weighing strategy:<br>0.  For uniform,<br>1.  for trans, or<br>2.  for log(trans). | 1 |
| 27 | \--enable-adaptive-time-stepping | A boolean value that turns on (true) or off (false) adaptive time stepping. If set to false the report time steps provided by the input deck are used. | true |
| 28 | \--enable-async-ecl-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to restart and summary files in the commercial simulator's format on a separate thread. | true |
| 29 | \--enable-async-vtk-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to the VTK output files on a separate thread. | true |
| 30 | \--enable-drift-compensation | A boolean value that enables (true) or disables (false) partial compensation of systematic mass losses via the source term of the next time step. | false |
| 31 | \--enable-dry-run | A boolean value that specifies if the simulation should actually run (true), or just check the input deck (false).<br>This option is equivalent to activating the NOSIM keyword in the RUNSPEC section of the input deck (see section [Error: Reference source not found](#anchor-1)[Error: Reference source not found](#anchor-1)).<br>The default value of "auto' will use whatever is stipulated in the input deck via the NOSIM keyword. | "auto" |
| 32 | \--enable-ecl-output | A boolean value that specifies if the binary output files (restart, summary files, etc.) should be written in the commercial simulator's format (true), or OPM Flow's format (false). | true |
| 33 | \--enable-esmry | A boolean value that switches on (true) or off (false) the output of SUMMARY vectors to the ESMRY file for fast loading of summary data. | false |
| 34 | \--enable-gravity | A boolean value that switches on (true) or off (false) the use of the gravity correction for the pressure gradients. | true |
| 35 | \--enable-grid-adaptation | A boolean value that enables (true) or disables (false) adaptive grid refinement/coarsening. Note that Eclipse grid output will be disabled if adaptive grid refinement/coarsening is enabled. | false |
| 36 | \--enable-intensive-quantity-cache | A boolean value that switches on (true) or off (false) the caching of intensive quantities. | true |
| 37 | \--enable-logging-fallout-warning | A boolean value that sets the developer option to see whether logging was on non-root processors (true). If set to true output will be appended to the \*.DBG or \*.PRT files. | false |
| 38 | \--enable-opm-rst-file | A boolean value set to true or false to write OPM specific data sets to the commercial simulators restart file to enable restart of OPM Flow runs by OPM Flow (true), or not to write the data (false). | false |
| 39 | \--enable-storage-cache | A boolean value that turns on (true) or off (false) storing previous storage terms and avoid re-calculating them. | true |
| 40 | \--enable-terminal-output | A boolean value that turns on (true) or off (false) high-level information about the simulation\'s progress to the terminal | true |
| 41 | \--enable-thermodynamic-hints | A boolean value that enables (true) or disables (false) thermodynamic hints. | false |
| 42 | \--enable-tuning | A boolean value that instructs OPM Flow to read the time stepping and convergence parameters from the TUNING keyword in the input deck, if set to true.<br>Note that only some of the TUNING keyword parameters are processed. | false |
| 43 | \--enable-vtk-output | A boolean value that turns on (true) or off (false) a global switch for writing VTK files. | false |
| 44 | \--enable-well-operability-check | A boolean value that enables (true) checking of a well's operating status, or disables (false) the checking. | true |
| 45 | \--enable-well-operability-check-iter | A boolean value that enables (true) checking of a well's operating status during iterations, or disables (false) the checking during iterations. | false |
| 46 | \--enable-write-all-solutions | A boolean value that turns on (true) or off (false) the writing of all solutions to disk instead of only the ones for the report steps. | false |
| 47 | \--end-time | A real value. The simulation time at which the simulation is finished \[s\]. | 1e+100 |
| 48 | \--explicit-rock-compaction | A boolean value. Use pressure from end of the last time step when evaluating rock compaction (true) or not (false). | false |
| 49 | \--external-partition | A quoted character string. Name of file from which to load an externally generated partitioning of the model\'s active cells for MPI distribution purposes. If empty, the built-in partitioning method will be employed. | "" |
| 50 | \--force-disable-fluid-in-place-output | A boolean value that instructs OPM Flow not to print the Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 51 | \--force-disable-resv-fluid-in-place-output | A boolean value that instructs OPM Flow to not to print the Reservoir Volume Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 52 | \--full-time-step-initially | A boolean value that instructs OPM Flow to always attempt to finish a report step using a single time step (true) or not (false). | false |
| 53 | \--gpu-device-id | An integet value. Choose device ID for cusparseSolver or openclSolver, use \'nvidia-smi\' or \'clinfo\' to determine valid IDs. | 0 |
| 54 | \--ignore-keywords | A character string that defines a list of keywords which should be ignored by OPM Flow. The keyword string should be enclosed in quotes and each keyword separated by a colon, that is \':\'. | "" |
| 55 | \--ilu-fillin-level | A positive integer value that sets the fill in level for the ILU preconditioner. | 0 |
| 56 | \--ilu-redblack | A boolean value that instructs OPM Flow to use red-black partitioning for the ILU preconditioner. | false |
| 57 | \--ilu-relaxation | A real positive double precision value that sets the relaxation factor of the linear solver\'s ILU preconditioner. | 0.9 |
| 58 | \--ilu-reorder-spheres | A boolean value that specifies OPM Flow to reorder the entries of the matrix in the red-black ILU preconditioner in spheres starting at an edge (true) or not (false).<br>If false the original ordering is preserved in each color. Otherwise try to ensure D4 ordering (in a 2D structured grid, the diagonal elements are consecutive). | false |
| 59 | \--imbalance-tol | A real value. Tolerable imbalance of the load balancing. | 1.1 |
| 60 | \--initial-time-step-in-days | A real double precision value that sets the size of initial time step in days. | 1.0 |
| 61 | \--initial-time-step-size | A real double precision value that sets the size of initial time step in seconds. | 86400 |
| 62 | \--inj-mult-damp-mult | A real value. Injection multiplier dampening factor (dampening multiplied by this each time oscillation is detected). | 0.9 |
| 63 | \--inj-mult-min-damp-factor | A real value. Minimum injection multiplier dampening factor (maximum dampening level). | 0.05 |
| 64 | \--inj-mult-osc-threshold | A real value. Injection multiplier oscillation threshold (used for multiplier dampening). | 0.1 |
| 65 | \--input-skip-mode | A defined character string. Set compatibility mode for the SKIP100/SKIP300 keywords. Options are: 100 (skip SKIP100..ENDSKIP, keep SKIP300..ENDSKIP), 300 (skip SKIP300..ENDSKIP, keep SKIP100..ENDSKIP) or all (skip both SKIP100..ENDSKIP and SKIP300..ENDSKIP). | \"100\" |
| 66 | \--linear-solver | A defined quoted character string that sets the configuration of the linear solver, valid values are:<br>1)  cprw[^1] [^2] [^3] (default),<br>2)  ilu0,<br>3)  dilu,<br>4)  cpr (an alias for cprw),<br>5)  cpr_quasiimpes,<br>6)  cpr_trueimpes,<br>7)  cpr_trueimpesanalytic,<br>8)  amg[^4],<br>9)  hybrid (experimental), or<br>10) a file name that has the extension ".json", that contains the linear solver configuration parameters.<br>Option (1) extends the existing Constrained Pressure Residual ("CPR") preconditioner to include wells. This option can also be invoked via the CPR keyword in the RUNSPEC section; however, the command line parameter takes precedence.<br>For option (10) one enters a character string enclosed in quotes that defines the filename of a JSON configuration file for the flexible linear solver system. In this case the file extension should be '.json'.<br>Note that the \*.PRT file contains the "Property tree for the linear solver" listing, which is the JSON specification of the current case, and can be used to configure a user specific linear solver JSON file. | \"cprw\" |
| 67 | \--linear-solver-ignore-convergence-failure | A boolean value that if set to true convergences failures in the linear solver are ignored.<br>This option should be used with care, as the results might be unreliable. | false |
| 68 | \--linear-solver-max-iter | A positive integer value that defines the maximum number of linear iterations. | 200 |
| 69 | \--linear-solver-print-json-definition | Write the JSON definition of the linear solver setup to the DBG file. | true |
| 70 | \--linear-solver-reduction | A real positive double precision value that sets the minimum reduction of the residual for the linear solver. The linear solver convergences when the residual is reduced sufficiently.<br>The simulator now overrides the default reduction to be 0.005 instead of 0.01, if the linear solver has been set to one of the cpr options, in a similar manner as how the default maximum number of linear iterations for the cpr and cprw options are changed to 20 instead of 200, unless specified by the command line option by the user. | 0.01 |
| 71 | \--linear-solver-restart | A positive integer value that sets the number of iterations after which GMRES is restarted. | 40 |
| 72 | \--linear-solver-verbosity | A positive integer value that defines the output from linear solver:<br>0.  No extra output,<br>1.  output per solution iteration, or<br>2.  output per iteration. | 0 |
| 73 | \--load-file | A character string enclosed in quotes that defines the FileName for the .OPMRST file used to load the serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 74 | \--load-step | An integer value that determines if the simulator should load the serialized state from OPM Flow\'s version of the restart file, and should be set to either a specific report step, or 0 to load the last stored report step.<br>The default value of -1 does not load the data from the OPM Flow specific restart file.<br>OPM Flow\'s version of the restart file, is written using the \--save-step=N option. | -1 |
| 75 | \--local-domains-ordering-measure | A character string enclosed in quotes that defines the subdomain ordering measure. Allowed values are \'maxpressure\', 'averagepressure' and \'residual\'. | \"maxpressure\" |
| 76 | \--local-domains-partition-well-neighbor-levels | An integer value. Number of neighbor levels around wells to include in the same domain during NLDD partitioning. | 1 |
| 77 | \--local-domains-partitioning-imbalance | A real positive double precision value that sets the subdomain partitioning imbalance tolerance. 1.03 is 3 percent imbalance. | 1.03 |
| 78 | \--local-domains-partitioning-method | A character string enclosed in quotes that defines the subdomain partitioning method. Allowed values are \'zoltan\', \'simple\', and the name of a partition file ending with \'.partition\'. | \"zoltan\" |
| 79 | \--local-solve-approach | A character string enclosed in quotes that defines the local solve approach. Valid choices are 'jacobi' and 'gauss-seidel'. | \"gauss-seidel\" |
| 80 | \--local-tolerance-scaling-cnv | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 0.1 |
| 81 | \--local-tolerance-scaling-mb | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 1 |
| 82 | \--local-well-solve-control-switching | A boolean value that allows (true) or disallows (false) control switching during local well solutions. | true |
| 83 | \--matrix-add-well-contributions | A boolean value that if set to true explicitly specifies the influences of wells between cells in the Jacobian and preconditioner matrices. | false |
| 84 | \--max-inner-iter-ms-wells | A positive integer value that defines the maximum number of inner iterations for multi-segment wells. | 100 |
| 85 | \--max-inner-iter-wells | A positive integer value that defines the maximum number of inner iterations for standard wells. | 50 |
| 86 | \--max-local-solve-iterations | A positive integer value that defines the maximum number of iterations for local solves with NLDD nonlinear solver. | 20 |
| 87 | \--max-newton-iterations-with-inner-well-iterations | A positive integer that specifies the maximum Newton iterations with inner well iterations. | 8 |
| 89 | \--max-pressure-change-ms-wells | A real positive value that defines the maximum relative pressure change for a single iteration of the multi-segment well model. | 1e+06 |
| 90 | \--max-residual-allowed | A real positive value that sets the absolute maximum tolerance for residuals without cutting the time step size. | 1e+07 |
| 91 | \--max-single-precision-days | A real positive value that sets the maximum time step size where single precision floating point arithmetic can be used for solving the linear systems of equations. | 20.0 |
| 92 | \--max-temperature-change | A real positive value that stipulates the maximum absolute change of temperature in a single iteration. | 5 |
| 93 | \--max-time-step-divisions | A positive integer that specifies the maximum number of divisions by two of the timestep size before the simulation bails out. | 10 |
| 94 | \--max-time-step-size | A real positive value that defines the maximum size to which all time steps are limited to in seconds. | inf |
| 95 | \--max-welleq-iter | A positive integer that defines the maximum number of iterations to determine the solution to the well equations. | 30 |
| 96 | \--maximum-number-of-group-switches | An integer value. Maximum number of times a group can switch to the same control. | 3 |
| 97 | \--maximum-number-of-well-switches | A positive **integer** values that stipulates the maximum number of times a well can switch to the same control. | 3 |
| 98 | \--maximum-water-saturation | A real positive value that defines the maximum water saturation. | 1.0 |
| 99 | \--metis-params | A character string. Configuration of Metis partitioner. You can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/manual.pdf for available METIS options. | \"default\" |
| 100 | \--milu-variant | A defined character string that specifies which variant of the modified ILU preconditioner ought to be used. Possible variants are:<br>1)  ILU (default, plain ILU),<br>2)  MILU_1 (lump diagonal with dropped row entries),<br>3)  MILU_2 (lump diagonal with the sum of the absolute values of the dropped row entries),<br>4)  MILU_3 (if diagonal is positive add sum of dropped row entries. Otherwise subtract them),<br>5)  MILU_4 (if diagonal is positive add sum of dropped row entries. Otherwise do nothing). | "ILU" |
| 101 | \--min-strict-cnv-iter | A positive integer that sets the minimum number of Newton iterations before relaxed tolerances are used for the CNV convergence criterion. | -1 |
| 102 | \--min-strict-mb-iter | An integer value defining the number of Newton iterations before relaxed tolerances can be used for the MB convergence criterion. Default -1 means that the relaxed tolerance is used when maximum number of Newton iterations are reached. | -1 |
| 103 | \--min-time-step-based-on-newton-iterations | A real positive value that sets the minimum time step size (in days for field and metric unit and hours for lab unit) can be reduced to based on Newton iteration counts. | 0.0 |
| 104 | \--min-time-step-before-shutting-problematic-wells-in-days | A real positive value that sets the minimum time step size in days for which problematic wells are not shut. Time steps below this value will result in problematic wells being shut-in by the simulator. | 0.01 |
| 105 | \--min-time-step-size | A real positive value that sets the minimum size to which all time steps are limited to in seconds. | 0.0 |
| 106 | \--network-max-iterations | Replaced by \--network-max-outer-iterations. | 200 |
| 107 | \--network-max-outer-iterations | An integer value. Maximum outer number of iterations in the network solver before giving up. | 10 |
| 108 | \--network-max-pressure-update-in-bars | A real value. Maximum pressure update in the inner network pressure update iterations. | 5 |
| 109 | \--network-max-strict-iterations | Replaced by \--network-max-strict-outer-iterations. | 100 |
| 110 | \--network-max-strict-outer-iterations | An integer value. Maximum outer iterations in network solver before relaxing tolerance. | 10 |
| 111 | \--network-max-sub-iterations | An integer value. Maximum number of sub-iterations to update network pressures (within a single well/group control update). | 20 |
| 112 | \--newton-max-error | A real positive value that sets the maximum error tolerated by the Newton method to which does not cause an abort. | 1e+100 |
| 113 | \--newton-max-iterations | A positive integer that defines the maximum number of Newton iterations per time step used by the simulator. | 20 |
| 114 | \--newton-max-relax | A real positive value that sets the maximum relaxation factor of a Newton iteration used by the simulator. | 0.5 |
| 115 | \--newton-min-iterations | A positive integer that sets the minimum number of Newton iterations per time step used by the simulator. | 2 |
| 116 | \--network-pressure-update-damping-factor | A real value. Damping factor in the inner network pressure update iterations. | 0.1 |
| 117 | \--newton-relaxation-type | A character string. The type of relaxation used by the Newton method. Valid options are: dampen or sor. | "dampen" |
| 118 | \--newton-target-iterations | A positive integer that sets the \'optimum\' number of Newton iterations per time step. | 10 |
| 119 | \--newton-tolerance | A real positive value that sets the maximum raw error tolerated by the Newtonmethod for considering a solution to be converged. | 0.01 |
| 120 | \--newton-verbose | A boolean value that specifies whether the Newton method should inform the user about its progress (true) or not (false). | true |
| 121 | \--newton-write-convergence | A boolean value that specifies whether to write the convergence behaviour of the Newton method to a VTK file (true) or not (false). | false |
| 122 | \--nldd-local-linear-solver | A defined character string. Configuration of NLDD local linear solver. Valid options are: ilu0 (default), dilu, cpr_quasiimpes and amg. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\'. | \"ilu0\" |
| 123 | \--nldd-local-linear-solver-max-iter | An integer value. The maximum number of iterations of the NLDD local linear solver. | 200 |
| 124 | \--nldd-local-linear-solver-reduction | A real value. The minimum reduction of the residual which the NLDD local linear solver must achieve. | 0.01 |
| 125 | \--nldd-num-initial-newton-iter | A positive integer that sets the number of initial global Newton iterations when running the NLDD nonlinear solver. | 1 |
| 126 | \--nonlinear-solver | A character string that specifies the nonlinear solver. Valid choices are newton or nldd. | \"newton\" |
| 127 | \--num-local-domains | A positive integer that sets the number of local domains for NLDD nonlinear solver.<br>Note this is an experimental feature in the current release 2023.10 that is expected to be more complete and tested by the 2024.10 release. | 0 |
| 128 | \--num-overlap | An integer value. Numbers of layers overlap in parallel partition. | 1 |
| 129 | \--num-pressure-points-equil | A positive integer that sets the number of pressure points (in each direction) in tables used for equilibration. | 2000 |
| 130 | \--num-satfunc-consistency-sample-points | An integer value. Maximum number of reported failures for each individual saturation function consistency check. | 5 |
| 131 | \--nupcol-group-rate-tolerance | A real value. Tolerance for acceptable changes in VREP/RAIN group rates. | 0.001 |
| 132 | \--opencl-ilu-parallel | A boolean value that if set to true then parallelize the ILU decomposition and application on GPU, or not (false). | true |
| 133 | \--opencl-platform-id | A positive integer that specifies the platform identification ("ID") for the openSolver. Use the "clinfo" command to determine valid IDs. | 0 |
| 134 | \--output-dir | A character string that defines the directory to which OPM Flow is to write the commercial simulator compatible output files (restart, summary files etc.).<br>The default value results in the files be written to the same directory as the input file. | "" |
| 135 | \--output-extra-convergence-info | A defined character string that specifies whether to provide additional convergence output to separate files for diagnostic purposes. The available options are:<br>1)  \"none\" results in no extra output and overrides all other options.<br>2)  \"steps\" writes out convergence information per time step, to a CASENAME.INFOSTEP file. The file is useful for identifying numerical issues.<br>3)  \"iterations\" writes out non-linear convergence metrics, i.e., the MB and CNV values, per phase, for each non-linear iteration in each time step, to a CASENAME.INFOITER file.<br>Options can be combined with commas, e.g.\"steps,iterations\" for multiple outputs.<br>The default value of \"none\" prevents the two files from being written out, for better compatibility with the commercial simulator. | "none" |
| 136 | \--output-interval | A positive integer that specifies the number of report steps between two consecutive writes of restart data. | 1 |
| 137 | \--output-mode | A defined character string that defines the output to the \*.PRT and \*.DBG files:<br>1)  "none": No output to the files.<br>2)  "log" or false: Output logging information only.<br>3)  "all" or true: Output everything.<br>For example to just output logging information use:<br>\--output-mode="log".<br>or<br>\--output-mode=false | "all" |
| 138 | \--owner-cells-first | A boolean value that determines if the cells owned by a rank should be ordered before ghost/overlapping the cells (true), or not (false). | true |
| 139 | \--parameter-file | A character string that defines the name of a parameter file which contains the simulator's set of run-time parameters, as listed in this table. | "" |
| 140 | \--parsing-strictness | Set strictness of parsing process. Available options are:<br>1)  \"normal\": stop for critical errors, and for unsupported keywords that would would change the simulator results if supported.<br>2)  \"high\": stop for all errors, that is even for unsupported keywords that do not effect the results, for example ECHO and NOECHO.<br>3)  \"low\": same as normal, except do not stop due to unsupported keywords that would change the simulator results if supported, and even if marked critical.<br>Default: \"normal\" | \"normal\" |
| 141 | \--partition-method | An integer value. Choose partitioning strategy: 0=simple, 1=Zoltan, 2=METIS, 3=Zoltan with all cells of well represented by one vertex. | 3 |
| 142 | \--pre-solve-network | A boolean value. Pre solve and iterate the network model at start-up. | true |
| 143 | \--predetermined-time-steps-file | A file with a list of predetermined time step sizes (one time step per line). | \"\" |
| 144 | \--pressure-max | A positive real value. Maximum absolute pressure. | 1e+99 |
| 145 | \--pressure-min | A real value. Minimum absolute pressure. | -1e+99 |
| 146 | \--pressure-scale | A positive real value. Scaling of pressure primary variable. | 1 |
| 147 | \--pri-var-oscilation-threshold | A real positive value that defines the threshold value for the primary variable switching conditions after its meaning has switched to hinder oscillations. | 1e-05 |
| 148 | \--print-parameters | A positive integer value that request that the run time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 149 | \--project-saturations | A boolean value that determines if all the fluid saturations should be scaled to ensure the values are in the interval (0, 1), including runs that use solvents (true), or not (false). | false |
| 150 | \--regularization-factor-wells | A real positive value that defines the "regularization factor" for wells. | 100 |
| 151 | \--relaxed-linear-solver-reduction | A real positive value that defines the minimum reduction of the residual which the linear solver need to achieve for the solution to be accepted. | 0.01 |
| 152 | \--relaxed-max-pv-fraction | A real positive value that defines The fraction of the pore volume of the reservoir where the volumetric error (CNV) might be violated during strict Newton iterations. | 0.03 |
| 153 | \--relaxed-pressure-tol-msw | A real positive value that sets the relaxation tolerance for the multi-segment well pressure solution in Pascals. | 10000 |
| 154 | \--relaxed-well-flow-tol | A real positive value that sets the relaxation tolerance for the well flow residual in reservoir cubic metres (rm3). | 0.001 |
| 155 | \--restart-time | A real positive value that sets the simulation time at which a restart should be attempted \[s\]. | -1e+35 |
| 156 | \--restart-writing-interval | A positive integer value that sets the frequency at which time steps are serialized to disk. | 16777215 |
| 157 | \--save-file | A character string that specifies the FileName for .OPMRST file used for saving serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 158 | \--save-step | A character string that determines if the simulator should save the serialized state of the OPM Flow simulator at one or more report steps to a special \*.OPMRST file. This is in addition to the normal restart files written, and consumes significantly more space than the normal restart files, but restarting OPM Flow from this file using the \--load-step option deviates less from the original run, compared to restarting using the normal restart features. The files produced are not compatible with other simulators, and also will not be compatible between different releases of OPM Flow<br>The parameter should be set to one of the following:<br>1)  \"all\" to save all report steps,<br>2)  \":x\" to save every x\'th step, or<br>3)  \"x\" to save a specif time step.<br>The default value of \"\" does not write anything to the OPM Flow specific restart file. | \"\" |
| 159 | \--scale-linear-system | A boolean value that switches on (true) or off (false) the scaling of linear system of equations according to the equation scale and primary variable types. | false |
| 160 | \--sched-restart | A boolean value that determines for a restart run if the case should initialize wells and groups from the historical SCHEDULE section (true), or from the well and group data on the restart file (false).<br>Note that the commercial simulator always uses data from the restart file (false). | false |
| 161 | \--serial-partitioning | A boolean value that determines if partitioning for parallel runs on a single process (true), or not (false). | false |
| 162 | \--shut-unsolvable-wells | A boolean value that determines if the simulator should shut unsolvable wells (true), or not (false). | true |
| 163 | \--slave | A boolean value. Specify if the simulation is a slave simulation in a master-slave simulation.<br>Note that reservoir coupling is not currently supported. This is a developer option that should not be used. | false |
| 164 | \--solve-welleq-initially | A boolean value that determines if the simulator should fully solve the well equations before each iteration of the reservoir model (true), or not (false).<br>Note that the well equations are always added to the full system and solved until convergence. | true |
| 165 | \--solver-continue-on-convergence-failure | A boolean value that stipulates if the simulator should continue (true) instead of stopping (false) when the minimum solver time step is reached. | false |
| 166 | \--solver-growth-factor | A real positive value that specifies the growth factor a time step can be increased by when recovering from one or more time step chops, subject to the maximum allowable time step size set by the \--solver-max-time-step-in-days parameter.<br>For example, if the current time step has converged at 5 days after a time step chop, and \--solver-growth-factor is set to the default value of 2.0, then the next time step will be 2.0 \* 5 days, that is at 10 days. | 2.0 |
| 167 | \--solver-max-growth | A real positive value that specifies the maximum growth factor a time step can be increased by after a report time step, subject to the maximum allowable time step size set by the \--solver-max-time-step-in-days parameter.<br>Thus, if the current time step has converged at 5 days after at a report step, and \--solver-max-growth is set to the default value of 3.0, then the next time step will be 3.0 \* 5 days, that is at 15 days. | 3.0 |
| 168 | \--solver-max-restarts | A positive integer that defines the number of allowed consecutive restarts (or time step chops) before the simulation is terminated. | 10 |
| 169 | \--solver-max-time-step-in-days | A real positive double precision value that specifies the maximum allowed time step size in days. | 365 |
| 170 | \--solver-min-time-step | A real positive double precision value that specifies the minimum size of a time step in days for field and metric units, and hours for laboratory units<br>If a time step cannot converge without getting cut below this time step size the simulator will stop. | 1e-12 |
| 171 | \--solver-restart-factor | A real positive double precision value that sets the time step chop factor of the time step after a convergence failure.<br>For example, if the current non-convergent time step is 30 days and \--solver-restart-factor is set to the default value, then the time step will be repeated using 0.33 \* 30 days as the time step, that is 9.9 days. | 0.33 |
| 172 | \--solver-verbosity | A positive integer that specifies the \"chattiness\" of the non-linear solver. | 1 |
| 173 | \--strict-inner-iter-wells | A positive integer that specifies the number of inner well iterations with strict tolerance. | 40 |
| 174 | \--strict-outer-iter-wells | A positive integer that specifies the number of Newton iterations for which wells are checked with strict tolerance. | 6 |
| 175 | \--temperature-max | A real positive value that sets the maximum absolute temperature. | 1e+09 |
| 176 | \--temperature-min | A real positive value that sets the minimum absolute temperature. | 0 |
| 177 | \--threads-per-process | A positive integer value that stipulates the maximum number of threads to be instantiated per process (\'-1\' means \'automatic\'). | 2 |
| 178 | \--time-step-after-event-in-days | A real double precision value that sets the maximum allowed time step after an event; for example, when a well is open or closed etc.<br>The default value of -1 means that events to do effect the time stepping. | -1 |
| 179 | \--time-step-control | A defined character string that defines the time stepping control algorithm and is set to one of the following:<br>1)  pid: PID controller based adaptive time step control as suggested by Turek and Kuzmin[^5].<br>2)  pid+iteration: Use PID and linear iteration numbers to guide the time step.<br>3)  pid+newtoniteration: Use PID and non-linear iterations numbers to guide the time step.<br>4)  Hardcoded: Use time steps supplied by user via the time-step-control-filename parameter. | "pid+newtoniteration" |
| 180 | \--time-step-control-decay-damping-factor | A real positive value that specifies the decay rate a time step can be decreased by after the number* target iterations *has been* exceeded* | 1.0 |
| 181 | \--time-step-control-decay-rate | A real positive value that specifies the decay rate a time step size can be decreased by after the number of target iterations has been exceeded | 0.75 |
| 182 | \--time-step-control-file-name | A character string enclosed in quotes that specifies a filename where time steps are specified. The default is the character string timesteps.<br>For instance time steps can be generated by the ecl_summary application in libecl as per the following UNIX command line:<br>path_to_libecl_applications/ecl_summary DECK TIME \> filename<br>Where:<br>DECK is the name of the data deck you want to get the time steps from,<br>TIME tells the application to return the timing for the run, and<br>\"filename\" is the name of the file the times are piped to. | "timesteps" |
| 183 | \--time-step-control-growth-damping-factor | A real positive value that specifies the growth rate of the time step increase when the number of target iterations are undercut. | 3.2 |
| 184 | \--time-step-control-growth-rate | A real positive value that specifies the growth rate of the time step size when the number of target iterations are undercut. | 1.25 |
| 185 | \--time-step-control-safety-factor | A real value to be multiplied with the time step control tolerance to ensure that the target relative change is lower than the tolerance. | 0.8 |
| 186 | \--time-step-control-target-iterations | A positive integer that defines the number of linear iterations which the time step control scheme should aim for (if applicable). | 30 |
| 187 | \--time-step-control-target-newton-iterations | A positive integer that specifies the number of Newton iterations which the time step control scheme should aim for (if applicable). | 8 |
| 188 | \--time-step-control-tolerance | A real double precision value that sets the tolerance for PID (only used with the pid and pid+ options defined by the \--time-step-control option). | 0.1 |
| 189 | \--time-step-verbosity | A positive integer that specifies the \"chattiness\" during the time integration. | 1 |
| 190 | \--tolerance-cnv | A real positive double precision value that specifies the maximum non-linear tolerance error. This is the local convergence tolerance (maximum of local saturation errors). | 0.01 |
| 191 | \--tolerance-cnv-energy | A real value. Local energy convergence tolerance (maximum of local energy errors). | 0.01 |
| 192 | \--tolerance-cnv-energy-relaxed | A real value. Relaxed local energy convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 193 | \--tolerance-cnv-relaxed | A real positive value that defines the relaxed local convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 194 | \--tolerance-energy-balance | A real value. Tolerated energy balance error relative to (scaled) total energy present. | 1e-07 |
| 195 | \--tolerance-energy-balance-relaxed | A real value. Relaxed tolerated energy balance error that applies for iterations after the iterations with the strict tolerance. | 1e-06 |
| 196 | \--tolerance-mb | A real positive double precision value that sets the maximum mass balance error, that is the tolerated mass balance error relative to total mass present. | 1e-07 |
| 197 | \--tolerance-mb-relaxed | A positive real value. Relaxed tolerated mass balance error that applies for iterations after the iterations with the strict tolerance. | 1e-06 |
| 198 | \--tolerance-pressure-ms-wells | A real positive double precision value that specifies the tolerance for the pressure equations for multi-segment wells. | 1000 |
| 199 | \--tolerance-well-control | A real positive double precision value that sets the maximum tolerance for the well control equations. | 1e-07 |
| 200 | \--tolerance-wells | A real positive double precision value that defines the maximum non-linear error for the well equations. | 1e-04 |
| 201 | \--update-equations-scaling | A boolean value that switches on (true) or off (false) the updating of the scaling factors for mass balance equations during the simulation. | false\ |
| 202 | \--use-average-density-ms-wells | A boolean value that specifies whether to approximate segment densitities by averaging over the segment and its outlet (true) or not (false). | false |
| 203 | \--use-gmres | A boolean value that when set to true OPM Flow will use Generalized Minimal Residual ("GMRES")[^6] and [^7] solver instead of Biconjugate Gradient Stabilized ("BiCGSTAB")[^8] and [^9] as the linear solver within the Newton iterations. | false |
| 204 | \--use-implicit-ipr | A boolean value. Compute implicit IPR for stability checks and stable solution search. | true |
| 205 | \--use-multisegment-well | A boolean value that when set to true the simulator will use the well model for multi-segment wells instead of the one for single-segment wells. | true |
| 206 | \--use-update-stabilization | A boolean value that switches on (true) or off (false) the stabilized Newton option, that attempts to detect and correct oscillations or stagnation during the Newton iterations.<br>This option may improve convergence for some cases. | true |
| 207 | \--water-only-threshold | A real positive value that defines the saturation threshold, for which cells with water saturations above or equal to this threshold are considered one-phase water only. | 1.0 |
| 208 | \--zoltan-imbalance-tol | Replaced by \--imbalance-tol. | 1.1 |
| 208 | \--zoltan-params | A character string that specifies the configuration of the Zoltan partitioner. Valid options are: graph, hypergraph or scotch. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See https://sandialabs.github.io/Zoltan/ug_html/ug.html for available Zoltan options. | \"graph\" |
| 209 | \--zoltan-phg-edge-size-threshold | A real value. Low-level threshold fraction in the range \[0,1\] controlling which hypergraph edge to omit. Used if \--zoltan-params=\"graph\" or if \--zoltan-params=\"hypergraph\". | 0.35 |
| Notes:<br>1)  Cells colored green in the No. column indicate new command line parameters for this release. Similarly for the Default column, cells colored green indicate the default value has changed from the previous release.<br>2)  Items shaded in gray are considered to be developer options that should be used with caution as the values associated with these command line parameters are subject to change. Cells colored orange in the No. column indicate new developer options for this release.<br>3)  Cells colored red in the No. column indicate command line parameters that have either been decrepated or removed from this release.<br>4)  VTK Graphics Command Line Parameters[^10] set of commands are no longer listed via the basic help command line command:<br>flow \--help<br>instead use:<br>flow \--help-all<br>to get a list of supported command line Parameters.<br>5)  The \--enable-vtk-output option above, if set to "true" will write out the data as stipulated by the compile options. One may need to compile the source code to obtain the desired output.<br>6)  As per all UNIX and LINUX based systems the input is case sensitive.<br>7)  If a parameter file is used to set one of the above parameters, the leading "\--" should not be incorporated in the parameter file. |  |  |  |

*<a id="REF_TABLE_OPM_FLOW_2025_04_APPENDIX_E"></a>Table A.1: OPM Flow 2025-04 Command Line Options*
A.  1.  ## Running OPM Flow 2024-10

The command line syntax for running OPM Flow is:

flow \[OPTIONS\] CASENAME

and typing the following command from your terminal:

flow CASENAME

will start the simulator and run the case specified by CASENAME.DATA.

OPM Flow accepts command line options to control various aspects of the simulator's run time behavior, as described in the table below. To give a command line option use "key=value" syntax, with no spaces around the equals sign. It is also possible to put multiple options together in a parameter file. To do so, put one option on each line of the file with ".param" as the extension and pass that filename as a command line parameter to OPM Flow using:

flow \--parameter-file=CASENAME.param

to instruct OPM Flow to read the parameter file.

| 1 | -h or \--help | A character string that causes OPM Flow to print a help message that gives a brief description of the available command line parameters.<br>This now only prints the active user facing command line options. | N/A |
| --- | --- | --- | --- |
| 2 | \--help-all | Prints all the command line options included in the release, including obsolete, hidden and deprecated options. | N/A |
| 3 | \--accelerator-mode | A defined character string that selects the linear solver, usage: \'\--accelerator-mode=\[none\|cusparse\|opencl\|amgcl\|rocalution\|rocsparse\]\'. | "none" |
| 4 | \--action-parsing-strictness | A defined character string. Set strictness of parsing process for ActionX and PyAction. Available options are normal (do not apply keywords that have not been tested for ActionX or PyAction) and low (try to apply all keywords, beware: the simulation outcome might be incorrect). | \"normal\" |
| 5 | \--allow-distributed-wells | Allow the perforations of a well to be distributed to interior of multiple processes. | false |
| 6 | \--alternative-well-rate-init | Use alternative well rate initialization procedure. | true |
| 7 | \--bda-device-id | Choose device ID for cusparseSolver or openclSolver, use \'nvidia-smi\' or \'clinfo\' commands to determine valid IDs. | 0 |
| 8 | \--check-group-constraints-inner-well-iterations | A boolean value. Allow checking of group constraints during inner well iterations. | true |
| 9 | \--continue-on-convergence-error | Continue with a non-converged solution instead of giving up if we encounter a time step size smaller than the minimum time step size. | false |
| 10 | \--convergence-monitoring | A boolean value. Enable convergence monitoring. | false |
| 11 | \--convergence-monitoring-cut-off | An integer value. Cut off limit for convergence monitoring. | 6 |
| 12 | \--convergence-monitoring-decay-factor | A real value. Decay factor for convergence monitoring. | 0.75 |
| 13 | \--cpr-reuse-interval | A positive integer that sets the reuse preconditioner interval. Used when<br>\--cpr-reuse-setup<br>is set to 4, then the preconditioner will be fully recreated instead of reused every N linear solve, where N is this parameter. | 30 |
| 14 | \--cpr-reuse-setup | A positive integer that defines if the CPR solver should re-use the AMG setup. Valid options are:<br>0.  Recreate the preconditioner for every linear solve.<br>1.  Recreate once every time step.<br>2.  Recreate if last linear solve took more than 10 iterations.<br>3.  Never recreate.<br>4.  Recreate every N linear solves, where N is the parameter *\--cpr-reuse-interval*.<br>Changed the default value from three to four. | 4 |
| 15 | \--dbph-max-rel | A real positive value that sets the maximum relative change of the bottom-hole pressure in a single iteration. | 1.0 |
| 16 | \--debug-emit-cell-partition | A boolean value that determines whether (true) or not (false) to emit cell partitions as a debugging aid. | false |
| 17 | \--dp-max-rel | A real positive double precision value that sets the maximum allowed relative change of pressure per iteration. | 0.3 |
| 18 | \--ds-max | A real positive double precision value that sets the maximum allowed change in saturation per iteration. | 0.2 |
| 19 | \--dwell-fraction-max | A real positive value that sets the maximum allowed change in well's volume fraction per iteration. | 0.2 |
| 20 | \--ecl-deck-file-name | A character string that defines the name of the OPM Flow input file which contains the simulator's ECLIPSE formatted input deck to be simulated.<br>Note that there must be no spaces in the filename. If there are spaces, which can typically occur on Windows based systems, then the filename should be enclosed in quotes; thus instead of FILE NAME use "FILE NAME". | "" |
| 21 | \--ecl-output-double-precision | A boolean value that switches on (true) or off (false) double precision in restart files.<br>Useful for \'perfect\' restarts. | false |
| 22 | \--ecl-output-interval | An integer value defining the number of report steps that ought to be skipped between two writes of restart files results. | -1 |
| 23 | \--edge-weights-method | A defined positive integer value that defines the edge-weighing strategy:<br>0.  For uniform,<br>1.  for trans, or<br>2.  for log(trans). | 1 |
| 24 | \--enable-adaptive-time-stepping | A boolean value that turns on (true) or off (false) adaptive time stepping. If set to false the report time steps provided by the input deck are used. | true |
| 25 | \--enable-async-ecl-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to restart and summary files in the commercial simulator's format on a separate thread. | true |
| 26 | \--enable-async-vtk-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to the VTK output files on a separate thread. | true |
| 27 | \--enable-drift-compensation | A boolean value that enables (true) or disables (false) partial compensation of systematic mass losses via the source term of the next time step. | false |
| 28 | \--enable-dry-run | A boolean value that specifies if the simulation should actually run (true), or just check the input deck (false).<br>This option is equivalent to activating the NOSIM keyword in the RUNSPEC section of the input deck (see section [Error: Reference source not found](#anchor-1)[Error: Reference source not found](#anchor-1)).<br>The default value of "auto' will use whatever is stipulated in the input deck via the NOSIM keyword. | "auto" |
| 29 | \--enable-ecl-output | A boolean value that specifies if the binary output files (restart, summary files, etc.) should be written in the commercial simulator's format (true), or OPM Flow's format (false). | true |
| 30 | \--enable-esmry | A boolean value that switches on (true) or off (false) the output of SUMMARY vectors to the ESMRY file for fast loading of summary data. | false |
| 31 | \--enable-gravity | A boolean value that switches on (true) or off (false) the use of the gravity correction for the pressure gradients. | true |
| 32 | \--enable-grid-adaptation | A boolean value that enables (true) or disables (false) adaptive grid refinement/coarsening. Note that Eclipse grid output will be disabled if adaptive grid refinement/coarsening is enabled. | false |
| 33 | \--enable-intensive-quantity-cache | A boolean value that switches on (true) or off (false) the caching of intensive quantities. | true |
| 34 | \--enable-logging-fallout-warning | A boolean value that sets the developer option to see whether logging was on non-root processors (true). If set to true output will be appended to the \*.DBG or \*.PRT files. | false |
| 35 | \--enable-opm-rst-file | A boolean value set to true or false to write OPM specific data sets to the commercial simulators restart file to enable restart of OPM Flow runs by OPM Flow (true), or not to write the data (false). | false |
| 36 | \--enable-storage-cache | A boolean value that turns on (true) or off (false) storing previous storage terms and avoid re-calculating them. | true |
| 37 | \--enable-terminal-output | A boolean value that turns on (true) or off (false) high-level information about the simulation\'s progress to the terminal | true |
| 38 | \--enable-thermodynamic-hints | A boolean value that enables (true) or disables (false) thermodynamic hints. | false |
| 39 | \--enable-tuning | A boolean value that instructs OPM Flow to read the time stepping parameters from the [Error: Reference source not found](#anchor-2) keyword in the input deck, if set to true.<br>Note that only the first record of the TUNING keyword is processed. | false |
| 40 | \--enable-vtk-output | A boolean value that turns on (true) or off (false) a global switch for writing VTK files. | false |
| 41 | \--enable-well-operability-check | A boolean value that enables (true) checking of a well's operating status, or disables (false) the checking. | true |
| 42 | \--enable-well-operability-check-iter | A boolean value that enables (true) checking of a well's operating status during iterations, or disables (false) the checking during iterations. | false |
| 43 | \--enable-write-all-solutions | A boolean value that turns on (true) or off (false) the writing of all solutions to disk instead of only the ones for the report steps. | false |
| 44 | \--end-time | A real value. The simulation time at which the simulation is finished \[s\]. | 1e+100 |
| 45 | \--explicit-rock-compaction | A boolean value. Use pressure from end of the last time step when evaluating rock compaction (true) or not (false). | false |
| 46 | \--external-partition | A quoted character string. Name of file from which to load an externally generated partitioning of the model\'s active cells for MPI distribution purposes. If empty, the built-in partitioning method will be employed. | "" |
| 47 | \--force-disable-fluid-in-place-output | A boolean value that instructs OPM Flow not to print the Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 48 | \--force-disable-resv-fluid-in-place-output | A boolean value that instructs OPM Flow to not to print the Reservoir Volume Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 49 | \--full-time-step-initially | A boolean value that instructs OPM Flow to always attempt to finish a report step using a single time step (true) or not (false). | false |
| 50 | \--ignore-keywords | A character string that defines a list of keywords which should be ignored by OPM Flow. The keyword string should be enclosed in quotes and each keyword separated by a colon, that is \':\'. | "" |
| 51 | \--ilu-fillin-level | A positive integer value that sets the fill in level for the ILU preconditioner. | 0 |
| 52 | \--ilu-redblack | A boolean value that instructs OPM Flow to use red-black partitioning for the ILU preconditioner. | false |
| 53 | \--ilu-relaxation | A real positive double precision value that sets the relaxation factor of the linear solver\'s ILU preconditioner. | 0.9 |
| 54 | \--ilu-reorder-spheres | A boolean value that specifies OPM Flow to reorder the entries of the matrix in the red-black ILU preconditioner in spheres starting at an edge (true) or not (false).<br>If false the original ordering is preserved in each color. Otherwise try to ensure D4 ordering (in a 2D structured grid, the diagonal elements are consecutive). | false |
| 55 | \--imbalance-tol | A real value. Tolerable imbalance of the load balancing. | 1.1 |
| 56 | \--initial-time-step-in-days | A real double precision value that sets the size of initial time step in days. | 1.0 |
| 57 | \--initial-time-step-size | A real double precision value that sets the size of initial time step in seconds. | 86400 |
| 58 | \--inj-mult-damp-mult | A real value. Injection multiplier dampening factor (dampening multiplied by this each time oscillation is detected). | 0.9 |
| 59 | \--inj-mult-min-damp-factor | A real value. Minimum injection multiplier dampening factor (maximum dampening level). | 0.05 |
| 60 | \--inj-mult-osc-threshold | A real value. Injection multiplier oscillation threshold (used for multiplier dampening). | 0.1 |
| 61 | \--input-skip-mode | A defined character string. Set compatibility mode for the SKIP100/SKIP300 keywords. Options are: 100 (skip SKIP100..ENDSKIP, keep SKIP300..ENDSKIP), 300 (skip SKIP300..ENDSKIP, keep SKIP100..ENDSKIP) or all (skip both SKIP100..ENDSKIP and SKIP300..ENDSKIP). | \"100\" |
| 62 | \--linear-solver | A defined quoted character string that sets the configuration of the linear solver, valid values are:<br>1)  cprw[^11] [^12] [^13] (default),<br>2)  ilu0,<br>3)  dilu,<br>4)  cpr (an alias for cprw),<br>5)  cpr_quasiimpes,<br>6)  cpr_trueimpes,<br>7)  cpr_trueimpesanalytic,<br>8)  amg[^14],<br>9)  hybrid (experimental), or<br>10) a file name that has the extension ".json", that contains the linear solver configuration parameters.<br>Option (1) extends the existing Constrained Pressure Residual ("CPR") preconditioner to include wells. This option can also be invoked via the CPR keyword in the RUNSPEC section; however, the command line parameter takes precedence.<br>For option (10) one enters a character string enclosed in quotes that defines the filename of a JSON configuration file for the flexible linear solver system. In this case the file extension should be '.json'.<br>Note that the \*.PRT file contains the "Property tree for the linear solver" listing, which is the JSON specification of the current case, and can be used to configure a user specific linear solver JSON file. | \"cprw\" |
| 63 | \--linear-solver-ignore-convergence-failure | A boolean value that if set to true convergences failures in the linear solver are ignored.<br>This option should be used with care, as the results might be unreliable. | false |
| 64 | \--linear-solver-max-iter | A positive integer value that defines the maximum number of linear iterations. | 200 |
| 65 | \--linear-solver-print-json-definition | Write the JSON definition of the linear solver setup to the DBG file. | true |
| 66 | \--linear-solver-reduction | A real positive double precision value that sets the minimum reduction of the residual for the linear solver. The linear solver convergences when the residual is reduced sufficiently.<br>The simulator now overrides the default reduction to be 0.005 instead of 0.01, if the linear solver has been set to one of the cpr options, in a similar manner as how the default maximum number of linear iterations for the cpr and cprw options are changed to 20 instead of 200, unless specified by the command line option by the user. | 0.01 |
| 67 | \--linear-solver-restart | A positive integer value that sets the number of iterations after which GMRES is restarted. | 40 |
| 68 | \--linear-solver-verbosity | A positive integer value that defines the output from linear solver:<br>0.  No extra output,<br>1.  output per solution iteration, or<br>2.  output per iteration. | 0 |
| 69 | \--load-file | A character string enclosed in quotes that defines the FileName for the .OPMRST file used to load the serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 70 | \--load-step | An integer value that determines if the simulator should load the serialized state from OPM Flow\'s version of the restart file, and should be set to either a specific report step, or 0 to load the last stored report step.<br>The default value of -1 does not load the data from the OPM Flow specific restart file.<br>OPM Flow\'s version of the restart file, is written using the *\--save-step=N* option. | -1 |
| 71 | \--local-domains-ordering-measure | A character string enclosed in quotes that defines the subdomain ordering measure. Allowed values are \'maxpressure\', 'averagepressure' and \'residual\'. | \"maxpressure\" |
| 72 | \--local-domains-partitioning-imbalance | A real positive double precision value that sets the subdomain partitioning imbalance tolerance. 1.03 is 3 percent imbalance. | 1.03 |
| 73 | \--local-domains-partitioning-method | A character string enclosed in quotes that defines the subdomain partitioning method. Allowed values are \'zoltan\', \'simple\', and the name of a partition file ending with \'.partition\'. | \"zoltan\" |
| 74 | \--local-solve-approach | A character string enclosed in quotes that defines the local solve approach. Valid choices are 'jacobi' and 'gauss-seidel'. | \"gauss-seidel\" |
| 75 | \--local-tolerance-scaling-cnv | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 0.1 |
| 76 | \--local-tolerance-scaling-mb | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 1 |
| 77 | \--local-well-solve-control-switching | A boolean value that allows (true) or disallows (false) control switching during local well solutions. | true |
| 78 | \--matrix-add-well-contributions | A boolean value that if set to true explicitly specifies the influences of wells between cells in the Jacobian and preconditioner matrices. | false |
| 79 | \--max-inner-iter-ms-wells | A positive integer value that defines the maximum number of inner iterations for multi-segment wells. | 100 |
| 80 | \--max-inner-iter-wells | A positive integer value that defines the maximum number of inner iterations for standard wells. | 50 |
| 81 | \--max-local-solve-iterations | A positive integer value that defines the maximum number of iterations for local solves with NLDD nonlinear solver. | 20 |
| 82 | \--max-newton-iterations-with-inner-well-iterations | A positive integer that specifies the maximum Newton iterations with inner well iterations. | 8 |
| 83 | \--max-pressure-change-ms-wells | A real positive value that defines the maximum relative pressure change for a single iteration of the multi-segment well model. | 1e+06 |
| 84 | \--max-residual-allowed | A real positive value that sets the absolute maximum tolerance for residuals without cutting the time step size. | 1e+07 |
| 85 | \--max-single-precision-days | A real positive value that sets the maximum time step size where single precision floating point arithmetic can be used for solving the linear systems of equations. | 20.0 |
| 86 | \--max-temperature-change | A real positive value that stipulates the maximum absolute change of temperature in a single iteration. | 5 |
| 87 | \--max-time-step-divisions | A positive integer that specifies the maximum number of divisions by two of the timestep size before the simulation bails out. | 10 |
| 88 | \--max-time-step-size | A real positive value that defines the maximum size to which all time steps are limited to in seconds. | inf |
| 89 | \--max-welleq-iter | A positive integer that defines the maximum number of iterations to determine the solution to the well equations. | 30 |
| 90 | \--maximum-number-of-well-switches | A positive integer values that stipulates the maximum number of times a well can switch to the same control. | 3 |
| 91 | \--maximum-water-saturation | A real positive value that defines the maximum water saturation. | 1.0 |
| 92 | \--metis-params | A character string. Configuration of Metis partitioner. You can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/manual.pdf for available METIS options. | \"default\" |
| 93 | \--milu-variant | A defined character string that specifies which variant of the modified ILU preconditioner ought to be used. Possible variants are:<br>1)  ILU (default, plain ILU),<br>2)  MILU_1 (lump diagonal with dropped row entries),<br>3)  MILU_2 (lump diagonal with the sum of the absolute values of the dropped row entries),<br>4)  MILU_3 (if diagonal is positive add sum of dropped row entries. Otherwise subtract them),<br>5)  MILU_4 (if diagonal is positive add sum of dropped row entries. Otherwise do nothing). | "ILU" |
| 94 | \--min-strict-cnv-iter | A positive integer that sets the minimum number of Newton iterations before relaxed tolerances are used for the CNV convergence criterion. | -1 |
| 95 | \--min-strict-mb-iter | An integer value defining the number of Newton iterations before relaxed tolerances can be used for the MB convergence criterion. Default -1 means that the relaxed tolerance is used when maximum number of Newton iterations are reached. | -1 |
| 96 | \--min-time-step-based-on-newton-iterations | A real positive value that sets the minimum time step size (in days for field and metric unit and hours for lab unit) can be reduced to based on Newton iteration counts. | 0.0 |
| 97 | \--min-time-step-before-shutting-problematic-wells-in-days | A real positive value that sets the minimum time step size in days for which problematic wells are not shut. Time steps below this value will result in problematic wells being shut-in by the simulator. | 0.01 |
| 98 | \--min-time-step-size | A real positive value that sets the minimum size to which all time steps are limited to in seconds. | 0.0 |
| 99 | \--network-max-iterations | A positive integer that sets the maximum number of iterations in the network solver before giving up. | 200 |
| 100 | \--network-max-strict-iterations | A positive integer that sets the maximum iterations in network solver before relaxing tolerance. | 100 |
| 101 | \--newton-max-error | A real positive value that sets the maximum error tolerated by the Newton method to which does not cause an abort. | 1e+100 |
| 102 | \--newton-max-iterations | A positive integer that defines the maximum number of Newton iterations per time step used by the simulator. | 20 |
| 103 | \--newton-max-relax | A real positive value that sets the maximum relaxation factor of a Newton iteration used by the simulator. | 0.5 |
| 104 | \--newton-min-iterations | A positive integer that sets the minimum number of Newton iterations per time step used by the simulator. | 2 |
| 105 | \--newton-relaxation-type | A character string. The type of relaxation used by the Newton method. Valid options are: dampen or sor. | "dampen" |
| 106 | \--newton-target-iterations | A positive integer that sets the \'optimum\' number of Newton iterations per time step. | 10 |
| 107 | \--newton-tolerance | A real positive value that sets the maximum raw error tolerated by the Newtonmethod for considering a solution to be converged. | 0.01 |
| 108 | \--newton-verbose | A boolean value that specifies whether the Newton method should inform the user about its progress (true) or not (false). | true |
| 109 | \--newton-write-convergence | A boolean value that specifies whether to write the convergence behaviour of the Newton method to a VTK file (true) or not (false). | false |
| 110 | \--nldd-local-linear-solver | A defined character string. Configuration of NLDD local linear solver. Valid options are: ilu0 (default), dilu, cpr_quasiimpes and amg. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\'. | \"ilu0\" |
| 111 | \--nldd-local-linear-solver-max-iter | An integer value. The maximum number of iterations of the NLDD local linear solver. | 200 |
| 112 | \--nldd-local-linear-solver-reduction | A real value. The minimum reduction of the residual which the NLDD local linear solver must achieve. | 0.01 |
| 113 | \--nldd-num-initial-newton-iter | A positive integer that sets the number of initial global Newton iterations when running the NLDD nonlinear solver. | 1 |
| 114 | \--nonlinear-solver | A character string that specifies the nonlinear solver. Valid choices are newton or nldd. | \"newton\" |
| 115 | \--num-local-domains | A positive integer that sets the number of local domains for NLDD nonlinear solver.<br>Note this is an experimental feature in the current release 2023.10 that is expected to be more complete and tested by the 2024.10 release. | 0 |
| 116 | \--num-pressure-points-equil | A positive integer that sets the number of pressure points (in each direction) in tables used for equilibration. | 2000 |
| 117 | \--opencl-ilu-parallel | A boolean value that if set to true then parallelize the ILU decomposition and application on GPU, or not (false). | true |
| 118 | \--opencl-platform-id | A positive integer that specifies the platform identification ("ID") for the openSolver. Use the "clinfo" command to determine valid IDs. | 0 |
| 119 | \--output-dir | A character string that defines the directory to which OPM Flow is to write the commercial simulator compatible output files (restart, summary files etc.).<br>The default value results in the files be written to the same directory as the input file. | "" |
| 120 | \--output-extra-convergence-info | A defined character string that specifies whether to provide additional convergence output to separate files for diagnostic purposes. The available options are:<br>1)  \"none\" results in no extra output and overrides all other options.<br>2)  \"steps\" writes out convergence information per time step, to a CASENAME.INFOSTEP file. The file is useful for identifying numerical issues.<br>3)  \"iterations\" writes out non-linear convergence metrics, i.e., the MB and CNV values, per phase, for each non-linear iteration in each time step, to a CASENAME.INFOITER file.<br>Options can be combined with commas, e.g.\"steps,iterations\" for multiple outputs.<br>The default value of \"none\" prevents the two files from being written out, for better compatibility with the commercial simulator. | "none" |
| 121 | \--output-interval | A positive integer that specifies the number of report steps between two consecutive writes of restart data. | 1 |
| 122 | \--output-mode | A defined character string that defines the output to the \*.PRT and \*.DBG files:<br>1)  "none": No output to the files.<br>2)  "log" or false: Output logging information only.<br>3)  "all" or true: Output everything.<br>For example to just output logging information use:<br>\--output-mode="log".<br>or<br>\--output-mode=false | "all" |
| 123 | \--owner-cells-first | A boolean value that determines if the cells owned by a rank should be ordered before ghost/overlapping the cells (true), or not (false). | true |
| 124 | \--parameter-file | A character string that defines the name of a parameter file which contains the simulator's set of run-time parameters, as listed in this table. | "" |
| 125 | \--parsing-strictness | Set strictness of parsing process. Available options are:<br>1)  \"normal\": stop for critical errors, and for unsupported keywords that would would change the simulator results if supported.<br>2)  \"high\": stop for all errors, that is even for unsupported keywords that do not effect the results, for example ECHO and NOECHO.<br>3)  \"low\": same as normal, except do not stop due to unsupported keywords that would change the simulator results if supported, and even if marked critical.<br>Default: \"normal\" | \"normal\" |
| 126 | \--partition-method | An integer value. Choose partitioning strategy: 0=simple, 1=Zoltan, 2=METIS. | 1 |
| 127 | \--predetermined-time-steps-file | A file with a list of predetermined time step sizes (one time step per line). | \"\" |
| 128 | \--pressure-max | A positive real value. Maximum absolute pressure. | 1e+99 |
| 129 | \--pressure-min | A real value. Minimum absolute pressure. | -1e+99 |
| 130 | \--pressure-scale | A positive real value. Scaling of pressure primary variable. | 1 |
| 131 | \--pri-var-oscilation-threshold | A real positive value that defines the threshold value for the primary variable switching conditions after its meaning has switched to hinder oscillations. | 1e-05 |
| 132 | \--print-parameters | A positive integer value that request that the run time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 133 | \--print-properties | A positive integer value that request that the compile time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 134 | \--project-saturations | A boolean value that determines if all the fluid saturations should be scaled to ensure the values are in the interval (0, 1), including runs that use solvents (true), or not (false). | false |
| 135 | \--regularization-factor-wells | A real positive value that defines the "regularization factor" for wells. | 100 |
| 136 | \--relaxed-linear-solver-reduction | A real positive value that defines the minimum reduction of the residual which the linear solver need to achieve for the solution to be accepted. | 0.01 |
| 137 | \--relaxed-max-pv-fraction | A real positive value that defines The fraction of the pore volume of the reservoir where the volumetric error (CNV) might be violated during strict Newton iterations. | 0.03 |
| 138 | \--relaxed-pressure-tol-msw | A real positive value that sets the relaxation tolerance for the multi-segment well *pressure* solution in Pascals. | 10000 |
| 139 | \--relaxed-well-flow-tol | A real positive value that sets the relaxation tolerance for the well flow residual in reservoir cubic metres (rm3). | 0.001 |
| 140 | \--restart-time | A real positive value that sets the simulation time at which a restart should be attempted \[s\]. | -1e+35 |
| 141 | \--restart-writing-interval | A positive integer value that sets the frequency at which time steps are serialized to disk. | 16777215 |
| 142 | \--save-file | A character string that specifies the FileName for .OPMRST file used for saving serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 143 | \--save-step | A character string that determines if the simulator should save the serialized state of the OPM Flow simulator at one or more report steps to a special \*.OPMRST file. This is in addition to the normal restart files written, and consumes significantly more space than the normal restart files, but restarting OPM Flow from this file using the *\--load-step* option deviates less from the original run, compared to restarting using the normal restart features. The files produced are not compatible with other simulators, and also will not be compatible between different releases of OPM Flow<br>The parameter should be set to one of the following:<br>1)  \"all\" to save all report steps,<br>2)  \":x\" to save every x\'th step, or<br>3)  \"x\" to save a specif time step.<br>The default value of \"\" does not write anything to the OPM Flow specific restart file. | \"\" |
| 144 | \--scale-linear-system | A boolean value that switches on (true) or off (false) the scaling of linear system of equations according to the equation scale and primary variable types. | false |
| 145 | \--sched-restart | A boolean value that determines for a restart run if the case should initialize wells and groups from the historical SCHEDULE section (true), or from the well and group data on the restart file (false).<br>Note that the commercial simulator always uses data from the restart file (false). | false |
| 146 | \--serial-partitioning | A boolean value that determines if partitioning for parallel runs on a single process (true), or not (false). | false |
| 147 | \--shut-unsolvable-wells | A boolean value that determines if the simulator should shut unsolvable wells (true), or not (false). | true |
| 148 | \--solve-welleq-initially | A boolean value that determines if the simulator should fully solve the well equations before each iteration of the reservoir model (true), or not (false).<br>Note that the well equations are always added to the full system and solved until convergence. | true |
| 149 | \--solver-continue-on-convergence-failure | A boolean value that stipulates if the simulator should continue (true) instead of stopping (false) when the minimum solver time step is reached. | false |
| 150 | \--solver-growth-factor | A real positive value that specifies the growth factor a time step can be increased by when recovering from one or more time step chops, subject to the maximum allowable time step size set by the *\--solver-max-time-step-in-days* parameter.<br>For example, if the current time step has converged at 5 days after a time step chop, and \--solver-growth-factor is set to the default value of 2.0, then the next time step will be 2.0 \* 5 days, that is at 10 days. | 2.0 |
| 151 | \--solver-max-growth | A real positive value that specifies the maximum growth factor a time step can be increased by after a report time step, subject to the maximum allowable time step size set by the \--solver-max-time-step-in-days parameter.<br>Thus, if the current time step has converged at 5 days after at a report step, and \--solver-*max-*growth is set to the default value of 3.0, then the next time step will be 3.0 \* 5 days, that is at 15 days. | 3.0 |
| 152 | \--solver-max-restarts | A positive integer that defines the number of allowed consecutive restarts (or time step chops) before the simulation is terminated. | 10 |
| 153 | \--solver-max-time-step-in-days | A real positive double precision value that specifies the maximum allowed time step size in days. | 365 |
| 154 | \--solver-min-time-step | A real positive double precision value that specifies the minimum size of a time step in days for field and metric units, and hours for laboratory units<br>If a time step cannot converge without getting cut below this time step size the simulator will stop. | 1e-12 |
| 155 | \--solver-restart-factor | A real positive double precision value that sets the time step chop factor of the time step after a convergence failure.<br>For example, if the current non-convergent time step is 30 days and *\--solver-restart-factor * is set to the default value, then the time step will be repeated using 0.33 \* 30 days as the time step, that is 9.9 days. | 0.33 |
| 156 | \--solver-verbosity | A positive integer that specifies the \"chattiness\" of the non-linear solver. | 1 |
| 157 | \--strict-inner-iter-wells | A positive integer that specifies the number of inner well iterations with strict tolerance. | 40 |
| 158 | \--strict-outer-iter-wells | A positive integer that specifies the number of Newton iterations for which wells are checked with strict tolerance. | 6 |
| 159 | \--temperature-max | A real positive value that sets the maximum absolute temperature. | 1e+09 |
| 160 | \--temperature-min | A real positive value that sets the minimum absolute temperature. | 0 |
| 161 | \--threads-per-process | A positive integer value that stipulates the maximum number of threads to be instantiated per process (\'-1\' means \'automatic\'). | -1 |
| 162 | \--time-step-after-event-in-days | A real double precision value that sets the maximum allowed time step after an event; for example, when a well is open or closed etc.<br>The default value of -1 means that events to do effect the time stepping. | -1 |
| 163 | \--time-step-control | A defined character string that defines the time stepping control algorithm and is set to one of the following:<br>1)  pid: PID controller based adaptive time step control as suggested by Turek and Kuzmin[^15].<br>2)  pid+iteration: Use PID and linear iteration numbers to guide the time step.<br>3)  pid+newtoniteration: Use PID and non-linear iterations numbers to guide the time step.<br>4)  Hardcoded: Use time steps supplied by user via the time-step-control-filename parameter. | "pid+newtoniteration" |
| 164 | \--time-step-control-decay-damping-factor | A real positive value that specifies the decay rate a time step can be decreased by after the number target iterations has been exceeded | 1.0 |
| 165 | \--time-step-control-decay-rate | A real positive value that specifies the decay rate a time step size can be decreased by after the number of target iterations has been exceeded | 0.75 |
| 166 | \--time-step-control-file-name | A character string enclosed in quotes that specifies a filename where time steps are specified. The default is the character string timesteps.<br>For instance time steps can be generated by the ecl_summary application in libecl as per the following UNIX command line:<br>path_to_libecl_applications/ecl_summary DECK TIME \> filename<br>Where:<br>DECK is the name of the data deck you want to get the time steps from,<br>TIME tells the application to return the timing for the run, and<br>\"filename\" is the name of the file the times are piped to. | "timesteps" |
| 167 | \--time-step-control-growth-damping-factor | A real positive value that specifies the growth rate of the *time step *increase when the number of target iterations are undercut. | 3.2 |
| 168 | \--time-step-control-growth-rate | A real positive value that specifies the growth rate of the *time step size* when the number of target iterations are undercut. | 1.25 |
| 169 | \--time-step-control-target-iterations | A positive integer that defines the number of linear iterations which the time step control scheme should aim for (if applicable). | 30 |
| 170 | \--time-step-control-target-newton-iterations | A positive integer that specifies the number of Newton iterations which the time step control scheme should aim for (if applicable). | 8 |
| 171 | \--time-step-control-tolerance | A real double precision value that sets the tolerance for PID (only used with the pid and pid+ options defined by the \--time-step-control option). | 0.1 |
| 172 | \--time-step-verbosity | A positive integer that specifies the \"chattiness\" during the time integration. | 1 |
| 173 | \--tolerance-cnv | A real positive double precision value that specifies the maximum non-linear tolerance error. This is the local convergence tolerance (maximum of local saturation errors). | 0.01 |
| 174 | \--tolerance-cnv-energy | A real value. Local energy convergence tolerance (maximum of local energy errors). | 0.01 |
| 175 | \--tolerance-cnv-energy-relaxed | A real value. Relaxed local energy convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 176 | \--tolerance-cnv-relaxed | A real positive value that defines the relaxed local convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 177 | \--tolerance-energy-balance | A real value. Tolerated energy balance error relative to (scaled) total energy present. | 1e-07 |
| 178 | \--tolerance-energy-balance-relaxed | A real value. Relaxed tolerated energy balance error that applies for iterations after the iterations with the strict tolerance. | 1e-06 |
| 179 | \--tolerance-mb | A real positive double precision value that sets the maximum mass balance error, that is the tolerated mass balance error relative to total mass present. | 1e-07 |
| 180 | \--tolerance-mb-relaxed | A positive real value. Relaxed tolerated mass balance error that applies for iterations after the iterations with the strict tolerance. | 1e-06 |
| 180 | \--tolerance-pressure-ms-wells | A real positive double precision value that specifies the tolerance for the pressure equations for multi-segment wells. | 1000 |
| 181 | \--tolerance-well-control | A real positive double precision value that sets the maximum tolerance for the well control equations. | 1e-07 |
| 182 | \--tolerance-wells | A real positive double precision value that defines the maximum non-linear error for the well equations. | 1e-04 |
| 183 | -update-equations-scaling | A boolean value that switches on (true) or off (false) the updating of the scaling factors for mass balance equations during the simulation. | false\ |
| 184 | \--use-average-density-ms-wells | A boolean value that specifies whether to approximate segment densitities by averaging over the segment and its outlet (true) or not (false). | false |
| 185 | \--use-gmres | A boolean value that when set to true OPM Flow will use Generalized Minimal Residual ("GMRES")[^16] and [^17] solver instead of Biconjugate Gradient Stabilized ("BiCGSTAB")[^18] and [^19] as the linear solver within the Newton iterations. | false |
| 186 | \--use-implicit-ipr | A boolean value. Compute implicit IPR for stability checks and stable solution search. | true |
| 187 | \--use-multisegment-well | A boolean value that when set to true the simulator will use the well model for multi-segment wells instead of the one for single-segment wells. | true |
| 188 | \--use-update-stabilization | A boolean value that switches on (true) or off (false) the stabilized Newton option, that attempts to detect and correct oscillations or stagnation during the Newton iterations.<br>This option may improve convergence for some cases. | true |
| 189 | \--water-only-threshold | A real positive value that defines the saturation threshold, for which cells with water saturations above or equal to this threshold are considered one-phase water only. | 1.0 |
| 190 | \--zoltan-imbalance-tol | A real value. Tolerable imbalance of the loadbalancing provided by Zoltan. This command line option has been deprecated; \--imbalance-tol should be used instead. | 1.1 |
| 191 | \--zoltan-params | A character string that specifies the configuration of the Zoltan partitioner. Valid options are: graph, hypergraph or scotch. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See https://sandialabs.github.io/Zoltan/ug_html/ug.html for available Zoltan options. | \"graph\" |
| Notes:<br>1)  Cells colored green in the No. column are new command line parameters for this release. Similarly for the Default column, cells colored green indicate the default value has changed from the previous release.<br>2)  Items shaded in gray are considered to be developer options that should be used with caution as the values associated with these command line parameters are subject to change.<br>3)  VTK Graphics Command Line Parameters[^20] set of commands are no longer listed via the basic help command line command:<br>flow \--help<br>instead use:<br>flow \--help-all<br>to get a list of supported command line Parameters.<br>3)  The \--enable-vtk-output option above, if set to "true" will write out the data as stipulated by the compile options. One may need to compile the source code to obtain the desired output.<br>4)  As per all UNIX and LINUX based system the input is case dependent.<br>5)  If a parameter file is used to set one of the above parameters, the leading "\--" should not be incorporated in the parameter file. |  |  |  |

*<a id="REF_TABLE_OPM_FLOW_2023_04_OPTIONS_2_2"></a>Table A.1: OPM Flow 2024-10 Command Line Options*
A.  1.  ## Running OPM Flow 2024-04

        > The command line syntax for running OPM Flow is:

flow \[OPTIONS\] CASENAME

and typing the following command from your terminal:

flow CASENAME

will start the simulator and run the case specified by CASENAME.DATA.

OPM Flow accepts command line options to control various aspects of the simulator's run time behavior, as described in the table below. To give a command line option use "key=value" syntax, with no spaces around the equals sign. It is also possible to put multiple options together in a parameter file. To do so, put one option on each line of the file with ".param" as the extension and pass that filename as a command line parameter to OPM Flow using:

flow \--parameter-file=CASENAME.param

to instruct OPM Flow to read the parameter file.

| 1 | -h or \--help | A character string that causes OPM Flow to print a help message that gives a brief description of the available command line parameters.<br>This now only prints the active user facing command line options. | N/A |
| --- | --- | --- | --- |
| 2 | \--help-all | Prints all the command line options included in the release, including obsolete, hidden and deprecated options. | N/A |
| 3 | \--accelerator-mode | A defined character string that selects the linear solver, usage: \'\--accelerator-mode=\[none\|cusparse\|opencl\|amgcl\|rocalution\|rocsparse\]\'. | "none" |
| 4 | \--allow-distributed-wells | Allow the perforations of a well to be distributed to interior of multiple processes. | false |
| 5 | \--alternative-well-rate-init | Use alternative well rate initialization procedure. | true |
| 6 | \--bda-device-id | Choose device ID for cusparseSolver or openclSolver, use \'nvidia-smi\' or \'clinfo\' commands to determine valid IDs. | 0 |
| 7 | \--continue-on-convergence-error | Continue with a non-converged solution instead of giving up if we encounter a time step size smaller than the minimum time step size. | false |
| 8 | \--cpr-reuse-interval | A positive integer that sets the reuse preconditioner interval. Used when<br>\--cpr-reuse-setup<br>is set to 4, then the preconditioner will be fully recreated instead of reused every N linear solve, where N is this parameter. | 30 |
| 9 | \--cpr-reuse-setup | A positive integer that defines if the CPR solver should re-use the AMG setup. Valid options are:<br>0.  Recreate the preconditioner for every linear solve.<br>1.  Recreate once every time step.<br>2.  Recreate if last linear solve took more than 10 iterations.<br>3.  Never recreate.<br>4.  Recreate every N linear solves, where N is the parameter *\--cpr-reuse-interval*.<br>Changed the default value from three to four. | 4 |
| 10 | \--dbph-max-rel | A real positive value that sets the maximum relative change of the bottom-hole pressure in a single iteration. | 1.0 |
| 11 | \--dp-max-rel | A real positive double precision value that sets the maximum allowed relative change of pressure per iteration. | 0.3 |
| 12 | \--ds-max | A real positive double precision value that sets the maximum allowed change in saturation per iteration. | 0.2 |
| 13 | \--dwell-fraction-max | A real positive value that sets the maximum allowed change in well's volume fraction per iteration. | 0.2 |
| 14 | \--debug-emit-cell-partition | A boolean value that determines whether (true) or not (false) to emit cell partitions as a debugging aid. | false |
| 15 | \--ecl-deck-file-name | A character string that defines the name of the OPM Flow input file which contains the simulator's ECLIPSE formatted input deck to be simulated.<br>Note that there must be no spaces in the filename. If there are spaces, which can typically occur on Windows based systems, then the filename should be enclosed in quotes; thus instead of FILE NAME use "FILE NAME". | "" |
| 16 | \--enable-drift-compensation | A boolean value that enables (true) or disables (false) partial compensation of systematic mass losses via the source term of the next time step. | true |
| 17 | \--ecl-enable-tuning | Honor some aspects of the TUNING keyword from the ECL deck. | false |
| 18 | \--ecl-newton-relaxed-tolerance | The maximum error which the volumetric residual may exhibit if it is in a \'relaxed\' region during a strict iteration. | 1e+09 |
| 19 | \--ecl-newton-relaxed-volume-fraction | The fraction of the pore volume of the reservoir where the volumetric error may be voilated during strict Newton iterations. | 0.03 |
| 20 | \--ecl-newton-strict-iterations | The number of Newton iterations where the volumetric error is considered. | 8 |
| 21 | \--ecl-newton-sum-tolerance | The maximum error tolerated by the Newton method for considering a solution to be converged. | 0.0001 |
| 22 | \--ecl-newton-sum-tolerance-exponent | The exponent used to scale the sum tolerance by the total pore volume of the reservoir. | 0.333333 |
| 23 | \--ecl-output-double-precision | A boolean value that switches on (true) or off (false) double precision in restart files.<br>Useful for \'perfect\' restarts. | false |
| 24 | \--ecl-output-interval | An integer value defining the number of report steps that ought to be skipped between two writes of restart files results. | -1 |
| 25 | \--edge-weights-method | A defined positive integer value that defines the edge-weighing strategy:<br>0.  For uniform,<br>1.  for trans, or<br>2.  for log(trans). | 1 |
| 26 | \--enable-adaptive-time-stepping | A boolean value that turns on (true) or off (false) adaptive time stepping. If set to false the report time steps provided by the input deck are used. | true |
| 27 | \--enable-async-ecl-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to restart and summary files in the commercial simulator's format on a separate thread. | true |
| 28 | \--enable-async-vtk-output | A boolean value that sets the output mode to be asynchronous (true), letting the simulator continue computing the next time step while writing results to the VTK output files on a separate thread. | true |
| 29 | \--enable-dry-run | A boolean value that specifies if the simulation should actually run (true), or just check the input deck (false).<br>This option is equivalent to activating the NOSIM keyword in the RUNSPEC section of the input deck (see section [Error: Reference source not found](#anchor-1)[Error: Reference source not found](#anchor-1)).<br>The default value of "auto' will use whatever is stipulated in the input deck via the NOSIM keyword. | "auto" |
| 30 | \--enable-ecl-output | A boolean value that specifies if the binary output files (restart, summary files, etc.) should be written in the commercial simulator's format (true), or OPM Flow's format (false). | true |
| 31 | \--enable-esmry | A boolean value that switches on (true) or off (false) the output of SUMMARY vectors to the ESMRY file for fast loading of summary data. | false |
| 32 | \--enable-gravity | A boolean value that switches on (true) or off (false) the use of the gravity correction for the pressure gradients. | true |
| 33 | \--enable-grid-adaptation | A boolean value that enables (true) or disables (false) adaptive grid refinement/coarsening. Note that Eclipse grid output will be disabled if adaptive grid refinement/coarsening is enabled. | false |
| 34 | \--enable-intensive-quantity-cache | A boolean value that switches on (true) or off (false) the caching of intensive quantities. | true |
| 35 | \--enable-logging-fallout-warning | A boolean value that sets the developer option to see whether logging was on non-root processors (true). If set to true output will be appended to the \*.DBG or \*.PRT files. | false |
| 36 | \--enable-opm-rst-file | A boolean value set to true or false to write OPM specific data sets to the commercial simulators restart file to enable restart of OPM Flow runs by OPM Flow (true), or not to write the data (false). | false |
| 37 | \--enable-storage-cache | A boolean value that turns on (true) or off (false) storing previous storage terms and avoid re-calculating them. | true |
| 38 | \--enable-terminal-output | A boolean value that turns on (true) or off (false) high-level information about the simulation\'s progress to the terminal | true |
| 39 | \--enable-thermodynamic-hints | A boolean value that enables (true) or disables (false) thermodynamic hints. | false |
| 40 | \--enable-tuning | A boolean value that instructs OPM Flow to read the time stepping parameters from the [Error: Reference source not found](#anchor-2) keyword in the input deck, if set to true.<br>Note that only the first record of the TUNING keyword is processed. | false |
| 41 | \--enable-vtk-output | A boolean value that turns on (true) or off (false) a global switch for writing VTK files. | false |
| 42 | \--enable-well-operability-check | A boolean value that enables (true) checking of a well's operating status, or disables (false) the checking. | true |
| 43 | \--enable-well-operability-check-iter | A boolean value that enables (true) checking of a well's operating status during iterations, or disables (false) the checking during iterations. | false |
| 44 | \--enable-write-all-solutions | A boolean value that turns on (true) or off (false) the writing of all solutions to disk instead of only the ones for the report steps. | false |
| 45 | \--end-time | The simulation time at which the simulation is finished \[s\]. | 1e+100 |
| 46 | \--explicit-rock-compaction | A boolean value. Use pressure from end of the last time step when evaluating rock compaction (true) or not (false). | false |
| 47 | \--external-partition | A quoted character string. Name of file from which to load an externally generated partitioning of the model\'s active cells for MPI distribution purposes. If empty, the built-in partitioning method will be employed. | "" |
| 48 | \--force-disable-fluid-in-place-output | A boolean value that instructs OPM Flow not to print the Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 49 | \--force-disable-resv-fluid-in-place-output | A boolean value that instructs OPM Flow to not to print the Reservoir Volume Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 50 | \--full-time-step-initially | A boolean value that instructs OPM Flow to always attempt to finish a report step using a single time step (true) or not (false). | false |
| 51 | \--ignore-keywords | A character string that defines a list of keywords which should be ignored by OPM Flow. The keyword string should be enclosed in quotes and each keyword separated by a colon, that is \':\'. | "" |
| 52 | \--ilu-fillin-level | A positive integer value that sets the fill in level for the ILU preconditioner. | 0 |
| 53 | \--ilu-redblack | A boolean value that instructs OPM Flow to use red-black partitioning for the ILU preconditioner. | false |
| 54 | \--ilu-relaxation | A real positive double precision value that sets the relaxation factor of the linear solver\'s ILU preconditioner. | 0.9 |
| 55 | \--ilu-reorder-spheres | A boolean value that specifies OPM Flow to reorder the entries of the matrix in the red-black ILU preconditioner in spheres starting at an edge (true) or not (false).<br>If false the original ordering is preserved in each color. Otherwise try to ensure D4 ordering (in a 2D structured grid, the diagonal elements are consecutive). | false |
| 56 | \--initial-time-step-in-days | A real double precision value that sets the size of initial time step in days. | 1.0 |
| 57 | \--initial-time-step-size | A real double precision value that sets the size of initial time step in seconds. | 86400 |
| 58 | \--linear-solver | A defined quoted character string that sets the configuration of the linear solver, valid values are:<br>1)  ilu0 (default),<br>2)  dilu,<br>3)  cprw or cpr (an alias for cprw),[^21] [^22] and [^23]<br>4)  cpr_quasiimpes,<br>5)  cpr_trueimpes,<br>6)  cpr_trueimpesanalytic,<br>7)  amg,[^24]<br>8)  hybrid (experimental), or<br>9)  a file name that has the extension ".json", that contains the linear solver configuration parameters.<br>Option (3) extends the existing Constrained Pressure Residual ("CPR") preconditioner to include wells. This option can also be invoked via the CPR keyword in the RUNSPEC section; however, the command line parameter takes precedence.<br>For option (9) one enters a character string enclosed in quotes that defines the filename of a JSON configuration file for the flexible linear solver system. In this case the file extension should be '.json'.<br>Note that the \*.PRT file contains the "Property tree for the linear solver" listing, which is the JSON specification of the current case, and can be used to configure a user specific linear solver JSON file.<br>The option \"cpr\" now is an alias for \"cprw\" instead of \"cpr_trueimpes\". | "ilu0" |
| 59 | \--linear-solver-ignore-convergence-failure | A boolean value that if set to true convergences failures in the linear solver are ignored.<br>This option should be used with care, as the results might be unreliable. | false |
| 60 | \--linear-solver-max-iter | A positive integer value that defines the maximum number of linear iterations. | 200 |
| 61 | \--linear-solver-print-json-definition | Write the JSON definition of the linear solver setup to the DBG file. | true |
| 62 | \--linear-solver-reduction | A real positive double precision value that sets the minimum reduction of the residual for the linear solver. The linear solver convergences when the residual is reduced sufficiently.<br>The simulator now overrides the default reduction to be 0.005 instead of 0.01, if the linear solver has been set to one of the cpr options, in a similar manner as how the default maximum number of linear iterations for the cpr and cprw options are changed to 20 instead of 200, unless specified by the command line option by the user. | 0.01 |
| 63 | \--linear-solver-restart | A positive integer value that sets the number of iterations after which GMRES is restarted. | 40 |
| 64 | \--linear-solver-verbosity | A positive integer value that defines the output from linear solver:<br>0.  No extra output,<br>1.  output per solution iteration, or<br>2.  output per iteration. | 0 |
| 65 | \--load-file | A character string enclosed in quotes that defines the FileName for the .OPMRST file used to load the serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 66 | \--load-step | An integer value that determines if the simulator should load the serialized state from OPM Flow\'s version of the restart file, and should be set to either a specific report step, or 0 to load the last stored report step.<br>The default value of -1 does not load the data from the OPM Flow specific restart file.<br>OPM Flow\'s version of the restart file, is written using the *\--save-step=N* option. | -1 |
| 67 | \--local-domains-ordering-measure | A character string enclosed in quotes that defines the subdomain ordering measure. Allowed values are \'maxpressure\', 'averagepressure' and \'residual\'. | \"maxpressure\" |
| 68 | \--local-domains-partitioning-imbalance | A real positive double precision value that sets the subdomain partitioning imbalance tolerance. 1.03 is 3 percent imbalance. | 1.03 |
| 69 | \--local-domains-partitioning-method | A character string enclosed in quotes that defines the subdomain partitioning method. Allowed values are \'zoltan\', \'simple\', and the name of a partition file ending with \'.partition\'. | \"zoltan\" |
| 70 | \--local-solve-approach | A character string enclosed in quotes that defines the local solve approach. Valid choices are 'jacobi' and 'gauss-seidel'. | \"gauss-seidel\" |
| 71 | \--local-tolerance-scaling-cnv | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 0.1 |
| 72 | \--local-tolerance-scaling-mb | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 1 |
| 73 | \--local-well-solve-control-switching | A boolean value that allows (true) or disallows (false) control switching during local well solutions. | false |
| 74 | \--matrix-add-well-contributions | A boolean value that if set to true explicitly specifies the influences of wells between cells in the Jacobian and preconditioner matrices. | false |
| 75 | \--max-inner-iter-ms-wells | A positive integer value that defines the maximum number of inner iterations for multi-segment wells. | 100 |
| 76 | \--max-inner-iter-wells | A positive integer value that defines the maximum number of inner iterations for standard wells. | 50 |
| 77 | \--max-local-solve-iterations | A positive integer value that defines the maximum number of iterations for local solves with NLDD nonlinear solver. | 20 |
| 78 | \--max-newton-iterations-with-inner-well-iterations | A positive integer that specifies the maximum Newton iterations with inner well iterations. | 8 |
| 79 | \--max-pressure-change-ms-wells | A real positive value that defines the maximum relative pressure change for a single iteration of the multi-segment well model. | 1.0 x 10^6^ |
| 80 | \--max-residual-allowed | A real positive value that sets the absolute maximum tolerance for residuals without cutting the time step size. | 1.0 x 10^7^ |
| 81 | \--max-single-precision-days | A real positive value that sets the maximum time step size where single precision floating point arithmetic can be used for solving the linear systems of equations. | 20.0 |
| 82 | \--max-temperature-change | A real positive value that stipulates the maximum absolute change of temperature in a single iteration. | 5 |
| 83 | \--max-time-step-divisions | A positive integer that specifies the maximum number of divisions by two of the timestep size before the simulation bails out. | 10 |
| 84 | \--max-time-step-size | A real positive value that defines the maximum size to which all time steps are limited to in seconds. | inf |
| 85 | \--max-welleq-iter | A positive integer that defines the maximum number of iterations to determine the solution to the well equations. | 30 |
| 86 | \--maximum-number-of-well-switches | A positive integer values that stipulates the maximum number of times a well can switch to the same control. | 3 |
| 87 | \--maximum-water-saturation | A real positive value that defines the maximum water saturation. | 1.0 |
| 88 | \--milu-variant | A defined character string that specifies which variant of the modified ILU preconditioner ought to be used. Possible variants are:<br>1)  ILU (default, plain ILU),<br>2)  MILU_1 (lump diagonal with dropped row entries),<br>3)  MILU_2 (lump diagonal with the sum of the absolute values of the dropped row entries),<br>4)  MILU_3 (if diagonal is positive add sum of dropped row entries. Otherwise subtract them),<br>5)  MILU_4 (if diagonal is positive add sum of dropped row entries. Otherwise do nothing). | "ILU" |
| 89 | \--min-strict-cnv-ite | A positive integer that sets the minimum number of Newton iterations before relaxed tolerances are used for the CNV convergence criterion. | 0 |
| 90 | \--min-strict-mb-iter | An integer value defining the number of Newton iterations before relaxed tolerances can be used for the MB convergence criterion. Default -1 means that the relaxed tolerance is used when maximum number of Newton iterations are reached. | -1 |
| 91 | \--min-time-step-based-on-newton-iterations | A real positive value that sets the minimum time step size (in days for field and metric unit and hours for lab unit) can be reduced to based on Newton iteration counts. | 0.0 |
| 92 | \--min-time-step-before-shutting-problematic-wells-in-days | A real positive value that sets the minimum time step size in days for which problematic wells are not shut. Time steps below this value will result in problematic wells being shut-in by the simulator. | 0.01 |
| 93 | \--min-time-step-size | A real positive value that sets the minimum size to which all time steps are limited to in seconds. | 0.0 |
| 94 | \--network-max-iterations | A positive integer that sets the maximum number of iterations in the network solver before giving up. | 200 |
| 95 | \--network-max-strict-iterations | A positive integer that sets the maximum iterations in network solver before relaxing tolerance. | 100 |
| 96 | \--newton-max-error | A real positive value that sets the maximum error tolerated by the Newton method to which does not cause an abort. | 1e+100 |
| 97 | \--newton-max-iterations | A positive integer that defines the maximum number of Newton iterations per time step used by the simulator. | 20 |
| 98 | \--newton-max-relax | A real positive value that sets the maximum relaxation factor of a Newton iteration used by the simulator. | 0.5 |
| 99 | \--newton-min-iterations | A positive integer that sets the minimum number of Newton iterations per time step used by the simulator. | 2 |
| 100 | \--newton-relaxation-type | A character string. The type of relaxation used by the Newton method. Valid options are: dampen or sor. | "dampen" |
| 101 | \--newton-target-iterations | A positive integer that sets the \'optimum\' number of Newton iterations per time step. | 10 |
| 102 | \--newton-tolerance | A real positive value that sets the maximum raw error tolerated by the Newtonmethod for considering a solution to be converged. | 0.01 |
| 103 | \--newton-verbose | A boolean value that specifies whether the Newton method should inform the user about its progress (true) or not (false). | true |
| 104 | \--newton-write-convergence | A boolean value that specifies whether to write the convergence behaviour of the Newton method to a VTK file (true) or not (false). | false |
| 105 | \--nldd-num-initial-newton-iter | A positive integer that sets the number of initial global Newton iterations when running the NLDD nonlinear solver. | 1 |
| 106 | \--nonlinear-solver | A character string that specifies the nonlinear solver. Valid choices are newton or nldd. | \"newton\" |
| 107 | \--num-local-domains | A positive integer that sets the number of local domains for NLDD nonlinear solver.<br>Note this is an experimental feature in the current release 2023.10 that is expected to be more complete and tested by the 2024.10 release. | 0 |
| 108 | \--num-pressure-points-equil | A positive integer that sets the number of pressure points (in each direction) in tables used for equilibration. | 2000 |
| 109 | \--opencl-ilu-parallel | A boolean value that if set to true then parallelize the ILU decomposition and application on GPU, or not (false). | true |
| 110 | \--opencl-platform-id | A positive integer that specifies the platform identification ("ID") for the openSolver. Use the "clinfo" command to determine valid IDs. | 0 |
| 111 | \--output-dir | A character string that defines the directory to which OPM Flow is to write the commercial simulator compatible output files (restart, summary files etc.).<br>The default value results in the files be written to the same directory as the input file. | "" |
| 112 | \--output-extra-convergence-info | A defined character string that specifies whether to provide additional convergence output to separate files for diagnostic purposes. The available options are:<br>1)  \"none\" results in no extra output and overrides all other options.<br>2)  \"steps\" writes out convergence information per time step, to a CASENAME.INFOSTEP file. The file is useful for identifying numerical issues.<br>3)  \"iterations\" writes out non-linear convergence metrics, i.e., the MB and CNV values, per phase, for each non-linear iteration in each time step, to a CASENAME.INFOITER file.<br>Options can be combined with commas, e.g.\"steps,iterations\" for multiple outputs.<br>The default value of \"none\" prevents the two files from being written out, for better compatibility with the commercial simulator. | "none" |
| 113 | \--output-interval | A positive integer that specifies the number of report steps between two consecutive writes of restart data. | 1 |
| 114 | \--output-mode | A defined character string that defines the output to the \*.PRT and \*.DBG files:<br>1)  "none": No output to the files.<br>2)  "log" or false: Output logging information only.<br>3)  "all" or true: Output everything.<br>For example to just output logging information use:<br>\--output-mode="log".<br>or<br>\--output-mode=false | "all" |
| 115 | \--owner-cells-first | A boolean value that determines if the cells owned by a rank should be ordered before ghost/overlapping the cells (true), or not (false). | true |
| 116 | \--parameter-file | A character string that defines the name of a parameter file which contains the simulator's set of run-time parameters, as listed in this table. | "" |
| 117 | \--parsing-strictness | Set strictness of parsing process. Available options are:<br>1)  \"normal\": stop for critical errors, and for unsupported keywords that would would change the simulator results if supported.<br>2)  \"high\": stop for all errors, that is even for unsupported keywords that do not effect the results, for example ECHO and NOECHO.<br>3)  \"low\": same as normal, except do not stop due to unsupported keywords that would change the simulator results if supported, and even if marked critical.<br>Default: \"normal\" | \"normal\" |
| 118 | \--predetermined-time-steps-file | A file with a list of predetermined time step sizes (one time step per line). | \"\" |
| 119 | \--pressure-max | A positive real value. Maximum absolute pressure. | 1e+99 |
| 120 | \--pressure-min | A real value. Minimum absolute pressure. | -1e+99 |
| 121 | \--pressure-scale | A positive real value. Scaling of pressure primary variable. | 1 |
| 122 | \--pri-var-oscilation-threshold | A real positive value that defines the threshold value for the primary variable switching conditions after its meaning has switched to hinder oscillations. | 1.0 x 10^-5^ |
| 123 | \--print-parameters | A positive integer value that request that the run time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 124 | \--print-properties | A positive integer value that request that the compile time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 125 | \--project-saturations | A boolean value that determines if all the fluid saturations should be scaled to ensure the values are in the interval (0, 1), including runs that use solvents (true), or not (false). | false |
| 126 | \--regularization-factor-wells | A real positive value that defines the "regularization factor" for wells. | 100 |
| 127 | \--relaxed-linear-solver-reduction | A real positive value that defines the minimum reduction of the residual which the linear solver need to achieve for the solution to be accepted. | 0.01 |
| 128 | \--relaxed-max-pv-fraction | A real positive value that defines The fraction of the pore volume of the reservoir where the volumetric error (CNV) might be violated during strict Newton iterations. | 0.03 |
| 129 | \--relaxed-pressure-tol-msw | A real positive value that sets the relaxation tolerance for the multi-segment well *pressure* solution in Pascals. | 10000 |
| 130 | \--relaxed-well-flow-tol | A real positive value that sets the relaxation tolerance for the well flow residual in reservoir cubic metres (rm3). | 0.001 |
| 131 | \--restart-time | A real positive value that sets the simulation time at which a restart should be attempted \[s\]. | -1e+35 |
| 132 | \--restart-writing-interval | A positive integer value that sets the frequency at which time steps are serialized to disk. | 16777215 |
| 133 | \--save-file | A character string that specifies the FileName for .OPMRST file used for saving serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 134 | \--save-step | A character string that determines if the simulator should save the serialized state of the OPM Flow simulator at one or more report steps to a special \*.OPMRST file. This is in addition to the normal restart files written, and consumes significantly more space than the normal restart files, but restarting OPM Flow from this file using the *\--load-step* option deviates less from the original run, compared to restarting using the normal restart features. The files produced are not compatible with other simulators, and also will not be compatible between different releases of OPM Flow<br>The parameter should be set to one of the following:<br>1)  \"all\" to save all report steps,<br>2)  \":x\" to save every x\'th step, or<br>3)  \"x\" to save a specif time step.<br>The default value of \"\" does not write anything to the OPM Flow specific restart file. | \"\" |
| 135 | \--scale-linear-system | A boolean value that switches on (true) or off (false) the scaling of linear system of equations according to the equation scale and primary variable types. | false |
| 136 | \--sched-restart | A boolean value that determines for a restart run if the case should initialize wells and groups from the historical SCHEDULE section (true), or from the well and group data on the restart file (false).<br>Note that the commercial simulator always uses data from the restart file (false). | false |
| 137 | \--serial-partitioning | A boolean value that determines if partitioning for parallel runs on a single process (true), or not (false). | false |
| 138 | \--shut-unsolvable-wells | A boolean value that determines if the simulator should shut unsolvable wells (true), or not (false). | true |
| 139 | \--solve-welleq-initially | A boolean value that determines if the simulator should fully solve the well equations before each iteration of the reservoir model (true), or not (false).<br>Note that the well equations are always added to the full system and solved until convergence. | true |
| 140 | \--solver-continue-on-convergence-failure | A boolean value that stipulates if the simulator should continue (true) instead of stopping (false) when the minimum solver time step is reached. | false |
| 141 | \--solver-growth-factor | A real positive value that specifies the growth factor a time step can be increased by when recovering from one or more time step chops, subject to the maximum allowable time step size set by the *\--solver-max-time-step-in-days* parameter.<br>For example, if the current time step has converged at 5 days after a time step chop, and \--solver-growth-factor is set to the default value of 2.0, then the next time step will be 2.0 \* 5 days, that is at 10 days. | 2.0 |
| 142 | \--solver-max-growth | A real positive value that specifies the maximum growth factor a time step can be increased by after a report time step, subject to the maximum allowable time step size set by the \--solver-max-time-step-in-days parameter.<br>Thus, if the current time step has converged at 5 days after at a report step, and \--solver-*max-*growth is set to the default value of 3.0, then the next time step will be 3.0 \* 5 days, that is at 15 days. | 3.0 |
| 143 | \--solver-max-restarts | A positive integer that defines the number of allowed consecutive restarts (or time step chops) before the simulation is terminated. | 10 |
| 144 | \--solver-max-time-step-in-days | A real positive double precision value that specifies the maximum allowed time step size in days. | 365 |
| 145 | \--solver-min-time-step | A real positive double precision value that specifies the minimum size of a time step in days for field and metric units, and hours for laboratory units<br>If a time step cannot converge without getting cut below this time step size the simulator will stop. | 1.0 x 10^-12^ |
| 146 | \--solver-restart-factor | A real positive double precision value that sets the time step chop factor of the time step after a convergence failure.<br>For example, if the current non-convergent time step is 30 days and *\--solver-restart-factor * is set to the default value, then the time step will be repeated using 0.33 \* 30 days as the time step, that is 9.9 days. | 0.33 |
| 147 | \--solver-verbosity | A positive integer that specifies the \"chattiness\" of the non-linear solver. | 1 |
| 148 | \--strict-inner-iter-wells | A positive integer that specifies the number of inner well iterations with strict tolerance. | 40 |
| 149 | \--strict-outer-iter-wells | A positive integer that specifies the number of Newton iterations for which wells are checked with strict tolerance. | 6 |
| 150 | \--temperature-max | A real positive value that sets the maximum absolute temperature. | 1.0 x 10^9^ |
| 151 | \--temperature-min | A real positive value that sets the minimum absolute temperature. | 0 |
| 152 | \--threads-per-process | A positive integer value that stipulates the maximum number of threads to be instantiated per process (\'-1\' means \'automatic\'). | -1 |
| 153 | \--tolerance-mb-relaxed | A positive real value. Relaxed tolerated mass balance error that applies for iterations after the iterations with the strict tolerance. | 1e-06 |
| 154 | \--time-step-after-event-in-days | A real double precision value that sets the maximum allowed time step after an event; for example, when a well is open or closed etc.<br>The default value of -1 means that events to do effect the time stepping. | -1 |
| 155 | \--time-step-control | A defined character string that defines the time stepping control algorithm and is set to one of the following:<br>1)  pid: PID controller based adaptive time step control as suggested by Turek and Kuzmin[^25].<br>2)  pid+iteration: Use PID and linear iteration numbers to guide the time step.<br>3)  pid+newtoniteration: Use PID and non-linear iterations numbers to guide the time step.<br>4)  Hardcoded: Use time steps supplied by user via the time-step-control-filename parameter. | "pid+newtoniteration" |
| 156 | \--time-step-control-decay-damping-factor | A real positive value that specifies the decay rate a time step can be decreased by after the number target iterations has been exceeded | 1.0 |
| 157 | \--time-step-control-decay-rate | A real positive value that specifies the decay rate a time step size can be decreased by after the number of target iterations has been exceeded | 0.75 |
| 158 | \--time-step-control-file-name | A character string enclosed in quotes that specifies a filename where time steps are specified. The default is the character string timesteps.<br>For instance time steps can be generated by the ecl_summary application in libecl as per the following UNIX command line:<br>path_to_libecl_applications/ecl_summary DECK TIME \> filename<br>Where:<br>DECK is the name of the data deck you want to get the time steps from,<br>TIME tells the application to return the timing for the run, and<br>\"filename\" is the name of the file the times are piped to. | "timesteps" |
| 159 | \--time-step-control-growth-damping-factor | A real positive value that specifies the growth rate of the *time step *increase when the number of target iterations are undercut. | 3.2 |
| 160 | \--time-step-control-growth-rate | A real positive value that specifies the growth rate of the *time step size* when the number of target iterations are undercut. | 1.25 |
| 161 | \--time-step-control-target-iterations | A positive integer that defines the number of linear iterations which the time step control scheme should aim for (if applicable). | 30 |
| 162 | \--time-step-control-target-newton-iterations | A positive integer that specifies the number of Newton iterations which the time step control scheme should aim for (if applicable). | 8 |
| 163 | \--time-step-control-tolerance | A real double precision value that sets the tolerance for PID (only used with the pid and pid+ options defined by the \--time-step-control option). | 0.1 |
| 164 | \--time-step-verbosity | A positive integer that specifies the \"chattiness\" during the time integration. | 1 |
| 165 | \--tolerance-cnv | A real positive double precision value that specifies the maximum non-linear tolerance error. This is the local convergence tolerance (maximum of local saturation errors). | 0.01 |
| 166 | \--tolerance-cnv-relaxed | A real positive value that defines the relaxed local convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 167 | \--tolerance-mb | A real positive double precision value that sets the maximum mass balance error, that is the tolerated mass balance error relative to total mass present. | 1.0 x 10^-6^ |
| 168 | \--tolerance-pressure-ms-wells | A real positive double precision value that specifies the tolerance for the pressure equations for multi-segment wells. | 1000 |
| 169 | \--tolerance-well-control | A real positive double precision value that sets the maximum tolerance for the well control equations. | 1.0 x 10^-7^ |
| 170 | \--tolerance-wells | A real positive double precision value that defines the maximum non-linear error for the well equations. | 1.0 x 10^-4^ |
| 171 | -update-equations-scaling | A boolean value that switches on (true) or off (false) the updating of the scaling factors for mass balance equations during the simulation. | false\ |
| 172 | \--use-average-density-ms-wells | A boolean value that specifies whether to approximate segment densitities by averaging over the segment and its outlet (true) or not (false). | false |
| 173 | \--use-gmres | A boolean value that when set to true OPM Flow will use Generalized Minimal Residual ("GMRES")[^26] and [^27] solver instead of Biconjugate Gradient Stabilized ("BiCGSTAB")[^28] and [^29] as the linear solver within the Newton iterations. | false |
| 174 | \--use-implicit-ipr | A boolean value. Compute implicit IPR for stability checks and stable solution search. | false |
| 175 | \--use-multisegment-well | A boolean value that when set to true the simulator will use the well model for multi-segment wells instead of the one for single-segment wells. | true |
| 176 | \--use-update-stabilization | A boolean value that switches on (true) or off (false) the stabilized Newton option, that attempts to detect and correct oscillations or stagnation during the Newton iterations.<br>This option may improve convergence for some cases. | true |
| 177 | \--water-only-threshold | A real positive value that defines the saturation threshold, for which cells with water saturations above or equal to this threshold are considered one-phase water only. | 1.0 |
| 178 | \--zoltan-imbalance-tol | A real positive value that defines the tolerable imbalance of the load balancing provided by Zoltan package. | 1.1 |
| 179 | \--zoltan-params | A character string that specifies the configuration of the Zoltan partitioner. Valid options are: graph, hypergraph or scotch. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See https://sandialabs.github.io/Zoltan/ug_html/ug.html for available Zoltan options. | \"graph\" |
| Notes:<br>1)  Cells colored green in the No. column are new command line parameters for this release. Similarly for the Default column, cells colored green indicate the default value has changed from the previous release.<br>2)  Items shaded in gray are considered to be developer options that should be used with caution as the values associated with these command line parameters are subject to change.<br>3)  VTK Graphics Command Line Parameters[^30] set of commands are no longer listed via the basic help command line command:<br>flow \--help<br>instead use:<br>flow \--help-all<br>to get a list of supported command line Parameters.<br>3)  The \--enable-vtk-output option above, if set to "true" will write out the data as stipulated by the compile options. One may need to compile the source code to obtain the desired output.<br>4)  As per all UNIX and LINUX based system the input is case dependent.<br>5)  If a parameter file is used to set one of the above parameters, the leading "\--" should not be incorporated in the parameter file. |  |  |  |

*<a id="REF_TABLE_OPM_FLOW_2023_04_OPTIONS_2_2"></a>Table A.3: OPM Flow 2024-04 Command Line Options*
A.  1.  ## Running OPM Flow 2023-10

        > The command line syntax for running OPM Flow is:

flow \[OPTIONS\] CASENAME

and typing the following command from your terminal:

flow CASENAME

will start the simulator and run the case specified by CASENAME.DATA.

OPM Flow accepts command line options to control various aspects of the simulator's run time behavior, as described in the table below. To give a command line option use "key=value" syntax, with no spaces around the equals sign. It is also possible to put multiple options together in a parameter file. To do so, put one option on each line of the file with ".param" as the extension and pass that filename as a command line parameter to OPM Flow using:

flow \--parameter-file=CASENAME.param

to instruct OPM Flow to read the parameter file.

| 1 | -h or \--help | A character string that causes OPM Flow to print a help message that gives a brief description of the available command line parameters.<br>This now only prints the active user facing command line options. | N/A |
| --- | --- | --- | --- |
| 2 | \--help-all | Prints all the command line options included in the release, including obsolete, hidden and deprecated options. | N/A |
| 3 | \--accelerator-mode | Choose a linear solver, usage: \'\--accelerator-mode=\[ none \| cusparse \| opencl \| amgcl \| rocalution \]\'. | "none" |
| 4 | \--allow-distributed-wells | Allow the perforations of a well to be distributed to interior of multiple processes. | false |
| 5 | \--alternative-well-rate-init | Use alternative well rate initialization procedure. | true |
| 6 | \--bda-device-id | Choose device ID for cusparseSolver or openclSolver, use \'nvidia-smi\' or \'clinfo\' commands to determine valid IDs. | 0 |
| 7 | \--continue-on-convergence-error | Continue with a non-converged solution instead of giving up if we encounter a time step size smaller than the minimum time step size. | false |
| 8 | \--cpr-reuse-interval | A positive integer that sets the reuse preconditioner interval. Used when<br>\--cpr-reuse-setup<br>is set to 4, then the preconditioner will be fully recreated instead of reused every N linear solve, where N is this parameter. | 30 |
| 9 | \--cpr-reuse-setup | A positive integer that defines if the CPR solver should re-use the AMG setup. Valid options are:<br>0.  Recreate the preconditioner for every linear solve.<br>1.  Recreate once every time step.<br>2.  Recreate if last linear solve took more than 10 iterations.<br>3.  Never recreate.<br>4.  Recreate every N linear solves, where N is the parameter *\--cpr-reuse-interval*.<br>Changed the default value from three to four. | 4 |
| 10 | \--dbph-max-rel | A real positive value that sets the maximum relative change of the bottom-hole pressure in a single iteration. | 1.0 |
| 11 | \--dp-max-rel | A real positive double precision value that sets the maximum allowed relative change of pressure per iteration. | 0.3 |
| 12 | \--ds-max | A real positive double precision value that sets the maximum allowed change in saturation per iteration. | 0.2 |
| 13 | \--dwell-fraction-max | A real positive value that sets the maximum allowed change in well's volume fraction per iteration. | 0.2 |
| 14 | \--ecl-deck-file-name | A character string that defines the name of the OPM Flow input file which contains the simulator's ECLIPSE formatted input deck to be simulated.<br>Note that there must be no spaces in the filename. If there are spaces, which can typically occur on Windows based systems, then the filename should be enclosed in quotes; thus instead of FILE NAME use \"FILE NAME\". | "" |
| 15 | \--ecl-enable-drift-compensation | A boolean value that enables (true) or disables (false) partial compensation of systematic mass losses via the source term of the next time step. | true |
| 16 | \--ecl-enable-tuning | Honor some aspects of the TUNING keyword from the ECL deck. | false |
| 17 | \--ecl-newton-relaxed-tolerance | The maximum error which the volumetric residual may exhibit if it is in a \'relaxed\' region during a strict iteration. | 1e+09 |
| 18 | \--ecl-newton-relaxed-volume-fraction | The fraction of the pore volume of the reservoir where the volumetric error may be voilated during strict Newton iterations. | 0.03 |
| 19 | \--ecl-newton-strict-iterations | The number of Newton iterations where the volumetric error is considered. | 8 |
| 20 | \--ecl-newton-sum-tolerance | The maximum error tolerated by the Newton method for considering a solution to be converged. | 0.0001 |
| 21 | \--ecl-newton-sum-tolerance-exponent | The exponent used to scale the sum tolerance by the total pore volume of the reservoir. | 0.333333 |
| 22 | \--ecl-output-double-precision | A boolean value that switches on (true) or off (false) double precision in restart files.<br>Useful for \'perfect\' restarts. | false |
| 23 | \--ecl-output-interval | An integer value defining the number of report steps that ought to be skipped between two writes of restart files results. | -1 |
| 24 | \--edge-weights-method | A defined positive integer value that defines the edge-weighing strategy:<br>0.  For uniform,<br>1.  for trans, or<br>2.  for log(trans). | 1 |
| 25 | \--enable-adaptive-time-stepping | A boolean value that turns on (true) or off (false) adaptive time stepping. If set to false the report time steps provided by the input deck are used. | true |
| 26 | \--enable-async-ecl-output | A boolean value that sets the output mode to be asynchronously (true), letting the simulator continue computing the next time step while writing results to restart and summary files in the commercial simulators format. | true |
| 27 | \--enable-async-vtk-output | A boolean value that sets the output mode to be asynchronously (true), letting the simulator continue computing the next time step while writing results to the VTK output files. | true |
| 28 | \--enable-dry-run | A boolean value that specifies if the simulation should actually run, (true) or just check the input deck (false).<br>This option is equivalent to activating the NOSIM keyword in the RUNSPEC section of the input deck (see section [Error: Reference source not found](#anchor-1)[Error: Reference source not found](#anchor-1)).<br>The default value of "auto' will use whatever is stipulated in the input deck via the NOSIM keyword. | "auto" |
| 29 | \--enable-ecl-output | A boolean value that specifies if the binary output files (restart, summary files, etc.) should be written in the commercial simulator's format (true), or OPM Flow's format (false). | true |
| 30 | \--enable-esmry | A boolean value that switches on (true) or off (false) the output SUMMARY vectors to the ESMRY file for fast loading of summary data. | false |
| 31 | \--enable-gravity | A boolean value that switches on (true) or off (false) the use of the gravity correction for the pressure gradients. | true |
| 32 | \--enable-grid-adaptation | A boolean value that enables (true) or disables (false) adaptive grid refinement/coarsening. Note that Eclipse grid output will be disabled if adaptive grid refinement/coarsening is enabled. | false |
| 33 | \--enable-intensive-quantity-cache | A boolean value that switches on (true) or off (false) the caching of intensive quantities. | true |
| 34 | \--enable-logging-fallout-warning | A boolean value that sets the developer option to see whether logging was on non-root processors (true). If set to true output will be appended to the \*.DBG or \*.PRT files. | false |
| 35 | \--enable-opm-rst-file | A boolean value set to true or false to write OPM specific data sets to the commercial simulators restart file to enable restart of an OPM Flow runs (true) by OPM Flow, or not to write the data (false). | false |
| 36 | \--enable-storage-cache | A boolean value that turns on (true) or off (false) storing previous storage terms and avoid re-calculating them. | true |
| 37 | \--enable-terminal-output | A boolean value that turns on (true) or off (false) high-level information about the simulation\'s progress to the terminal | true |
| 38 | \--enable-thermodynamic-hints | A boolean value that enables (true) or disables (false) thermodynamic hints. | false |
| 39 | \--enable-tuning | A boolean value that instructs OPM Flow to read the time stepping parameters from the [Error: Reference source not found](#anchor-2) keyword in the input deck, if set to true.<br>Note that only the first record of the TUNING keyword is processed. | false |
| 40 | \--enable-vtk-output | A boolean value that turns on (true) or off (false) a global switch for writing VTK files. | false |
| 41 | \--enable-well-operability-check | A boolean value that enables (true) checking of a well's operating status, or disables (false) the checking. | true |
| 42 | \--enable-well-operability-check-iter | A boolean value that enables (true) checking of a well's operating status during iterations, or disables (false) the checking during iterations. | false |
| 43 | \--enable-write-all-solutions | A boolean value that turns on (true) or off (false) the writing of all solutions to disk instead of only the ones for the report steps. | false |
| 44 | \--end-time | The simulation time at which the simulation is finished \[s\]. | 1e+100 |
| 45 | \--force-disable-fluid-in-place-output | A boolean value that instructs OPM Flow not to print the Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 46 | \--force-disable-resv-fluid-in-place-output | A boolean value that instructs OPM Flow to not to print the Reservoir Volume Fluid In-Place report after each report time step (true) or not (false).<br>Note this parameter will override the print request in the input deck. | false |
| 47 | \--full-time-step-initially | A boolean value that instructs OPM Flow to always attempt to finish a report step using a single time step (true) or not (false). | false |
| 48 | \--ignore-keywords | A character string that defines a list of keywords which should be ignored by OPM Flow. The keyword string should be enclosed in quotes and each keyword separated by a colon, that is \':\'. | "" |
| 49 | \--ilu-fillin-level | A positive integer value that sets the fill in level for the ILU preconditioner. | 0 |
| 50 | \--ilu-redblack | A boolean value that instructs OPM Flow to use red-black partitioning for the ILU preconditioner. | false |
| 51 | \--ilu-relaxation | A real positive double precision value that sets the relaxation factor of the linear solver\'s ILU preconditioner. | 0.9 |
| 52 | \--ilu-reorder-spheres | A boolean value that specifies OPM Flow to reorder the entries of the matrix in the red-black ILU preconditioner in spheres starting at an edge (true) or not (false).<br>If false the original ordering is preserved in each color. Otherwise try to ensure D4 ordering (in a 2D structured grid, the diagonal elements are consecutive). | false |
| 53 | \--initial-time-step-in-days | A real double precision value that sets the size of initial time step in days. | 1.0 |
| 54 | \--initial-time-step-size | A real double precision value that sets the size of initial time step in seconds. | 86400 |
| 55 | \--linear-solver | A defined quoted character string that sets the configuration of the linear solver, valid values are:<br>1)  ilu0 (default),<br>2)  cprw or cpr (an alias for cprw),[^31] [^32] and [^33]<br>3)  cpr_quasiimpes,<br>4)  cpr_trueimpes,<br>5)  amg,[^34]<br>6)  hybrid (experimental), or<br>7)  a file name that has the extension ".json", that contains the linear solver configuration parameters.<br>Option (2) extends the existing Constrained Pressure Residual ("CPR") preconditioner to include wells. This option can also be invoked via the CPR keyword in the RUNSPEC section; however, the command line parameter takes precedence.<br>For option (7) one enters a character string enclosed in quotes that defines the filename of a JSON configuration file for the flexible linear solver system. In this case the file extension should be '.json'.<br>Note that the \*.PRT file contains the "Property tree for the linear solver" listing, which is the JSON specification of the current case, and can be used to configure a user specific linear solver JSON file.<br>The option \"cpr\" now is an alias for \"cprw\" instead of \"cpr_trueimpes\". | "ilu0" |
| 56 | \--linear-solver-ignore-convergence-failure | A boolean value that if set to true convergences failures in the linear solver are ignored.<br>This option should be used with care, as the results might be unreliable. | false |
| 57 | \--linear-solver-max-iter | A positive integer value that defines the maximum number of linear iterations. | 200 |
| 58 | \--linear-solver-print-json-definition | Write the JSON definition of the linear solver setup to the DBG file. | true |
| 59 | \--linear-solver-reduction | A real positive double precision value that sets the minimum reduction of the residual for the linear solver. The linear solver convergences when the residual is reduced sufficiently.<br>The simulator now overrides the default reduction to be 0.005 instead of 0.01, if the linear solver has been set to one of the cpr options, in a similar manner as how the default maximum number of linear iterations for the cpr and cprw options are changed to 20 instead of 200, unless specified by the command line option by the user. | 0.01 |
| 60 | \--linear-solver-restart | A positive integer value that sets the number of iterations after which GMRES is restarted. | 40 |
| 61 | \--linear-solver-verbosity | A positive integer value that defines the output from linear solver:<br>0.  No extra output,<br>1.  output per solution iteration, or<br>2.  output per iteration. | 0 |
| 62 | \--load-file | A character string enclosed in quotes that defines the FileName for the .OPMRST file used to load the serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 63 | \--load-step | An integer value that determines if the simulator should load the serialized state from OPM Flow\'s version of the restart file, and should be set to either a specific report step, or 0 to load the last stored report step.<br>The default value of -1 does not load the data from the OPM Flow specific restart file.<br>OPM Flow\'s version of the restart file, is written using the *\--save-step=N* option. | -1 |
| 64 | \--local-domains-ordering-measure | A character string enclosed in quotes that defines the subdomain ordering measure. Allowed values are \'pressure\' and \'residual\'. | \"pressure\" |
| 65 | \--local-domains-partitioning-imbalance | A real positive double precision value that sets the subdomain partitioning imbalance tolerance. 1.03 is 3 percent imbalance. | 1.03 |
| 66 | \--local-domains-partitioning-method | A character string enclosed in quotes that defines the subdomain partitioning method. Allowed values are \'zoltan\', \'simple\', and the name of a partition file ending with \'.partition\'. | \"zoltan\" |
| 67 | \--local-solve-approach | A character string enclosed in quotes that defines the local solve approach. Valid choices are 'jacobi' and 'gauss-seidel'. | \"jacobi\" |
| 68 | \--local-tolerance-scaling-cnv | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 0.01 |
| 69 | \--local-tolerance-scaling-mb | A real positive double precision value that sets the convergence tolerance for local solves. Set to lower than 1.0 to use stricter convergence tolerance for local solves. | 1 |
| 70 | \--local-well-solve-control-switching | A boolean value that allows (true) or disallows (false) control switching during local well solutions. | false |
| 71 | \--matrix-add-well-contributions | A boolean value that if set to true explicitly specifies the influences of wells between cells in the Jacobian and preconditioner matrices. | false |
| 72 | \--max-inner-iter-ms-wells | A positive integer value that defines the maximum number of inner iterations for multi-segment wells. | 100 |
| 73 | \--max-inner-iter-wells | A positive integer value that defines the maximum number of inner iterations for standard wells. | 50 |
| 74 | \--max-local-solve-iterations | A positive integer value that defines the maximum number of iterations for local solves with NLDD nonlinear solver. | 20 |
| 75 | \--max-newton-iterations-with-inner-well-iterations | A positive integer that specifies the maximum Newton iterations with inner well iterations. | 8 |
| 76 | \--max-pressure-change-ms-wells | A real positive value that defines the maximum relative pressure change for a single iteration of the multi-segment well model. | 1.0 x 10^6^ |
| 77 | \--max-residual-allowed | A real positive value that sets the absolute maximum tolerance for residuals without cutting the time step size. | 1.0 x 10^7^ |
| 78 | \--max-single-precision-days | A real positive value that sets the maximum time step size where single precision floating point arithmetic can be used for solving the linear systems of equations. | 20.0 |
| 79 | \--max-temperature-change | A real positive value that stipulates the maximum absolute change of temperature in a single iteration. | 5 |
| 80 | \--max-time-step-divisions | A positive integer that specifies the maximum number of divisions by two of the timestep size before the simulation bails out. | 10 |
| 81 | \--max-time-step-size | A real positive value that defines the maximum size to which all time steps are limited to in seconds. | inf |
| 82 | \--max-welleq-iter | A positive integer that defines the maximum number of iterations to determine the solution to the well equations. | 30 |
| 83 | \--maximum-number-of-well-switches | A positive integer values that stipulates the maximum number of times a well can switch to the same control. | 3 |
| 84 | \--maximum-water-saturation | A real positive value that defines the maximum water saturation. | 1.0 |
| 85 | \--milu-variant | A defined character string that specifies which variant of the modified ILU preconditioner ought to be used. Possible variants are:<br>1)  ILU (default, plain ILU),<br>2)  MILU_1 (lump diagonal with dropped row entries),<br>3)  MILU_2 (lump diagonal with the sum of the absolute values of the dropped row entries),<br>4)  MILU_3 (if diagonal is positive add sum of dropped row entries. Otherwise subtract them),<br>5)  MILU_4 (if diagonal is positive add sum of dropped row entries. Otherwise do nothing).<br>The default is "ILU" | "ILU" |
| 86 | \--min-strict-cnv-ite | A positive integer that sets the minimum number of Newton iterations before relaxed tolerances are used for the CNV convergence criterion. | 0 |
| 87 | \--min-time-step-based-on-newton-iterations | A real positive value that sets the minimum time step size (in days for field and metric unit and hours for lab unit) can be reduced to based on Newton iteration counts. | 0.0 |
| 88 | \--min-time-step-before-shutting-problematic-wells-in-days | A real positive value that sets the minimum time step size in days for which problematic wells are not shut. Time steps below this value will result in problematic wells being shut-in by the simulator. | 0.01 |
| 89 | \--min-time-step-size | A real positive value that sets the minimum size to which all time steps are limited to in seconds. | 0.0 |
| 90 | \--network-max-iterations | A positive integer that sets the maximum number of iterations in the network solver before giving up. | 200 |
| 91 | \--network-max-strict-iterations | A positive integer that sets the maximum iterations in network solver before relaxing tolerance. | 100 |
| 92 | \--newton-max-error | A real positive value that sets the maximum error tolerated by the Newton method to which does not cause an abort. | 1e+10 |
| 93 | \--newton-max-iterations | A positive integer that defines the maximum number of Newton iterations per time step used by the simulator. | 20 |
| 94 | \--newton-max-relax | A real positive value that sets the maximum relaxation factor of a Newton iteration used by the simulator. | 0.5 |
| 95 | \--newton-min-iterations | A positive integer that sets the minimum number of Newton iterations per time step used by the simulator.<br>The default value of one ensures that at least one Newton iteration is performed after the previous time step. | 1 |
| 96 | \--newton-relaxation-type | A character string. The type of relaxation used by the Newton method. Valid options are: dampen or sor. | "dampen" |
| 97 | \--newton-target-iterations | A positive integer that sets the \'optimum\' number of Newton iterations per time step. | 6 |
| 98 | \--newton-tolerance | A real positive value that sets the maximum raw error tolerated by the Newtonmethod for considering a solution to be converged. | 0.01 |
| 99 | \--newton-verbose | A boolean value that specifies whether the Newton method should inform the user about its progress (true) or not (false). | true |
| 100 | \--newton-write-convergence | A boolean value that specifies whether to write the convergence behaviour of the Newton method to a VTK file (true) or not (false). | false |
| 101 | \--nldd-num-initial-newton-iter | A positive integer that sets the number of initial global Newton iterations when running the NLDD nonlinear solver. | 1 |
| 102 | \--nonlinear-solver | A character string that specifies the nonlinear solver. Valid choices are newton or nldd. | \"newton\" |
| 103 | \--num-local-domains | A positive integer that sets the number of local domains for NLDD nonlinear solver.<br>Note this is an experimental feature in the current release 2023.10 that is expected to be more complete and tested by the 2024.10 release. | 0 |
| 104 | \--num-pressure-points-equil | A positive integer that sets the number of pressure points (in each direction) in tables used for equilibration. | 2000 |
| 105 | \--opencl-ilu-parallel | A boolean value that if set to true then parallelize the ILU decomposition and application on GPU, or not (false). | true |
| 106 | \--opencl-platform-id | A positive integer that specifies the platform identification ("ID") for the openSolver. Use the "clinfo" command to determine valid IDs. | 0 |
| 107 | \--output-dir | A character string that defines the directory to which OPM Flow is to write the commercial simulator compatible output files (restart, summary files etc.).<br>The default value results in the files be written to the same directory as the input file. | "" |
| 108 | \--output-extra-convergence-info | A defined character string that specifies whether to provide additional convergence output to separate files for diagnostic purposes. The available options are:<br>1)  \"none\" results in no extra output and overrides all other options.<br>2)  \"steps\" writes out convergence information per time step, to a CASENAME.INFOSTEP file. The file is useful for identifying numerical issues.<br>3)  \"iterations\" writes out non-linear convergence metrics, i.e., the MB and CNV values, per phase, for each non-linear iteration in each time step, to a CASENAME.*INFOITER* file.<br>Options can be combined with commas, e.g.\"steps,iterations\" for multiple outputs.<br>The default value of \"none\" prevents the two files from being written out, for better compatibility with the commercial simulator. | "none" |
| 109 | \--output-interval | A positive integer that specifies the number of report steps between two consecutive writes of restart data. | 1 |
| 110 | \--output-mode | A defined character string that defines the output to the \*.PRT and \*.DBG files:<br>1)  "none": No output to the files.<br>2)  "log" or false: Output logging information only.<br>3)  "all" or true: Output everything.<br>For example to just output logging information use:<br>\--output-mode="log".<br>or<br>\--output-mode=false | "all" |
| 111 | \--owner-cells-first | A boolean value that determines if the cells owned by a rank should be ordered before ghost/overlapping the cells (true), or not (false). | true |
| 112 | \--parameter-file | A character string that defines the name of a parameter file which contains the simulator's set of run-time parameters, as listed in this table. | "" |
| 113 | \--parsing-strictness | Set strictness of parsing process. Available options are:<br>1)  \"normal\": stop for critical errors, and for unsupported keywords that would would change the simulator results if supported.<br>2)  \"high\": stop for all errors, that is even for unsupported keywords that do not effect the results, for example ECHO and NOECHO.<br>3)  \"low\": same as normal, except do not stop due to unsupported keywords that would change the simulator results if supported, and even if marked critical.<br>Default: \"normal\" | \"normal\" |
| 114 | \--predetermined-time-steps-file | A file with a list of predetermined time step sizes (one time step per line). | \"\" |
| 115 | \--pri-var-oscilation-threshold | A real positive value that defines the threshold value for the primary variable switching conditions after its meaning has switched to hinder oscillations. | 1.0 x 10^-5^ |
| 116 | \--print-parameters | A positive integer value that request that the run time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 117 | \--print-properties | A positive integer value that request that the compile time parameters be printed at the start of the run:<br>0.  No output to the files.<br>1.  Output \*.DBG file.<br>2.  Output to \*.DBG and \*.PRT files (default). | 2 |
| 118 | \--project-saturations | A boolean value that determines if all the fluid saturations should be scaled to ensure the values are in the interval (0, 1), including runs that use solvents (true), or not (false). | false |
| 119 | \--regularization-factor-wells | A real positive value that defines the "regularization factor" for wells. | 100 |
| 120 | \--relaxed-linear-solver-reduction | A real positive value that defines the minimum reduction of the residual which the linear solver need to achieve for the solution to be accepted. | 0.01 |
| 121 | \--relaxed-max-pv-fraction | A real positive value that defines The fraction of the pore volume of the reservoir where the volumetric error (CNV) might be violated during strict Newton iterations. | 0.03 |
| 122 | \--relaxed-pressure-tol-msw | A real positive value that sets the relaxation tolerance for the multi-segment well *pressure* solution in Pascals. | 10000 |
| 123 | \--relaxed-well-flow-tol | A real positive value that sets the relaxation tolerance for the well flow residual in reservoir cubic metres (rm3). | 0.001 |
| 124 | \--restart-time | A real positive value that sets the simulation time at which a restart should be attempted \[s\]. | -1e+35 |
| 125 | \--restart-writing-interval | A positive integer value that sets the frequency at which time steps are serialized to disk. | 16777215 |
| 126 | \--save-file | A character string that specifies the FileName for .OPMRST file used for saving serialized state. If empty, CASENAME.OPMRST is used. | \"\" |
| 127 | \--save-step | A character string that determines if the simulator should save the serialized state of the OPM Flow simulator at one or more report steps to a special \*.OPMRST file. This is in addition to the normal restart files written, and consumes significantly more space than the normal restart files, but restarting OPM Flow from this file using the *\--load-step* option deviates less from the original run, compared to restarting using the normal restart features. The files produced are not compatible with other simulators, and also will not be compatible between different releases of OPM Flow<br>The parameter should be set to one of the following:<br>1)  \"all\" to save all report steps,<br>2)  \":x\" to save every x\'th step, or<br>3)  \"x\" to save a specif time step.<br>The default value of \"\" does not write anything to the OPM Flow specific restart file. | \"\" |
| 128 | \--scale-linear-system | A boolean value that switches on (true) or off (false) the scaling of linear system of equations according to the equation scale and primary variable types. | false |
| 129 | \--sched-restart | A boolean value that determines for a restart run if the case should initialize wells and groups from the historical SCHEDULE section (true), or from the well and group data on the restart file (false).<br>Note that the commercial simulator always uses data from the restart file (false). | FALSe |
| 130 | \--serial-partitioning | A boolean value that determines if partitioning for parallel runs on a single process (true), or not (false). | false |
| 131 | \--shut-unsolvable-wells | A boolean value that determines if the simulator should shut unsolvable wells (true), or not (false). | true |
| 132 | \--solve-welleq-initially | A boolean value that determines if the simulator should fully solve the well equations before each iteration of the reservoir model (true), or not (false).<br>Note that the well equations are always added to the full system and solved until convergence. | true |
| 133 | \--solver-continue-on-convergence-failure | A boolean value that stipulates if the simulator should continue (true) instead of stopping (false) when the minimum solver time step is reached. | false |
| 134 | \--solver-growth-factor | A real positive value that specifies the growth factor a time step can be increased by when recovering from one or more time step chops, subject to the maximum allowable time step size set by the *\--solver-max-time-step-in-days* parameter.<br>For example, if the current time step has converged at 5 days after a time step chop, and \--solver-growth-factor is set to the default value of 2.0, then the next time step will be 2.0 \* 5 days, that is at 10 days. | 2.0 |
| 135 | \--solver-max-growth | A real positive value that specifies the maximum growth factor a time step can be increased by after a report time step, subject to the maximum allowable time step size set by the \--solver-max-time-step-in-days parameter.<br>Thus, if the current time step has converged at 5 days after at a report step, and \--solver-*max-*growth is set to the default value of 3.0, then the next time step will be 3.0 \* 5 days, that is at 15 days. | 3.0 |
| 136 | \--solver-max-restarts | A positive integer that defines the number of allowed consecutive restarts (or time step chops) before the simulation is terminated. | 10 |
| 137 | \--solver-max-time-step-in-days | A real positive double precision value that specifies the maximum allowed time step size in days. | 365 |
| 138 | \--solver-min-time-step | A real positive double precision value that specifies the minimum size of a time step in days for field and metric units, and hours for laboratory units<br>If a time step cannot converge without getting cut below this time step size the simulator will stop. | 1.0 x 10^-12^ |
| 139 | \--solver-restart-factor | A real positive double precision value that sets the time step chop factor of the time step after a convergence failure.<br>For example, if the current non-convergent time step is 30 days and *\--solver-restart-factor * is set to the default value, then the time step will be repeated using 0.33 \* 30 days as the time step, that is 9.9 days. | 0.33 |
| 140 | \--solver-verbosity | A positive integer that specifies the \"chattiness\" of the non-linear solver. | 1 |
| 141 | \--strict-inner-iter-wells | A positive integer that specifies the number of inner well iterations with strict tolerance. | 40 |
| 142 | \--strict-outer-iter-wells | A positive integer that specifies the number of Newton iterations for which wells are checked with strict tolerance. | 6 |
| 143 | \--temperature-max | A real positive value that sets the maximum absolute temperature. | 1.0 x 10^9^ |
| 144 | \--temperature-min | A real positive value that sets the minimum absolute temperature. | 0 |
| 145 | \--threads-per-process | A positive integer value that stipulates the maximum number of threads to be instantiated per process (\'-1\' means \'automatic\'). | -1 |
| 146 | \--time-step-after-event-in-days | A real double precision value that sets the maximum allowed time step after an event; for example, when a well is open or closed etc.<br>The default value of -1 means that events to do effect the time stepping. | -1 |
| 147 | \--time-step-control | A defined character string that defines the time stepping control algorithm and is set to one of the following:<br>1)  pid: PID controller based adaptive time step control as suggested by Turek and Kuzmin[^35].<br>2)  pid+iteration: Use PID and linear iteration numbers to guide the time step.<br>3)  pid+newtoniteration: Use PID and non-linear iterations numbers to guide the time step.<br>4)  Hardcoded: Use time steps supplied by user via the time-step-control-filename parameter. | "pid+newtoniteration" |
| 148 | \--time-step-control-decay-damping-factor | A real positive value that specifies the decay rate a time step can be decreased by after the number target iterations has been exceeded | 1.0 |
| 149 | \--time-step-control-decay-rate | A real positive value that specifies the decay rate a time step size can be decreased by after the number of target iterations has been exceeded | 0.75 |
| 150 | \--time-step-control-file-name | A character string enclosed in quotes that specifies a filename where time steps are specified. The default is the character string timesteps.<br>For instance time steps can be generated by the ecl_summary application in libecl as per the following UNIX command line:<br>path_to_libecl_applications/ecl_summary DECK TIME \> filename<br>Where:<br>DECK is the name of the data deck you want to get the time steps from,<br>TIME tells the application to return the timing for the run, and<br>\"filename\" is the name of the file the times are piped to. | "timesteps" |
| 151 | \--time-step-control-growth-damping-factor | A real positive value that specifies the growth rate of the *time step *increase when the number of target iterations are undercut. | 3.2 |
| 152 | \--time-step-control-growth-rate | A real positive value that specifies the growth rate of the *time step size* when the number of target iterations are undercut. | 1.25 |
| 153 | \--time-step-control-target-iterations | A positive integer that defines the number of linear iterations which the time step control scheme should aim for (if applicable). | 30 |
| 154 | \--time-step-control-target-newton-iterations | A positive integer that specifies the number of Newton iterations which the time step control scheme should aim for (if applicable). | 8 |
| 155 | \--time-step-control-tolerance | A real double precision value that sets the tolerance for PID (only used with the pid and pid+ options defined by the \--time-step-control option). | 0.1 |
| 156 | \--time-step-verbosity | A positive integer that specifies the \"chattiness\" during the time integration. | 1 |
| 157 | \--tolerance-cnv | A real positive double precision value that specifies the maximum non-linear tolerance error. This is the local convergence tolerance (maximum of local saturation errors). | 0.01 |
| 158 | \--tolerance-cnv-relaxed | A real positive value that defines the relaxed local convergence tolerance that applies for iterations after the iterations with the strict tolerance. | 1.0 |
| 159 | \--tolerance-mb | A real positive double precision value that sets the maximum mass balance error, that is the tolerated mass balance error relative to total mass present. | 1.0 x 10^-6^ |
| 160 | \--tolerance-pressure-ms-wells | A real positive double precision value that specifies the tolerance for the pressure equations for multi-segment wells. | 1000 |
| 161 | \--tolerance-well-control | A real positive double precision value that sets the maximum tolerance for the well control equations. | 1.0 x 10^-7^ |
| 162 | \--tolerance-wells | A real positive double precision value that defines the maximum non-linear error for the well equations. | 1.0 x 10^-4^ |
| 163 | -update-equations-scaling | A boolean value that switches on (true) or off (false) the updating of the scaling factors for mass balance equations during the simulation. | false\ |
| 164 | \--use-average-density-ms-wells | A boolean value that specifies whether to approximate segment densitities by averaging over the segment and its outlet (true) or not (false). | false |
| 165 | \--use-gmres | A boolean value that when set to true OPM Flow will use Generalized Minimal Residual ("GMRES")[^36] and [^37] solver instead of Biconjugate Gradient Stabilized ("BiCGSTAB")[^38] and [^39] as the linear solver within the Newton iterations. | false |
| 166 | \--use-multisegment-well | A boolean value that when set to true the simulator will use the well model for multi-segment wells instead of the one for single-segment wells. | true |
| 167 | \--use-update-stabilization | A boolean value that switches on (true) or off (false) the stabilized Newton option, that attempts to detect and correct oscillations or stagnation during the Newton iterations.<br>This option may improve convergence for some cases. | true |
| 168 | \--water-only-threshold | A real positive value that defines the saturation threshold, for which cells with water saturations above or equal to this threshold are considered one-phase water only. | 1.0 |
| 169 | \--zoltan-imbalance-tol | A real positive value that defines the tolerable imbalance of the load balancing provided by Zoltan package. | 1.1 |
| 170 | \--zoltan-params | A character string that specifies the configuration of the Zoltan partitioner. Valid options are: graph, hypergraph or scotch. Alternatively, you can request a configuration to be read from a JSON file by giving the filename here, ending with \'.json.\' See https://sandialabs.github.io/Zoltan/ug_html/ug.html for available Zoltan options. | \"graph\" |
| Notes:<br>1)  Cells colored green in the No. column are new command line parameters for this release. Similarly for the Default column, cells colored green indicate the default value has changed from the previous release.<br>2)  Items shaded in gray are considered to be developer options that should be used with caution as the values associated with these command line parameters are subject to change.<br>3)  VTK Graphics Command Line Parameters[^40] set of commands are no longer listed via the basic help command line command:<br>flow \--help<br>instead use:<br>flow \--help-all<br>to get a list of supported command line Parameters.<br>3)  The \--enable-vtk-output option above, if set to "true" will write out the data as stipulated by the compile options. One may need to compile the source code to obtain the desired output.<br>4)  As per all UNIX and LINUX based system the input is case dependent.<br>5)  If a parameter file is used to set one of the above parameters, the leading "\--" should not be incorporated in the parameter file. |  |  |  |

*Table A.4: OPM Flow 2023-10 Command Line Options*
[^1]: Wallis, J. R., Little, T. E., and Nolen, J. S.: \"Constrained Residual Acceleration of Conjugate Residual Methods,\" paper SPE 13536 presented at the SPE Reservoir Simulation Symposium, Dallas, Texas, USA (February 10-13, 1985).

[^2]: R. Scheichl, M. Roland, J. Wendebourg, Decoupling and block preconditioning for sedimentary basin simulations, Computational Geosciences 7 (2003) 295{318.

[^3]: Klemetsdal, Ø.S., Møyner, O. & Lie, KA. Accelerating multiscale simulation of complex geomodels by use of dynamically adapted basis functions. Comput Geosci 24, 459--476 (2020). https://doi.org/10.1007/s10596-019-9827-z.

[^4]: M. Blatt, A parallel algebraic multigrid method for elliptic problems with highly discontinuous coefficients, Ph.D. thesis, Ruprecht-Karls-Universität Heidelberg (2010).

[^5]: Algebraic Flux Correction III. Incompressible Flow Problems. Uni Dortmund, Turek and Kuzmin, January, 2006 (DOI: 10.1007/3-540-27206-2_8)

[^6]: Y. Saad, A flexible inner-outer preconditioned GMRES algorithm, SIAM J. Sci. Statist. Comput.,14, (1993).

[^7]: Y. Saad and M.H. Schultz, GMRES: A generalized minimum residual algorithm for solving nonsymmetric linear systems, SIAM J. Sci. Statist. Comput., 7 (1986), pp. 856{869.

[^8]: Van der Vorst, H. A. (1992). \"Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems\". SIAM J. Sci. Stat. Comput. 13 (2): 631--644. doi:10.1137/0913035. hdl:10338.dmlcz/104566

[^9]: Sleijpen, G. L. G.; Fokkema, D. R. (November 1993). \"BiCGstab(l) for linear equations involving unsymmetric matrices with complex spectrum\" (PDF). Electronic Transactions on Numerical Analysis. Kent, OH: Kent State University. 1: 11--32. ISSN 1068-9613.

[^10]: Virtualization ToolKit ("VTK") files used to visualize the 3D results from the model using ParaView, an open-source, multi-platform general purpose data analysis and visualization application (<https://www.paraview.org/overview/>). For the commercial simulator's compatible output files OPM's ResInsight 3D visualization package can be used instead and is specifically tailored for OPM Flow and the commercial simulator.

[^11]: Wallis, J. R., Little, T. E., and Nolen, J. S.: \"Constrained Residual Acceleration of Conjugate Residual Methods,\" paper SPE 13536 presented at the SPE Reservoir Simulation Symposium, Dallas, Texas, USA (February 10-13, 1985).

[^12]: R. Scheichl, M. Roland, J. Wendebourg, Decoupling and block preconditioning for sedimentary basin simulations, Computational Geosciences 7 (2003) 295{318.

[^13]: Klemetsdal, Ø.S., Møyner, O. & Lie, KA. Accelerating multiscale simulation of complex geomodels by use of dynamically adapted basis functions. Comput Geosci 24, 459--476 (2020). https://doi.org/10.1007/s10596-019-9827-z.

[^14]: M. Blatt, A parallel algebraic multigrid method for elliptic problems with highly discontinuous coefficients, Ph.D. thesis, Ruprecht-Karls-Universität Heidelberg (2010).

[^15]: Algebraic Flux Correction III. Incompressible Flow Problems. Uni Dortmund, Turek and Kuzmin, January, 2006 (DOI: 10.1007/3-540-27206-2_8)

[^16]: Y. Saad, A flexible inner-outer preconditioned GMRES algorithm, SIAM J. Sci. Statist. Comput.,14, (1993).

[^17]: Y. Saad and M.H. Schultz, GMRES: A generalized minimum residual algorithm for solving nonsymmetric linear systems, SIAM J. Sci. Statist. Comput., 7 (1986), pp. 856{869.

[^18]: Van der Vorst, H. A. (1992). \"Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems\". SIAM J. Sci. Stat. Comput. 13 (2): 631--644. doi:10.1137/0913035. hdl:10338.dmlcz/104566

[^19]: Sleijpen, G. L. G.; Fokkema, D. R. (November 1993). \"BiCGstab(l) for linear equations involving unsymmetric matrices with complex spectrum\" (PDF). Electronic Transactions on Numerical Analysis. Kent, OH: Kent State University. 1: 11--32. ISSN 1068-9613.

[^20]: Virtualization ToolKit ("VTK") files used to visualize the 3D results from the model using ParaView, an open-source, multi-platform general purpose data analysis and visualization application (<https://www.paraview.org/overview/>). For the commercial simulator's compatible output files OPM's ResInsight 3D visualization package can be used instead and is specifically tailored for OPM Flow and the commercial simulator.

[^21]: Wallis, J. R., Little, T. E., and Nolen, J. S.: \"Constrained Residual Acceleration of Conjugate Residual Methods,\" paper SPE 13536 presented at the SPE Reservoir Simulation Symposium, Dallas, Texas, USA (February 10-13, 1985).

[^22]: R. Scheichl, M. Roland, J. Wendebourg, Decoupling and block preconditioning for sedimentary basin simulations, Computational Geosciences 7 (2003) 295{318.

[^23]: Klemetsdal, Ø.S., Møyner, O. & Lie, KA. Accelerating multiscale simulation of complex geomodels by use of dynamically adapted basis functions. Comput Geosci 24, 459--476 (2020). https://doi.org/10.1007/s10596-019-9827-z.

[^24]: M. Blatt, A parallel algebraic multigrid method for elliptic problems with highly discontinuous coefficients, Ph.D. thesis, Ruprecht-Karls-Universität Heidelberg (2010).

[^25]: Algebraic Flux Correction III. Incompressible Flow Problems. Uni Dortmund, Turek and Kuzmin, January, 2006 (DOI: 10.1007/3-540-27206-2_8)

[^26]: Y. Saad, A flexible inner-outer preconditioned GMRES algorithm, SIAM J. Sci. Statist. Comput.,14, (1993).

[^27]: Y. Saad and M.H. Schultz, GMRES: A generalized minimum residual algorithm for solving nonsymmetric linear systems, SIAM J. Sci. Statist. Comput., 7 (1986), pp. 856{869.

[^28]: Van der Vorst, H. A. (1992). \"Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems\". SIAM J. Sci. Stat. Comput. 13 (2): 631--644. doi:10.1137/0913035. hdl:10338.dmlcz/104566

[^29]: Sleijpen, G. L. G.; Fokkema, D. R. (November 1993). \"BiCGstab(l) for linear equations involving unsymmetric matrices with complex spectrum\" (PDF). Electronic Transactions on Numerical Analysis. Kent, OH: Kent State University. 1: 11--32. ISSN 1068-9613.

[^30]: Virtualization ToolKit ("VTK") files used to visualize the 3D results from the model using ParaView, an open-source, multi-platform general purpose data analysis and visualization application (<https://www.paraview.org/overview/>). For the commercial simulator's compatible output files OPM's ResInsight 3D visualization package can be used instead and is specifically tailored for OPM Flow and the commercial simulator.

[^31]: Wallis, J. R., Little, T. E., and Nolen, J. S.: \"Constrained Residual Acceleration of Conjugate Residual Methods,\" paper SPE 13536 presented at the SPE Reservoir Simulation Symposium, Dallas, Texas, USA (February 10-13, 1985).

[^32]: R. Scheichl, M. Roland, J. Wendebourg, Decoupling and block preconditioning for sedimentary basin simulations, Computational Geosciences 7 (2003) 295{318.

[^33]: Klemetsdal, Ø.S., Møyner, O. & Lie, KA. Accelerating multiscale simulation of complex geomodels by use of dynamically adapted basis functions. Comput Geosci 24, 459--476 (2020). https://doi.org/10.1007/s10596-019-9827-z.

[^34]: M. Blatt, A parallel algebraic multigrid method for elliptic problems with highly discontinuous coefficients, Ph.D. thesis, Ruprecht-Karls-Universität Heidelberg (2010).

[^35]: Algebraic Flux Correction III. Incompressible Flow Problems. Uni Dortmund, Turek and Kuzmin, January, 2006 (DOI: 10.1007/3-540-27206-2_8)

[^36]: Y. Saad, A flexible inner-outer preconditioned GMRES algorithm, SIAM J. Sci. Statist. Comput.,14, (1993).

[^37]: Y. Saad and M.H. Schultz, GMRES: A generalized minimum residual algorithm for solving nonsymmetric linear systems, SIAM J. Sci. Statist. Comput., 7 (1986), pp. 856{869.

[^38]: Van der Vorst, H. A. (1992). \"Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG for the Solution of Nonsymmetric Linear Systems\". SIAM J. Sci. Stat. Comput. 13 (2): 631--644. doi:10.1137/0913035. hdl:10338.dmlcz/104566

[^39]: Sleijpen, G. L. G.; Fokkema, D. R. (November 1993). \"BiCGstab(l) for linear equations involving unsymmetric matrices with complex spectrum\" (PDF). Electronic Transactions on Numerical Analysis. Kent, OH: Kent State University. 1: 11--32. ISSN 1068-9613.

[^40]: Virtualization ToolKit ("VTK") files used to visualize the 3D results from the model using ParaView, an open-source, multi-platform general purpose data analysis and visualization application (<https://www.paraview.org/overview/>). For the commercial simulator's compatible output files OPM's ResInsight 3D visualization package can be used instead and is specifically tailored for OPM Flow and the commercial simulator.

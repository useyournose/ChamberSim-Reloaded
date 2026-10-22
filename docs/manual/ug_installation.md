# Installation and first start

## Installation

Release builds are available from the project’s [GitHub release page](https://github.com/Schildkroet/ChamberSim-Reloaded/releases/latest) as Assets.

- `ChamberSimReloaded-*.x86_64.AppImage` for Linux, you need to make executable
- `ChamberSimReloaded-*.x86_64.zip` for Windows, you just need to extract into a folder

No installation is required. Both come with the manual (**Help** → **User manual F1**).
The Windows archive also contains the Visual C++ runtime, so nothing else has to be installed.

Windows settings will be stored in the Registry `HKEY_LOCAL_MACHINE/Software/ChamberSimReloaded` and `%AppData%\ChamberSimReloaded`.

## Build from sources

To build the ChamberSim-Reloaded yourself

- Qt 6.4 or newer
- CMake 3.16 or newer and
- a C++ 20 compiler

is needed.

Run `tools/build.sh release` and find the binaries in `build/release/ChamberSimReloaded`.

## Safety notice

At every start a safety notice is shown.

Read it.  
Choose "I understand" to continue.  
Check "Do not show this again" and "I understand" will supress the notice for later starts.  
Quit closes the program.


## Command-line options

```
ChamberSimReloaded [options] [load.csrload ...]
    -d, --database <file> the original's (plain) database
    -r, --reference <f>   overlay a reference result (JSON) on the chart
    --calibration <m>     solver model: original|published|physical
    --language <code>     de_DE, en_US, fr_FR, it_IT
    --theme <t>           light | dark
    --units <system>      metric | imperial | original
    --log-level <level>   debug | info | warning | error
    --help                all options
```

Files given on the command line are opened as loads.  
- `--theme` applies to this run only, while `--units` and `--calibration` are saved in the settings.
- `--screenshot` saves an image of the window and exits. Check `--help` to read more about `--tab`, `--input-tab` and`--result-tab`, supported by this option.

## Simulating without the window

The program `csr_sim` runs simulations without a graphical interface,
for scripts and batch jobs. It reads `.csrload` and `.grtload` files and
prints one row per load and ladder step.

``` csr_sim --help
Usage: csr_sim.exe [options] load...
Simulates loads without a GUI. Units: g, mm, bar, m/s, J, ms. Exit code 0 = all ok, 1 = a simulation failed, 2 = usage or read error.

Options:
  -?, -h, --help      Displays help on commandline options.
  --help-all          Displays help including Qt specific options.
  --profile <name>    model: original, published or physical (default)
  --grt-original      use the Original model for .grtload files (like the
                      setting in the program)
  --charge <g>        override the charge of the load (g)
  --ladder-count <n>  override the number of ladder steps
  --ladder-step <g>   override the charge difference of the ladder (g)
  --format <fmt>      output: table (default), csv or json
  --out <file>        write the results to this file instead of stdout
  --curve <file>      write the pressure/velocity curve (CSV) of the focused
                      ladder step; {name} is replaced by the load's base name
  --steps <n>         position steps of the solver (default 2000)

Arguments:
  load                load file(s): .csrload or .grtload
```

The program’s project data (physical burn values of the powders and the
factors of the pistol and revolver calibers) are built in, so the
results equal those of the program.

Each row holds the charge, maximum and muzzle pressure, muzzle velocity,
energy and time, burnt fraction, efficiency, burnout in the barrel, load
ratio and the status.

Units are *g*, *mm*, *bar*, *m/s*, *J* and *ms*.

The exit code is `0` when all simulations succeeded, `1` when at least one
failed (for example because the charge does not fit into the case) and `2`
for a usage or file error.

# The database

The "Database" tab lists the Calibers, Projectiles and Propellants available for loads.  
The filter field searches all columns.  
You can click a column header to sort.

<figure id="fig:database" data-latex-placement="ht">
<img src="images/database.png" />
<figcaption>The Database tab.</figcaption>
</figure>

## Where the records come from

ChamberSim-Reloaded supports three different data sources, which are shown in the "Source" column:

1. **Project** - calibers, projectiles and propellants that come with ChamberSim-Reloaded.

2. **Personal** -  Your own records, stored in the file `ChamberSimReloaded.db`. in
    the application data folder. Everything you create or copy is stored
    here.

3. **Original GRT** - Optionally you can import the records of *Gordon’s Reloading Tool*.
    The import process is described in the next chapter.

## Using the original’s database

Gordon’s Reloading Tool (GRT) keeps its calibers, projectiles and propellants
in an encrypted SQLite database `GordonsReloadingTool.db`. You need your own
installation of GRT as ChamberSim-Reloaded does not contain a copy. A helper
script makes a *plain* (unencrypted) *copy*. The original program and its
database stay unchanged. Only the copy is created.

### How it works

The script creates a copy of the original program files and starts that copy.
As soon as GRT has unlocked its database, the script asks it to remove the
encryption from that copy. Nothing is compiled and no key required.

### Linux

The following steps works on Debian, Ubuntu, Mint, Fedora,
Arch, Manjaro and openSUSE.

1. Unpack the *Linux* version of GRT into a folder
2. Copy the file `./tools/grt_decrypt_db.sh` from the ChamberSim-Reloaded
   Github repository into the same folder
3. Open a terminal in that folder and run `./grt_decrypt_db.sh`
4. The script checks the dependencies and, after user approval, installs missing
   requirements using `sudo`. Dependencies are

   - the debugger `gdb`
   - the 32-bit `GTK 2` runtime required by GRT
   - a virtual display, in headless setups

   and the runs GRT.
5. After a few seconds the file `GordonsReloadingTool.plain.db` will be created
    in the same folder.

CLI Options:

- `-o FILE` (name of the output file)
- `-y` (install without asking)
- `-c` (only report what is found and missing, change nothing),
- `--headless` (use a virtual display, no window appears)
- `-t SECONDS` (timeout, default 90) and
- `-h` (help).

### Windows

1. Unpack the *Windows* version of GRT into a folder
1. Copy the files `tools/grt_decrypt_db.cmd` and `tools/grt_decrypt_db.ps1`
   from the ChamberSim-Reloaded Github repository into the same folder
   (next to `GordonsReloadingTool.exe`).
1. Double-click `grt_decrypt_db.cmd`. After user approval, Python
   (with `winget`) and the Python package `frida` is installed into a virtual
   environment under `%LOCALAPPDATA%\ChamberSimReloaded\`.
1. After the process, `GordonsReloadingTool.plain.db` is in the same
   folder.

PowerShell CLI options:

- `-Out FILE`
- `-Yes`
- `-Check` (report only) and
- `-Timeout SECONDS`.

### Using the copy

Open **File** → **Settings** → **Database**, choose
`GordonsReloadingTool.plain.db` as the original database. The status
line at the bottom then shows the file name and the number of calibers,
projectiles and propellants, and the records appear in the Database tab
with the source **Original GRT**. They are read-only. To change one, create a
copy. Alternatively start ChamberSim-Reloaded with the Command Line Parameter
`-d GordonsReloadingTool.plain.db`.

> [!NOTE]
> Do not distribute the plain copy. It is for your own use with your own
> copy of Gordon’s Reloading Tool. If the original program is updated,
> create a new copy.

## Working with records

Depending on the record type, you can use the following actions:

- **New…**: adds a new record. Fill in the fields; labels show the unit of each
field.
- **Copy…**: adds a changed copy of the selected record. A double click on a record
shows it and offers the same.
- **Edit…**: changes the selected record.
- **Delete**: removes the selected record. Load files, using that record data, are not affected.
- **Export…**: saves the record as a file, to contribute it to the project’s database.
- **Import bullets**: (Projectiles only) adds the bullets of a manufacturer's bullet file
  (`.csrbullets`, or a plain `.json` file) to your own records after
  asking for confirmation. The format is specified in `docs/BULLET_FILE.md`.

Only **Personal** records can be edited or deleted. To change a record, marked as **Project** or
**Original GRT**, create a copy.

Double-clicking a record opens the details view.

Propellants allow you to attach an overview photo and a detail photo
(**Choose file…** and fill the scale in px/mm when possible ) in the detail view.

The **Projectiles** view has a **Validated** column.

- A green check mark means that the bullet length was measured on the bullet or checked
against the original's database.
- a red cross means it has not been validated by hand, as the length may be taken from the manufacturer's data or be an estimate.
  You'll find details on the record's details view.

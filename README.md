# pyMIBiG

A small tool to download, match and save target sequences from [MIBiG](https://mibig.secondarymetabolites.org/).

## Usage

Download the available package of `pyMIBiG` and execute `./pymibig <target>` where target is the term you wanto to search in MIBiG database.

By default `pyMIBiG` will fetch sequences with complete cluster data and complete information.

You may change that using optional aguments passed after the `<target>`:

```{bash}
usage: pymibig [-h] [-c {complete,incomplete,Unknown}] [-m] target

positional arguments:
  target                Search term to query in database

options:
  -h, --help            show this help message and exit
  -c {complete,incomplete,Unknown}, --completeness {complete,incomplete,Unknown}
                        Loci completeness.
  -m, --minimal         Minimal annotation.
```

## License

`pyMiBiG` is distributed under the terms of the [LGPL 3.0](https://spdx.org/licenses/LGPL-3.0-or-later.html) license.

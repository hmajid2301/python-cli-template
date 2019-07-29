# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2019-07-29
### Changed
- Main folder now uses `package_name` and src folder uses `module_name`.

## [0.3.2] - 2019-07-29
### Fixed
- Some cookiecutter variables were still using `project_title` instead of `project_name`.

## [0.3.1] - 2019-07-29
### Changed
- `project_title` is not `project_name` to be more consistent with other names.

### Fixed
- `module_name` was using `project_name` instead of `package_name`.

## [0.3.0] - 2019-07-29
### Changed
- `package_name` is now `module_name` as it's more obvious what it is.
- `project_name` is not `package_name`.

## [0.2.2] - 2019-07-24
### Changed
- `code-formatter` to include `{posargs}` so we can use it to format our code, and also to check it in the same target.

### Removed
- `code-formatter-check` target in tox.

## [0.2.1] - 2019-07-23
### Added
- `project_title` which contains the full title with spaces (if required).

### Changed
- `package_name` to `project_name`, so project_name has `-` and package_name has `_`.

### Removed
- `module_name` replaced by `package_name`


## [0.2.0] - 2019-07-23
### Fixed
- Missing version in setup.cfg, was hard coded to 0.5.2.

### Removed
- Pipfile, will not be using pipenv.

## [0.1.2] - 2019-07-23
### Fixed
- Using `package_name` instead of `module_name` in `setup.py`.

## [0.1.1] - 2019-07-23
### Changed
- README.rst to include sections.

## [0.1.0] - 2019-07-23
### Added
- Initial Release. 

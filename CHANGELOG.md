# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2020-02-29
### Added
- Post generation hook which creates git commit and virtualenv.
- `dev-requirements.txt` which contains the dev requirements.
- `isort` to sort our imports for us.
- `:dev` to install virtualenv for us using tox.

### Changed
- Python versions now available are `3.6`, `3.7` and `3.8`.

### Fixed
- Updated `.gitlab-ci.yml` in wrong place in last update, updated correct CI file now.

### Removed
- All packages from `requirements.txt`, this should be all pinned packages within the cli tools itself.
- Unnecessary steps in `README.md`, this will down to specific library itself.
- Folder with name `{{cookiecutter.project_name}}`.

### Removed
- Variables from `.gitlab-ci.yml` file, use predefined variables in Gitlab CI.

## [0.4.1] - 2020-02-23
### Removed
- Variables from `.gitlab-ci.yml` file, use predefined variables in Gitlab CI.

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

[0.5.0]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.4.1...release%2F0.5.0
[0.4.1]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.4.0...release%2F0.4.1
[0.4.0]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.3.2...release%2F0.4.0
[0.3.2]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.3.1...release%2F0.3.2
[0.3.1]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.3.0...release%2F0.3.1
[0.3.0]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.2.2...release%2F0.3.0
[0.2.2]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.2.1...release%2F0.2.2
[0.2.1]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.2.0...release%2F0.2.1
[0.2.0]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.1.2...release%2F0.2.0
[0.1.2]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.1.1...release%2F0.1.2
[0.1.1]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/compare/release%2F0.1.0...release%2F0.1.1
[0.1.0]: https://gitlab.com/hmajid2301/python-cli-cookiecutter/-/tags/release%2F0.1.0
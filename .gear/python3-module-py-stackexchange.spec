%define _unpackaged_files_terminate_build 1
%define pypi_name py-stackexchange
%define short_name stackexchange

%def_with check

Name:    python3-module-%pypi_name
Version: 2.2.7
Release: alt1

Summary: Stack overflow command line interface
License: BSD-3-Clause
Group:   Other
URL:     https://pypi.org/project/%pypi_name
VCS:     https://github.com/lucjon/Py-StackExchange.git

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_without check
%pyproject_builddeps_metadata
# %pyproject_builddeps_metadata_extra testsuite.py
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source:  %name-%version.tar
Source1: %pyproject_deps_config_name

%description
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

%package tests
Summary: Tests for %name
Group: Development/Python3
Requires: %name = %EVR

%description tests
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

This package contains tests for %pypi_name.

%package demo
Summary: Demo for %name
Group: Development/Python3
Requires: %name = %EVR

%description demo
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

This package contains demo for %pypi_name.


%prep
%setup -n %name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# %tox_create_default_config
# %tox_check_pyproject
# echo "rlnbesiorng\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
# %pyproject_run_pytest -vra %buildroot/testsuite.py
# echo "rlnbesiorng\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

%files
%doc *.md
%python3_sitelibdir/%short_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/stackauth.py
%exclude %python3_sitelibdir/__pycache__/*
%exclude %python3_sitelibdir/testsuite.py

%changelog
* Mon Apr 22 2024 Yuri Kozyrev <kozyrevid@altlinux.org> 2.2.7-alt1
- initial build
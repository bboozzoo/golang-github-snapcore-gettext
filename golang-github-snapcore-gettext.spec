# Generated by go2rpm 1
%bcond_without check

# https://github.com/snapcore/go-gettext
%global goipath         github.com/snapcore/go-gettext
%global commit          a77afd68d2bd1740e0d843e28cc756ee59493e24

%gometa

%global common_description %{expand:
A native Go library for accessing gettext internationalization files.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Native Go library for accessing gettext internationalization files
# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Aug 23 07:33:12 UTC 2019 Maciek Borzecki <maciek.borzecki@gmail.com> - 0-0.1.20190823gita77afd6
- Initial package


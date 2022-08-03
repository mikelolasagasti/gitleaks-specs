# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/zricethezav/gitleaks
%global forgeurl        https://github.com/zricethezav/gitleaks
%global goipath         github.com/zricethezav/gitleaks/v8
Version:                8.9.0

%gometa

%global common_description %{expand:
Scan git repos (or files) for secrets using regex and entropy}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           gitleaks
Release:        %autorelease
Summary:        Scan git repos (or files) for secrets using regex and entropy

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  git-core

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/gitleaks %{goipath}
%{gobuilddir}/bin/%{name} completion bash > %{name}.bash
%{gobuilddir}/bin/%{name} completion fish > %{name}.fish
%{gobuilddir}/bin/%{name} completion zsh  > %{name}.zsh


%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dp %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dp %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}


%gopkgfiles

%changelog
%autochangelog

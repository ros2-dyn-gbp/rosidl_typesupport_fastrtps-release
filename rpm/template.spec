%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rosidl-typesupport-fastrtps-cpp
Version:        2.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosidl_typesupport_fastrtps_cpp package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-devel
Requires:       ros-humble-ament-cmake-ros
Requires:       ros-humble-ament-index-python
Requires:       ros-humble-fastcdr
Requires:       ros-humble-fastrtps-cmake-module
Requires:       ros-humble-rmw
Requires:       ros-humble-rosidl-cli
Requires:       ros-humble-rosidl-cmake
Requires:       ros-humble-rosidl-generator-cpp
Requires:       ros-humble-rosidl-runtime-c
Requires:       ros-humble-rosidl-runtime-cpp
Requires:       ros-humble-rosidl-typesupport-interface
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-cmake-python
BuildRequires:  ros-humble-ament-index-python
BuildRequires:  ros-humble-fastcdr
BuildRequires:  ros-humble-fastrtps-cmake-module
BuildRequires:  ros-humble-rmw
BuildRequires:  ros-humble-rosidl-cli
BuildRequires:  ros-humble-rosidl-cmake
BuildRequires:  ros-humble-rosidl-runtime-c
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rosidl-typesupport-cpp-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-cmake-pytest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
BuildRequires:  ros-humble-osrf-testing-tools-cpp
BuildRequires:  ros-humble-performance-test-fixture
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rosidl-typesupport-cpp-packages(all)
%endif

%description
Generate the C++ interfaces for eProsima FastRTPS.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Jul 18 2023 Shane Loretz <shane@openrobotics.org> - 2.2.1-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Shane Loretz <shane@openrobotics.org> - 2.2.0-2
- Autogenerated by Bloom

* Wed Mar 30 2022 Shane Loretz <shane@openrobotics.org> - 2.2.0-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Shane Loretz <shane@openrobotics.org> - 2.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Shane Loretz <shane@openrobotics.org> - 2.0.4-2
- Autogenerated by Bloom


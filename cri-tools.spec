#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cri-tools
Version  : 1.18.0
Release  : 18
URL      : https://github.com/kubernetes-sigs/cri-tools/archive/v1.18.0.tar.gz
Source0  : https://github.com/kubernetes-sigs/cri-tools/archive/v1.18.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT
Requires: cri-tools-bin = %{version}-%{release}
Requires: cri-tools-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-main_unix-Define-crio.sock-as-default-socket.patch
Patch2: 0002-Enable-static-pie-linkage-for-binaries.patch

%description
This is a work-in-progress HTTP/2 implementation for Go.
It will eventually live in the Go standard library and won't require
any changes to your code to use.  It will just be automatic.

%package bin
Summary: bin components for the cri-tools package.
Group: Binaries
Requires: cri-tools-license = %{version}-%{release}

%description bin
bin components for the cri-tools package.


%package license
Summary: license components for the cri-tools package.
Group: Default

%description license
license components for the cri-tools package.


%prep
%setup -q -n cri-tools-1.18.0
cd %{_builddir}/cri-tools-1.18.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595439982
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  V=1 VERSION=%{version}


%install
export SOURCE_DATE_EPOCH=1595439982
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cri-tools
cp %{_builddir}/cri-tools-1.18.0/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/hack/repo-infra/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/836ef1b46953afdb78ce3929bc6831ca83620b65
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/c700a8b9312d24bdc57570f7d6a131cf63d89016
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/20b06a68cf65738d43afa04acce0126f341c77f8
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/5476f2f91673ef040f1956907e7f45e72d5e11ee
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/c6821d75aac4a65fae7d56a425e304beb3689c26
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/cri-tools/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/271aeaf56ee621c5accfc2a9db0b10717e038eaf
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/golang/glog/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/hpcloud/tail/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/a792f3e236631b46c9ea1a9f86ab3a6c24b17c89
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/hpcloud/tail/ratelimiter/Licence %{buildroot}/usr/share/package-licenses/cri-tools/15e225f105ead05a4d06cdf7723bb6ec11e92304
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/d676a57141ac47c27699fc8b03e1a2e59abb96ef
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/onsi/ginkgo/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/onsi/gomega/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/package-licenses/cri-tools/76a37a42a06aa6e231383fb93d9161f074d5962b
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/cri-tools/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/pborman/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/cri-tools-1.18.0/vendor/github.com/urfave/cli/v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/cri-tools-1.18.0/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/fsnotify.v1/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/tomb.v1/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/178b27feb961b28990b377da59e9d43d868a0a6f
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/cri-tools/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/cri-tools-1.18.0/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/component-base/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/klog/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/kubectl/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cri-tools-1.18.0/vendor/sigs.k8s.io/structured-merge-diff/v3/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/cri-tools-1.18.0/vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/271aeaf56ee621c5accfc2a9db0b10717e038eaf
%make_install BINDIR=%{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/crictl
/usr/bin/critest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cri-tools/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/cri-tools/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/cri-tools/15e225f105ead05a4d06cdf7723bb6ec11e92304
/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/cri-tools/178b27feb961b28990b377da59e9d43d868a0a6f
/usr/share/package-licenses/cri-tools/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/cri-tools/271aeaf56ee621c5accfc2a9db0b10717e038eaf
/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/cri-tools/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/cri-tools/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/cri-tools/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/cri-tools/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/cri-tools/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/cri-tools/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
/usr/share/package-licenses/cri-tools/76a37a42a06aa6e231383fb93d9161f074d5962b
/usr/share/package-licenses/cri-tools/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/cri-tools/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/cri-tools/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/cri-tools/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/cri-tools/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/cri-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
/usr/share/package-licenses/cri-tools/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/cri-tools/a792f3e236631b46c9ea1a9f86ab3a6c24b17c89
/usr/share/package-licenses/cri-tools/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/cri-tools/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/cri-tools/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/cri-tools/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/cri-tools/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/cri-tools/c6821d75aac4a65fae7d56a425e304beb3689c26
/usr/share/package-licenses/cri-tools/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/cri-tools/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/cri-tools/d676a57141ac47c27699fc8b03e1a2e59abb96ef
/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/cri-tools/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/cri-tools/e2ee43b586677eaafd7dd7af25adff48adfa7cf3

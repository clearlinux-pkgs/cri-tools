#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : cri-tools
Version  : 1.27.1
Release  : 64
URL      : https://github.com/kubernetes-sigs/cri-tools/archive/v1.27.1/cri-tools-1.27.1.tar.gz
Source0  : https://github.com/kubernetes-sigs/cri-tools/archive/v1.27.1/cri-tools-1.27.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT
Requires: cri-tools-bin = %{version}-%{release}
Requires: cri-tools-license = %{version}-%{release}
BuildRequires : go
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# cri-tools
CLI and validation tools for Kubelet Container Runtime Interface (CRI) .

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
%setup -q -n cri-tools-1.27.1
cd %{_builddir}/cri-tools-1.27.1
pushd ..
cp -a cri-tools-1.27.1 buildavx2
popd

%build
## build_prepend content
unset CLEAR_DEBUG_TERSE
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689087030
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  V=1 VERSION=%{version}

pushd ../buildavx2
## build_prepend content
unset CLEAR_DEBUG_TERSE
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}  V=1 VERSION=%{version}
popd

%install
export SOURCE_DATE_EPOCH=1689087030
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cri-tools
cp %{_builddir}/cri-tools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/836ef1b46953afdb78ce3929bc6831ca83620b65 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/b2e4520feb0f9b51ad373256b94c3faf4c1e6871 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/blang/semver/v4/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/16e22f58039363cff486afeac52bde18cd4ab5b3 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/cenkalti/backoff/v4/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/101c182fa18fd56a09164278f17e4282264c5e9e || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/7be82c1a81e7197640a88df91dc82d64b77c7acd || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/b7a606730713ac061594edab33cf941704b4a95c || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/cyphar/filepath-securejoin/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/8fb92f475d78da1315877a719c6856fc64531d30 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d2f340a01dd48b589a70f627cf7058c585a315e4 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/c700a8b9312d24bdc57570f7d6a131cf63d89016 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/20b06a68cf65738d43afa04acce0126f341c77f8 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/5476f2f91673ef040f1956907e7f45e72d5e11ee || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/3110e55750143a84918d7423febc9c83a55bc28c || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/emicklei/go-restful/v3/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/felixge/httpsnoop/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/d3d30f733d36ea721eb89e9c37f899f729a0ea5e || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/135191231608cd88684768718b8a2f439c9e1817 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-logr/logr/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-logr/stdr/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-openapi/jsonpointer/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-openapi/jsonreference/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-openapi/swag/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/go-task/slim-sprig/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/535e3badf5b532d842627b504976fbb93bc2d8b8 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/06b27345acae9303e13dde9974d2b2e318b05989 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/golang/glog/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/aa9b240f558caed367795f667629ccbca28f20b2 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/google/gnostic/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/5a7d7df655ba40478fae80a6abafc6afc36f9b6a || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7080652cc78cd9855d39e324529a3b5f3745dcd6 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/google/pprof/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/grpc-ecosystem/grpc-gateway/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/c2add16c875ec7abad9c453d0a0c325dc814e8f2 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/josharian/intern/license.md %{buildroot}/usr/share/package-licenses/cri-tools/8b31eebf3b5472b746a3a34142877b3bb6bd8e68 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/810612ee8c1872b7ee4dba34c090ebd8f7491aa1 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/mailru/easyjson/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/d676a57141ac47c27699fc8b03e1a2e59abb96ef || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/moby/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/moby/term/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/20b06a68cf65738d43afa04acce0126f341c77f8 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/munnerz/goautoneg/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/3486abfdd66d1bd30f9edeeb779a7f04d043d457 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/onsi/ginkgo/v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/onsi/gomega/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/93ac97c9679b68518f1fd7de627ce2f77f44082d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/cri-tools/979fd7d5c67073b265d96f584aac3de1c419b8e2 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/8ff574408142cd6bbb2a1b83302de24cb7b35e8b || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/pborman/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/fd6460234f122a19f21affb6d6885269340b9176 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/da34754c05d40ff81f91de8c1b85ea6e5503e21d || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/a1c7852c717fed2c9a0284ed112ea66013230da6 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/b3c86ae465b21f7323059db335158b48187731c7 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/urfave/cli/v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/0ff5762fb1296d6a75b95d4f4d62f48248a494b3 || :
cp %{_builddir}/cri-tools-%{version}/vendor/github.com/xrash/smetrics/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/1970a503235b08e0bc9f922144970d0de225ab9f || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/internal/retry/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/otlptrace/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/metric/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/sdk/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/otel/trace/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/go.opentelemetry.io/proto/otlp/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/term/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/golang.org/x/tools/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/74850a25a5319bdddc0d998eb8926c18bada282b || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/cri-tools/ad00ce7340d89dc13ccc59920ef75cb55af5b164 || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785 || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/b74b3b31bc15ad5e94fc1947d682aa3d84132fce || :
cp %{_builddir}/cri-tools-%{version}/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/apimachinery/third_party/forked/golang/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/component-base/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/klog/v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kube-openapi/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kube-openapi/pkg/internal/third_party/go-json-experiment/json/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/6c1c86ffff267e1d7d8f03dca1c41492e62f265b || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kube-openapi/pkg/validation/spec/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kube-openapi/pkg/validation/spec/license.go %{buildroot}/usr/share/package-licenses/cri-tools/555e9ac61d94352b3c2935e77b51fc6dc31d4822 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kubectl/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/cri-tools-%{version}/vendor/k8s.io/utils/internal/third_party/forked/golang/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b || :
cp %{_builddir}/cri-tools-%{version}/vendor/sigs.k8s.io/json/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/1fec85ad53bebf4bffc9cf02a7dfcfa56ad6b94d || :
cp %{_builddir}/cri-tools-%{version}/vendor/sigs.k8s.io/structured-merge-diff/v4/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/cri-tools-%{version}/vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/271aeaf56ee621c5accfc2a9db0b10717e038eaf || :
pushd ../buildavx2/
%make_install_v3 BINDIR=/usr/bin
popd
%make_install BINDIR=/usr/bin
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/crictl
/V3/usr/bin/critest
/usr/bin/crictl
/usr/bin/critest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cri-tools/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/cri-tools/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/cri-tools/0ff5762fb1296d6a75b95d4f4d62f48248a494b3
/usr/share/package-licenses/cri-tools/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/cri-tools/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/cri-tools/135191231608cd88684768718b8a2f439c9e1817
/usr/share/package-licenses/cri-tools/16e22f58039363cff486afeac52bde18cd4ab5b3
/usr/share/package-licenses/cri-tools/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/cri-tools/1970a503235b08e0bc9f922144970d0de225ab9f
/usr/share/package-licenses/cri-tools/1fec85ad53bebf4bffc9cf02a7dfcfa56ad6b94d
/usr/share/package-licenses/cri-tools/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/cri-tools/271aeaf56ee621c5accfc2a9db0b10717e038eaf
/usr/share/package-licenses/cri-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/cri-tools/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/cri-tools/3486abfdd66d1bd30f9edeeb779a7f04d043d457
/usr/share/package-licenses/cri-tools/535e3badf5b532d842627b504976fbb93bc2d8b8
/usr/share/package-licenses/cri-tools/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/cri-tools/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51
/usr/share/package-licenses/cri-tools/555e9ac61d94352b3c2935e77b51fc6dc31d4822
/usr/share/package-licenses/cri-tools/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/cri-tools/5a7d7df655ba40478fae80a6abafc6afc36f9b6a
/usr/share/package-licenses/cri-tools/6c1c86ffff267e1d7d8f03dca1c41492e62f265b
/usr/share/package-licenses/cri-tools/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/cri-tools/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/cri-tools/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/cri-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/cri-tools/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/cri-tools/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/cri-tools/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/cri-tools/8b31eebf3b5472b746a3a34142877b3bb6bd8e68
/usr/share/package-licenses/cri-tools/8fb92f475d78da1315877a719c6856fc64531d30
/usr/share/package-licenses/cri-tools/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/cri-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/cri-tools/93ac97c9679b68518f1fd7de627ce2f77f44082d
/usr/share/package-licenses/cri-tools/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/cri-tools/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/cri-tools/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/cri-tools/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
/usr/share/package-licenses/cri-tools/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/cri-tools/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
/usr/share/package-licenses/cri-tools/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/cri-tools/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/cri-tools/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/cri-tools/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/cri-tools/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/cri-tools/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/cri-tools/c2add16c875ec7abad9c453d0a0c325dc814e8f2
/usr/share/package-licenses/cri-tools/c700a8b9312d24bdc57570f7d6a131cf63d89016
/usr/share/package-licenses/cri-tools/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/cri-tools/d3d30f733d36ea721eb89e9c37f899f729a0ea5e
/usr/share/package-licenses/cri-tools/d676a57141ac47c27699fc8b03e1a2e59abb96ef
/usr/share/package-licenses/cri-tools/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/cri-tools/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/cri-tools/fd6460234f122a19f21affb6d6885269340b9176

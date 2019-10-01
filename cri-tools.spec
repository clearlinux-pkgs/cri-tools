#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cri-tools
Version  : 1.16.1
Release  : 12
URL      : https://github.com/kubernetes-sigs/cri-tools/archive/v1.16.1/cri-tools-1.16.1.tar.gz
Source0  : https://github.com/kubernetes-sigs/cri-tools/archive/v1.16.1/cri-tools-1.16.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 GPL-3.0 ISC MIT MPL-2.0
Requires: cri-tools-bin = %{version}-%{release}
Requires: cri-tools-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0002-Define-crio.sock-as-default-socket.patch

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
%setup -q -n cri-tools-1.16.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1569898983
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1569898983
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cri-tools
cp LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/LICENSE
cp hack/repo-infra/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/hack_repo-infra_LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_Microsoft_go-winio_LICENSE
cp vendor/github.com/OpenPeeDeeP/depguard/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_OpenPeeDeeP_depguard_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_docker_distribution_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_docker_go-units_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_docker_spdystream_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_docker_spdystream_LICENSE.docs
cp vendor/github.com/fatih/color/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_fatih_color_LICENSE.md
cp vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_fsnotify_fsnotify_LICENSE
cp vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_ghodss_yaml_LICENSE
cp vendor/github.com/go-critic/go-critic/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-critic_go-critic_LICENSE
cp vendor/github.com/go-lintpack/lintpack/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-lintpack_lintpack_LICENSE
cp vendor/github.com/go-toolsmith/astcast/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astcast_LICENSE
cp vendor/github.com/go-toolsmith/astcopy/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astcopy_LICENSE
cp vendor/github.com/go-toolsmith/astequal/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astequal_LICENSE
cp vendor/github.com/go-toolsmith/astfmt/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astfmt_LICENSE
cp vendor/github.com/go-toolsmith/astp/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astp_LICENSE
cp vendor/github.com/go-toolsmith/strparse/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_strparse_LICENSE
cp vendor/github.com/go-toolsmith/typep/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_typep_LICENSE
cp vendor/github.com/gobwas/glob/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_gobwas_glob_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/glog/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golang_glog_LICENSE
cp vendor/github.com/golang/mock/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golang_mock_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/golangci/check/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_check_LICENSE
cp vendor/github.com/golangci/dupl/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_dupl_LICENSE
cp vendor/github.com/golangci/errcheck/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_errcheck_LICENSE
cp vendor/github.com/golangci/go-misc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-misc_LICENSE
cp vendor/github.com/golangci/go-tools/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_LICENSE
cp vendor/github.com/golangci/go-tools/lint/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_lint_LICENSE
cp vendor/github.com/golangci/go-tools/ssa/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_ssa_LICENSE
cp vendor/github.com/golangci/goconst/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_goconst_LICENSE
cp vendor/github.com/golangci/gocyclo/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gocyclo_LICENSE
cp vendor/github.com/golangci/gofmt/gofmt/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gofmt_gofmt_LICENSE
cp vendor/github.com/golangci/gofmt/goimports/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gofmt_goimports_LICENSE
cp vendor/github.com/golangci/golangci-lint/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_golangci-lint_LICENSE
cp vendor/github.com/golangci/gosec/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gosec_LICENSE.txt
cp vendor/github.com/golangci/ineffassign/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_ineffassign_LICENSE
cp vendor/github.com/golangci/lint-1/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_lint-1_LICENSE
cp vendor/github.com/golangci/maligned/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_maligned_LICENSE
cp vendor/github.com/golangci/misspell/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_misspell_LICENSE
cp vendor/github.com/golangci/prealloc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_prealloc_LICENSE
cp vendor/github.com/golangci/revgrep/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_revgrep_LICENSE
cp vendor/github.com/golangci/unconvert/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_unconvert_LICENSE
cp vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_google_gofuzz_LICENSE
cp vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_google_uuid_LICENSE
cp vendor/github.com/gostaticanalysis/analysisutil/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_gostaticanalysis_analysisutil_LICENSE
cp vendor/github.com/hashicorp/hcl/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_hashicorp_hcl_LICENSE
cp vendor/github.com/hpcloud/tail/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_hpcloud_tail_LICENSE.txt
cp vendor/github.com/hpcloud/tail/ratelimiter/Licence %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_hpcloud_tail_ratelimiter_Licence
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_json-iterator_go_LICENSE
cp vendor/github.com/kisielk/gotool/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_kisielk_gotool_LICENSE
cp vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_konsorten_go-windows-terminal-sequences_LICENSE
cp vendor/github.com/magiconair/properties/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_magiconair_properties_LICENSE
cp vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_mattn_go-colorable_LICENSE
cp vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_mattn_go-isatty_LICENSE
cp vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_go-homedir_LICENSE
cp vendor/github.com/mitchellh/go-wordwrap/LICENSE.md %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_go-wordwrap_LICENSE.md
cp vendor/github.com/mitchellh/mapstructure/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_mapstructure_LICENSE
cp vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_modern-go_concurrent_LICENSE
cp vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_modern-go_reflect2_LICENSE
cp vendor/github.com/nbutton23/zxcvbn-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_nbutton23_zxcvbn-go_LICENSE.txt
cp vendor/github.com/onsi/ginkgo/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_LICENSE
cp vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_reporters_stenographer_support_go-colorable_LICENSE
cp vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_reporters_stenographer_support_go-isatty_LICENSE
cp vendor/github.com/onsi/gomega/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_gomega_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_go-digest_LICENSE.code
cp vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_go-digest_LICENSE.docs
cp vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_selinux_LICENSE
cp vendor/github.com/pborman/uuid/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_pborman_uuid_LICENSE
cp vendor/github.com/pelletier/go-toml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_pelletier_go-toml_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/sourcegraph/go-diff/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_sourcegraph_go-diff_LICENSE
cp vendor/github.com/spf13/afero/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_afero_LICENSE.txt
cp vendor/github.com/spf13/cast/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_cast_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/jwalterweatherman/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_jwalterweatherman_LICENSE
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_pflag_LICENSE
cp vendor/github.com/spf13/viper/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_viper_LICENSE
cp vendor/github.com/timakin/bodyclose/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_timakin_bodyclose_LICENSE
cp vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_github.com_urfave_cli_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_oauth2_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_text_LICENSE
cp vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_time_LICENSE
cp vendor/golang.org/x/tools/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_golang.org_x_tools_LICENSE
cp vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_google.golang.org_appengine_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_google.golang.org_grpc_LICENSE
cp vendor/gopkg.in/fsnotify.v1/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_fsnotify.v1_LICENSE
cp vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_inf.v0_LICENSE
cp vendor/gopkg.in/tomb.v1/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_tomb.v1_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_NOTICE
cp vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_api_LICENSE
cp vendor/k8s.io/apiextensions-apiserver/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_apiextensions-apiserver_LICENSE
cp vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_apimachinery_LICENSE
cp vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_apiserver_LICENSE
cp vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_client-go_LICENSE
cp vendor/k8s.io/component-base/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_component-base_LICENSE
cp vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_cri-api_LICENSE
cp vendor/k8s.io/klog/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_klog_LICENSE
cp vendor/k8s.io/kubectl/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_kubectl_LICENSE
cp vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_kubernetes_LICENSE
cp vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_k8s.io_utils_LICENSE
cp vendor/mvdan.cc/interfacer/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_interfacer_LICENSE
cp vendor/mvdan.cc/lint/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_lint_LICENSE
cp vendor/mvdan.cc/unparam/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_unparam_LICENSE
cp vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_sigs.k8s.io_yaml_LICENSE
cp vendor/sourcegraph.com/sqs/pbtypes/LICENSE %{buildroot}/usr/share/package-licenses/cri-tools/vendor_sourcegraph.com_sqs_pbtypes_LICENSE
%make_install BINDIR=%{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/crictl
/usr/bin/critest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cri-tools/LICENSE
/usr/share/package-licenses/cri-tools/hack_repo-infra_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/cri-tools/vendor_github.com_Microsoft_go-winio_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_OpenPeeDeeP_depguard_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_docker_distribution_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_docker_docker_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_docker_go-units_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_docker_spdystream_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_docker_spdystream_LICENSE.docs
/usr/share/package-licenses/cri-tools/vendor_github.com_fatih_color_LICENSE.md
/usr/share/package-licenses/cri-tools/vendor_github.com_fsnotify_fsnotify_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_ghodss_yaml_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-critic_go-critic_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-lintpack_lintpack_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astcast_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astcopy_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astequal_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astfmt_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_astp_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_strparse_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_go-toolsmith_typep_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_gobwas_glob_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golang_glog_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golang_mock_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_check_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_dupl_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_errcheck_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-misc_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_lint_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_go-tools_ssa_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_goconst_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gocyclo_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gofmt_gofmt_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gofmt_goimports_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_golangci-lint_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_gosec_LICENSE.txt
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_ineffassign_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_lint-1_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_maligned_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_misspell_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_prealloc_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_revgrep_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_golangci_unconvert_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_google_gofuzz_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_google_uuid_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_gostaticanalysis_analysisutil_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_hashicorp_hcl_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_hpcloud_tail_LICENSE.txt
/usr/share/package-licenses/cri-tools/vendor_github.com_hpcloud_tail_ratelimiter_Licence
/usr/share/package-licenses/cri-tools/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_json-iterator_go_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_kisielk_gotool_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_konsorten_go-windows-terminal-sequences_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_magiconair_properties_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_mattn_go-colorable_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_mattn_go-isatty_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_go-homedir_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_go-wordwrap_LICENSE.md
/usr/share/package-licenses/cri-tools/vendor_github.com_mitchellh_mapstructure_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_modern-go_concurrent_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_modern-go_reflect2_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_nbutton23_zxcvbn-go_LICENSE.txt
/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_reporters_stenographer_support_go-colorable_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_ginkgo_reporters_stenographer_support_go-isatty_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_onsi_gomega_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_go-digest_LICENSE.code
/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_go-digest_LICENSE.docs
/usr/share/package-licenses/cri-tools/vendor_github.com_opencontainers_selinux_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_pborman_uuid_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_pelletier_go-toml_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_sourcegraph_go-diff_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_afero_LICENSE.txt
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_cast_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_jwalterweatherman_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_spf13_viper_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_timakin_bodyclose_LICENSE
/usr/share/package-licenses/cri-tools/vendor_github.com_urfave_cli_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_oauth2_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_time_LICENSE
/usr/share/package-licenses/cri-tools/vendor_golang.org_x_tools_LICENSE
/usr/share/package-licenses/cri-tools/vendor_google.golang.org_appengine_LICENSE
/usr/share/package-licenses/cri-tools/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/cri-tools/vendor_google.golang.org_grpc_LICENSE
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_fsnotify.v1_LICENSE
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_inf.v0_LICENSE
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_tomb.v1_LICENSE
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/cri-tools/vendor_gopkg.in_yaml.v2_NOTICE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_api_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_apiextensions-apiserver_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_apimachinery_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_apiserver_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_client-go_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_component-base_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_cri-api_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_klog_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_kubectl_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_kubernetes_LICENSE
/usr/share/package-licenses/cri-tools/vendor_k8s.io_utils_LICENSE
/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_interfacer_LICENSE
/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_lint_LICENSE
/usr/share/package-licenses/cri-tools/vendor_mvdan.cc_unparam_LICENSE
/usr/share/package-licenses/cri-tools/vendor_sigs.k8s.io_yaml_LICENSE
/usr/share/package-licenses/cri-tools/vendor_sourcegraph.com_sqs_pbtypes_LICENSE
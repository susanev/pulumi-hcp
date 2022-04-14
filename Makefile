# Lowercase variables are considered internal implementation details,
# and shouldn't be modified.
pack            := hcp
project         := github.com/grapl-security/pulumi-$(pack)
version_path    := provider/pkg/version.Version
tfgen           := pulumi-tfgen-$(pack)
provider        := pulumi-resource-$(pack)
version         := $(shell pulumictl get version)
nodejs_version  := $(shell pulumictl get version --language javascript)
pypi_version    := $(shell pulumictl get version --language python)
# dotnet_version := $(shell pulumictl get version --language dotnet)

provider_readme := $(CURDIR)/README.md

# These are the plugins that are needed to generate our provider;
# Pulumi >= 3.26.1 will pull in the current latest version.
plugins := random aws

# Supported SDKs we'll generate
# TODO: add dotnet
sdks := nodejs python go

# All the `go.mod` files we care about
go_mods = $(shell find . -type f -name go.mod -not -path "./sdk/*")

# Uppercase variables can be modified as needed to work on your
# system.
TESTPARALLELISM := 4
# Binary Tools; adjust these according to what you have installed locally.
GOLANGCI_LINT := $(shell go env GOPATH)/bin/golangci-lint
PYTHON        := python3

########################################################################

SHELL := bash
.ONESHELL:
.SHELLFLAGS := -o errexit -o nounset -o pipefail -c

.DEFAULT_GOAL := all

# Providers can be built without the SDKs, and SDKs can be built
# without the providers.
.PHONY: all
all: build-all-providers
all: sdks

# Build Provider
########################################################################

bin/$(tfgen): provider/cmd/pulumi-tfgen-hcp/main.go
# TODO: fold this command into the goreleaser file?
	cd provider
	go build \
		-o $(CURDIR)/bin/$(tfgen) \
		-ldflags "-X $(project)/$(version_path)=$(version)" \
		$(project)/provider/cmd/$(tfgen)

provider/cmd/$(provider)/schema.json: install-plugins
provider/cmd/$(provider)/schema.json: bin/$(tfgen)
provider/cmd/$(provider)/schema.json: provider/resources.go
provider/cmd/$(provider)/schema.json: provider/shim/go.mod
	cd provider
	$(CURDIR)/bin/$(tfgen) schema -v=2 --out cmd/$(provider)

provider/cmd/$(provider)/schema.go: provider/cmd/$(provider)/schema.json
	cd provider
	VERSION=$(version) go generate -v -x cmd/$(provider)/main.go

.PHONY: lint
# We must have schema.go present for our code to lint properly
lint: provider/cmd/$(provider)/schema.go
lint: # Lint the provider code
	(cd provider && $(GOLANGCI_LINT) run -v)
	(cd examples && $(GOLANGCI_LINT) run -v)

.PHONY: format
format: # Format all code
	gofmt -s -w provider
	gofmt -s -w examples

.PHONY: build-all-providers
build-all-providers: export GORELEASER_CURRENT_TAG=$(version)
build-all-providers: ## Just to ensure we can build across all platforms
	goreleaser build --snapshot --rm-dist

# This is a shortcut for just building the provider for the current
# machine's OS / architecture.
bin/$(provider): export GORELEASER_CURRENT_TAG=$(version)
bin/$(provider):
	goreleaser build \
		--output=bin/$(provider) \
		--single-target \
		--snapshot \
		--rm-dist

# This is just a helpful alias for the above target
.PHONY: provider
provider: bin/$(provider)

# Build all SDKs
########################################################################

sdk_deps := bin/$(tfgen) provider/cmd/$(provider)/schema.go

.PHONY: sdks
sdks: $(addsuffix -sdk,$(sdks))
sdks: # Build all the SDKs

.PHONY: nodejs-sdk
nodejs-sdk: $(sdk_deps)
nodejs-sdk: # Build the Node SDK
	rm -Rf sdk/nodejs/bin/dist
	bin/$(tfgen) nodejs \
		--overlays provider/overlays/nodejs \
		--out sdk/nodejs
	cd sdk/nodejs
	yarn install
	yarn run tsc
	cp -R scripts bin
	cp $(provider_readme) ./bin/README.md
	cp ../../LICENSE \
		package.json \
		yarn.lock \
		./bin/
	sed -i.bak \
		-e "s/\$${VERSION}/$(nodejs_version)/g" \
		./bin/package.json
	rm bin/package.json.bak
	# # TODO: Find a better way to handle this
	# sed -i.bak \
	#	-e "s/download\/\$${VERSION}/download\/$(nodejs_version)/g" \
	#	./bin/scripts/install-pulumi-plugin.js
	# rm bin/scripts/install-pulumi-plugin.js.bak
	cd bin
	npm pack
	mkdir dist
	mv *.tgz dist

.PHONY: python-sdk
python-sdk: $(sdk_deps)
python-sdk: # Build the Python SDK
	bin/$(tfgen) python \
		--overlays provider/overlays/python \
		--out sdk/python
	cd sdk/python
	cp $(provider_readme) README.md
	$(PYTHON) setup.py clean --all
	rm -rf ./bin/ ../python.bin/
# Conceptually, we'd want something like `cp -R . ./bin`, but that's
# not allowed.
	cp -R . ../python.bin
	mv ../python.bin ./bin
	cd ./bin
	sed -i.bak \
		-e 's/^VERSION = .*/VERSION = "$(pypi_version)"/g' \
		-e 's/$${VERSION}/$(pypi_version)/g' \
		-e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(version)"/g' \
		setup.py
	rm setup.py.bak
	sed -i.bak \
		-e 's/$${VERSION}/$(version)/g' \
		pulumi_hcp/_utilities.py
	rm pulumi_hcp/_utilities.py.bak
	$(PYTHON) setup.py build sdist

.PHONY: go-sdk
go-sdk: $(sdk_deps)
go-sdk: # Build the Go SDK
	bin/$(tfgen) go \
		--overlays provider/overlays/go \
		--out sdk/go

# Clean Targets
########################################################################

.PHONY: clean
clean: clean-sdks
	rm -f provider/cmd/$(provider)/schema.go
	rm -f provider/cmd/$(provider)/schema.json
	rm -Rf bin
# Generated by goreleaser
	rm -Rf dist
	rm -f install-plugins

.PHONY: clean-sdks
clean-sdks: ## Remove all generated SDK code

define clean-sdk =
clean-sdks: clean-$1-sdk

.PHONY: clean-$1-sdk
clean-$1-sdk:
	rm -Rf sdk/$1
endef

$(foreach sdk,$(sdks),$(eval $(call clean-sdk,$(sdk))))

# Install Targets
########################################################################

.PHONY: install-sdks
install-sdks: install-go-sdk
install-sdks: install-nodejs-sdk
install-sdks: install-python-sdk

# No-op, but exists to ensure a consistent interface
.PHONY: install-go-sdk
install-go-sdk:

.PHONY: install-nodejs-sdk
install-nodejs-sdk:
	yarn link --cwd sdk/nodejs/bin

# No-op, but exists to ensure a consistent interface
.PHONY: install-python-sdk
install-python-sdk:

# Testing
########################################################################

.PHONY: test
test:

define gen-tests =
test: test-$1

.PHONY: test-$1
test-$1: bin/$(provider)
test-$1: install-$1-sdk
# Ensure the compiled provider binary is on the path
test-$1: export PATH=$(CURDIR)/bin:${PATH}
test-$1:
	cd examples
	go test -v \
		-count=1 \
		-cover \
		-timeout 2h \
		-tags=$1 \
		-parallel $(TESTPARALLELISM) \
		.
endef

$(foreach sdk,$(sdks),$(eval $(call gen-tests,$(sdk))))

# Utility Tasks
########################################################################

# NOTE: if new versions of the plugins are released, this won't
# automatically re-run; you'll need to either do a `make clean` or
# remove the `install-plugins` file and then rebuild.
install-plugins: ## Install all required Pulumi plugins
	$(foreach plugin,$(plugins),pulumi plugin install resource $(plugin);)
	touch $@

.PHONY: tidy
tidy: ## Run `go mod tidy` in all places necessary
	@$(foreach d,$(dir $(go_mods)),cd $d; go mod tidy; cd -;)

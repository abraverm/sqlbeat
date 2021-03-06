BEAT_NAME=sqlbeat
BEAT_DIR=github.com/abraverm/sqlbeat
SYSTEM_TESTS=false
TEST_ENVIRONMENT=false
ES_BEATS=./vendor/github.com/elastic/beats
GOPACKAGES=$(shell glide novendor)
PREFIX?=.

# Path to the libbeat Makefile
-include $(ES_BEATS)/libbeat/scripts/Makefile

# Initial beat setup
.PHONY: setup
setup: copy-vendor
	make update

# Copy beats into vendor directory
.PHONY: copy-vendor
copy-vendor:
	mkdir -p vendor/github.com/elastic/
	-cp -R ${GOPATH}/src/github.com/elastic/beats vendor/github.com/elastic/
	rm -rf vendor/github.com/elastic/beats/.git

.PHONY: update-deps
update-deps:
	glide update


# This is called by the beats packer before building starts
.PHONY: before-build
before-build:

# Checks project and source code if everything is according to standard
.PHONY: check
check:

# Collects all dependencies and then calls update
.PHONY: collect
collect:


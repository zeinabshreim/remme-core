# Copyright 2018 REMME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

RELEASE_NUMBER ?= $(shell git describe --abbrev=0 --tags)

COMPOSE_DIR = ./docker-compose
COMPOSE_BUILD = $(COMPOSE_DIR)/base.yml
COMPOSE_BASE = $(COMPOSE_DIR)/base.yml
COMPOSE_GENESIS = $(COMPOSE_DIR)/genesis.yml

BUILD = docker-compose -f $(COMPOSE_BUILD) build
GENESIS_PREAMBLE = docker-compose -f $(COMPOSE_BASE) -f $(COMPOSE_GENESIS) --project-name remme
RUN_GENESIS = $(GENESIS_PREAMBLE) up
RUN_PREAMBLE = docker-compose -f $(COMPOSE_BASE) --project-name remme
RUN = $(RUN_PREAMBLE) up
LOGIO_PREAMBLE = docker-compose -f $(COMPOSE_DIR)/logio.yml --project-name remme
LOGIO = $(LOGIO_PREAMBLE) up

include ./config/network-config.env

.PHONY: release

build:
	git submodule update --init
	$(BUILD)

rebuild:
	$(BUILD) --no-cache

run_genesis: build
	$(RUN_GENESIS)

run_genesis_bg: build
	$(RUN_GENESIS) -d

stop_genesis:
	$(GENESIS_PREAMBLE) down

run: build
	$(RUN)

run_bg: build
	$(RUN) -d

stop:
	$(RUN_PREAMBLE) down

run_docs:
	docker-compose -f $(COMPOSE_DIR)/docs.yml up --build

run_logio:
	$(LOGIO)

run_logio_bg:
	$(LOGIO) -d

stop_logio:
	$(LOGIO_PREAMBLE) down

test:
	docker build --target build -t remme/remme-core-dev:latest .
	docker-compose -f $(COMPOSE_DIR)/test.yml up --build --abort-on-container-exit

release:
	git checkout $(RELEASE_NUMBER)
	$(BUILD) --no-cache
	mkdir $(RELEASE_NUMBER)-release
	mkdir $(RELEASE_NUMBER)-release/docker-compose
	cp {run,genesis}.sh ./$(RELEASE_NUMBER)-release
	cp $(COMPOSE_BASE) ./$(RELEASE_NUMBER)-release/docker-compose
	cp $(COMPOSE_GENESIS) ./$(RELEASE_NUMBER)-release/docker-compose
	docker tag remme/remme-core:latest remme/remme-core:$(RELEASE_NUMBER)
	sed -i -e 's/remme-core:latest/remme-core:$(RELEASE_NUMBER)/' $(RELEASE_NUMBER)-release/docker-compose/*.yml
	cp -R config ./$(RELEASE_NUMBER)-release
	git checkout @{-1}

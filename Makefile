# Convenience targets for the OPM Flow Reference Manual Markdown pipeline.
#
# All targets assume you are in the repository root and have run
#   pip install -e scripts/python
# (or the equivalent Poetry installation), plus mkdocs and pandoc for the
# build-html / build-pdf targets.

PYTHON ?= python3
PARTS  ?= parts
DOCS   ?= docs

.PHONY: convert-all build-html build-pdf serve check clean-docs

convert-all:
	$(PYTHON) -m fodt.fodt2md.cli convert-all --parts-root $(PARTS) --docs-root $(DOCS)

check:
	$(PYTHON) -m fodt.fodt2md.cli convert-all --parts-root $(PARTS) --docs-root $(DOCS) --check

build-html:
	$(PYTHON) -m fodt.fodt2md.cli build-html

serve:
	mkdocs serve

build-pdf:
	$(PYTHON) -m fodt.fodt2md.cli build-pdf

clean-docs:
	# Remove generated Markdown but keep the hand-written index, assets,
	# overrides and templates.
	find $(DOCS) -name '*.md' \
		! -path '$(DOCS)/index.md' \
		! -path '$(DOCS)/_templates/*' \
		-delete
	rm -rf $(DOCS)/_images $(DOCS)/links_report.json

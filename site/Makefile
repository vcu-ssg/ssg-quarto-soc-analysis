

# Default target
.PHONY: help
help:
	@echo "Available targets:"
	@awk -F':' '/^[a-zA-Z0-9_-]+:/ { print "  " $$1 }' $(MAKEFILE_LIST) | sort | uniq | grep -v '^help$$'

files := 10_download.qmd 20_clean.qmd 25_review.qmd 30_explore.qmd 31_explore.qmd 40_workload.qmd about.qmd index.qmd

# Example targets
.PHONY: build
build:
	$(foreach file,$(files),quarto render $(file);)
	@quarto render depts
	

.PHONY: test
test:
	@echo "Running tests..."

.PHONY: clean
clean:
	@echo "Cleaning up the project..."

.PHONY: verify test pipeline

verify:
	scripts/test_pipeline.sh

test:
	scripts/test_pipeline.sh

pipeline:
	scripts/run_pipeline.sh

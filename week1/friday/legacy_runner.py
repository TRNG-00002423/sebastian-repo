import random
import time

from logging_config import setup_logging


logger = setup_logging()


def run_test(test_name):
    """Run a single test (simulated)."""
    logger.info("Running test: %s", test_name)
    duration = random.uniform(0.1, 2.0)
    logger.debug("Generated duration for %s: %.2fs", test_name, duration)
    time.sleep(0.01)  # Simulate work

    if random.random() < 0.2:
        logger.error("%s failed!", test_name)
        logger.debug("Duration for failed test %s: %.2fs", test_name, duration)
        return False

    logger.info("%s passed (%.2fs)", test_name, duration)
    return True


def run_suite(suite_name, test_names):
    """Run a suite of tests."""
    logger.debug("%s", "=" * 50)
    logger.info("Starting suite: %s", suite_name)
    logger.info("Tests to run: %d", len(test_names))
    logger.debug("%s", "=" * 50)

    results = {"passed": 0, "failed": 0}

    for i, test in enumerate(test_names, 1):
        logger.info("Progress [%d/%d]: %s", i, len(test_names), test)
        if run_test(test):
            results["passed"] += 1
        else:
            results["failed"] += 1

    total = results["passed"] + results["failed"]
    rate = results["passed"] / total * 100 if total else 0

    logger.debug("%s", "=" * 50)
    logger.info("Results: %d/%d passed (%.1f%%)", results["passed"], total, rate)

    if rate < 80:
        logger.warning("Pass rate below 80%!")
    if rate < 50:
        logger.critical("More than half the tests failed!")

    return results


def main():
    logger.info("QA Test Framework v1.0")
    logger.info("Initializing...")

    suites = {
        "Smoke Tests": ["test_login", "test_homepage", "test_search"],
        "Regression": [
            "test_checkout",
            "test_payment",
            "test_profile",
            "test_settings",
            "test_logout",
        ],
        "Performance": ["test_load_page", "test_api_response"],
    }

    all_results = {"passed": 0, "failed": 0}

    for suite_name, tests in suites.items():
        try:
            result = run_suite(suite_name, tests)
            all_results["passed"] += result["passed"]
            all_results["failed"] += result["failed"]
        except Exception:
            logger.error("Suite %s crashed", suite_name, exc_info=True)

    total = all_results["passed"] + all_results["failed"]
    logger.info("Final: %d/%d overall", all_results["passed"], total)


if __name__ == "__main__":
    main()

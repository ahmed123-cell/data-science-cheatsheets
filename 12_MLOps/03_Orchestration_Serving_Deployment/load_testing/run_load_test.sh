#!/usr/bin/env bash
# Headless Locust Load Test Runner
# Ramps up to 100 concurrent users at 10 users/second for 60 seconds

locust -f locustfile.py \
       --headless \
       --host http://localhost:8000 \
       --users 100 \
       --spawn-rate 10 \
       --run-time 60s \
       --csv=load_test_results \
       --html=load_test_report.html

echo "Load test complete. Report saved to load_test_report.html"

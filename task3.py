#new file
def analyze_methods(data):
    report = {}
    for item in data:
        method = item["method"]
        error = item ["error"]
        time_ms=item["time_ms"]
        if report.get(method, "default")=="default":
            report[method]={"max_error": error, "total_time_ms": time_ms, "iterations_count": 1}
        else:
            if error>report[method]["max_error"]:
                report[method]["max_error"] = error
            report[method]["total_time_ms"]+=time_ms
            report[method]["iterations_count"]+=1
    return report

experiments_data = [
{"method": "Euler", "iteration": 1, "error": 0.15, "time_ms": 1.2},
{"method": "Runge-Kutta", "iteration": 1, "error": 0.01, "time_ms": 3.5},
{"method": "Euler", "iteration": 2, "error": 0.18, "time_ms": 1.3},
{"method": "Runge-Kutta", "iteration": 2, "error": 0.008, "time_ms": 3.6},
{"method": "Euler", "iteration": 3, "error": 0.22, "time_ms": 1.2},
{"method": "Newton", "iteration": 1, "error": 0.05, "time_ms": 2.1}
]
report= analyze_methods(experiments_data)

for method, value in report.items():
    print(f"Method: {method}")
    print(f"    max_error: {value["max_error"]}")
    print(f"    total_time_ms: {value["total_time_ms"]}")
    print(f"    iterations_count: {value["iterations_count"]}")
    print("")
#new file
def analyze_methods(data):
    report = {}
    for item in data:
        method = item["method"]
        error = item ["error"]
        time_ms=item["time_ms"]
        if report.get(method, default)==default:
            report["method"]={max_error: error, total_time_ms: time_ms, iterations_count: 1}
        else:
            if error>report[method]["error"]:
                report[method]["max_error"] = error
            report[method]["total_time_ms"]+=time_ms
            report[method]["iterations_count"]+=1
    return report
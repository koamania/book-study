import csv
import glob
import pprint

GROUP = 0
PACKAGE = 1
CLASS = 2
INSTRUCTION_MISSED = 3
INSTRUCTION_COVERED = 4
BRANCH_MISSED = 5
BRANCH_COVERED = 6
LINE_MISSED = 7
LINE_COVERED = 8
COMPLEXITY_MISSED = 9
COMPLEXITY_COVERED = 10
METHOD_MISSED = 11
METHOD_COVERED = 12


def read_csv(filepath):
    with open(filepath) as raw:
        lines = raw.readlines()
    return lines[1][0], csv.reader(lines[1:])


def aggregate_coverage(coverage_infos):
    coverage_dict = {
        "total_lines": 0,
        "instruction": {
            "covered": 0,
            "uncovered": 0,
        },
        "branch": {
            "covered": 0,
            "uncovered": 0,
        },
        "line": {
            "covered": 0,
            "uncovered": 0,
        },
        "complexity": {
            "covered": 0,
            "uncovered": 0,
        },
        "method": {
            "covered": 0,
            "uncovered": 0,
        }
    }

    for coverage_info in coverage_infos:
        instruction_uncovered = int(coverage_info[INSTRUCTION_MISSED])
        instruction_covered = int(coverage_info[INSTRUCTION_COVERED])
        coverage_dict["total_lines"] += instruction_uncovered + instruction_covered
        coverage_dict["instruction"]["uncovered"] += instruction_uncovered
        coverage_dict["instruction"]["covered"] += instruction_covered

        branch_uncovered = int(coverage_info[BRANCH_MISSED])
        branch_covered = int(coverage_info[BRANCH_COVERED])
        coverage_dict["total_lines"] += branch_uncovered + branch_covered
        coverage_dict["branch"]["uncovered"] += branch_uncovered
        coverage_dict["branch"]["covered"] += branch_covered

        line_uncovered = int(coverage_info[LINE_MISSED])
        line_covered = int(coverage_info[LINE_COVERED])
        coverage_dict["total_lines"] += line_uncovered + line_covered
        coverage_dict["line"]["uncovered"] += line_uncovered
        coverage_dict["line"]["covered"] += line_covered

        complexity_uncovered = int(coverage_info[COMPLEXITY_MISSED])
        complexity_covered = int(coverage_info[COMPLEXITY_COVERED])
        coverage_dict["total_lines"] += complexity_uncovered + complexity_covered
        coverage_dict["complexity"]["uncovered"] += complexity_uncovered
        coverage_dict["complexity"]["covered"] += complexity_covered

        method_uncovered = int(coverage_info[METHOD_MISSED])
        method_covered = int(coverage_info[METHOD_COVERED])
        coverage_dict["total_lines"] += method_uncovered + method_covered
        coverage_dict["method"]["uncovered"] += method_uncovered
        coverage_dict["method"]["covered"] += method_covered

    return coverage_dict


def main(jacoco_csv_file):
    coverage = read_csv(jacoco_csv_file)
    module_name = coverage[0]
    coverage_dict = aggregate_coverage(coverage[1])

    print(module_name)
    pprint.pprint(coverage_dict)
    # pprint.pprint(backoffice_coverage_dict)


if __name__ == '__main__':
    # D:\\workspace\\unicorn-web\\module-common\\build\\jacoco\\jacoco.csv

    for filename in glob.iglob('D:\\workspace\\unicorn-web\\**\\jacoco.csv', recursive=True):
        # 얘를 파싱해서 어디다가 보내지
        main(filename)
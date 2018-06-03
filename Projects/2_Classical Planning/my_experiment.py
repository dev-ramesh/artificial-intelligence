from run_search import main, SEARCHES
import io
from contextlib import redirect_stdout
from datetime import datetime


def search_experiment(problems, searches, path):
    """[summary]

    Arguments:
        searches {iterable} -- search algorithems
        problems {list} -- problems to be solved
        searches {iterable} -- search algorithems
        path {str} -- file to write experiment result
    """
    for problem in problems:
        for search in searches:
            f = io.StringIO()
            log = open(path, "a+")
            with redirect_stdout(f):
                main([problem], [search])
            out = f.getvalue()
            log.write(out)
            log.close()
            print("problem %d search %d finished" %
                  (problem, search), datetime.now())


def process_log_data(path):
    log = open(path, "r")
    process_log = open("processed_" + path, "a+")
    process_log.write(
        "Problem Search Actions Expansions Goal_Tests New_Nodes Plan_Length Time_Elapsed\n")
    row = []
    flag = 0
    for line in log:
        # record Actions, Expansions, Goal Tests, New Nodes
        if flag == 1:
            row.extend(line.split())
            flag = 0
            continue
        # problem name, search name
        if line.startswith("Solving"):
            start = line.index("Solving") + len("Solving")
            end = line.index("using")
            row.append(line[start:end])

            start = end + len("using")
            end = line.index("...")
            row.append(line[start:end])
        # Actions, Expansions, Goal Tests, New Nodes
        elif line.startswith("# Actions"):
            flag = 1
        # Plan Length, Time elapsed
        elif line.startswith("Plan"):
            start = line.index("length:") + len("length:")
            end = line.index("Time")
            row.append(line[start:end])
            start = line.index("seconds:") + len("seconds:")
            row.append(line[start:])
            process_log.write(" ".join(map(lambda s: s.replace(' ', ''), row)))
            row = []
        else:
            pass
    log.close()
    process_log.close()


if __name__ == "__main__":
    # run all of the search algorithms on the first two problems
    # run at least one uninformed search, two heuristics with greedy best first search
    # and two heuristics with A* on problems 3 and 4
    # search_experiment(problems=range(1, 5), searches=range(
    #     1, len(SEARCHES)+1), path="log.md")

    # process log data
    process_log_data(path="log1.md")

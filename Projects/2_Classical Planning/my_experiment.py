from run_search import main, SEARCHES
import io
from contextlib import redirect_stdout
from datetime import datetime


def search_experiment(problems, searches, path):
    """[summary]

    Arguments:
        problems {list} -- problems to be solved
        searches {iterable} -- search algorithems
        path {str} -- file to write experiment result
    """

    log = open(path, "a+")
    for search in searches:
        f = io.StringIO()
        with redirect_stdout(f):
            main(problems, [search+1])
        out = f.getvalue()
        log.write(out)
        print("search %d finished" % (search+1), datetime.now())
    log.close()


def process_log_data(path):
    log = open(path, "r")
    process_log = open("processed_" + path, "a+")
    process_log.write(
        "Problem Search Actions Expansions Goal_Tests New_Nodes Time_elapsed\n")
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
        # Time elapsed
        elif line.startswith("Plan"):
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
    search_experiment(problems=[1, 2], searches=range(
        len(SEARCHES)), path="log.md")

    # run at least one uninformed search, two heuristics with greedy best first search
    # and two heuristics with A* on problems 3 and 4
    search_experiment(problems=[3, 4], searches=[0, 3, 4, 7, 8], path="log.md")

    # process log data
    process_log_data(path="log.md")

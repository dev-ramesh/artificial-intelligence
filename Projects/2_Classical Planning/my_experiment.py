from run_search import main, SEARCHES
import io
from contextlib import redirect_stdout
from datetime import datetime

# problems = [1, 2]
# log = open("log.md", "a+")
# for search in range(len(SEARCHES)):
#     f = io.StringIO()
#     with redirect_stdout(f):
#         main(problems, [search+1])
#     out = f.getvalue()
#     log.write(out)
#     print("search %d finished" % (search+1), datetime.now())
# log.close()

problems = [3, 4]
log = open("log.md", "a+")
for search in range(len(SEARCHES)):
    f = io.StringIO()
    with redirect_stdout(f):
        main(problems, [search+1])
    out = f.getvalue()
    log.write(out)
    print("search %d finished" % (search+1), datetime.now())
log.close()

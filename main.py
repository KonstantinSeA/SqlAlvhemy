from data import db_session
from data.jobs import Jobs
import datetime
from data import db_session
from data.users import User

db_session.global_init('db/blogs.sqlite')
jobs = Jobs(
    team_leader='1',
    job='deployment of residential modules 1 and 2',
    work_size=15,
    collaborators='2, 3',
    start_date=datetime.datetime.now(),
    is_finished=False
)
db_sess = db_session.create_session()
db_sess.add(jobs)
db_sess.commit()

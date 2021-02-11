
from app import db
from sesh import Sesh
from workout import Workout
from antagonaist import Antagonist
import os

db.create_all()

b_sesh = Sesh(level = 'beginner', warm_up = 'Sloth/Monkey + Quiet Feet + Three Strikes x 3', projecting = 'pick 3 v3+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')
i_sesh = Sesh(level = 'intermediate', warm_up = 'Sloth/Monkey + Power Drivers + Three Strikes x 3', projecting = 'pick 3 v5+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')
a_sesh = Sesh(level = 'advanced', warm_up = 'Sloth/Monkey + Perfect Reapeat + Three Strikes x 3', projecting = 'pick 3 v8+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')

db.session.add(b_sesh)
db.session.add(i_sesh)
db.session.add(a_sesh)
try:
    db.session.commit()
except Exception:
    db.session.rollback()

b_workout = Workout(level = 'beginner', pull = 'pull-ups x 3-5', push = 'push-ups x 10', hip = 'goblet squat (10-15 lbs) x 5-10', core = 'V-ups x 15')
i_workout = Workout(level = 'intermediate', pull = 'pull-ups (weighted) x 5', push = 'Shoulder press x 5', hip = 'Sumo Deadlift x 10', core = 'Hanging Leg Raises x 5-10')
a_workout = Workout(level = 'advanced', pull = ' offset pull-ups x 3/side', push = 'Overhead press w/ barbell x 5', hip = 'Deadlift x 3', core = 'TRX saws x 15 + V-ups x 20')

db.session.add(b_workout)
db.session.add(i_workout)
db.session.add(a_workout)
try:
    db.session.commit()
except Exception:
    db.session.rollback()

db.session.close()

# b_antagonist = []
# i_antagonist = []
# a_antagonist = []
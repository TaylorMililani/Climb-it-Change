
from app import db
from models import Workout, Sesh, Antagonist
import os

db.create_all()

b_sesh = Sesh(level = 'Beginner', warm_up = 'Sloth/Monkey + Quiet Feet + Three Strikes x 3', projecting = 'pick 3 v3+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')
i_sesh = Sesh(level = 'Intermediate', warm_up = 'Sloth/Monkey + Power Drivers + Three Strikes x 3', projecting = 'pick 3 v5+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')
a_sesh = Sesh(level = 'Advanced', warm_up = 'Sloth/Monkey + Perfect Reapeat + Three Strikes x 3', projecting = 'pick 3 v8+ boulders to project, 15-20 minutes per boulder', cool_down = '3 easy boulders')

db.session.add(b_sesh)
db.session.add(i_sesh)
db.session.add(a_sesh)
try:
    db.session.commit()
except Exception:
    db.session.rollback()

b_workout = Workout(level = 'Beginner', pull = 'Pull-ups x 3-5', push = 'Push-ups x 10', hip = 'Goblet Squat (10-15 lbs) x 5-10', core = 'V-ups x 15')
i_workout = Workout(level = 'Intermediate', pull = 'Pull-ups (weighted) x 5', push = 'Shoulder press x 5', hip = 'Sumo Deadlift x 10', core = 'Hanging Leg Raises x 5-10')
a_workout = Workout(level = 'Advanced', pull = 'Offset Pull-ups x 3/side', push = 'Overhead press w/ barbell x 5', hip = 'Deadlift x 3', core = 'TRX saws x 15 + V-ups x 20')

db.session.add(b_workout)
db.session.add(i_workout)
db.session.add(a_workout)
try:
    db.session.commit()
except Exception:
    db.session.rollback()

b_antagonist = Antagonist(level = 'Beginner', ant1 = 'Band Finger Extensions x 20', ant2 = 'I-Y-Ts (2 lbs weights) x 20', ant3 = 'Shoulder press (10 lbs) x 15', ant4 = 'Reverse Wrist Curls (10 lbs) x 15')
i_antagonist = Antagonist(level = 'Intermediate', ant1 = 'DB Internal Rotation (5 lbs) x 20/side', ant2 = 'I-Y-Ts (5 lbs weights) x 20', ant3 = 'Dips x 15-20', ant4 = 'Reverse Wrist Curls (15 lbs) x 20')
a_antagonist = Antagonist(level = 'Advanced', ant1 = 'Barbell Overhead Press (45 lbs+) x 5', ant2 = 'TRX Sling Trainer Ts x 10', ant3 = 'Barbell Deadlift x 5', ant4 = 'Scapular Pull-ups x 10')

db.session.add(b_antagonist)
db.session.add(i_antagonist)
db.session.add(a_antagonist)
try:
    db.session.commit()
except Exception:
    db.session.rollback()

db.session.close()
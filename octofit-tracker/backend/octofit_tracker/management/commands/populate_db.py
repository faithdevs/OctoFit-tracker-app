from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": timedelta(hours=1).total_seconds()},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": timedelta(hours=2).total_seconds()},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": timedelta(hours=1, minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": timedelta(minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15).total_seconds()},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
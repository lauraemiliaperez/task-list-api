from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, default=None)
    #Relationship
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'))
    goal = db.relationship("Goal", back_populates="tasks")

    
    def to_dict(self):
        dict = {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": not self.completed_at is None
        }
        if not self.goal_id is None:
            dict["goal_id"] = self.goal_id
        return dict

    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(title=task_data["title"],
                        description=task_data["description"],
                        completed_at = task_data.get("completed_at"))
        return new_task

class Course:
    def __init__(self, title=None, schedule=None, description=None):
        self.title = title
        self.schedule = schedule
        self.description = description

    def get_title(self):
        return self.title

    def get_schedule(self):
        return self.schedule

    def get_description(self):
        return self.description

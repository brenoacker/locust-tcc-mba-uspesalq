

class TestStagesConfig:

    @staticmethod
    def get_stages():
        return [
            {
                "duration": 30,
                "users": 30,
                "spawn_rate": 1,
                "name": "_ramp"
                },
                {
                "duration": 60,
                "users": 30,
                "spawn_rate": 1,
                "name": "_5x"
                }
        ]


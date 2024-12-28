

class TestStagesConfig:

    @staticmethod
    def get_stages():
        return [
            {
                "duration": 50,
                "users": 50,
                "spawn_rate": 1,
                "name": "_ramp"
                },
                {
                "duration": 100,
                "users": 50,
                "spawn_rate": 1,
                "name": "_5x"
                }
        ]


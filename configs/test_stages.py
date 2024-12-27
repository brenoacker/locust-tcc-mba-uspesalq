

class TestStagesConfig:

    @staticmethod
    def get_stages():
        return [
            {
                "duration": 100,
                "users": 100,
                "spawn_rate": 1,
                "name": "_ramp"
                },
                {
                "duration": 200,
                "users": 100,
                "spawn_rate": 1,
                "name": "_5x"
                }
        ]


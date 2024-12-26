class UserPayload:

    def create_user(name, email, age, gender, phone_number, password):
        return {
            "name": name,
            "email": email,
            "age": age,
            "gender": gender,
            "phone_number": phone_number,
            "password": password
        } 
from flask_app.config.mysqlconnection import connectToMySQL


class Trip:
    db = "vacation_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location= data['location']
        self.duration= data['duration']
        self.departure_date =data['departure_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

#we dont need any other data so we only need cls  for a get all method 
    @classmethod
    def get_all_trips(cls):
        query = """
            SELECT * FROM trips;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_trips = []
        for trip in results:
            all_trips.append(cls(trip))

        return all_trips 
    
    # now create a dashboard for this trip as well to display this 
    #and a url 

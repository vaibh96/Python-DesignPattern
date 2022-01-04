try:
    import csv
    import json
    import psycopg2
except Exception as e:
    raise Exception("Error {}".format(e))


class Secret(object):
    def __init__(self):
        self.database = "test"
        self.user = "postgres"
        self.password = "admin"
        self.host = "localhost"
        self.port = "5432"

        self.connect = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
        )


class SQLServer(Secret):
    TABLE_NAME = "persons"

    def __init__(self, filename):
        self.file_name = filename
        self.first_name = None
        self.last_name = None
        self.email = None
        self.Date_Of_Birth = None
        Secret.__init__(self)
        self.connection = self.connect

    def __str__(self):
        return "SQLServer Object"

    def write_data(self, query_list):
        cursor = self.connection.corsor()

        for data in query_list:
            q = str(data)
            print(q)
            cursor.execute(q)

        self.connection.commit()
        self.connection.close()
        print("data inserted successfully")

    def read_from_csv(self):

        try:
            with open("data.csv") as f:
                reader = csv.DictReader(f, delimiter=",")
                query_builder = []
                for row in reader:
                    self.first_name = "'" + row["First Name"] + "'"
                    self.last_name = "'" + row["Last Name"] + "'"
                    self.Date_Of_Birth = "'" + row["Date Of Birth"] + "'"
                    self.email = "'" + row["Email"] + "'"
                    query = (
                        "insert into "
                        + self.TABLE_NAME
                        + " (first_name, last_name, dob, email) values ("
                        + self.first_name
                        + ", "
                        + self.last_name
                        + ", "
                        + self.Date_Of_Birth
                        + ","
                        + self.email
                        + ");"
                    )
                    query_builder.append(query)
            self.write_data(query_builder)
        except Exception as e:
            raise print("Error : Database Connection issue")
        finally:
            self.connection.close

    def read_data_db(self, query):
        """
        reading data from dataase batch wise
        :return:None
        """
        try:
            print("Reading data from database" + query)
            cursor = self.connection.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]

            while True:
                result = cursor.fetchmany(2)

                if not result:
                    break
                else:
                    items = [dict(zip(data, columns)) for data in result]
                    yield items
        except Exception as e:
            print(e)


def Main():
    obj = SQLServer("vaibhav.csv")
    # obj.read_from_csv()
    result = obj.read_data_db("select * from persons")
    for i in result:
        print(i)
        print()


if __name__ == "__main__":
    Main()

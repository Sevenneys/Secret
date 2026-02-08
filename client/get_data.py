from client.lib import *
from client.json_coding import *

desc = os.path.dirname(os.path.dirname(__file__))
create_descriptor = os.path.join(desc, "config", "files", "user_data.json")

class CreateDataCollection:

    user_id = "Null"
    user_name = "Null"
    oc_name = "Null"
    
    def data_intilization(self) -> dict:

        try:

            user_id = os.getpid()
            user_name = os.getlogin()
            oc_name = platform.platform()

            coding_str = str(oc_name).lower()
            
            oc = ""

            if sys.platform.startswith('linux'):
                oc = "linux"
            elif sys.platform.startswith("windows"):
                oc = "windows"

            return {
                "user_id": user_id,
                "user_name": user_name,
                "oc_name": oc
            }

        except Exception as err:
            print(f"Error: {err}")
    
    def write_file(self, data):

        try:

            with open(create_descriptor, "w+") as w_file:

                js_coding = run_json(state=1, value=data)
                w_file.write(js_coding)

        except Exception as err:
            print(f"Произошла ошибка, при записи файла: {err}")



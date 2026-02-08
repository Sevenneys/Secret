from client.get_data import *
from client.ui.interface import *

create_in = ConsoleInterface(version="v 2.1")

def main():
    
    # if not os.path.exists(create_descriptor):

    #     create_data = CreateDataCollection()
    #     get_data = create_data.data_intilization()
    #     wr_file = create_data.write_file(get_data)
    
    # else:
    #     print("Файл существует!")

    try:

        while True:
            res_main_menu = create_in.create_main_menu()

            if res_main_menu == "0":
                print("Завершаем программу..")
                time.sleep(1)
                sys.exit()
            
            elif res_main_menu == "1":
                
                while True:

                    res_algo_encr = create_in.encrypt_interface()

                    if res_algo_encr == "0":
                        print("Шаг назад..")
                        time.sleep(1)
                        break
                    
                    elif res_algo_encr == "1":
                        pass

                    else:
                        print()

                        print("=====================================")
                        print(f"\nНеверная комманда..\n")
                        print("=====================================")
                
                        print()

                        time.sleep(1)

            elif res_main_menu == "2":
                print("Переходим в кодированние")

            else:
                print()

                print("=====================================")
                print(f"\nНеверная комманда..\n")
                print("=====================================")
                
                print()

                time.sleep(1)

    except KeyboardInterrupt as err:
        print("CTRL + C")
        print("Выходим из программы..\n")
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    main()
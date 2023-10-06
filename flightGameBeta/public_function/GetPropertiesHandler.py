# Properties to  dict
def getProperties(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            con= file.readlines();
            # acorrd condition to get a new list
            content = [item for item in con if "#" not in item and item != '\n'];
            TempList = [];
            for i in content:
                TempList.append(tuple(i.strip('\n').split("=")));
                dataDict = dict(TempList);
            return dataDict;
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {str(e)}");
    except PermissionError as e:
        print(f"PermissionError: {str(e)}");
    except Exception as e:
        print(f"UnknowError: {str(e)}");
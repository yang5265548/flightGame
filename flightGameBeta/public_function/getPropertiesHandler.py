# Properties to dict
def getProperties(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.readlines();
            list = [];
            for i in content:
                list.append(tuple(i.split("=")));
                dataDict = dict(list);
            return dataDict;
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {str(e)}")
    except PermissionError as e:
        print(f"PermissionError: {str(e)}")
    except Exception as e:
        print(f"UnknowError: {str(e)}")
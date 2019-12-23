filmNames = ["误杀","半个喜剧","教授与疯子","叶问4：完结篇 葉問4","只有芸知道"]
rantings = [7.7,7.7,7.5,7.3,6.5]

filmDict = dict(zip(filmNames,rantings))

class EmptyValueError(Exception):
    def __init__(self,error_message="Values are not allowed to be empty!"):
        Exception.__init__(self,error_message)

if __name__ == "__main__":
    try:
        newFilmName = input("请输入电影名称：")
        newRating   = input("请输入电影评分：")
        
        if newFilmName == '':
            raise EmptyValueError()
        elif newRating == '':
            raise EmptyValueError()
        elif float(newRating) > 10:
            raise ValueError
        filmDict[newFilmName] = float(newRating)
        print("\n")
        for n in filmDict:
            print(n,filmDict[n])
    except EmptyValueError:
        print("不允许为空值，输入失败！")
    except ValueError:
        print("评分输入格式错误，请输入十以内的数字！")

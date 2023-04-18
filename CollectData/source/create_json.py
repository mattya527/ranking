import os
import csv

# レースidごとにcsvを取得して返す
def getHourseInfoByRaceId(race_id,year,month):
    with open("../csv/hourse/{}/{}/{}.csv".format(year,month,race_id), 'r',encoding="utf8") as f:
        csv_reader = csv.reader(f)
        response = []
        for i,row in enumerate(csv_reader):
            if i == 0: continue
            response.append(row)
        return response
    

# メイン関数
def main():
    year = 2000
    month = 1

    race_path = "../csv/race/{}/".format(year)

    if os.path.isdir(race_path):
        file_list = os.listdir(race_path)
        # print(file_list)
        for file in file_list:
            with open(race_path+file, "r",encoding="utf8") as f:
                csv_reader = csv.reader(f)
                for i,row in enumerate(csv_reader):
                    # print(i,row)
                    if i == 0: continue
                    hourse_info = getHourseInfoByRaceId(row[0],year,month)
                    print(hourse_info)
                    if i == 1: break

main()
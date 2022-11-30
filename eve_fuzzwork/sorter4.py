import csv

from eve_utils import corp

# skip_corp = ['1000137',   конкорд
#              '1000292',   триглавы
#              '1000298',   триглавы
#              '1000294',   триглавы
#              '1000293']   триглавы

SKIP_CORP = ['1000137',
             '1000292',
             '1000298',
             '1000294',
             '1000293']


class LPsorter:
    def __init__(self):
        pass

        self.data = self.load_csv()
        self.work_data = []

        # дефолтный сорт.
        # self.sort_002(self.data)

        # 5% / количество > 5, отсеивает одиночные ордера
        # self.sort_002(self.data)

        # State Protectorate
        # self.sort_003(self.data)

        # Cap Booster
        self.sort_004(self.data)

        print(f'{len(self.work_data)=}')

        self.table_print(self.work_data, 10, 3000)

    def load_csv(self):
        # with open('full.csv', newline='') as f:
        with open('pl_list.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        print(f'{len(data)=}')
        return data

    def work_data_update(self, data, i):
        self.work_data.append([
            int(data[i][0]),  # corp    0
            corp[data[i][0]],
            int(data[i][1]),  # item    2
            int(data[i][2]),  # lp      3
            int(data[i][3]),  # Isk     4
            data[i][4],  # name         5
            float(data[i][5]),  # Other Cost    6
            int(data[i][6]),  # Quantity        7
            float(data[i][7]),  # Buy Price     8
            int(data[i][8]),  # 5% Volume       9
            float(data[i][9]),  # isk/lp        10

            # перерасчет формулы
            # float(data[i][7]) - float(data[i][5]) - int(data[i][3])

        ])

    def sort_001(self, data):

        for i, _ in enumerate(data):
            if all([
                int(data[i][2]) != 0,
                data[i][0] not in SKIP_CORP,
            ]):
                self.work_data_update(data, i)

    def sort_002(self, data):

        for i, _ in enumerate(data):
            if all([
                int(data[i][2]) != 0,
                data[i][0] not in SKIP_CORP,
            ]):
                if float(data[i][8]) != 0 and float(data[i][6]) != 0 and float(data[i][8]) / float(data[i][6]) >= 5:
                    self.work_data_update(data, i)

    def sort_003(self, data):

        for i, _ in enumerate(data):
            if all([
                int(data[i][2]) != 0,
                data[i][0] not in SKIP_CORP,
                data[i][0] == '1000180'
            ]):
                self.work_data_update(data, i)

    def sort_004(self, data):
        for i, _ in enumerate(data):
            if all([
                data[i][0] == '1000180',
                'Cap Booster' in data[i][4]
            ]):
                self.work_data_update(data, i)

    def table_print(self, _work_data, sort_col, cut):
        _work_data.sort(reverse=True, key=lambda i: i[sort_col])

        from prettytable import PrettyTable

        mytable = PrettyTable()

        mytable.field_names = ['corpid', 'corp name', 'item id', 'lp', '-isk', 'item name', 'ingr -isk', 'колво',
                               '+isk', '5%', 'isk/lp']
        # int(data[i][0]),  # corp    0
        # corp[data[i][0]],
        # int(data[i][1]),  # item    2
        # int(data[i][2]),  # lp      3
        # int(data[i][3]),  # Isk     4
        # data[i][4],  # name         5
        # float(data[i][5]),  # Other Cost    6
        # int(data[i][6]),  # Quantity        7
        # float(data[i][7]),  # Buy Price     8
        # int(data[i][8]),  # 5% Volume       9
        # float(data[i][9]),  # isk/lp        10

        # имена полей таблицы
        # mytable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
        # добавление списка строк
        mytable.add_rows(
            _work_data[:cut]
        )

        mytable.align = "l"

        print(mytable)


LPsorter()

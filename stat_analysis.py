import pandas as pd

# Прирост числа зрителей за рассматриваемый период (10 минут), который означает, что число зрителей стрима достигло пика.
NORM_VIEWERS_COUNT_FOR_PERIOD = 100
# Верхняя граница прироста зрителей после достижения пика.
# Если прирост выше этой границы, то стримера можно заподозрить в потенциальной накрутке.
PEAK_STREAM_VIEWERS_GROWTH = 1000 # Можно заменить на динамическое значение этой переменной. Например: Пиковое количество зрителей / определенный коэффициент
DATA_PATH = "data/dataset.xlsx"


def viewers_analysis(table_path):
    table = pd.read_excel(table_path)
    datetime = table["datetime"]
    viewers_list = table["viewers"]
    last_viewers_count = 0
    peak_viewership = False
    potential_cheating = False
    point_time_indices = []

    for viewers_count in viewers_list:
        viewership_growth = viewers_count - last_viewers_count
        if peak_viewership and viewership_growth > PEAK_STREAM_VIEWERS_GROWTH:
            potential_cheating = True
            point_time_indices.append(table.index[table["viewers"]==viewers_count].tolist()[0])
        elif viewership_growth < NORM_VIEWERS_COUNT_FOR_PERIOD:
            peak_viewership = True
        last_viewers_count = viewers_count

    if potential_cheating:
        print("The streamer is probably cheating the number of viewers with the help of bots")
        print("Points in time at which suspicious activity was detected:")
        for moment_index in point_time_indices:
            begin_moment = datetime[moment_index]
            end_moment = datetime[moment_index + 1]
            print(str(begin_moment) + ' - ' + str(end_moment))
    else:
        print("No suspicious activity was observed. The streamer is unlikely to use bots to increase the number of viewers")



viewers_analysis(DATA_PATH)
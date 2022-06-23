import csv

# 変数の設定
h = 0.01  # 時刻の刻み幅(s)
g = 9.80665  # 重力加速度(m/s^2)
v0 = float(input("初速度を入力してください(m/s) "))  # 初速度(m/s)
x0 = float(input("初期高度を入力してください(m) "))  # 初期高度(m)

# 初期高度がx0<=0の場合のエラー処理
while x0 <= 0:

    print("初期高度は正の値を入力してください")
    x0 = float(input("初期高度を入力してください(m) "))

    if x0 > 0:

        break

t = 0  # 時刻(s)
x = x0  # 高度(m)
v = v0  # 速度(m/s)

# 時刻(0s), 初期高度, 初速度をdata_listとしてリスト化
data_list = [["{:.2f}".format(t), "{:.3f}".format(x), "{:.3f}".format(v)]]


# オイラー法を用いて時刻tにおける高度xおよび速度vを計算する関数
def Euler_method(t, x, v):

    while x >= 0:

        v = v + g * h
        x = x - v * h
        t = t + h

        if x < 0:

            break

        data_list.append(
            ["{:.2f}".format(t), "{:.3f}".format(x), "{:.3f}".format(v)])

    return data_list


# Euler_methodを実行
Euler_method(t, x, v)

# 結果をcsvで出力
with open("data_E.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_list)
    f.close()

print("初速度", "{:.3f}".format(v0), "m/s,", "初期高度",
      "{:.3f}".format(x0), "mにおける物体の落下運動のシミュレーションをdata_E.csvに出力しました")

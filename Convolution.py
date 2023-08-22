import numpy as np
import matplotlib.pyplot as plt

# گرفتن دو رشته عدد از کاربر
str1 = input("لطفا رشته اول را وارد کنید (به صورت عدد ها با فاصله): ")
str2 = input("لطفا رشته دوم را وارد کنید (به صورت عدد ها با فاصله): ")

# تبدیل رشته ها به لیست های عددی
list1 = [float(i) for i in str1.split()]
list2 = [float(i) for i in str2.split()]

# محاسبه کانولوشن دو لیست
conv_result = np.convolve(list1, list2)

# رسم نمودار
plt.stem(conv_result)
plt.title('نتیجه کانولوشن')
plt.show()

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import unicodedata
import pandas as pd

cur_dir = os.getcwd()
customers = pd.read_csv('root.csv', encoding='ISO-8859-1')


print(customers.shape)
#Loại bỏ cột AccountID khỏi custumers
customers = customers.drop("AccountID", axis='columns')


#BEGIN//remove all null/error data
customers['Tenure'] = customers['Tenure'].replace('#', None)

customers['Gender'] = customers['Gender'].replace('F', None)
customers['Gender'] = customers['Gender'].replace('M', None)

customers['Account_user_count'] = customers['Account_user_count'].replace('@', None)

customers['Marital_Status'] = customers['Marital_Status'].replace('nan', None)

customers['account_segment'] = customers['account_segment'].replace('Regular +', None)
customers['account_segment'] = customers['account_segment'].replace('Super +', None)

customers['rev_per_month'] = customers['rev_per_month'].replace('+', None)

customers['rev_growth_yoy'] = customers['rev_growth_yoy'].replace('$', None)


customers['coupon_used_for_payment'] = customers['coupon_used_for_payment'].replace('#', None)
customers['coupon_used_for_payment'] = customers['coupon_used_for_payment'].replace('$', None)
customers['coupon_used_for_payment'] = customers['coupon_used_for_payment'].replace('*', None)

customers['Day_Since_CC_connect'] = customers['Day_Since_CC_connect'].replace('$', None)

customers['cashback'] = customers['cashback'].replace('$', None)

customers['Login_device'] = customers['Login_device'].replace('&&&&', None)
#END//replace all special values to NaN



# Đường dẫn tới file .csv đầu vào
input_file_path = 'root.csv'

# Đọc dữ liệu từ file CSV vào DataFrame
data = customers.copy()

# In ra DataFrame ban đầu
print("DataFrame ban đầu:")
print(data)

# Xóa các hàng có giá trị null từ DataFrame
data_cleaned = data.dropna()

# In ra DataFrame sau khi xóa hàng
print("\nDataFrame sau khi xóa hàng:")
print(data_cleaned)

# Lưu DataFrame đã xóa hàng vào tệp CSV mới
output_file_path = 'new.csv'
data_cleaned.to_csv(output_file_path, index=False)

print("\nĐã xóa các hàng có giá trị null thành công!")




# Đường dẫn tới file .csv đầu vào
input_file_path = 'new.csv'

# Đọc dữ liệu từ file CSV vào DataFrame
data = pd.read_csv(input_file_path)

# In ra DataFrame ban đầu
print("DataFrame ban đầu:")
print(data)

# Xác định số lượng hàng muốn giữ lại
desired_row_count = 2000  # Thay đổi thành số lượng hàng bạn muốn giữ lại

# Kiểm tra số lượng hàng trong DataFrame
current_row_count = data.shape[0]

# Xóa ngẫu nhiên hàng cho đến khi chỉ còn desired_row_count hàng
while current_row_count > desired_row_count:
    # Lựa chọn ngẫu nhiên một hàng để xóa
    random_row_index = data.sample(n=1).index[0]
    
    # Xóa hàng được lựa chọn
    data = data.drop(index=random_row_index)
    
    # Cập nhật số lượng hàng hiện tại sau khi xóa
    current_row_count -= 1

# In ra DataFrame sau khi xóa hàng
print("\nDataFrame sau khi xóa hàng:")
print(data)

# Lưu DataFrame đã xóa hàng vào tệp CSV mới
output_file_path = 'final.csv'
data.to_csv(output_file_path, index=False)

print(f"\nĐã xóa ngẫu nhiên các hàng cho đến khi chỉ còn {desired_row_count} hàng thành công!")

customers_train, customers_test = train_test_split(data, test_size= 0.2, random_state=42, stratify=data['Marital_Status'])
customers_test = pd.DataFrame(customers_test)
customers_train.to_csv(cur_dir + '/exp/train.csv', index = False)
customers_test.to_csv(cur_dir + '/exp/test.csv', index=False)
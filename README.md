# DỰ ĐOÁN KHÁCH HÀNG RỜI BỎ

## Thành viên nhóm
* Nguyễn Minh Quân - 20200509
* Nguyễn Hoàng Lâm - 20203882

## Hướng dẫn 
* Đường link đến tập dữ liệu: https://www.kaggle.com/code/vsridevi/capstone-project-churn-prediction/data?scriptVersionId=110749928
* Mô tả:
  Một nhà cung cấp dịch vụ DTH (Direct to Home) trên thị trường đang phải đối mặt với những thách thức để giữ chân khách hàng hiện tại do có sự cạnh tranh gay gắt trong tình hình hiện tại. Trong công ty này, một tài khoản có thể có nhiều khách hàng được gắn thẻ, vì thế khi mất một tài khoản, công ty có thể mất nhiều hơn một khách hàng. Đồng thời, chi phí để quáng cáo sản phẩm tới những khách hàng mới thường đắt đỏ hơn với việc giữ chân khách hàng cũ. Do đó, tài khoản rời đi là một vấn đề lớn cần giải quyết. Dự đoán khách hàng rời bỏ có nghĩa là phát hiện khách hàng nào có khả năng rời khỏi dịch vụ hoặc hủy đăng ký dịch vụ. Khi bạn có thể xác định những khách hàng có nguy cơ hủy bỏ, bạn nên biết chính xác hành động tiếp thị nào cần thực hiện cho từng khách hàng riêng lẻ để tối đa hóa cơ hội khách hàng sẽ ở lại.
 <b>Nhiệm vụ vủa bạn là dựa trên tập dữ liệu đã có, xây dựng mô hình có thể dự đoán được khách hàng có khả năng rời bỏ trong tương lai</b>
* Mã nguồn gồm các file chính:
  - description.csv: file csv mô tả các trường trong tập dữ liệu
  - train.csv: tập huấn luyện sau khi được chia tách 
  - test.csv: tập kiểm tra sau khi được chia tách
  - split_data.py: file python dùng để chia tập dữ liệu gốc ra làm 2 file train.csv và test.csv, đồng thời cũng dùng để điền lại các giá trị không đồng nhất và giá trị khác biệt có trong tập dữ liệu
  - exp: thư mục hoạt động chính, bao gồm:
    - EDA.ipynb: file notebook cho việc khai phá dữ liệu
    - Datapipeline.py: file python tạo pipeline xử lý dữ liệu
    - OutlierHandling.py: file python xử lý outlier (viết theo api của scikit-learn)
    - CrossValidation.ipynb: file notebook thử nghiệm mô hình và lựa chọn, đánh giá bằng kiểm định chéo
    - Predict.ipynb: file notebook dự đoán lại trên tập kiểm tra

# Selenium Test Login - Chuỗi Cafe T.G

## 📌 Yêu cầu
- Python 3.x
- Selenium (`pip install selenium`)
- Web browser Chrome + ChromeDriver

## 📂 Cấu trúc project
selenium_test/
├── test_login.py
├── test_results.txt
├── test_results.csv
└── README.md

## 🏃 Hướng dẫn chạy test
1. Mở Terminal.
2. Vào thư mục project:

    ```
    cd ~/selenium_test
    ```
3. Chạy test:

    ```
    python3 test_login.py
    ```
4. Kết quả test sẽ lưu trong:

    ```
    test_results.txt
    test_results.csv
    ```
## ✅ 6 Test cases

1. Đăng nhập thành công ✅


- Tên đăng nhập = admin, Mật khẩu = admin1234 → chuyển sang Dashboard.


2. Sai Mật khẩu ✅

- Tên đăng nhập đúng, mật khẩu sai → hiển thị thông báo “Sai mật khẩu!”.

3. Sai Tên đăng nhập ✅


- Tên đăng nhập sai → hiển thị “Tên đăng nhập hoặc mật khẩu không đúng!”.


 4. Bỏ trống trường ✅


- Nếu để trống Tên đăng nhập hoặc Mật khẩu → hiển thị “Vui lòng nhập đầy đủ Username và Password!”.


 5. Link Forgot password? ✅


- Có thể click (dẫn đến # tạm).


 6. Nút social login ✅


- 3 nút hiển thị và có thể click được (Facebook, Google, Instagram).

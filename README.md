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
## ✅ Test cases
1. TC1 - Đăng nhập thành công
2. TC2 - Sai mật khẩu
3. TC3 - Sai username
4. TC4 - Bỏ trống username hoặc password
5. TC5 - Forgot Password
6. TC6 - Social Login (ví dụ Facebook/instagram/email)

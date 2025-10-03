from selenium import webdriver
from selenium.webdriver.common.by import By
import time, csv, os

# Khởi tạo Chrome
driver = webdriver.Chrome()

# Mở file login.html (sửa đường dẫn cho đúng máy bạn)
driver.get("file:///Users/hothicam/Desktop/testlogin.html")
time.sleep(1)

# Lưu kết quả test
results = {}

# --- Test case 1: Đăng nhập thành công ---
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
loginBtn = driver.find_element(By.ID, "loginBtn")

username.send_keys("admin")
password.send_keys("admin1234")
loginBtn.click()
time.sleep(1)
results["TC1 - Đăng nhập thành công"] = "PASS" if "Xin chào" in driver.page_source else "FAIL"

driver.refresh()

# --- Test case 2: Sai mật khẩu ---
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("sai")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
results["TC2 - Sai mật khẩu"] = "PASS" if "Sai mật khẩu!" in driver.page_source else "FAIL"

driver.refresh()

# --- Test case 3: Sai username ---
driver.find_element(By.ID, "username").send_keys("saiuser")
driver.find_element(By.ID, "password").send_keys("admin1234")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
results["TC3 - Sai username"] = "PASS" if "Tên đăng nhập hoặc mật khẩu không đúng!" in driver.page_source else "FAIL"

driver.refresh()

# --- Test case 4: Bỏ trống ---
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1)
results["TC4 - Bỏ trống"] = "PASS" if "Vui lòng nhập đầy đủ" in driver.page_source else "FAIL"

# --- Test case 5: Link Forgot Password ---
forgot = driver.find_element(By.ID, "forgotPwd")
results["TC5 - Forgot Password"] = "PASS" if "forgot" in forgot.get_attribute("href") else "FAIL"

# --- Test case 6: Social login buttons ---
fb = driver.find_element(By.ID, "fbBtn")
gg = driver.find_element(By.ID, "ggBtn")
ig = driver.find_element(By.ID, "igBtn")
results["TC6 - Social Login"] = "PASS" if (fb.is_displayed() and gg.is_displayed() and ig.is_displayed()) else "FAIL"

driver.quit()

# --- In kết quả ra terminal ---
print("\n===== KẾT QUẢ TEST =====")
for k, v in results.items():
    print(f"{k}: {v}")

# --- Xuất ra file TXT ---
with open("test_results.txt", "w", encoding="utf-8") as f:
    for k, v in results.items():
        f.write(f"{k}: {v}\n")

# --- Xuất ra file CSV ---
with open("test_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Test Case", "Result"])
    for k, v in results.items():
        writer.writerow([k, v])

print("\n✅ Đã chạy xong test, kết quả lưu trong test_results.txt và test_results.csv")
print(f"📂 Vị trí: {os.getcwd()}")

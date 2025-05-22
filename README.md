# 🤖 Crypto Wallet Assistant - Rasa Chatbot

Trợ lý AI chuyên nghiệp cho quản lý ví tiền điện tử, hỗ trợ giao dịch crypto, quản lý danh bạ và bảo mật ví.

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Cài đặt](#-cài-đặt)
- [Cấu hình](#️-cấu-hình)
- [Chạy ứng dụng](#-chạy-ứng-dụng)
- [Huấn luyện mô hình](#-huấn-luyện-mô-hình)
- [Kiểm tra và Test](#-kiểm-tra-và-test)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [API và Tích hợp](#-api-và-tích-hợp)
- [Troubleshooting](#-troubleshooting)

## 🚀 Tính năng chính

### 💰 Giao dịch Crypto
- Chuyển tiền điện tử giữa các ví
- Mua/bán crypto với giá thị trường
- Kiểm tra giá crypto realtime
- Xem số dư và portfolio

### 👥 Quản lý Danh bạ
- Thêm/sửa/xóa liên hệ ví
- Tìm kiếm contacts
- Lưu trữ địa chỉ ví an toàn
- Quản lý danh sách người nhận

### 🔐 Bảo mật & Backup
- Xác thực sinh trắc học
- Backup/restore ví
- Đặt giới hạn chi tiêu
- Export lịch sử giao dịch

### 📊 Phân tích Tài chính
- Xem tổng quan portfolio
- Lịch sử giao dịch chi tiết
- Báo cáo tài chính
- Thống kê đầu tư

## 🛠 Cài đặt

### Yêu cầu hệ thống
- Python 3.8+ 
- pip
- Git

### 1. Clone repository
```bash
git clone <repository-url>
cd rasa-crypto-wallet
```

### 2. Tạo virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux  
source venv/bin/activate
```

### 3. Cài đặt dependencies
```bash
pip install rasa
pip install rasa-sdk
pip install requests
```

### 4. Kiểm tra cài đặt
```bash
rasa --version
# Kết quả mong muốn: Rasa 3.x.x
```

## ⚙️ Cấu hình

Dự án đã được tối ưu hóa với **cấu hình crypto chuyên nghiệp**:
- `config.yml` - Pipeline NLU & Core policies tối ưu
- `domain.yml` - Domain với 12 intents crypto và wallet management
- `actions.py` - Custom actions cho crypto operations

### Cấu hình Endpoints
```bash
# Đảm bảo action server được kích hoạt
# File endpoints.yml đã được cấu hình sẵn
```

## 🚀 Chạy ứng dụng

### Bước 1: Khởi động Action Server
```bash
# Terminal 1 - Action Server
rasa run actions
```
*Action server sẽ chạy trên port 5055*

### Bước 2: Khởi động Rasa Bot
```bash  
# Terminal 2 - Rasa Bot
rasa shell --endpoints endpoints.yml
```

### Chạy với REST API
```bash
rasa run --enable-api --cors "*" --endpoints endpoints.yml
```

### Chạy Rasa X (GUI Interface)
```bash
rasa x --endpoints endpoints.yml
```

### Chạy Interactive Mode (Debug & Training)
```bash
rasa interactive --endpoints endpoints.yml
```

## 🎯 Huấn luyện mô hình

### Huấn luyện model crypto
```bash
rasa train
```

### Huấn luyện với force (khi thay đổi config)
```bash
rasa train --force
```

### Huấn luyện với debug mode
```bash
rasa train --debug
```

## 🧪 Kiểm tra và Test

### Validate dữ liệu
```bash
rasa data validate
```

### Test NLU
```bash
rasa test nlu
```

### Test Core (Stories)
```bash
rasa test core --stories data/stories.yml
```

### Test toàn bộ
```bash
rasa test
```

### Cross-validation
```bash
rasa test nlu --cross-validation --runs 3 --folds 5
```

## 🔧 Interactive Mode - Debug & Training

### Khởi động Interactive
```bash
# Interactive mode cơ bản
rasa interactive

# Với action server (khuyến nghị)
rasa interactive --endpoints endpoints.yml

# Với model cụ thể
rasa interactive --model models/your-model.tar.gz
```

### Cách sử dụng Interactive
1. **Test conversation flow**: Chat thực tế với bot
2. **Correct predictions**: Fix khi bot dự đoán sai
3. **Add training data**: Thêm data mới ngay trong conversation
4. **Export improvements**: Save corrections thành training data

### Commands trong Interactive
```bash
Ctrl+C          # Thoát interactive
/stop           # Dừng conversation hiện tại
/restart        # Restart conversation
/save           # Lưu conversation
/export         # Export thành training data
/help           # Hiển thị help
```

### Workflow Interactive
```
1. User: "chuyển 100 USDT cho John"
2. Bot prediction: intent=transfer_crypto ✅ 
3. Action prediction: action_check_balance ❌
4. Correct → action_search_contact ✅
5. Export → Add to training data ✅
```

## 📂 Cấu trúc dự án

```
rasa-crypto-wallet/
├── 📁 actions/                 # Custom actions
│   ├── actions.py             # Crypto actions (330+ training support)
│   └── __init__.py           # Package init
├── 📁 data/                   # Training data
│   ├── nlu.yml               # NLU với 12 intents crypto (330+ examples)
│   ├── stories.yml           # Stories crypto (15+ conversation flows)
│   └── rules.yml             # Rules cho crypto operations
├── 📁 models/                 # Trained models
├── 📁 tests/                  # Test files
├── 📁 results/               # Test results và reports
├── config.yml                # Optimized crypto configuration
├── domain.yml                # Crypto domain với wallet management
├── endpoints.yml             # Action server config
├── credentials.yml           # Platform credentials
├── .gitignore                # Git ignore file
└── README.md                 # Documentation
```

## 🔗 API và Tích hợp

### REST API Endpoints
```bash
# Gửi tin nhắn
POST http://localhost:5005/webhooks/rest/webhook
Content-Type: application/json

{
  "sender": "user123",
  "message": "xem số dư BTC"
}
```

### Webhook Integration
```bash
# Cấu hình webhook cho platforms
# Xem file credentials.yml
```

### Custom Actions API
```bash
# Action server: http://localhost:5055/webhook
# Xem actions/actions.py để tùy chỉnh
```

## 🎮 Hướng dẫn sử dụng

### Câu lệnh cơ bản

#### 💡 **Tip**: Sử dụng `rasa interactive --endpoints endpoints.yml` để test và debug bot real-time!

```
# Chào hỏi
"Xin chào" / "Hello"

# Kiểm tra số dư  
"Xem số dư" / "Check balance"
"Số dư BTC của tôi"

# Chuyển tiền
"Chuyển 100 USDT cho John"
"Transfer 0.5 BTC to mẹ"

# Mua/bán crypto
"Mua 1 ETH"
"Bán 50 BNB với giá 400 USDT"

# Quản lý danh bạ
"Xem danh bạ"
"Thêm contact John với ví myburner.gm"
"Tìm liên hệ mẹ"

# Bảo mật
"Backup ví"
"Đặt giới hạn 1000 USDT"
"Kích hoạt xác thực vân tay"
```

### Workflow phức tạp
```
User: "Xin chào"
Bot: "Chào bạn! Tôi sẵn sàng hỗ trợ..."

User: "Xem portfolio"  
Bot: "Tổng số dư ví: BTC: 0.5, ETH: 2.3..."

User: "Chuyển 100 USDT cho John"
Bot: "Xác nhận giao dịch: 100 USDT → John. Phí: ~$0.15. Xác nhận?"

User: "Có"
Bot: "Vui lòng xác thực vân tay..."
Bot: "🎉 Giao dịch thành công!"
```

## 🔧 Troubleshooting

### Lỗi common và cách fix

#### 1. Port đã sử dụng
```bash
# Lỗi: [Errno 48] Address already in use
# Fix: Kill process và restart
lsof -i :5005
kill <PID>
rasa shell --endpoints endpoints.yml
```

#### 2. Action server không kết nối
```bash
# Lỗi: Cannot connect to action server
# Fix: Đảm bảo action server chạy trước
rasa run actions  # Terminal 1
rasa shell --endpoints endpoints.yml  # Terminal 2
```

#### 3. Intent không được nhận diện
```bash
# Fix: Retrain model
rasa train --force
```

#### 4. Validation errors
```bash
# Fix: Kiểm tra domain và data consistency
rasa data validate
```

### Performance Tips

#### Tối ưu training
```bash
# Sử dụng GPU (nếu có)
export CUDA_VISIBLE_DEVICES=0

# Giảm epochs cho test nhanh
# Sửa config: epochs: 50 (thay vì 100)
```

#### Memory optimization
```bash
# Giới hạn memory sử dụng
export TF_MEMORY_GROWTH=True
```

## 📊 Monitoring và Analytics

### View training metrics
```bash
# Sau khi train xong, check results/
ls results/
# - intent_report.json
# - story_report.json  
# - confusion_matrix.png
```

### Live monitoring
```bash
# Sử dụng Rasa X để monitor conversations
rasa x --production
```

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch: `git checkout -b feature/new-intent`
3. Commit changes: `git commit -m "Add crypto staking intent"`
4. Push branch: `git push origin feature/new-intent`
5. Tạo Pull Request

## 📞 Hỗ trợ

- **Issues**: [GitHub Issues](your-repo/issues)
- **Docs**: [Rasa Documentation](https://rasa.com/docs)
- **Community**: [Rasa Forum](https://forum.rasa.com)

## 📄 License

MIT License - xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

> 💡 **Tip**: Luôn backup dữ liệu trước khi update và test trên môi trường dev trước khi deploy production!

**Happy Chatbotting! 🚀🤖**